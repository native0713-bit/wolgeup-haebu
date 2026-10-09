#!/usr/bin/env python3
"""월급해부학 링크허브 - 상품 추가 스크립트

예시:
  python3 add_product.py --num 6 --date 2026-10-10 --title "10/10 버블 놀이" \
      --category 육아용품 --name "상품명" --price 12900 \
      --url https://link.coupang.com/a/XXXX --emoji 🫧

번호(--num) 규칙: 포스트(영상) 1개 = 번호 1개. 같은 포스트의 상품은 같은 번호를 쓰고,
페이지에서 자동으로 006번① 006번② 처럼 표시됩니다.
--num 을 생략하면: 같은 포스트가 있으면 그 번호, 없으면 (최대 번호 + 1)을 씁니다.

같은 날짜+제목의 포스트가 있으면 그 포스트에 상품을 추가하고,
없으면 새 포스트를 만들어 맨 위(최신순)에 둡니다.
"""
import argparse, json, re, sys
from pathlib import Path

CATS = ["소비해부", "최저가", "육아용품", "생활용품", "차량용품", "아이 축구용품"]
PATH = Path(__file__).with_name("products.json")

def all_nums(data):
    return [int(x["num"]) for p in data["posts"] for x in p["products"] if str(x.get("num", "")).isdigit()]

def main():
    p = argparse.ArgumentParser(description="products.json에 상품 추가")
    p.add_argument("--num", help="상품 번호 1~999 (3자리로 저장, 예: 6 → 006). 생략 시 자동")
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

    if a.num is not None:
        if not re.fullmatch(r"\d{1,3}", a.num) or not 1 <= int(a.num) <= 999:
            sys.exit("--num 은 1~999 숫자여야 합니다.")
        num = f"{int(a.num):03d}"
        # 다른 포스트가 이미 쓰는 번호인지 확인
        for q in data["posts"]:
            if q is not post and any(x.get("num") == num for x in q["products"]):
                sys.exit(f"{num}번은 이미 '{q['title']}' 포스트에서 사용 중입니다.")
    elif post and post["products"]:
        num = post["products"][0]["num"]
    else:
        num = f"{max(all_nums(data), default=0) + 1:03d}"

    if post is None:
        post = {"id": f"{a.date}-{num}", "date": a.date, "title": a.title,
                "category": a.category, "products": []}
        data["posts"].append(post)
    post["products"].append({"num": num, "name": a.name, "price": price, "url": a.url, "emoji": a.emoji})
    data["posts"].sort(key=lambda x: (x["products"][0]["num"] if x["products"] else "", x["date"]), reverse=True)

    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    nxt = max(all_nums(data)) + 1
    print(f"추가 완료: {num}번 [{a.category}] {a.title} / {a.name} {price:,}원  (다음 새 포스트 번호: {nxt:03d})")

if __name__ == "__main__":
    main()
