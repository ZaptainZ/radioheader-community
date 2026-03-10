#!/usr/bin/env python3
"""
Archive low-quality or stale entries based on scores.json.

Moves entries from pool/ to archive/ (soft delete).
Adds 'verified: true' tag to high-quality entries.
"""

import json
import os
import re
from pathlib import Path


def main():
    scores_path = Path("scores.json")
    if not scores_path.exists():
        print("No scores.json found. Skipping archive.")
        return

    with open(scores_path) as f:
        scores = json.load(f)

    pool_dir = Path("pool")
    archive_dir = Path("archive")

    archived = 0
    verified = 0

    for entry_id, data in scores.items():
        pool_file = pool_dir / f"{entry_id}.md"
        if not pool_file.exists():
            continue

        # Archive: low quality or stale
        if data.get("archive", False):
            archive_dir.mkdir(exist_ok=True)
            dest = archive_dir / f"{entry_id}.md"
            pool_file.rename(dest)
            archived += 1
            print(f"  Archived: {entry_id} (score={data['score']}, usage={data['usage']})")
            continue

        # Verified: add tag if not already present
        if data.get("verified", False):
            content = pool_file.read_text()
            if "verified:" not in content:
                # Add verified field after the last frontmatter field (before closing ---)
                lines = content.split("\n")
                new_lines = []
                in_frontmatter = False
                added = False
                dash_count = 0
                for line in lines:
                    if line.strip() == "---":
                        dash_count += 1
                        if dash_count == 2 and not added:
                            new_lines.append(f"community_verified: true")
                            added = True
                    new_lines.append(line)
                if added:
                    pool_file.write_text("\n".join(new_lines))
                    verified += 1
                    print(f"  Verified: {entry_id} (score={data['score']}, usage={data['usage']})")

    if archived == 0 and verified == 0:
        print("No entries to archive or verify.")
    else:
        if archived > 0:
            print(f"Archived {archived} entries.")
        if verified > 0:
            print(f"Verified {verified} entries.")


if __name__ == "__main__":
    main()
