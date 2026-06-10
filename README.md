# MagicSquare_1004

4×4 **부분 마방진**(빈칸 2개, 1~16, 합 34) 학습자가 빈칸을 채운 뒤 **10선**(행 4 + 열 4 + 대각 2) 합이 34인지 빠르게 확인하고, 틀렸을 때 **어느 줄**인지 바로 짚을 수 있게 하는 검증 프로젝트입니다.

> **한 줄 요약:** 빈칸을 채운 직후, 10선 합 34 여부를 한 번에 판정하고 실패 줄(`R*`/`C*`/`D*`)을 명시한다.

상세 요구사항: [`docs/PRD.md`](docs/PRD.md)

---

## 진짜 문제 (Mom Test)

> 빈칸을 채운 뒤 행·열·대각선 합이 맞다고 믿었지만, **대각선 하나를 빠뜨린 채** 틀린 답을 붙잡고 **20분을 더 썼다**.

| 증거 | 인용 |
|------|------|
| ① | "빈칸 2개 넣고" |
| ② | "행열 대각선 합을 맞췄는데" |
| ③ | "대각선 하나를 빼먹어서 20분 날렸다" |

근거: [`Report/MomTest_워크북.md`](Report/MomTest_워크북.md)

---

## 현재 상태 (세션 3)

| 항목 | 상태 |
|------|------|
| Harness (`pyproject.toml`, `src/`, `tests/`) | ✅ |
| `.cursorrules` · ARRR Command · Skill | ✅ |
| `validate_lines` 구현 | ⏳ 스텁 |
| RED 테스트 (T1~T5) | ⏳ 미작성 |

---

## 빠른 시작

```bash
# 개발 의존성
pip install -e ".[dev]"

# 테스트 (현재: 테스트 함수 없음 → 0 collected)
python -m pytest tests/test_validate_lines.py -v
```

| 요구 | 버전 |
|------|------|
| Python | ≥ 3.11 |
| pytest | ≥ 8.0 (`[dev]` optional) |

---

## 도메인

| 규칙 | 값 |
|------|-----|
| 격자 | 4×4 `list[list[int]]` |
| 빈칸 | `0` (부분 마방진 — 2개) |
| 채워진 칸 | `1~16` |
| 마법 상수 | **34** |
| 10선 ID | `R1`~`R4`, `C1`~`C4`, `D1`(↘), `D2`(↙) |

### 검증 Rule (R1~R5)

| ID | Rule |
|----|------|
| R1~R2 | 각 행·열 합 = 34 |
| R3~R4 | 주대각·부대각 합 = 34 |
| R5 | `0` 포함 → `incomplete` (완성 검증 불가) |

**대각선(D1·D2) 검사 생략 금지** — Mom Test 핵심 실패 조건.

---

## 핵심 API

```python
def validate_lines(grid: list[list[int]]) -> dict:
    # {"status": "pass" | "fail" | "incomplete", "failed_lines": ["R1", "C2", "D1", ...]}
```

| `status` | 조건 | `failed_lines` |
|----------|------|----------------|
| `pass` | 10선 모두 34, 빈칸 없음 | `[]` |
| `fail` | 빈칸 없음, 합≠34 줄 존재 | 틀린 줄 ID **전부** |
| `incomplete` | `0` 1개 이상 | `[]` |

### 정답 격자 예 (T1 Green)

```python
[[16,  3,  2, 13],
 [ 5, 10, 11,  8],
 [ 9,  6,  7, 12],
 [ 4, 15, 14,  1]]
```

---

## Test Loop (세션 3)

| ID | 유형 | 기대 |
|----|------|------|
| T1 | Green | `pass` |
| T2 | Red | `fail`, `R*`/`C*` 포함 |
| T3 | Red | `incomplete` |
| T4 | Red | `fail`, `D1` 또는 `D2` |
| T5 | Red | 복수 `failed_lines` |

파일: `tests/test_validate_lines.py`

---

## TDD · ARRR

```
RED (tests/만) → GREEN (src/ 최소) → REFACTOR (계약 불변)
```

### ARRR 실습 순서

```
/red-test-plan → /red-skeleton → /green-minimal → /golden-master
→ /refactor-smell → /refactor-safe → /export-session
```

| Command | ARRR | 설명 |
|---------|------|------|
| `/red-test-plan` | Ask | C2C 설계표 (파일 없음) |
| `/red-skeleton` | Agent | `pytest.fail` 스켈레톤 |
| `/green-minimal` | Agent | 최소 구현 |
| `/golden-master` | Agent | Golden (PASS 후) |
| `/refactor-smell` | Ask | 스멜 표 |
| `/refactor-safe` | Agent | 스멜 1개 리팩터 |
| `/export-session` | Repeat | Report + Transcript |
| `/tdd-red` | RED | 세션 3 단순 RED |

Skill: `.cursor/skills/magic-square-tdd/` · `.cursor/skills/magic-square-docs/`

---

## 하지 않을 것 (세션 3)

| 제외 | 이유 |
|------|------|
| Solver / 빈칸 자동 채우기 | pain은 **맞는지 확인** |
| PyQt / UI | 표면 솔루션 |
| 1~16 중복·범위 검증 | 후속 Entity |
| ECB 전체 한꺼번에 | `validate_lines` 집중 |

---

## 프로젝트 구조

```
MagicSquare_xx/
├── .cursorrules
├── .cursor/
│   ├── commands/              # ARRR 슬래시 Command
│   └── skills/                # magic-square-tdd, magic-square-docs
├── docs/
│   └── PRD.md
├── src/
│   └── validate_lines.py      # 세션 3 Command (스텁)
├── tests/
│   └── test_validate_lines.py
├── Report/                    # NN.REPORT.md
├── Prompt/                    # NN.Export-Transcript.md
└── pyproject.toml
```

---

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | 제품 요구사항 (SSOT) |
| [Report/MomTest_워크북.md](Report/MomTest_워크북.md) | Mom Test 인터뷰 |
| [Report/3. Session3_Workbook.md](Report/3.%20Session3_Workbook.md) | R-G-I-O · SC · 8계층 |
| [Report/01.REPORT.md](Report/01.REPORT.md) | Harness·Command 준비 |
| [Prompt/MomTest_인터뷰.md](Prompt/MomTest_인터뷰.md) | Mom Test 프롬프트 |

---

## 다음 단계

1. `/tdd-red` 또는 `/red-skeleton` — T2 Red 테스트 작성 → **FAIL** 확인
2. `/green-minimal` — `src/validate_lines.py` 최소 구현 → **PASS**
3. T3~T5 · T1 순차 GREEN
4. `/export-session` — 세션 Export

---

## 후속 (세션 4+)

PRD §10 참고 — **현재 범위 밖**

| Track | 예시 |
|-------|------|
| **B — Logic** | `D-LOC-01` `find_blank_coords`, G1 격자 |
| **A — UI** | `U-IN-01` 입력 검증 (`E003` 등) |

---

*MagicSquare_1004 · 저장소 `MagicSquare_xx` · PRD v0.1*
