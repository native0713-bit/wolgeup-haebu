# 월급해부학 브랜드 토큰

링크허브(index.html의 `:root`)와 같은 값입니다. 릴스 커버·썸네일·헤더 이미지에도 이 값을 그대로 쓰세요.

## 컬러
| 토큰 | HEX | 용도 |
|---|---|---|
| Navy | `#0F1B3D` | 메인 배경·로고·선택된 탭·고정 배너 |
| Navy 2 | `#1C2B57` | 그라데이션 끝, 보조 텍스트(진한) |
| Navy Tint | `#EEF1F8` | 썸네일 원 배경, 카테고리 칩 |
| Coral | `#FF6B5B` | 포인트(CTA 버튼, 강조 단어, 점) |
| Coral Deep | `#E8503F` | 번호 텍스트(`006번`), 눌림 상태 |
| Coral Soft | `#FFEDEA` | 번호 칩 배경, 부드러운 강조 면 |
| Background | `#F4F6FA` | 페이지/커버 바탕 |
| Surface | `#FFFFFF` | 카드·버튼 면 |
| Text | `#191F28` | 본문 |
| Sub | `#6B7684` | 보조 설명 |
| Muted | `#9AA3AE` | 캡션, 플레이스홀더 |
| Line | `#E5E8EB` | 구분선, 테두리 |

규칙: 한 화면에 Coral은 "가장 중요한 1곳"에만. 나머지는 Navy + 무채색.

## 타이포그래피
- 서체: **Pretendard** (웹: `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css`)
- 자간: 기본 -1%, 제목 -2~-3%. 줄바꿈 `word-break: keep-all`.
- 숫자(번호·가격): 고정폭 숫자 `font-variant-numeric: tabular-nums`.

| 스타일 | 크기/굵기 | 예시 |
|---|---|---|
| Display | 24px / 800 | 월급해부학 |
| Section | 17px / 800 | 🥇최근 영상 속 제품 |
| Title | 17px / 700 | 10/3 커피값 해부 |
| Body | 15px / 600 | 상품명, 버튼 라벨 |
| Number | 15px / 800, Coral Deep | 006번① |
| Caption | 12–12.5px / 500, Sub | 작성일 기준 가격 |

릴스/커버(1080px 기준)는 위 크기 × 약 3 (Display ≈ 72px, Body ≈ 45px).

## 형태
- 필 버튼: 높이 68px, 완전 둥근 모서리(999px), 흰 면 + 그림자 `0 1px 2px rgba(15,27,61,.04), 0 6px 20px rgba(15,27,61,.06)`
- 썸네일: 지름 44px 원, 배경 Navy Tint, 이모지 22px — 모든 상품 동일
- 카드 모서리 20px, CTA 버튼 모서리 14px / 높이 50px
- 여백: 좌우 20px, 섹션 간 36–44px, 버튼 간 12px

## 번호 규칙
영상(포스트) 1개 = 번호 1개(3자리). 한 영상에 상품이 여러 개면 `006번①`, `006번②`.
