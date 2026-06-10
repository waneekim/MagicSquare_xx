# /refactor-safe — ARRR R단계 (Refine = Agent ⑧)

MagicSquare_1004 · **스멜 1개만** 안전 리팩터.  
**목표:** `/refactor-smell` P0 후보 1개를 Budget 내에서 실행한다.

**추가 입력 없이 즉시 실행.** 대상 스멜은 **직전 `/refactor-smell` 표**·**채팅**에서 **P0 #1** 자동 선택. **추가 질문 금지**.

**SSOT:** `.cursorrules` · `docs/PRD.md` · `.cursor/skills/magic-square-tdd/SKILL.md`

---

## Phase 선언 (응답 첫 줄 필수)

```
Phase: refactor | Layer: command | Track: Logic | Step: safe | Target: P0 #1
```

---

## Refine ⑧ 절차

1. **전제** — `pytest tests/ -v` **전부 PASS** (실행 후 확인)
2. **대상 선택** — P0 후보 **#1** (없으면 P1 첫 항목)
3. **리팩터 1건** — Change Budget 준수
4. **회귀** — `pytest tests/ -v` **PASS 유지**
5. **Golden** — 해당 Test ID golden 있으면 **matched** 확인
6. **보고** — Budget 사용량 · 변경 파일

---

## Change Budget (엄수)

| 항목 | 상한 |
|------|------|
| 파일 | ≤ 3 |
| 클래스 | ≤ 1 |
| 메서드 | ≤ 3 |

**불변:** 공개 API · 테스트 assert 기대값 · golden 파일 내용 · `validate_lines` 반환 계약

### 기본 P0 예 (`validate_lines`)

- 추출: `_collect_failed_line_ids(grid) -> list[str]`
- 파일: `src/validate_lines.py` 1개
- 메서드: 헬퍼 1 + 본문 정리 ≤2

---

## 금지

| 금지 | 이유 |
|------|------|
| Budget 초과 | 안전 리팩터 원칙 |
| 스멜 2개 이상 동시 처리 | 1턴 1스멜 |
| assert·golden 수동 수정 | 우회 |
| RED / GREEN 재진입 | 단계 혼입 |
| `git commit` / `git push` / **브랜치** | 사용자 요청 시만 |

---

## 보고 형식

```markdown
## REFACTOR Safe 보고

| 항목 | 내용 |
|------|------|
| 대상 | P0 #1 — _collect_failed_line_ids 추출 |
| 변경 파일 | src/validate_lines.py |
| Budget | 1/3 파일 · 2/3 메서드 |
| pytest | N passed (회귀 OK) |
| golden | matched / 해당 없음 |

### 다음
/refactor-smell 재실행 또는 /export-session
```

---

## 완료 한 줄

```
/export-session 또는 다음 /refactor-safe 준비됐다
```

---

## 사용

```
/refactor-safe
```
