# /golden-master — ARRR R단계 (Respond = Golden Master)

MagicSquare_1004 · **pytest PASS 후** Approval/Golden 기준 파일 구축.  
**목표:** UI 출력·복합 결과를 Golden 파일로 고정한다.

**추가 입력 없이 즉시 실행.** 대상 Test ID는 **채팅**·**최근 GREEN 완료**·**PRD**에서 자동 추출. **추가 질문 금지**.

**SSOT:** `.cursorrules` · `docs/PRD.md` · `.cursor/skills/magic-square-tdd/SKILL.md`

---

## Phase 선언 (응답 첫 줄 필수)

```
Phase: green | Layer: entity | Track: Logic | ID: D-LOC-01 | Step: golden
```

---

## 전제 조건 (미충족 시 중단)

| 조건 | 확인 |
|------|------|
| 대상 테스트 **PASS** | `pytest <대상> -v` |
| `tests/entity/test_*.py` 또는 boundary 테스트 **존재** | 파일 있음 |
| RED/GREEN **선행 완료** | 스텁·pytest.fail 없음 |

**미충족 시:** Golden 구축 **중단** · 선행 `/red-skeleton` → `/green-minimal` 안내 · **질문 금지**.

---

## Golden 절차

1. **PASS 재확인** — 대상 테스트 단일 명령 PASS
2. **Harness** — `tests/_approval.py`에 `assert_matches_golden(actual, relative)` (없으면 생성)
3. **연결** — 테스트에서 golden 경로 지정 (예: `tests/golden/d_loc_01_g1_blank_coords.approved.txt`)
4. **기준 생성** — `UPDATE_GOLDEN=1` 환경변수 + pytest (Windows: `$env:UPDATE_GOLDEN=1`)
5. **검증** — `UPDATE_GOLDEN` 없이 pytest → **matched**
6. **보고** — golden 경로 · matched 여부 · diff 요약

---

## Golden 규칙

| 항목 | 규칙 |
|------|------|
| **포맷** | `int[6]` 1-index · 에러 코드 문자열 — PRD·Skill SSOT |
| **금지** | golden 파일 **수동 편집**으로 통과 우회 |
| **범위** | 이번 Test ID 1묶음 |
| **불변** | GREEN assert 기대값과 golden 내용 일치 |

### 명령 예

```bash
# 기준 생성 (1회)
$env:UPDATE_GOLDEN=1; python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v

# 검증
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

---

## 금지

| 금지 | 이유 |
|------|------|
| PASS 전 golden 생성 | 기준 오염 |
| 미구현 Test ID (예: D-SOL-01 선행 없음) | 전제 위반 |
| `git commit` / **브랜치** | 사용자 요청 시만 |
| RED·REFACTOR 혼입 | 단계 분리 |

---

## 보고 형식

```markdown
## Golden Master 보고

| 항목 | 내용 |
|------|------|
| Test ID | D-LOC-01 |
| golden 파일 | tests/golden/d_loc_01_....approved.txt |
| matched | ✅ / ❌ |
| diff | (있으면 한 줄 요약) |

### 다음
/refactor-smell 또는 다음 RED
```

---

## 사용

```
/golden-master
```
