---
name: magic-square-tdd
description: MagicSquare_1004 Dual-Track TDD ARRR 워크플로. RED/GREEN/REFACTOR, validate_lines, D-*/U-* Test ID, ECB·Mock 규칙. TDD·ARRR Command 사용 시 적용.
---

# magic-square-tdd

MagicSquare_1004 · Dual-Track TDD · ARRR · ECB SSOT.

**읽기 순서:** `.cursorrules` → `docs/PRD.md` → 본 Skill

---

## ARRR ↔ Command

| ARRR | 단계 | Command | 모드 | 수정 범위 |
|------|------|---------|------|-----------|
| **A — Ask** | RED ③ 설계 | `/red-test-plan` | Ask | 없음 |
| **A — Ask** | RED ④ 스켈레톤 | `/red-skeleton` | Agent | `tests/`만 |
| **R — Respond** | GREEN | `/green-minimal` | Agent | `src/` + 해당 tests |
| **R — Respond** | Golden | `/golden-master` | Agent | `tests/` golden |
| **R — Refine** | 스멜 | `/refactor-smell` | Ask | 없음 |
| **R — Refine** | 안전 리팩터 | `/refactor-safe` | Agent | Budget 내 `src/` |
| **R — Repeat** | Export | `/export-session` | Agent | Report·Prompt |

**세션 3 단순 RED:** `/tdd-red` (`tests/`만, `validate_lines` T1~T5)

**실습 순서:**

```
/red-test-plan → /red-skeleton → /green-minimal → /golden-master
→ /refactor-smell → /refactor-safe → /export-session
```

---

## Phase 선언 (TDD 응답 첫 줄)

```
Phase: red | Layer: entity | Track: Logic | ID: D-LOC-01
Phase: green | Layer: entity | Track: Logic | ID: D-LOC-01
Phase: refactor | Layer: command | Track: Logic | Step: smell
```

| Layer | Track | 경로 |
|-------|-------|------|
| `entity` | Logic (B) | `tests/entity/`, `src/entity/` |
| `boundary` | UI (A) | `tests/boundary/`, `src/boundary/` |
| `command` | Logic | `tests/test_validate_lines.py`, `src/validate_lines.py` |

---

## 도메인 SSOT

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 `list[list[int]]` |
| 빈칸 | `0` (정확히 2개 — 부분 마방진) |
| 값 | `1~16` |
| 마법 상수 | `34` |
| 10선 ID | `R1`~`R4`, `C1`~`C4`, `D1`, `D2` |

### validate_lines 계약

```python
def validate_lines(grid) -> {"status": "pass"|"fail"|"incomplete", "failed_lines": [...]}
```

| status | 조건 |
|--------|------|
| `pass` | 10선 합 34, 빈칸 없음 |
| `fail` | 빈칸 없음, 합≠34 줄 존재 |
| `incomplete` | `0` 포함, `failed_lines=[]` |

---

## Test ID (참고)

### 세션 3 — Command (`validate_lines`)

| ID | 유형 | 기대 |
|----|------|------|
| T1 | Green | `pass` |
| T2 | Red | `fail`, R*/C* |
| T3 | Red | `incomplete` |
| T4 | Red | `fail`, D1/D2 |
| T5 | Red | 복수 failed_lines |

### Track B — Entity (`D-*`)

| ID | FR | 함수 | Then (예) |
|----|-----|------|-----------|
| D-LOC-01 | FR-LOC-01 | `find_blank_coords` | `[(2,3),(4,4)]` |
| D-MIS-01 | FR-MIS-01 | `find_not_exist_nums` | `[7,10]` |
| D-SOL-01 | FR-SOL-01 | `solution` | Step A 성공 |

### Track A — Boundary (`U-*`)

| ID | Given | Then |
|----|-------|------|
| U-IN-01 | `grid=None` | `E003` |
| U-IN-02 | 셀 `17` | `E002` |

**RED 권장 순서:** `D-VAL-04` → `D-VAL-05` → … → `D-LOC-01` → `U-IN-*`

---

## TDD 규칙

| 규칙 | 내용 |
|------|------|
| RED 1턴 | Test ID **1묶음** |
| RED | `tests/`만 · `pytest.fail` 또는 ImportError |
| GREEN | 최소 구현 · fail→assert |
| REFACTOR | 계약·테스트·golden 불변 |
| 금지 | assert 완화 · skip · xfail |

---

## ECB · Mock

| Track | Domain Mock | E001~E005 |
|-------|-------------|-----------|
| Logic (B) | **금지** | entity emit **금지** |
| UI (A) | 허용 | boundary **전담** |

**import:** entity → boundary/control **금지**

| 코드 | 의미 |
|------|------|
| E001 | 격자 크기 |
| E002 | 값 범위 |
| E003 | None 입력 |
| E004 | 타입 |
| E005 | 예약 |

---

## G1 격자 SSOT (PRD §10.2)

```text
[[16,  3,  2, 13],
 [ 5, 10,  0,  8],
 [ 9,  6,  7, 12],
 [ 4, 15, 14,  0]]
```

- 0-index 빈칸: `(1,2)`, `(3,3)`
- 1-index row-major: `(2,3)`, `(4,4)`
- 픽스처: `grid_g1` (`tests/conftest.py`)

---

## REFACTOR Budget

파일≤3 · 클래스≤1 · 메서드≤3

---

## Git

`git commit` / `git push` / 브랜치 — **사용자 명시 요청 시만**
