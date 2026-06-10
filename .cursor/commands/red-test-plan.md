# /red-test-plan — ARRR A단계 (Ask = RED ③)

MagicSquare_1004 · **C2C 설계표·테스트 플랜만** 작성한다.  
**목표:** RED 구현 전 Ask 단계 — 표 4블록 출력. **파일은 만들지 않는다.**

**추가 입력 없이 즉시 실행.** 세션 주제·Test ID·Layer·Track은 **현재 채팅**과 **`docs/PRD.md`**(없으면 `.cursorrules`)에서 자동 추출. 사용자에게 번호·주제 **추가 질문 금지**.

**SSOT (읽기만):** `.cursorrules` · `docs/PRD.md` · `.cursor/commands/export-session.md` · `.cursor/skills/magic-square-tdd/SKILL.md`

---

## Phase 선언 (응답 첫 줄 필수)

```
Phase: red | Layer: entity | Track: Logic
```

| 자동 추출 | 규칙 |
|-----------|------|
| **Layer** | Track B → `entity` · Track A → `boundary` |
| **Track** | Logic Track B → `Logic` · UI Track A → `UI` |
| **Test ID** | 채팅 RED 묶음 또는 PRD §8·§10 Test Loop (예: `T2`, `D-LOC-01`, `U-IN-01`) |

**Track A 재사용:** 본 Command는 Track B(Logic·entity) 기본. **Layer만 `boundary`**, **Track만 `UI`**로 바꾸면 Track A에 그대로 재사용 가능 (`tests/boundary/`, `U-*` ID).

---

## Ask 절차 (RED ③)

1. **SSOT 확인** — `docs/PRD.md` FR·G1·Test ID. 없으면 `.cursorrules` Test Loop T1~T5·`validate_lines` 계약.
2. **RED 묶음 확정** — 이번 1~3 Test ID (채팅·PRD에서 1개 우선).
3. **표 4블록 출력** — 아래 템플릿 그대로 (빈 칸 없이).
4. **완료 한 줄** — `/red-skeleton 으로 넘길 준비됐다`

**pytest 실행 금지** (설계 단계). `tests/`·`src/` **파일 생성·수정 금지**.

---

## 출력 4블록 (필수)

응답 본문은 **아래 4개 섹션만** 표 형식으로 작성한다.

---

### 블록 1 — C2C (Rule 1~3)

**Rule 1~3** = 도메인 SSOT (PRD R-01~R-03 또는 `.cursorrules` 격자·값·빈칸 규칙).

| 항목 | 내용 |
|------|------|
| **Rule 1** | (예: 격자 4×4) |
| **Rule 2** | (예: 셀 값 `0` 또는 `1~16`) |
| **Rule 3** | (예: 빈칸 2개 / 10선 합 34 / row-major 등 — 대상 FR에 맞게) |
| **PRD ID** | (예: `FR-LOC-01`, `F2~F4`, `FR-VAL-04`) |
| **PRD 인용** | `docs/PRD.md` §N 한 줄 인용 + **판단** (0/1-index, 범위 외 항목 명시) |
| **PRD C2C** | PRD C2C·AC 한 줄 (함수·기대 동작) |
| **To-Do 1개** | 판단 포함 **구현 목표 1문장** (어느 파일·함수·반환 — **범위 외** 명시) |

#### Test ID → Given / When / Then

| Test ID | Given | When | Then |
|---------|-------|------|------|
| (ID) | (격자·픽스처·입력) | (호출 함수·인자) | (기대값·status·failed_lines 등) |

---

### 블록 2 — Track B 표 (Logic · entity)

> Track A일 때: 섹션 제목을 **「Track A 표 (UI · boundary)」**로 바꾸고 Test ID를 `U-*`로 기입.

| Test ID | 대상 함수 | Given→Then | Invariant | Expected RED Failure |
|---------|-----------|------------|-----------|----------------------|
| (ID) | `함수()` | G1 → 기대값 | I? (row-major, 10선 전체 등) | `ImportError` / `AttributeError` / `pytest.fail` / assert FAIL 유형 |

**세션 3 `validate_lines` 예 (참고):**

| Test ID | 대상 함수 | Given→Then | Invariant | Expected RED Failure |
|---------|-----------|------------|-----------|----------------------|
| T2 | `validate_lines()` | 완성 격자, R2·C2 교차 셀 변경 → `fail`, `R2`·`C2` ∈ failed_lines | 10선 ID: R1~R4,C1~C4,D1,D2 | `AssertionError` (스텁 `...`) |
| T3 | `validate_lines()` | `0` 포함 격자 → `incomplete`, `[]` | R5 incomplete | 동일 |
| T4 | `validate_lines()` | D2만 ≠34 → `fail`, `D2` 포함 | D1·D2 생략 금지 | 동일 |

---

### 블록 3 — 테스트 플랜

| 항목 | 내용 |
|------|------|
| **파일 경로** | (예: `tests/entity/test_d_loc_01.py` · `tests/test_validate_lines.py`) |
| **함수명** | (예: `test_d_loc_01_blank_coords_row_major` · `test_t2_fail_r2_and_c2_...`) |
| **conftest 픽스처** | (예: `grid_g1` — PRD §10.2 G1 SSOT; 없으면 테스트 내 literal) |
| **pytest 명령** | `python -m pytest <파일>::<함수> -v` |
| **RED 묶음 범위** | 이번 1~3 Test ID (예: `D-LOC-01` 단독 · `T2` 단독) |

---

### 블록 4 — ECB·Mock 점검

| 항목 | Logic Track (B) | UI Track (A) |
|------|-----------------|--------------|
| **Domain Mock** | **금지** | 허용 (boundary UI·입력) |
| **E001~E005 emit** | entity/control **금지** | boundary **전담** (E002 값, E003 None 등) |
| **import 방향** | entity → boundary/control **금지** | boundary → entity API 호출 허용 |
| **이번 RED** | (해당 없음 한 줄) | (해당 없음 한 줄) |

**Logic Track 필수 문구:** Domain Mock 금지 · entity에서 E001~E005 raise/return 금지.

---

## 금지 (Ask · RED ③)

| 금지 | 이유 |
|------|------|
| `tests/`·`src/` **파일 생성·수정** | `/red-skeleton` 전용 |
| `src/` 구현·스텁 변경 | GREEN 전용 |
| GREEN / REFACTOR 단계 언급·혼입 | ARRR 단계 분리 |
| `@pytest.mark.skip`, `xfail` | RED 우회 |
| pytest 실행·코드 블록으로 테스트 작성 | 설계표만 |
| 사용자에게 Test ID·Layer **추가 질문** | 자동 추출 |

---

## 완료 한 줄 (응답 마지막 필수)

```
/red-skeleton 으로 넘길 준비됐다
```

---

## 자동 추출 우선순위

1. **채팅** — "이번 RED 묶음: D-LOC-01", "T4", "U-IN-01" 등
2. **`docs/PRD.md`** — §8 Test Loop · §10 FR-* · G1 SSOT
3. **`.cursorrules`** — T1~T5 · `validate_lines` API · 10선 ID
4. **기본값** — 세션 3 미진행 시 `T2` (행·열 fail) 또는 PRD 권장 첫 ID

---

## ARRR 체인

```
/red-test-plan   ← Ask (본 Command, 설계표만)
/red-skeleton    ← Agent (pytest.fail 스켈레톤)
/green-minimal   ← Agent (최소 구현)
/golden-master   ← Agent (PASS 후 Golden)
/refactor-smell  ← Ask (스멜 표)
/refactor-safe   ← Agent (스멜 1개)
/export-session  ← Repeat (Report + Transcript)
```

---

## 사용 예

```
/red-test-plan
```

추가 설명 없이 Enter만으로 실행. 채팅에 Test ID가 있으면 그걸 우선 사용.

**Track B (entity · Logic) — 기본**

```
/red-test-plan
```

**Track A (boundary · UI) — Layer·Track만 변경**

채팅에 `Layer: boundary`, `Track: UI`, `U-IN-01` 맥락이 있으면 자동 반영. 없으면 entity·Logic 기본.
