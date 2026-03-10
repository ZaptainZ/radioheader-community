#!/usr/bin/env python3
"""
Aggregate votes from votes/*.jsonl into scores.json.

Scoring formula (Stigmergy pheromone model):
  raw_score = sum(positive) - sum(negative) * 2   # negative votes weighted 2x
  age_days  = now - first_vote_date
  decay     = e^(-age_days / 180)                  # half-life ~125 days
  final_score = raw_score * decay
  usage     = total vote count (positive + negative)

Output: scores.json with per-entry scores.
"""

import json
import math
import os
from datetime import datetime, date
from pathlib import Path
from collections import defaultdict


def load_votes(votes_dir: Path) -> dict:
    """Load all votes from JSONL files, deduplicated by (hash, id)."""
    entries = defaultdict(lambda: {
        "positive": 0,
        "negative": 0,
        "first_vote": None,
        "votes": [],
        "seen_hashes": set(),
    })

    for jsonl_file in sorted(votes_dir.glob("*.jsonl")):
        with open(jsonl_file) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    vote = json.loads(line)
                except json.JSONDecodeError:
                    continue

                entry_id = vote.get("id", "")
                vote_val = vote.get("vote", 0)
                ts = vote.get("ts", "")
                vote_hash = vote.get("hash", "")

                if not entry_id or vote_val not in (1, -1):
                    continue

                entry = entries[entry_id]

                # Deduplicate: same hash + same entry = one vote
                if vote_hash:
                    dedup_key = f"{vote_hash}:{entry_id}"
                    if dedup_key in entry["seen_hashes"]:
                        continue
                    entry["seen_hashes"].add(dedup_key)

                # Count
                if vote_val == 1:
                    entry["positive"] += 1
                else:
                    entry["negative"] += 1

                # Track first vote date
                if ts:
                    try:
                        vote_date = datetime.strptime(ts, "%Y-%m-%d").date()
                        if entry["first_vote"] is None or vote_date < entry["first_vote"]:
                            entry["first_vote"] = vote_date
                    except ValueError:
                        pass

    return entries


def compute_scores(entries: dict) -> dict:
    """Compute final scores with pheromone decay."""
    today = date.today()
    scores = {}

    for entry_id, data in entries.items():
        raw_score = data["positive"] - data["negative"] * 2
        usage = data["positive"] + data["negative"]

        # Decay based on age since first vote
        age_days = 0
        first_vote_str = ""
        if data["first_vote"]:
            age_days = (today - data["first_vote"]).days
            first_vote_str = data["first_vote"].isoformat()

        decay = math.exp(-age_days / 180)
        final_score = round(raw_score * decay, 2)

        # Determine status
        verified = usage >= 5 and final_score >= 8
        stale = age_days > 180 and usage == 0
        low_quality = usage >= 10 and final_score <= 0

        scores[entry_id] = {
            "score": final_score,
            "raw_score": raw_score,
            "usage": usage,
            "positive": data["positive"],
            "negative": data["negative"],
            "first_vote": first_vote_str,
            "age_days": age_days,
            "decay": round(decay, 4),
            "verified": verified,
            "archive": stale or low_quality,
        }

    return scores


def main():
    votes_dir = Path("votes")
    if not votes_dir.exists():
        print("No votes directory found. Nothing to aggregate.")
        return

    entries = load_votes(votes_dir)
    if not entries:
        print("No votes found.")
        return

    scores = compute_scores(entries)

    # Write scores.json
    with open("scores.json", "w") as f:
        json.dump(scores, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # Summary
    total = len(scores)
    verified = sum(1 for s in scores.values() if s["verified"])
    to_archive = sum(1 for s in scores.values() if s["archive"])
    print(f"Aggregated {total} entries: {verified} verified, {to_archive} to archive")


if __name__ == "__main__":
    main()
