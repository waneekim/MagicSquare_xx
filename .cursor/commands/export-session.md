# /export-session — ARRR Repeat (세션 Export)

MagicSquare_1004 · **Report + Prompt Transcript** 한 번에 저장.  
**목표:** 현재 채팅 ARRR 세션을 문서화한다.

**추가 입력 없이 즉시 실행.** 세션 주제·Phase·산출물은 **현재 채팅**에서 자동 추출. **추가 질문 금지**.

**SSOT:** `.cursorrules` · `docs/PRD.md` · `.cursor/skills/magic-square-docs/SKILL.md`

**별칭:** `/export` (동일 동작 — `export.md` 선택 시)

---

## Phase 선언 (응답 첫 줄)

```
Phase: repeat | Layer: — | Track: Logic+UI | Step: export
```

---

## 파일 규칙 (`NN.XXX`)

| 종류 | 경로 | 예시 |
|------|------|------|
| 보고서 | `Report/NN.REPORT.md` | `Report/02.REPORT.md` |
| Transcript | `Prompt/NN.Export-Transcript.md` | `Prompt/02.Export-Transcript.md` |

- `Report/`·`Prompt/` 최대 `NN` + 1 (2자리)
- **덮어쓰기 금지**
- 템플릿: `.cursor/skills/magic-square-docs/templates/`

---

## Export 절차

1. **수집** — Phase·Test ID·변경 파일·pytest·User/Cursor 전문
2. **Report** — `templates/report-template.md` 기반 작성
3. **Transcript** — `templates/transcript-template.md` 기반 (**생략 금지**)
4. **보고** — 생성 경로 2개

---

## 금지

| 금지 | 이유 |
|------|------|
| Transcript 요약·생략 | Export 목적 |
| `git commit` / `git push` | 사용자 요청 시만 |
| `.env` 커밋 | 비밀 |

---

## 완료 보고

```markdown
## Export 완료

| 파일 | 경로 |
|------|------|
| 보고서 | Report/NN.REPORT.md |
| Transcript | Prompt/NN.Export-Transcript.md |
```

---

## 사용

```
/export-session
```
