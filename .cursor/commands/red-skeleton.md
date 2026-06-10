# /red-skeleton — ARRR A단계 (Agent = RED ④)

MagicSquare_1004 · **RED 스켈레톤만** 작성한다.  
**목표:** `/red-test-plan` 설계표를 `tests/`에 `pytest.fail` 스켈레톤으로 옮긴다.

**추가 입력 없이 즉시 실행.** Test ID·파일·픽스처는 **현재 채팅**·**직전 `/red-test-plan` 출력**·**`docs/PRD.md`**(없으면 `.cursorrules`)에서 자동 추출. **추가 질문 금지**.

**SSOT:** `.cursorrules` · `docs/PRD.md` · `.cursor/skills/magic-square-tdd/SKILL.md`

---

## Phase 선언 (응답 첫 줄 필수)

```
Phase: red | Layer: entity | Track: Logic | ID: D-LOC-01
```

| 자동 추출 | 규칙 |
|-----------|------|
| **Layer** | Track B → `entity` · Track A → `boundary` |
| **Track** | B → `Logic` · A → `UI` |
| **Test ID** | 채팅·설계표 (예: `T2`, `D-LOC-01`, `U-IN-01`) |
| **파일** | B → `tests/entity/test_<id>.py` · A → `tests/boundary/test_<id>.py` · 세션3 → `tests/test_validate_lines.py` |

---

## RED ④ 절차

1. **설계표 확인** — 직전 `/red-test-plan` 4블록 또는 PRD Test Loop
2. **스켈레톤 작성** — `tests/`에 테스트 함수 1개 (RED 묶음 1개)
3. **pytest 실행** — 대상 함수 단일 명령
4. **RED 확인** — **FAIL** (의도적 `pytest.fail` 또는 ImportError)
5. **보고** — 아래 형식

---

## 스켈레톤 규칙

| 항목 | 규칙 |
|------|------|
| **AAA 주석** | `# Given:` · `# When:` · `# Then:` |
| **Then** | `pytest.fail("RED: <Test ID> — 구현 없음, 의도적 실패")` **한 줄만** |
| **금지** | assert 본문 · skip · xfail · 통과 더미 · `self` 불필요 시 생략 |
| **픽스처** | `grid_g1` 등 conftest SSOT (없으면 literal + 주석) |
| **import** | 테스트 대상 함수 import (미구현 → ImportError도 RED 성공) |

### Track B 예시 (`D-LOC-01`)

```python
import pytest


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    # Then: [(2,3),(4,4)] 반환 (1-index, row-major)
    pytest.fail("RED: D-LOC-01 — 구현 없음, 의도적 실패")
```

### 세션 3 예시 (`T2`)

```python
from src.validate_lines import validate_lines


def test_t2_fail_r2_and_c2_when_intersection_cell_changed():
    # Given: 완성 격자, R2·C2 교차 셀 10→11
    grid = [
        [16,  3,  2, 13],
        [ 5, 11, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]
    # When: validate_lines(grid) 호출
    # Then: status fail, R2·C2 ∈ failed_lines
    pytest.fail("RED: T2 — 구현 없음, 의도적 실패")
```

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/` **수정** | GREEN 전용 |
| assert·실제 검증 로직 | `/green-minimal`에서 승격 |
| GREEN / REFACTOR 혼입 | ARRR 단계 분리 |
| `git commit` / `git push` / **브랜치 생성** | 사용자 명시 요청 시만 |
| 설계표 재작성 | `/red-test-plan` 역할 |

---

## 보고 형식

```markdown
## RED 스켈레톤 보고

| 항목 | 내용 |
|------|------|
| Phase | red \| Layer: entity \| Track: Logic |
| Test ID | D-LOC-01 |
| 파일 | tests/entity/test_d_loc_01.py |
| pytest | FAIL (기대) |
| FAIL 한 줄 | Failed: RED: D-LOC-01 — … |

### 다음
/green-minimal
```

---

## 완료 한 줄 (응답 마지막)

```
/green-minimal 으로 넘길 준비됐다
```

---

## 사용

```
/red-skeleton
```
