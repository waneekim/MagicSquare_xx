# MagicSquare_1004 — PRD (Product Requirements Document)

| 항목 | 내용 |
|------|------|
| 프로젝트 | MagicSquare_1004 (`MagicSquare_xx`) |
| 버전 | 0.1 |
| 생성일 | 2026-06-10 |
| 근거 | [Report/MomTest_워크북.md](../Report/MomTest_워크북.md) · [Report/3. Session3_Workbook.md](../Report/3.%20Session3_Workbook.md) · [Report/01.REPORT.md](../Report/01.REPORT.md) |
| SSOT | [`.cursorrules`](../.cursorrules) · 본 PRD · [`.cursor/skills/magic-square-tdd/SKILL.md`](../.cursor/skills/magic-square-tdd/SKILL.md) |

---

## 1. 개요

### 1.1 배경

4×4 **부분** 마방진(빈칸 2개, 1~16, 합 34)을 손으로/코드로 다루는 학습자는, 빈칸을 채운 **직후** **10선**(행 4 + 열 4 + 주대각 1 + 부대각 1) 합이 34인지 확인하는 데 시간이 많이 든다. 특히 **대각선 한 줄을 빼먹은 채** “맞다”고 판정하면 같은 시도를 반복하며 시간을 잃는다.

**Mom Test 증거 (실제 인터뷰 — [Report/MomTest_워크북.md](../Report/MomTest_워크북.md)):**

1. "빈칸 2개 넣고"
2. "행열 대각선 합을 맞췄는데"
3. "대각선 하나를 빼먹어서 20분 날렸다"

### 1.2 표면 문제 (금지 — 솔루션 혼입)

> "4×4 부분 마방진용 **검증 프로그램을 만들면**, 행·열·대각선 합을 자동으로 확인할 수 있다."

### 1.3 진짜 문제 (한 문장)

> 빈칸을 채운 뒤 행·열·대각선 합이 맞다고 믿었지만, **대각선 하나를 빠뜨린 채** 틀린 답을 붙잡고 **20분을 더 썼다**.

**PRD 관점 재정의:**

> 4×4 부분 마방진에서 빈칸 2개를 채운 뒤 **10선 합 34 여부를 확인할 때 일부 줄(특히 대각선)을 빼먹어** 맞는지 판정하지 못하고, 같은 시도를 반복하며 **20분** 같은 시간을 잃는다.

### 1.4 주제 (1문장)

> **4×4 부분 마방진에서 빈칸을 채운 직후, 행·열·대각선 10선이 각각 34인지 빠르게 확정하고, 틀리면 어느 줄인지 바로 짚을 수 있게 검증 규칙과 테스트 루프를 만든다.**

### 1.5 이번 릴리스 목표 (세션 3)

**판정·확인 비용**을 줄이기 위해 다음만 제공한다.

| 계층 | 산출물 |
|------|--------|
| **Rule** | R1~R5 (10선 합 34, incomplete) |
| **Command** | `validate_lines(grid)` |
| **(Skill)** | `magic-square-tdd`, ARRR Command |
| **Test Loop** | T1~T5 (pytest) |

**의도적 배제:** Solver, PyQt UI, ECB 전체, 1~16 중복·범위 검증 — Mom Test **표면 솔루션** 또는 **후속 세션**.

### 1.6 현재 구현 상태 ([Report/01.REPORT.md](../Report/01.REPORT.md))

| 항목 | 상태 |
|------|------|
| Harness | `pyproject.toml`, `src/validate_lines.py` 스텁, `tests/test_validate_lines.py` import만 |
| `.cursorrules` | ✅ |
| ARRR Command·Skill | ✅ (인프라 준비) |
| RED 테스트 본문 | ⏳ 미작성 (T2~T5 대기) |
| `validate_lines` 구현 | ⏳ 스텁 (`...`) |

---

## 2. 사용자 및 사용 시나리오

### 2.1 R-G-I-O

| | 내용 |
|---|---|
| **R — Role** | 4×4 **부분** 마방진 학습자. 빈칸 2개(0)를 1~16으로 채운 뒤 **맞았는지 스스로 확인**해야 함 |
| **G — Goal** | 빈칸 채운 후 **10선 합 34 여부를 즉시 판정**하고, 틀리면 **어느 행·열·대각선(R1~R4, C1~C4, D1, D2)** 인지 식별 *(20분 낭비 → 처음·한 번에)* |
| **I — Input** | 4×4 정수 격자 `list[list[int]]`. 셀 값 **0**(빈칸) 또는 **1~16** |
| **O — Output** | `validate_lines` 반환: `status` (`pass` \| `fail` \| `incomplete`) + `failed_lines` (실패 줄 ID 목록) |

### 2.2 페르소나

| 항목 | 내용 |
|------|------|
| 역할 | 4×4 부분 마방진 학습자 |
| 행동 범위 | 손으로 풀기 / 코드로 다루기 |
| 도메인 | 4×4 격자, **빈칸 2개(0)**, **1~16**, **합 34**, **10선** |

### 2.3 예시 격자 (과제 기준 — 부분)

| | | | |
|---|---|---|---|
| 16 | 3 | 2 | 13 |
| 5 | 10 | 11 | **?** |
| 9 | 6 | **?** | 12 |
| 4 | 15 | 14 | 1 |

*(빈칸 0-index: `(1,3)`, `(2,2)`)*

### 2.4 예시 격자 (정답 완성 — T1 Green)

```text
[[16,  3,  2, 13],
 [ 5, 10, 11,  8],
 [ 9,  6,  7, 12],
 [ 4, 15, 14,  1]]
```

### 2.5 핵심 시나리오

1. 학습자가 4×4 격자에 빈칸 2칸을 1~16 값으로 채운다.
2. **`validate_lines(grid)`** 한 번으로 10선 합을 검사한다.
3. **`pass`** → 완료. **`fail`** → `failed_lines`로 어느 줄이 34가 아닌지 확인 후 수정.
4. **`incomplete`** (0 포함) → 완성 검증 불가, 빈칸 채우기 선행.
5. **Test Loop**(T1~T5)로 Red → Green 재현.

---

## 3. 도메인 규칙

### 3.1 MagicSquare 정의

| ID | 규칙 | 설명 |
|----|------|------|
| R-01 | 격자 | 4×4 정수 배열 |
| R-02 | 값 범위 | **0** = 빈칸, **1~16** = 채워진 칸 |
| R-03 | 빈칸 | 정확히 **2개** (0) — 부분 마방진 입력 가정 |
| R-04 | 마법 상수 | **34** |
| R-05 | 10선 | 행 4 + 열 4 + 주대각 `D1` + 부대각 `D2` |

### 3.2 검증 Rule (세션 3 — `validate_lines`)

| ID | Rule | 실패 조건 |
|----|------|-----------|
| R1 | 각 **행** `R1`~`R4` 합 = 34 | `sum(row) ≠ 34` |
| R2 | 각 **열** `C1`~`C4` 합 = 34 | `sum(col) ≠ 34` |
| R3 | **주대각** `D1` `(0,0)(1,1)(2,2)(3,3)` 합 = 34 | `sum ≠ 34` |
| R4 | **부대각** `D2` `(3,0)(2,1)(1,2)(0,3)` 합 = 34 | `sum ≠ 34` |
| R5 | 격자에 **0(빈칸)** 있으면 완성 검증 불가 | `0 in grid` → `incomplete` |

**대각선(D1·D2) 검사 생략 금지** — Mom Test 핵심 실패 조건.

### 3.3 10선 ID (1-index, `.cursorrules` SSOT)

| ID | 의미 |
|----|------|
| `R1`~`R4` | 1~4행 |
| `C1`~`C4` | 1~4열 |
| `D1` | 주대각선 ↘ |
| `D2` | 부대각선 ↙ |

---

## 4. 기능 요구사항

### 4.1 In Scope (세션 3)

| ID | 계층 | 요구사항 | 우선순위 |
|----|------|----------|----------|
| F1 | **Rule** | R1~R5 정의 (본 PRD §3.2, `.cursorrules`) | P0 |
| F2 | **Command** | 4×4 격자 입력 → 10선 각 합 계산 | P0 |
| F3 | **Command** | 각 줄 합과 34 비교 → `pass` / `fail` / `incomplete` | P0 |
| F4 | **Command** | `fail` 시 **틀린 줄 ID** 전부 `failed_lines`에 반환 | P0 |
| F5 | **Test Loop** | T2~T5 Red 테스트 (실패 재현) | P0 |
| F6 | **Test Loop** | T1 Green 테스트 (정답 통과) | P0 |
| F7 | **(Skill)** | ARRR Command + `magic-square-tdd` | P1 |
| F8 | **Harness** | `pyproject.toml`, `src/`, `tests/` 골격 | P0 |

**핵심 Command:**

```python
def validate_lines(grid: list[list[int]]) -> dict:
    # {"status": "pass" | "fail" | "incomplete", "failed_lines": ["R1", "C2", "D1", ...]}
```

### 4.2 Out of Scope (표면 문제 — 하지 않음)

| 제외 | 이유 (Mom Test) |
|------|-----------------|
| `Solver` / 빈칸 자동 채우기 / 힌트 | pain은 **풀기**보다 **맞는지 확인** |
| PyQt / `GridUI` / 입력 편집기 | UI는 **표면 솔루션** |
| ECB 전체 한꺼번에 (`MissingFinder`, `Solver` 등) | 세션 3은 **validate_lines** 집중 |
| 1~16 **중복·범위** 검증 | 세션 3 범위 밖 — **합 34 판정** 우선 |
| 풀이 공유·Mom Test 미검증 기능 | 증거 없음 — Won't |
| `git commit` 자동화 | 사용자 명시 요청 시만 |

---

## 5. 입출력 명세

### 5.1 Input

```text
grid: list[list[int]]  # 4×4, 값 0 또는 1~16
```

### 5.2 Output

```text
{
  "status": "pass" | "fail" | "incomplete",
  "failed_lines": ["R1", "C2", "D1", ...]  # fail 시 틀린 줄 전부; incomplete/pass 시 []
}
```

| status | 조건 | failed_lines |
|--------|------|--------------|
| `pass` | 10선 모두 34, `0` 없음 | `[]` |
| `fail` | `0` 없음, 합≠34 줄 1개 이상 | 해당 ID **전부** (누락 없음) |
| `incomplete` | `0` 1개 이상 | `[]` |

---

## 6. 성공 기준 (Acceptance Criteria)

| # | 기준 | Mom Test 증거 | 세션 3 Test ID |
|---|------|---------------|----------------|
| **AC1** | 단일 Command로 **10선** 합 검증 (행·열·**대각 2개** 누락 없음) | ② "행·열·**대각선** 합 맞췄는데 **대각선 하나를 빼먹어서**" | T1, T4 |
| **AC2** | 합≠34 격자 → `fail`, **최소 1개** `failed_lines` | ③ "20분 날렸다" → 즉시 재현 | T2, T5 |
| **AC3** | 정답 완성 격자 → `pass` | Green 기준 | T1 |
| **AC4** | 빈칸(0) 포함 → `incomplete`, pass 아님 | 미완성 판정 | T3 |
| **AC5** | Test Loop Red·Green **자동 재현** | ③ 확인·재작업 비용 감소 | T1~T5 |
| **AC6** | 실패 시 **어느 줄**인지 `failed_lines` 명시 (10선 전부 검사) | "어느 줄이 34가 아닌지" | T2, T4, T5 |

### 6.1 워크북 SC 매핑 ([Report/3. Session3_Workbook.md](../Report/3.%20Session3_Workbook.md))

| 워크북 | PRD 세션 3 범위 |
|--------|------------------|
| SC1 (10선 한 번에) | AC1 — **In Scope** |
| SC2 (1~16 중복·범위) | **Out of Scope** — 후속 Entity |
| SC3 (테스트 통과 → 확신) | AC5 — Test Loop |

---

## 7. 테스트 케이스 (Test Loop — 세션 3)

| ID | 유형 | 설명 | 기대 |
|----|------|------|------|
| **T1** | Green | 과제 슬라이드 **정답** 4×4 (§2.4) | `status=pass`, `failed_lines=[]` |
| **T2** | Red | 행·열 합 ≠ 34 (예: R2·C2 교차 셀 변경) | `status=fail`, `R2`·`C2` ∈ `failed_lines` |
| **T3** | Red | 빈칸(0) 1개 이상 | `status=incomplete`, `failed_lines=[]` |
| **T4** | Red | 대각선만 ≠ 34 (행·열은 34) | `status=fail`, `D1` 또는 `D2` ∈ `failed_lines` |
| **T5** | Red | 여러 줄 동시 실패 | 모든 틀린 줄 ID 반환 |

**파일:** `tests/test_validate_lines.py`  
**명령:** `python -m pytest tests/test_validate_lines.py -v`

---

## 8. C2C 추적 (Rule 1~3 — RED 설계용)

| 항목 | 세션 3 (`validate_lines`) |
|------|---------------------------|
| **Rule 1** | 격자 4×4 |
| **Rule 2** | 셀 값 `0` 또는 `1~16` |
| **Rule 3** | 10선 합 34 · `0` 있으면 `incomplete` |
| **PRD ID** | F2~F4 |
| **To-Do** | `src/validate_lines.py` — 10선 검사, `failed_lines` 반환 |
| **Test ID** | T1~T5 |

---

## 9. ARRR · Cursor 8계층

### 9.1 ARRR ↔ Command

| ARRR | Command | 모드 |
|------|---------|------|
| **A — Ask** | `/red-test-plan` → `/red-skeleton` | Ask → Agent |
| **R — Respond** | `/green-minimal` → `/golden-master` | Agent |
| **R — Refine** | `/refactor-smell` → `/refactor-safe` | Ask → Agent |
| **R — Repeat** | `/export-session` | Agent |

**세션 3 단순 RED:** `/tdd-red`

### 9.2 8계층 매핑 (세션 3)

| 계층 | PRD | 산출물 |
|------|-----|--------|
| **Rule** | §3.2 | `.cursorrules`, 본 PRD |
| **Command** | §4.1 F2~F4 | `validate_lines`, `.cursor/commands/` |
| **(Skill)** | §4.1 F7 | `.cursor/skills/magic-square-tdd/` |
| **Test Loop** | §7 | `tests/test_validate_lines.py` |

### 9.3 TDD 규칙

- RED → GREEN → REFACTOR
- RED: `tests/`만 · skip/xfail 금지
- GREEN: 최소 구현
- REFACTOR: Budget 파일≤3 · 클래스≤1 · 메서드≤3

---

## 10. 후속 세션 — Entity·Boundary (참고)

> 세션 4+ · **본 PRD v0.1 범위 밖**. C2C·`/red-test-plan` 설계 시 참고.

### 10.1 FR-LOC-01 — 빈칸 좌표

| 항목 | 내용 |
|------|------|
| **요구** | 4×4 격자 빈칸(0) 좌표를 **1-index row-major** 반환 |
| **함수** | `find_blank_coords(grid) -> list[tuple[int, int]]` |
| **Test ID** | D-LOC-01 |
| **Then** | `[(2, 3), (4, 4)]` (G1 기준) |

### 10.2 G1 격자 SSOT (픽스처 공통)

```text
[[16,  3,  2, 13],
 [ 5, 10,  0,  8],
 [ 9,  6,  7, 12],
 [ 4, 15, 14,  0]]
```

| 항목 | 값 |
|------|-----|
| 0-index 빈칸 | `(1, 2)`, `(3, 3)` |
| 1-index row-major | `(2, 3)`, `(4, 4)` |
| 픽스처 | `grid_g1` (`tests/conftest.py` — 후속) |

### 10.3 Track B RED 후보

| Test ID | 함수 | Given→Then |
|---------|------|------------|
| D-LOC-01 | `find_blank_coords` | G1 → `[(2,3),(4,4)]` |
| D-MIS-01 | `find_not_exist_nums` | G1 → `[7, 10]` |
| D-SOL-01 | `solution` | G1 Step A 성공 |

### 10.4 Track A Boundary 후보

| Test ID | Given | Then |
|---------|-------|------|
| U-IN-01 | `grid=None` | `E003` |
| U-IN-02 | 셀 `17` | `E002` |

### 10.5 ECB

| Track | Domain Mock | E001~E005 |
|-------|-------------|-----------|
| Logic (B) | **금지** | entity emit **금지** |
| UI (A) | 허용 | boundary **전담** |

| 코드 | 의미 |
|------|------|
| E001 | 격자 크기 |
| E002 | 값 범위 |
| E003 | None 입력 |
| E004 | 타입 |
| E005 | 예약 |

---

## 11. 프로젝트 구조 (목표)

```
MagicSquare_xx/
├── .cursorrules
├── .cursor/
│   ├── commands/          # ARRR 슬래시 Command
│   └── skills/            # magic-square-tdd, magic-square-docs
├── docs/
│   └── PRD.md             # 본 문서
├── src/
│   └── validate_lines.py  # 세션 3 Command
├── tests/
│   └── test_validate_lines.py
├── Report/                # NN.REPORT.md
├── Prompt/                # NN.Export-Transcript.md
└── pyproject.toml
```

---

## 12. 관련 문서

| 문서 | 설명 |
|------|------|
| [Report/MomTest_워크북.md](../Report/MomTest_워크북.md) | Mom Test 인터뷰·진짜 문제 |
| [Report/3. Session3_Workbook.md](../Report/3.%20Session3_Workbook.md) | R-G-I-O·SC·8계층 |
| [Report/01.REPORT.md](../Report/01.REPORT.md) | 세션 3 Harness·Command 준비 |
| [Prompt/MomTest_인터뷰.md](../Prompt/MomTest_인터뷰.md) | Mom Test 프롬프트 |
| [`.cursor/skills/magic-square-docs/SKILL.md`](../.cursor/skills/magic-square-docs/SKILL.md) | Export 템플릿 |

---

## 13. 리스크 및 미확정

| 항목 | 상태 | 조치 |
|------|------|------|
| 20분 동안 **구체적 행동** (행·열만 vs 빈칸 값 변경) | 미수집 | Mom Test 추궁 1회 |
| 워크북 SC2 (1~16 중복) vs 세션 3 범위 | **Out of Scope**로 명시 | Entity 후속 |
| `docs/PRD.md` 부재 | **본 문서로 해소** | Command·Skill SSOT 연동 |
| RED 테스트 미작성 | [01.REPORT](../Report/01.REPORT.md) | `/tdd-red` 또는 `/red-skeleton` |

---

*PRD v0.1 — MagicSquare_1004 세션 3 `validate_lines` + ARRR 인프라 + 세션 4 Entity 참고.*
