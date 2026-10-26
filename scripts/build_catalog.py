#!/usr/bin/env python3
"""扫描 cards/ 下的技能卡片，生成 CATALOG.md 总索引。仅用标准库。

卡片格式见 templates/skill-card.md：标题行 `# 名称`，其后是
`- 字段: 值` 行。必填字段：分类 / 来源 / 一句话。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = ROOT / "cards"
OUT = ROOT / "CATALOG.md"

CATEGORY_ORDER = [
    "写作与出版",
    "分析与诊断",
    "逆向工程",
    "视频与视觉",
    "行为与决策",
    "教育与学习",
    "外部收藏",
]
REQUIRED = ["分类", "来源", "一句话"]
FIELD_RE = re.compile(r"^-\s*([^:：]+)[:：]\s*(.+)$")


def parse_card(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    card = {"_path": path}
    for line in text.splitlines():
        if line.startswith("# ") and "名称" not in card:
            card["名称"] = line[2:].strip()
        m = FIELD_RE.match(line.strip())
        if m:
            card[m.group(1).strip()] = m.group(2).strip()
    return card


def main() -> int:
    cards = []
    errors = []
    for path in sorted(CARDS_DIR.rglob("*.md")):
        card = parse_card(path)
        missing = [f for f in REQUIRED if not card.get(f)]
        if not card.get("名称"):
            missing.append("标题(# 名称)")
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: 缺字段 {', '.join(missing)}")
        else:
            cards.append(card)

    if errors:
        print("卡片校验失败：")
        for e in errors:
            print(" -", e)
        return 1

    by_cat = {}
    for c in cards:
        by_cat.setdefault(c["分类"], []).append(c)
    ordered_cats = [c for c in CATEGORY_ORDER if c in by_cat]
    ordered_cats += [c for c in by_cat if c not in CATEGORY_ORDER]

    lines = [
        "# CATALOG · 技能总索引",
        "",
        f"共 {len(cards)} 张卡，{len(ordered_cats)} 个分类。本文件由 `scripts/build_catalog.py` 自动生成，不要手改。",
        "",
    ]
    for cat in ordered_cats:
        lines.append(f"## {cat}")
        lines.append("")
        for c in sorted(by_cat[cat], key=lambda x: x["名称"]):
            rel = c["_path"].relative_to(ROOT)
            lines.append(f"### [{c['名称']}]({rel})")
            lines.append("")
            lines.append(f"- 一句话: {c['一句话']}")
            lines.append(f"- 来源: {c['来源']}")
            if c.get("许可"):
                lines.append(f"- 许可: {c['许可']}")
            if c.get("位置"):
                lines.append(f"- 位置: {c['位置']}")
            if c.get("调用"):
                lines.append(f"- 调用: {c['调用']}")
            lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"OK: {len(cards)} 张卡 -> {OUT.name}（分类: {', '.join(ordered_cats)}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
