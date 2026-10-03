#!/usr/bin/env python3
"""월급해부학 링크허브 - 상품 추가 스크립트

예시:
  python3 add_product.py --date 2026-10-04 --title "10/4 배달비 해부" \
      --category 소비해부 --name "상품명" --price 12900 \
      --url https://link.coupang.com/a/XXXX --emoji 🍱

같은 날짜+제목의 포스트가 있으면 그 포스트에 상품을 추가하고,
없으면 새 포스트를 만들어 맨 위(최신순)에 둡니다.
"""
import argparse, json, re, sys
from pathlib import Path

CATS = ["소비해부", "최저가", "육아용품", "생활용품", "차량용품", "아이 축구용품"]
PATH = Path(__file__).with_name("products.json")

def main():
    p = argparse.ArgumentParser(description="products.json에 상품 추가")
    p.add_argument("--date", required=True, help="YYYY-MM-DD (작성일)")
    p.add_argument("--title", required=True, help='포스트 제목, 예: "10/4 배달비 해부"')
    p.add_argument("--category", required=True, choices=CATS)
    p.add_argument("--name", required=True)
    p.add_argument("--price", required=True, help="숫자 (예: 16900 또는 16,900)")
    p.add_argument("--url", required=True)
    p.add_argument("--emoji", default="🛒")
    a = p.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
        sys.exit("날짜 형식은 YYYY-MM-DD 입니다.")
    if not a.url.startswith("https://"):
        sys.exit("URL은 https:// 로 시작해야 합니다.")
    price = int(re.sub(r"[^\d]", "", a.price))

    data = json.loads(PATH.read_text(encoding="utf-8")) if PATH.exists() else {"posts": []}
    post = next((x for x in data["posts"] if x["date"] == a.date and x["title"] == a.title), None)
    if post is None:
        post = {"id": f"{a.date}-{len(data['posts'])+1}", "date": a.date, "title": a.title,
                "category": a.category, "products": []}
        data["posts"].append(post)
    post["products"].append({"name": a.name, "price": price, "url": a.url, "emoji": a.emoji})
    data["posts"].sort(key=lambda x: x["date"], reverse=True)

    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"추가 완료: [{a.category}] {a.title} / {a.name} {price:,}원")

if __name__ == "__main__":
    main()
