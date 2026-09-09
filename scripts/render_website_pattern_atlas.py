#!/usr/bin/env python3
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "research/website-patterns"
G = R / "generated"
README = ROOT / "README.md"
README_START = "<!-- WEBSITE_PATTERN_RESEARCH_START -->"
README_END = "<!-- WEBSITE_PATTERN_RESEARCH_END -->"


def j(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def font(size, bold=False):
    path = Path(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    )
    return ImageFont.truetype(str(path), size) if path.exists() else ImageFont.load_default()


def fit(image, width, height):
    copy = image.copy()
    copy.thumbnail((width, height), Image.Resampling.LANCZOS)
    return copy


def bounds(image, b):
    width, height = image.size
    x = round(b["x"] * width)
    y = round(b["y"] * height)
    return (
        x,
        y,
        min(width, round((b["x"] + b["width"]) * width)),
        min(height, round((b["y"] + b["height"]) * height)),
    )


def render(cohort_dir, taxonomy):
    docs = []
    for path in sorted((cohort_dir / "sites").glob("*.json")):
        data = j(path)
        site = data["site"]
        last_y = -1
        for section in site["sections"]:
            if section["type"] not in taxonomy:
                raise SystemExit(f'{path}: unknown type {section["type"]}')
            b = section["bounds_normalized"]
            valid = (
                0 <= b["y"] <= 1
                and 0 < b["height"] <= 1
                and b["y"] + b["height"] <= 1.0001
                and b["y"] >= last_y
            )
            if not valid:
                raise SystemExit(f"{path}: invalid bounds")
            last_y = b["y"]

        source = ROOT / site["source_repo_path"]
        if not source.exists():
            raise SystemExit(f"Missing source screenshot: {source}")
        docs.append((site, Image.open(source).convert("RGB")))

    cohort = j(cohort_dir / "cohort.json")
    cohort_id = cohort["id"]
    section_counts = Counter()
    site_presence = Counter()
    transitions = Counter()

    for site, _image in docs:
        sequence = [section["type"] for section in site["sections"]]
        section_counts.update(sequence)
        site_presence.update(set(sequence))
        transitions.update(zip(sequence, sequence[1:]))

    G.mkdir(parents=True, exist_ok=True)
    summary = {
        "cohort": cohort_id,
        "name": cohort.get("name", cohort_id),
        "site_count": len(docs),
        "section_counts": dict(section_counts),
        "site_presence": dict(site_presence),
        "transitions": [
            {"from": a, "to": b, "count": count}
            for (a, b), count in transitions.most_common()
        ],
    }
    (G / f"{cohort_id}-summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    with (G / f"{cohort_id}-transitions.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(["from", "to", "count"])
        for (a, b), count in transitions.most_common():
            writer.writerow([a, b, count])

    width = 4700
    row_height = 700
    height = 250 + row_height * len(docs)
    out = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(out)
    draw.text(
        (40, 30),
        f'{summary["name"].upper()} · WEBSITE PATTERN ATLAS',
        font=font(44, True),
        fill="#111",
    )
    draw.text(
        (40, 90),
        "Screenshot → semantic crops → structure sequence → aggregate evidence",
        font=font(24),
        fill="#475569",
    )

    for index, (site, image) in enumerate(docs):
        y0 = 200 + index * row_height
        draw.text((40, y0 + 10), site["name"], font=font(24, True), fill="#111")
        full = fit(image, 210, 600)
        out.paste(full, (40, y0 + 55))

        crop_x = 290
        for section_index, section in enumerate(site["sections"]):
            cx = crop_x + (section_index % 5) * 510
            cy = y0 + 55 + (section_index // 5) * 285
            color = taxonomy[section["type"]]["color"]
            draw.rounded_rectangle(
                (cx, cy, cx + 490, cy + 265),
                radius=10,
                fill="white",
                outline="#CBD5E1",
                width=2,
            )
            draw.rectangle((cx, cy, cx + 9, cy + 265), fill=color)
            crop = fit(
                image.crop(bounds(image, section["bounds_normalized"])), 460, 175
            )
            out.paste(crop, (cx + 15 + (460 - crop.width) // 2, cy + 10))
            draw.text(
                (cx + 18, cy + 195),
                taxonomy[section["type"]]["label"],
                font=font(15, True),
                fill=color,
            )
            draw.text(
                (cx + 18, cy + 220),
                section["label"][:56],
                font=font(14),
                fill="#475569",
            )

        structure_x = 2860
        structure_y = y0 + 55
        draw.text(
            (structure_x, structure_y),
            "STRUCTURE",
            font=font(18, True),
            fill="#111",
        )
        structure_y += 35
        for section in site["sections"]:
            info = taxonomy[section["type"]]
            draw.rounded_rectangle(
                (structure_x, structure_y, structure_x + 420, structure_y + 35),
                radius=6,
                fill=info["color"],
            )
            draw.text(
                (structure_x + 10, structure_y + 8),
                info["label"],
                font=font(14),
                fill="white",
            )
            structure_y += 41

        transition_x = 3370
        transition_y = y0 + 55
        draw.text(
            (transition_x, transition_y),
            "TRANSITIONS",
            font=font(18, True),
            fill="#111",
        )
        transition_y += 34
        for a, b in zip(site["sections"], site["sections"][1:]):
            draw.text(
                (transition_x, transition_y),
                f'{taxonomy[a["type"]]["label"]} → {taxonomy[b["type"]]["label"]}',
                font=font(14),
                fill="#334155",
            )
            transition_y += 23

    out.save(G / f"{cohort_id}-atlas.png", optimize=True)
    return summary


def percent(count, total):
    return f"{round((count / total) * 100)}%" if total else "0%"


def readme_block(summaries, taxonomy):
    lines = [
        README_START,
        "",
        "## Website Pattern Research",
        "",
        "> Auto-generated from the cohort JSON manifests. Edit the JSON, not this block. GitHub Actions rebuilds the analysis.",
        "",
    ]

    for summary in summaries:
        cohort_id = summary["cohort"]
        name = summary.get("name", cohort_id)
        total = summary["site_count"]
        presence = summary["site_presence"]

        lines.extend(
            [
                f"### {name}",
                "",
                f"**{total} reference sites analyzed**",
                "",
                f"[Open full atlas](./research/website-patterns/generated/{cohort_id}-atlas.png) · "
                f"[Summary JSON](./research/website-patterns/generated/{cohort_id}-summary.json) · "
                f"[Transitions CSV](./research/website-patterns/generated/{cohort_id}-transitions.csv)",
                "",
                f"[![{name} website pattern atlas](./research/website-patterns/generated/{cohort_id}-atlas.png)]"
                f"(./research/website-patterns/generated/{cohort_id}-atlas.png)",
                "",
                "| Pattern | Sites | Coverage |",
                "| --- | ---: | ---: |",
            ]
        )

        ordered = sorted(
            presence.items(),
            key=lambda item: (-item[1], taxonomy.get(item[0], {}).get("label", item[0])),
        )
        for section_type, count in ordered:
            if section_type == "capture_partial":
                continue
            label = taxonomy.get(section_type, {}).get("label", section_type)
            lines.append(f"| {label} | {count}/{total} | {percent(count, total)} |")

        lines.extend(
            [
                "",
                "**Most common page-flow transitions**",
                "",
                "| Transition | Count |",
                "| --- | ---: |",
            ]
        )
        for transition in summary["transitions"][:8]:
            from_label = taxonomy.get(transition["from"], {}).get(
                "label", transition["from"]
            )
            to_label = taxonomy.get(transition["to"], {}).get(
                "label", transition["to"]
            )
            lines.append(
                f'| {from_label} → {to_label} | {transition["count"]} |'
            )
        lines.append("")

    lines.extend([README_END, ""])
    return "\n".join(lines)


def update_readme(summaries, taxonomy):
    block = readme_block(summaries, taxonomy)
    original = README.read_text(encoding="utf-8") if README.exists() else "# UI Ideas\n"

    if README_START in original and README_END in original:
        before, remainder = original.split(README_START, 1)
        _old, after = remainder.split(README_END, 1)
        updated = before.rstrip() + "\n\n" + block + after
    else:
        lines = original.splitlines()
        if lines and lines[0].startswith("# "):
            updated = lines[0] + "\n\n" + block + "\n".join(lines[1:]).lstrip()
        else:
            updated = block + original.lstrip()

    README.write_text(updated.rstrip() + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cohort")
    args = parser.parse_args()

    taxonomy = j(R / "taxonomy.json")["section_types"]
    cohort_dirs = (
        [R / "cohorts" / args.cohort]
        if args.cohort
        else [
            path
            for path in (R / "cohorts").iterdir()
            if path.is_dir() and (path / "cohort.json").exists()
        ]
    )
    summaries = [render(path, taxonomy) for path in sorted(cohort_dirs)]
    G.mkdir(exist_ok=True)
    (G / "all-cohorts-summary.json").write_text(
        json.dumps(summaries, indent=2), encoding="utf-8"
    )
    update_readme(summaries, taxonomy)
    print(f"Rendered {len(summaries)} cohort(s) and updated README.md.")


if __name__ == "__main__":
    main()
