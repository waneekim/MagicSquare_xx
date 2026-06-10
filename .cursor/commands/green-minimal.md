# /green-minimal — ARRR R단계 (Respond = GREEN)

MagicSquare_1004 · **최소 구현으로 테스트 PASS**.  
**목표:** RED 스켈레톤 대상 1묶음을 GREEN 처리한다.

**추가 입력 없이 즉시 실행.** RED 대상·Test ID·파일은 **채팅**·**최근 RED 스켈레톤**·**PRD**에서 자동 추출. **추가 질문 금지**.

**SSOT:** `.cursorrules` · `docs/PRD.md` · `.cursor/skills/magic-square-tdd/SKILL.md`

---

## Phase 선언 (응답 첫 줄 필수)

```
Phase: green | Layer: entity | Track: Logic | ID: D-LOC-01
```

---

## GREEN 절차

1. **RED 재확인** — 대상 테스트 **FAIL** 확인 (`pytest` 단일 명령)
2. **최소 구현** — `src/`에 통과에 필요한 **최소** 코드만 추가
3. **assert 승격** — `pytest.fail` → 실제 `assert` (기대값은 설계표·PRD SSOT)
4. **PASS 확인** — 대상 테스트 **PASS**
5. **회귀** — `tests/` 관련 범위 PASS 유지 보고
6. **보고** — 아래 형식

---

## 구현 규칙

| 항목 | 규칙 |
|------|------|
| **범위** | 이번 Test ID 1묶음만 — YAGNI |
| **수정** | `src/` + 해당 `tests/` (fail → assert 교체만) |
| **ECB** | entity는 boundary/control import 금지 · E001~E005 emit 금지 |
| **API** | 공개 시그니처·반환 키 변경 금지 (`.cursorrules` 계약) |
| **상수** | `MAGIC_CONSTANT=34`, `GRID_SIZE=4`, `BLANK_CELL=0` — `constants.py` SSOT |

### Track B 예 (`D-LOC-01`)

- 파일: `src/entity/find_blank_coords.py` (또는 `loc.py`)
- Then: `assert find_blank_coords(grid_g1) == [(2, 3), (4, 4)]`

### 세션 3 예 (`T2`)

- 파일: `src/validate_lines.py`
- Then: `status == "fail"`, `"R2" in failed_lines`, `"C2" in failed_lines`

---

## 금지

| 금지 | 이유 |
|------|------|
| RED 설계표 재작성 | `/red-test-plan` |
| REFACTOR·헬퍼 과다 추출 | `/refactor-safe` |
| assert 완화 · skip · xfail | TDD 우회 |
| 관련 없는 Test ID 동시 구현 | 1묶음 원칙 |
| `git commit` / `git push` / **브랜치** | 사용자 명시 요청 시만 |

---

## 보고 형식

```markdown
## GREEN 보고

| 항목 | 내용 |
|------|------|
| Phase | green \| Layer: entity \| Track: Logic |
| Test ID | D-LOC-01 |
| src/ 변경 | src/entity/find_blank_coords.py (신규) |
| tests/ 변경 | pytest.fail → assert |
| pytest | PASS |
| 회귀 | tests/entity/ N passed |

### 다음
/golden-master (해당 시) 또는 다음 RED 묶음
```

---

## 완료 한 줄

```
/golden-master 또는 다음 RED 묶음으로 넘길 준비됐다
```

---

## 사용

```
/green-minimal
```
