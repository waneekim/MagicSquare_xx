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

근거: [`docs/PRD.md` §7](docs/PRD.md#7-테스트-케이스-test-loop--세션-3) · 파일: `tests/test_validate_lines.py`

```bash
python -m pytest tests/test_validate_lines.py -v
```

### 요약

| ID | 유형 | 검증 의도 | 기대 `status` | 기대 `failed_lines` |
|----|------|-----------|---------------|---------------------|
| **T1** | Green | 정답 완성 격자 10선 통과 | `pass` | `[]` |
| **T2** | Red | 행·열 합 ≠ 34 즉시 재현 | `fail` | `R2`, `C2` 포함 |
| **T3** | Red | 빈칸(0) 있으면 완성 검증 불가 (R5) | `incomplete` | `[]` |
| **T4** | Red | **대각선(D1·D2) 검사 누락 방지** (Mom Test) | `fail` | `D1` 또는 `D2` 포함 |
| **T5** | Red | 복수 줄 동시 실패 — 누락 없이 전부 반환 | `fail` | 틀린 줄 ID **전부** |

### AC 매핑

| AC | 기준 | Test ID |
|----|------|---------|
| AC1 | 10선(행·열·**대각 2개**) 한 번에 검증 | T1, T4 |
| AC2 | 합≠34 → `fail` + `failed_lines` | T2, T5 |
| AC3 | 정답 완성 → `pass` | T1 |
| AC4 | `0` 포함 → `incomplete` | T3 |
| AC5 | Red·Green 자동 재현 | T1~T5 |
| AC6 | 실패 줄 ID 명시 | T2, T4, T5 |

### 실행 순서 (TDD)

| 단계 | Test ID | 이유 |
|------|---------|------|
| 1 | **T2** | 첫 RED — 행·열 `fail` + `failed_lines` 계약 확립 |
| 2 | T3 | `incomplete` 분기 (R5) |
| 3 | T4 | 대각선 검사 필수 (Mom Test 핵심) |
| 4 | T5 | 복수 `failed_lines` 누락 없음 |
| 5 | **T1** | Green — 정답 `pass` 확정 |

---

## 테스트 플랜 (T1~T5)

공통 **When:** `result = validate_lines(grid)`  
공통 **Assert:** `result["status"]`, `result["failed_lines"]` (키 이름·10선 ID 고정)

### T1 — Green · 정답 완성

| 항목 | 내용 |
|------|------|
| **유형** | Green |
| **Given** | PRD §2.4 과제 슬라이드 정답 4×4 (빈칸 없음) |
| **When** | `validate_lines(grid)` |
| **Then** | `status == "pass"`, `failed_lines == []` |
| **AC** | AC3, AC5 |
| **함수명 (권장)** | `test_t1_pass_on_complete_answer_grid` |

```python
grid_t1 = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]
```

| 10선 | 합 | 10선 | 합 |
|------|-----|------|-----|
| R1~R4 | 각 34 | C1~C4 | 각 34 |
| D1 ↘ | 34 | D2 ↙ | 34 |

---

### T2 — Red · 행·열 교차 셀 변경

| 항목 | 내용 |
|------|------|
| **유형** | Red |
| **Given** | T1 기준, **R2∩C2** 교차 셀 `(1,1)` 값 `10→11` |
| **When** | `validate_lines(grid)` |
| **Then** | `status == "fail"`, `"R2" in failed_lines`, `"C2" in failed_lines` |
| **AC** | AC2, AC6 |
| **함수명 (권장)** | `test_t2_fail_r2_and_c2_when_intersection_cell_changed` |
| **RED 실패** | 스텁 `...` → `AssertionError` |

```python
grid_t2 = [
    [16,  3,  2, 13],
    [ 5, 11, 11,  8],  # (1,1): 10→11 → R2·C2 동시 ≠34
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]
```

| 깨진 줄 | 합 | 비고 |
|---------|-----|------|
| R2 | 35 | 5+11+11+8 |
| C2 | 35 | 3+11+6+15 |
| D1, D2 | 34 | 대각선은 유지 — 행·열만 깨는 케이스 |

---

### T3 — Red · 빈칸(0) 포함

| 항목 | 내용 |
|------|------|
| **유형** | Red |
| **Given** | 완성 격자에 빈칸 `0` 1개 이상 (예: `(1,3)`) |
| **When** | `validate_lines(grid)` |
| **Then** | `status == "incomplete"`, `failed_lines == []` |
| **AC** | AC4 |
| **함수명 (권장)** | `test_t3_incomplete_when_blank_cell_exists` |
| **Invariant** | R5 — `0 in grid`이면 10선 검사 없이 `incomplete` |

```python
grid_t3 = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  0],  # (1,3) 빈칸
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]
```

---

### T4 — Red · 대각선만 ≠ 34 (행·열은 34)

| 항목 | 내용 |
|------|------|
| **유형** | Red |
| **Given** | **반마방진** — 행·열 8선 합은 각 34, 대각선(D1·D2)만 ≠34 |
| **When** | `validate_lines(grid)` |
| **Then** | `status == "fail"`, `"D1" in failed_lines`, `"D2" in failed_lines` |
| **AC** | AC1, AC6 — Mom Test: "대각선 하나를 빼먹어서" 방지 |
| **함수명 (권장)** | `test_t4_fail_diagonals_when_rows_and_cols_are_34` |
| **Invariant** | D1·D2 검사 **생략 금지** (`.cursorrules`) |

```python
# 행·열 34, D1=31, D2=49 (반마방진)
grid_t4 = [
    [ 7, 12,  1, 14],
    [14,  8, 11,  1],
    [ 2, 13,  8, 11],
    [11,  1, 14,  8],
]
```

| 10선 | 합 | 판정 |
|------|-----|------|
| R1~R4, C1~C4 | 각 34 | 통과 |
| D1 ↘ | 31 | **실패** |
| D2 ↙ | 49 | **실패** |

> 행·열만 검산하면 "맞다"고 착각하는 상황을 재현한다. 구현은 **반드시 D1·D2**를 검사해야 T4·T1이 통과한다.

---

### T5 — Red · 여러 줄 동시 실패

| 항목 | 내용 |
|------|------|
| **유형** | Red |
| **Given** | T1 기준, 한 셀 변경으로 **R1·C1·D1** 동시 ≠34 |
| **When** | `validate_lines(grid)` |
| **Then** | `status == "fail"`, `failed_lines`에 `R1`, `C1`, `D1` **모두** 포함 (누락 없음) |
| **AC** | AC2, AC6 |
| **함수명 (권장)** | `test_t5_fail_multiple_lines_all_reported` |

```python
grid_t5 = [
    [15,  3,  2, 13],  # (0,0): 16→15
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]
```

| 깨진 줄 | 합 |
|---------|-----|
| R1 | 33 |
| C1 | 33 |
| D1 | 33 |

**Assert 예시:**

```python
assert result["status"] == "fail"
assert set(result["failed_lines"]) >= {"R1", "C1", "D1"}
```

---

### C2C 요약표

| Test ID | Given | When | Then |
|---------|-------|------|------|
| T1 | `grid_t1` (§2.4 정답) | `validate_lines(grid)` | `pass`, `[]` |
| T2 | `grid_t2` (R2∩C2 셀 변경) | 동일 | `fail`, `R2`·`C2` ∈ `failed_lines` |
| T3 | `grid_t3` (`0` 포함) | 동일 | `incomplete`, `[]` |
| T4 | `grid_t4` (행·열 34, 대각 ≠34) | 동일 | `fail`, `D1`·`D2` ∈ `failed_lines` |
| T5 | `grid_t5` (복수 줄 실패) | 동일 | `fail`, `R1`·`C1`·`D1` ⊆ `failed_lines` |

### pytest 명령 (개별)

```bash
python -m pytest tests/test_validate_lines.py::test_t2_fail_r2_and_c2_when_intersection_cell_changed -v
python -m pytest tests/test_validate_lines.py::test_t3_incomplete_when_blank_cell_exists -v
python -m pytest tests/test_validate_lines.py::test_t4_fail_diagonals_when_rows_and_cols_are_34 -v
python -m pytest tests/test_validate_lines.py::test_t5_fail_multiple_lines_all_reported -v
python -m pytest tests/test_validate_lines.py::test_t1_pass_on_complete_answer_grid -v
```

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
