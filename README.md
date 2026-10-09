# 월급해부학 링크허브

`@wolgeup_haebu` 프로필 링크용 상품 모음 페이지 (GitHub Pages).

상품 추가:
```
python3 add_product.py --num 6 --date 2026-10-04 --title "10/4 배달비 해부" --category 소비해부 \
  --name "상품명" --price 12900 --url https://link.coupang.com/a/XXXX --emoji 🍱
git add products.json && git commit -m "add product" && git push
```
카테고리: 소비해부 / 최저가 / 육아용품 / 생활용품 / 차량용품 / 아이 축구용품

번호: 영상(포스트) 1개 = 3자리 번호 1개. 같은 포스트 상품은 같은 번호(페이지에 ①② 자동 표기). `--num` 생략 시 자동 지정.
디자인 토큰: BRAND.md
