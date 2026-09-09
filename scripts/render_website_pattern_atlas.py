#!/usr/bin/env python3
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "research/website-patterns"
G = R / "generated"
README = ROOT / "README.md"
START = "<!-- WEBSITE_PATTERN_RESEARCH_START -->"
END = "<!-- WEBSITE_PATTERN_RESEARCH_END -->"
SUCCESS = {"ok", "success", "captured", "complete"}

FINAL_DECIDED_STRUCTURE = [
    {"position": 1, "type": "navigation", "label": "Header", "color": "#546E7A"},
    {"position": 2, "type": "hero_cta", "label": "Hero", "color": "#1565C0"},
    {"position": 3, "type": "quick_actions", "label": "Quick Actions", "color": "#00838F"},
    {"position": 4, "type": "product_offers", "label": "Offers / Plans", "color": "#2E7D32"},
    {"position": 5, "type": "service_categories", "label": "Service Categories", "color": "#6A1B9A"},
    {"position": 6, "type": "business_section", "label": "Business & Government", "color": "#3949AB"},
    {"position": 7, "type": "content_feature", "label": "PNG / National Story", "color": "#8E24AA"},
    {"position": 8, "type": "news", "label": "Notices & News", "color": "#C62828"},
    {"position": 9, "type": "faq_help", "label": "Help / Support / Stores", "color": "#9E6B00"},
    {"position": 10, "type": "footer", "label": "Footer", "color": "#263238"},
]


def J(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def F(n, b=False):
    p = Path(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if b
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    )
    return ImageFont.truetype(str(p), n) if p.exists() else ImageFont.load_default()


def fit(im, w, h):
    x = im.copy()
    x.thumbnail((w, h), Image.Resampling.LANCZOS)
    return x


def box(im, b):
    w, h = im.size
    return (
        round(b["x"] * w),
        round(b["y"] * h),
        min(w, round((b["x"] + b["width"]) * w)),
        min(h, round((b["y"] + b["height"]) * h)),
    )


def ell(d, xy, text, width, f, fill):
    original = str(text)
    s = original
    while s and d.textbbox((0, 0), s, font=f)[2] > width:
        s = s[:-1]
    if s != original and len(s) > 3:
        s = s[:-3].rstrip() + "..."
    d.text(xy, s, font=f, fill=fill)


def pct_num(n, d):
    return round(n / d * 100) if d else 0


def pct(n, d):
    return f"{pct_num(n, d)}%" if d else "n/a"


def clean_seq(sections):
    seq = []
    for q in sections:
        typ = q["type"]
        if typ == "capture_partial":
            continue
        if not seq or seq[-1] != typ:
            seq.append(typ)
    return seq


def metadata(cohort):
    root = ROOT / cohort["source_root"]
    name = cohort.get("metadata_file")
    if not name and (root / "capture-results.json").exists():
        name = "capture-results.json"
    if not name or not (root / name).exists():
        return {}, {}
    data = J(root / name)
    results = {x["slug"]: x for x in data.get("results", []) if x.get("slug")}
    excluded = {
        x["slug"]: x.get("reason", "Excluded by capture curation")
        for x in data.get("excluded", [])
        if x.get("slug")
    }
    return results, excluded


def source_for(root, slug, s, m):
    candidates = []
    if s and s.get("source_repo_path"):
        candidates.append(ROOT / s["source_repo_path"])
    candidates.append(root / f"{slug}.png")
    if m and m.get("researchFilename"):
        candidates.append(root / m["researchFilename"])
    for p in candidates:
        if p.exists():
            return p
    return None


def exclusion_reason(slug, s, m, curated_excluded, src):
    if slug in curated_excluded:
        return curated_excluded[slug]
    if src is None:
        return "No usable screenshot file"
    mstatus = str((m or {}).get("status", "")).strip().lower()
    if mstatus and mstatus not in SUCCESS:
        return f"Capture metadata status: {mstatus}"
    sstatus = str((s or {}).get("capture_status", "")).strip().lower()
    if sstatus and sstatus not in SUCCESS:
        return f"Semantic capture status: {sstatus}"
    if s and any(q.get("type") == "capture_partial" for q in s.get("sections", [])):
        return "Semantic review marked screenshot as partial / unreliable"
    return None


def inventory(cd, tax):
    cohort = J(cd / "cohort.json")
    root = ROOT / cohort["source_root"]
    meta, curated_excluded = metadata(cohort)
    semantic = {}

    if (cd / "sites").exists():
        for p in sorted((cd / "sites").glob("*.json")):
            s = J(p)["site"]
            last = -1
            for q in s.get("sections", []):
                if q["type"] not in tax:
                    raise SystemExit(f'{p}: unknown type {q["type"]}')
                b = q["bounds_normalized"]
                valid = (
                    0 <= b["x"] <= 1
                    and 0 <= b["y"] <= 1
                    and 0 < b["width"] <= 1
                    and 0 < b["height"] <= 1
                    and b["x"] + b["width"] <= 1.0001
                    and b["y"] + b["height"] <= 1.0001
                    and b["y"] >= last
                )
                if not valid:
                    raise SystemExit(f"{p}: invalid bounds")
                last = b["y"]
            semantic[s["slug"]] = s

    slugs = set(cohort.get("sites", [])) | set(meta) | set(semantic) | set(curated_excluded)
    if not slugs:
        slugs = {p.stem for p in root.glob("*.png")}

    out = []
    excluded = []
    for slug in sorted(slugs):
        s = semantic.get(slug)
        m = meta.get(slug, {})
        src = source_for(root, slug, s, m)
        reason = exclusion_reason(slug, s, m, curated_excluded, src)
        name = s.get("name") if s else m.get("name") or slug.replace("-", " ").title()
        url = s.get("url") if s else m.get("url") or m.get("requestedUrl") or m.get("finalUrl") or ""

        if reason:
            excluded.append({"slug": slug, "name": name, "url": url, "reason": reason})
            continue

        sections = s.get("sections", []) if s else []
        out.append(
            {
                "slug": slug,
                "name": name,
                "url": url,
                "source": src,
                "sections": sections,
                "analysis_status": "analyzed" if sections else "pending",
                "cohort_id": cohort["id"],
                "cohort_name": cohort.get("name", cohort["id"]),
            }
        )
    return cohort, out, excluded


def positional_patterns(analyzed):
    by_pos = defaultdict(Counter)
    for x in analyzed:
        for i, typ in enumerate(clean_seq(x["sections"])):
            by_pos[i][typ] += 1

    out = []
    n = len(analyzed)
    for pos in sorted(by_pos):
        candidates = [
            {"type": typ, "count": count, "coverage_pct": pct_num(count, n)}
            for typ, count in by_pos[pos].most_common()
        ]
        out.append({"position": pos + 1, "candidates": candidates})
    return out


def summary(cohort, items, excluded):
    analyzed = [x for x in items if x["analysis_status"] == "analyzed"]
    sc = Counter()
    pres = Counter()
    tr = Counter()

    for x in analyzed:
        seq = clean_seq(x["sections"])
        sc.update(seq)
        pres.update(set(seq))
        tr.update(zip(seq, seq[1:]))

    pos = positional_patterns(analyzed)
    rec = [{"position": p["position"], **p["candidates"][0]} for p in pos if p["candidates"]]
    return {
        "cohort": cohort["id"],
        "name": cohort.get("name", cohort["id"]),
        "candidate_site_count": len(items) + len(excluded),
        "reference_site_count": len(items),
        "excluded_site_count": len(excluded),
        "excluded_sites": excluded,
        "analyzed_site_count": len(analyzed),
        "pending_site_count": len(items) - len(analyzed),
        "section_counts": dict(sc),
        "site_presence": dict(pres),
        "position_patterns": pos,
        "recommended_structure": rec,
        "transitions": [{"from": a, "to": b, "count": n} for (a, b), n in tr.most_common()],
    }


def final_decision():
    return {
        "status": "decided",
        "title": "Final Decided Structure",
        "basis": "Project-approved homepage information architecture. Research statistics are kept separately and are not used as percentages for this final structure.",
        "final_structure": FINAL_DECIDED_STRUCTURE,
    }


def row(canvas, d, item, tax, y0, rh, cohort_label=False):
    if (y0 // rh) % 2 == 0:
        d.rectangle((0, y0, 3980, y0 + rh - 2), fill="#F8FAFC")

    title = (item["cohort_name"] + " · " if cohort_label else "") + item["name"]
    ell(d, (35, y0 + 13), title, 1900, F(20, True), "#111827")
    if item["url"]:
        ell(d, (35, y0 + 41), item["url"], 1900, F(12), "#64748B")

    im = Image.open(item["source"]).convert("RGB")
    full = fit(im, 180, 330)
    canvas.paste(full, (38 + (180 - full.width) // 2, y0 + 73))
    d.rectangle((38, y0 + 73, 218, y0 + 403), outline="#CBD5E1", width=2)
    d.text((38, y0 + 407), f"{im.width}×{im.height}", font=F(10), fill="#64748B")

    sec = item["sections"]
    cx0 = 245
    cw = 395
    ch = 157
    if sec:
        for i, q in enumerate(sec):
            rr, cc = divmod(i, 6)
            x = cx0 + cc * 407
            y = y0 + 72 + rr * 169
            info = tax[q["type"]]
            d.rounded_rectangle((x, y, x + cw, y + ch), radius=9, fill="white", outline="#CBD5E1", width=1)
            d.rectangle((x, y, x + 8, y + ch), fill=info["color"])
            cr = fit(im.crop(box(im, q["bounds_normalized"])), cw - 28, 90)
            canvas.paste(cr, (x + 14 + (cw - 28 - cr.width) // 2, y + 8))
            ell(d, (x + 15, y + 106), info["label"], cw - 28, F(11, True), info["color"])
            ell(d, (x + 15, y + 129), q["label"], cw - 28, F(10), "#475569")
    else:
        d.rounded_rectangle((cx0, y0 + 88, 2678, y0 + 352), radius=13, fill="#F1F5F9", outline="#CBD5E1", width=2)
        d.text((cx0 + 32, y0 + 142), "SEMANTIC ANALYSIS PENDING", font=F(23, True), fill="#64748B")
        d.text((cx0 + 32, y0 + 188), "Clean screenshot included. Add JSON to unlock crops, structure and statistics.", font=F(15), fill="#475569")

    sx = 2710
    sy = y0 + 72
    d.text((sx, sy), "STRUCTURE CODE", font=F(15, True), fill="#111827")
    sy += 29
    if sec:
        for q in sec[:11]:
            info = tax[q["type"]]
            d.rounded_rectangle((sx, sy, sx + 500, sy + 27), radius=5, fill=info["color"])
            ell(d, (sx + 8, sy + 6), info["label"], 482, F(10), "white")
            sy += 32
    else:
        d.text((sx, sy), "Pending JSON", font=F(13), fill="#94A3B8")

    tx = 3240
    ty = y0 + 72
    d.text((tx, ty), "PAGE FLOW", font=F(15, True), fill="#111827")
    ty += 30
    if sec:
        clean = [q for q in sec if q["type"] != "capture_partial"]
        for a, b in zip(clean, clean[1:]):
            ell(d, (tx, ty), tax[a["type"]]["label"] + " → " + tax[b["type"]]["label"], 715, F(10), "#334155")
            ty += 24
            if ty > y0 + rh - 20:
                break
    else:
        d.text((tx, ty), "Pending semantic analysis", font=F(12), fill="#94A3B8")

    im.close()


def global_panel(d, decision):
    x, y, w = 4005, 28, 955
    d.rounded_rectangle((x, y, x + w, y + 760), radius=18, fill="#F1F5F9", outline="#CBD5E1", width=2)
    d.text((x + 27, y + 24), "FINAL DECIDED STRUCTURE", font=F(22, True), fill="#111827")
    d.text((x + 27, y + 64), "Telikom homepage information architecture", font=F(14), fill="#475569")

    yy = y + 112
    for z in decision["final_structure"]:
        d.rounded_rectangle((x + 27, yy, x + w - 27, yy + 44), radius=7, fill=z["color"])
        d.text((x + 42, yy + 12), f'{z["position"]}.', font=F(12, True), fill="white")
        ell(d, (x + 78, yy + 12), z["label"], w - 132, F(12, True), "white")
        yy += 52

    yy += 12
    d.text((x + 27, yy), "Final project direction", font=F(11, True), fill="#334155")
    d.text((x + 27, yy + 22), "No research-derived percentages are applied to this list.", font=F(10), fill="#64748B")


def render(items, title, path, tax, decision=None, cohort_label=False):
    W = 5000
    H0 = 205
    RH = 430
    H = max(H0 + RH * len(items) + 35, 900 if decision else 0)
    c = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(c)
    d.text((35, 28), title.upper(), font=F(36, True), fill="#111827")
    analyzed = sum(x["analysis_status"] == "analyzed" for x in items)
    d.text((35, 80), f'{len(items)} clean screenshots visible · {analyzed} analyzed · {len(items) - analyzed} pending', font=F(19), fill="#475569")
    d.text((35, 114), "Screenshot → semantic crops → structure code → page flow → final page structure", font=F(16), fill="#64748B")

    for i, item in enumerate(items):
        row(c, d, item, tax, H0 + i * RH, RH, cohort_label)

    if decision:
        global_panel(d, decision)

    c.save(path, "JPEG", quality=70, optimize=True, progressive=True)
    c.close()


def write_files(cohort, s):
    G.mkdir(parents=True, exist_ok=True)
    cid = cohort["id"]
    (G / f"{cid}-summary.json").write_text(json.dumps(s, indent=2), encoding="utf-8")

    with (G / f"{cid}-transitions.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["from", "to", "count"])
        for z in s["transitions"]:
            w.writerow([z["from"], z["to"], z["count"]])

    with (G / f"{cid}-recommended-structure.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["position", "type", "coverage_pct", "count"])
        for z in s["recommended_structure"]:
            w.writerow([z["position"], z["type"], z["coverage_pct"], z["count"]])


def readme_block(sums, tax, decision):
    total = sum(s["reference_site_count"] for s in sums)
    analyzed = sum(s["analyzed_site_count"] for s in sums)
    excluded = sum(s["excluded_site_count"] for s in sums)

    L = [
        START,
        "",
        "## Website Pattern Research",
        "",
        "> Auto-generated from clean screenshot inventory + semantic JSON. Failed, partial, blocked and unreliable captures are excluded from the atlas and research statistics.",
        "",
        f"**{total} clean reference screenshots tracked · {analyzed} semantically analyzed · {excluded} captures excluded**",
        "",
        "[Open the all-reference atlas](./research/website-patterns/generated/all-reference-atlas.jpg) · [Final decided structure](./research/website-patterns/generated/final-structure-recommendation.json) · [All cohort summaries](./research/website-patterns/generated/all-cohorts-summary.json)",
        "",
        "[![All website research atlas](./research/website-patterns/generated/all-reference-atlas.jpg)](./research/website-patterns/generated/all-reference-atlas.jpg)",
        "",
        "### Final decided page structure",
        "",
        "This is the project-approved homepage information architecture. It is shown without research-derived percentages.",
        "",
        "| Order | Section |",
        "| ---: | --- |",
    ]

    for z in decision["final_structure"]:
        L.append(f'| {z["position"]} | {z["label"]} |')

    L += [
        "",
        "### Analysis coverage",
        "",
        "| Cohort | Candidates | Included clean captures | Excluded captures | Analyzed | Pending |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for s in sums:
        L.append(
            f'| {s["name"]} | {s["candidate_site_count"]} | {s["reference_site_count"]} | '
            f'{s["excluded_site_count"]} | {s["analyzed_site_count"]} | {s["pending_site_count"]} |'
        )

    L.append("")
    for s in sums:
        cid = s["cohort"]
        a = s["analyzed_site_count"]
        L += [
            f'### {s["name"]}',
            "",
            f'**{s["reference_site_count"]} clean screenshots · {a} analyzed · {s["excluded_site_count"]} excluded · {s["pending_site_count"]} pending**',
            "",
            f'[Open cohort atlas](./research/website-patterns/generated/{cid}-atlas.jpg) · [Summary JSON](./research/website-patterns/generated/{cid}-summary.json) · [Observed structure CSV](./research/website-patterns/generated/{cid}-recommended-structure.csv) · [Transitions CSV](./research/website-patterns/generated/{cid}-transitions.csv)',
            "",
        ]

        if a:
            L += [
                "**Observed section pattern at each page position**",
                "",
                "| Position | Most common observed section | Sites at this exact position |",
                "| ---: | --- | ---: |",
            ]
            for z in s["recommended_structure"][:12]:
                L.append(
                    f'| {z["position"]} | {tax.get(z["type"], {}).get("label", z["type"])} | '
                    f'{z["count"]}/{a} ({z["coverage_pct"]}%) |'
                )

            L += [
                "",
                "**Section presence across clean analyzed sites**",
                "",
                "| Pattern | Analyzed sites | Coverage |",
                "| --- | ---: | ---: |",
            ]
            for typ, n in sorted(
                s["site_presence"].items(),
                key=lambda z: (-z[1], tax.get(z[0], {}).get("label", z[0])),
            ):
                if typ != "capture_partial":
                    L.append(f'| {tax.get(typ, {}).get("label", typ)} | {n}/{a} | {pct(n, a)} |')

            L += [
                "",
                "**Most common page-flow transitions**",
                "",
                "| Transition | Count |",
                "| --- | ---: |",
            ]
            for z in s["transitions"][:8]:
                L.append(
                    f'| {tax.get(z["from"], {}).get("label", z["from"])} → '
                    f'{tax.get(z["to"], {}).get("label", z["to"])} | {z["count"]} |'
                )
        else:
            L.append("_No clean semantically analyzed screenshots are currently available for this cohort._")

        if s["excluded_sites"]:
            L += [
                "",
                "**Excluded capture attempts**",
                "",
                "| Site | Reason |",
                "| --- | --- |",
            ]
            for z in s["excluded_sites"]:
                L.append(f'| {z["name"]} | {z["reason"]} |')

        L.append("")

    L += [END, ""]
    return "\n".join(L)


def update_readme(sums, tax, decision):
    block = readme_block(sums, tax, decision)
    old = README.read_text(encoding="utf-8") if README.exists() else "# UI Ideas\n"

    if START in old and END in old:
        before, rest = old.split(START, 1)
        _, after = rest.split(END, 1)
        new = before.rstrip() + "\n\n" + block + after
    else:
        lines = old.splitlines()
        new = (
            lines[0] + "\n\n" + block + "\n".join(lines[1:]).lstrip()
            if lines and lines[0].startswith("# ")
            else block + old.lstrip()
        )

    README.write_text(new.rstrip() + "\n", encoding="utf-8")


def main():
    tax = J(R / "taxonomy.json")["section_types"]
    dirs = sorted(p for p in (R / "cohorts").iterdir() if p.is_dir() and (p / "cohort.json").exists())
    sums = []
    all_items = []
    G.mkdir(parents=True, exist_ok=True)

    for cd in dirs:
        cohort, items, excluded = inventory(cd, tax)
        s = summary(cohort, items, excluded)
        sums.append(s)
        all_items.extend(items)
        write_files(cohort, s)
        render(items, cohort.get("name", cohort["id"]) + " · Pattern Atlas", G / f'{cohort["id"]}-atlas.jpg', tax)

    decision = final_decision()
    render(
        all_items,
        "PNG + Telecom · All Website Research Atlas",
        G / "all-reference-atlas.jpg",
        tax,
        decision=decision,
        cohort_label=True,
    )
    (G / "all-cohorts-summary.json").write_text(json.dumps(sums, indent=2), encoding="utf-8")
    (G / "final-structure-recommendation.json").write_text(json.dumps(decision, indent=2), encoding="utf-8")
    update_readme(sums, tax, decision)

    print(
        f'Included {len(all_items)} clean screenshots across {len(sums)} cohorts; '
        f'excluded {sum(s["excluded_site_count"] for s in sums)} failed/partial captures; '
        f'{sum(s["analyzed_site_count"] for s in sums)} analyzed. '
        "Final decided structure written without research-derived percentages."
    )


if __name__ == "__main__":
    main()
