---
name: magic-square-docs
description: MagicSquare_1004 Report·Prompt Export. /export-session, NN.REPORT.md, NN.Export-Transcript.md, ARRR 세션 문서화.
---

# magic-square-docs

MagicSquare_1004 · Report / Prompt Export SSOT.

**Command:** `/export-session` (별칭 `/export`)  
**템플릿:** `templates/report-template.md` · `transcript-template.md` · `checklist-template.md`

---

## Export 규칙

| 항목 | 규칙 |
|------|------|
| 보고서 | `Report/NN.REPORT.md` |
| Transcript | `Prompt/NN.Export-Transcript.md` |
| 번호 | 2자리 `01`~`99`, 기존 최대+1 |
| 덮어쓰기 | **금지** |
| Transcript | **전문** — 생략·요약 금지 |

**추가 입력 없이** 현재 채팅에서 Phase·Test ID·파일·pytest 자동 추출.

---

## Report 필수 섹션

1. **요약** — Phase · Test ID · pytest · 판정
2. **핵심 산출물** — 변경 파일 표
3. **다음 단계** — 다음 Command 1줄
4. **관련 문서** — Transcript·PRD 링크

템플릿: [`templates/report-template.md`](templates/report-template.md)

---

## Transcript 필수 형식

```markdown
# MagicSquare_1004 — {세션 주제}
_Exported on YYYY-MM-DD from Cursor_

---

**User**
(원문)

---

**Cursor**
(원문)
```

템플릿: [`templates/transcript-template.md`](templates/transcript-template.md)

---

## ARRR Phase별 Report 초점

| Phase | Report 강조 |
|-------|-------------|
| red (plan) | C2C 4블록 요약 · 파일 미생성 |
| red (skeleton) | FAIL 한 줄 · tests/만 |
| green | src/ 변경 · PASS |
| golden | matched · golden 경로 |
| refactor (smell) | 스멜 표 · 코드 미변경 |
| refactor (safe) | Budget · 회귀 PASS |
| repeat | 1사이클 누적 요약 |

---

## 체크리스트 (세션 마무리)

템플릿: [`templates/checklist-template.md`](templates/checklist-template.md)

- [ ] Phase 선언 있었는가
- [ ] SSOT(`.cursorrules`·PRD) 위반 없었는가
- [ ] pytest 결과 Report에 있는가
- [ ] Transcript 전문 저장했는가
- [ ] git commit은 요청 시만 했는가

---

## SSOT 링크

| 문서 | 경로 |
|------|------|
| Rule | `.cursorrules` |
| PRD | `docs/PRD.md` |
| TDD Skill | `.cursor/skills/magic-square-tdd/SKILL.md` |
| Export Command | `.cursor/commands/export-session.md` |

---

## 금지

- Transcript 요약
- `.env`·토큰 Report 포함
- 사용자에게 번호·주제 추가 질문
