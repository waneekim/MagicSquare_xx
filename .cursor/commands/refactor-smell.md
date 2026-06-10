# /refactor-smell — ARRR R단계 (Refine = Ask ⑦)

MagicSquare_1004 · **스멜 탐지 표만** 출력한다.  
**목표:** GREEN·Golden 이후 코드 냄새를 표로 정리한다. **코드 수정 없음.**

**추가 입력 없이 즉시 실행.** 대상 범위·파일은 **채팅**·**최근 GREEN**·**`src/`·`tests/`**에서 자동 추출. **추가 질문 금지**.

**SSOT:** `.cursorrules` · `docs/PRD.md` · `.cursor/skills/magic-square-tdd/SKILL.md`

---

## Phase 선언 (응답 첫 줄 필수)

```
Phase: refactor | Layer: command | Track: Logic | Step: smell
```

---

## Ask ⑦ 절차

1. **전제 확인** — `tests/` 전체 또는 관련 범위 **PASS** (pytest 결과 채팅·리포트에서 추출; 없으면 "미실행" 표기)
2. **스캔** — `src/`·`tests/` 읽기만 (Ask 모드 원칙)
3. **스멜 표** — P0~P2 우선순위
4. **`/refactor-safe` 후보** — Change Budget 내 1~3개
5. **보고** — 코드 **미변경** 명시

---

## 스멜 표 (필수 출력)

| 우선순위 | 스멜 | 위치(파일:함수) | 근거 | Change Budget 내 리팩터 후보 |
|----------|------|-----------------|------|------------------------------|
| P0 | (예: Duplicated Code) | validate_lines.py:validate_lines | 행·열·D1·D2 동일 패턴 4회 | `_collect_failed_line_ids(grid)` 추출 |
| P1 | … | … | … | … |
| P2 | … | … | … | … |

**Change Budget:** 파일≤3 · 클래스≤1 · 메서드≤3

### `/refactor-safe` 후보 (Budget 내 1~3개)

| # | 우선순위 | 대상 | 작업 |
|---|----------|------|------|
| 1 | P0 | `validate_lines.py:validate_lines` | `_collect_failed_line_ids(grid)` 헬퍼 추출 |
| 2 | P1 | … | P0 연계 Long Method 분해 |
| 3 | P1 | … | G1 격자 단일 SSOT화 |

---

## 스멜 후보 (MagicSquare SSOT)

| 스멜 | 흔한 위치 |
|------|-----------|
| Duplicated Code | `validate_lines` 10선 반복 |
| Long Method | `validate_lines` 본문 25줄+ |
| Magic Number | `34`, `0`, `4` 리터럴 |
| Mysterious Name | `i`, `j` 루프 변수 |
| Duplicated Data | `GRID_G1` conftest vs boundary 이중 정의 |

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/`·`tests/` **수정** | `/refactor-safe` 전용 |
| RED / GREEN 재실행 | 단계 혼입 |
| Budget 초과 제안 | 파일>3 · 메서드>3 |
| 공개 API·테스트 기대값 변경 제안 | 계약 불변 |
| `git commit` / **브랜치** | 사용자 요청 시만 |

---

## 보고 형식

```markdown
## REFACTOR Ask 보고

| 항목 | 내용 |
|------|------|
| Phase | refactor \| Step: smell |
| pytest 전제 | N passed / 미실행 |
| P0 | 1건 |
| refactor-safe 후보 | #1 P0 … |

### 다음
/refactor-safe — P0 후보 #1
```

---

## 완료 한 줄

```
/refactor-safe 로 P0 후보 1개 실행할 준비됐다
```

---

## 사용

```
/refactor-smell
```
