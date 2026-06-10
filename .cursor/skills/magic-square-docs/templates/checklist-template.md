# MagicSquare_1004 — ARRR 세션 체크리스트

> SSOT: `.cursorrules` · `docs/PRD.md` · `magic-square-tdd` · `magic-square-docs`

**세션:** {주제}  
**날짜:** YYYY-MM-DD  
**Test ID:** {ID}

---

## ARRR 단계

| 단계 | Command | 완료 | 비고 |
|------|---------|------|------|
| Ask RED ③ | `/red-test-plan` | [ ] | 설계표만, 파일 없음 |
| Agent RED ④ | `/red-skeleton` | [ ] | tests/만, FAIL 확인 |
| Respond GREEN | `/green-minimal` | [ ] | src/ 최소, PASS |
| Respond Golden | `/golden-master` | [ ] | PASS 후, matched |
| Refine Ask | `/refactor-smell` | [ ] | 스멜 표, 코드 없음 |
| Refine Agent | `/refactor-safe` | [ ] | Budget 내 1스멜 |
| Repeat | `/export-session` | [ ] | Report + Transcript |

---

## TDD 게이트

- [ ] Phase 선언 (응답 첫 줄)
- [ ] RED: `tests/`만 수정
- [ ] GREEN: assert 승격 (fail 제거)
- [ ] skip / xfail 없음
- [ ] 공개 API·golden 불변 (REFACTOR)

---

## ECB · Track

- [ ] Logic Track: Domain Mock 금지
- [ ] entity: E001~E005 emit 금지
- [ ] 10선 검사 생략 없음 (validate_lines)

---

## 문서 · Git

- [ ] `Report/NN.REPORT.md` 생성
- [ ] `Prompt/NN.Export-Transcript.md` 전문 저장
- [ ] git commit — **사용자 요청 시만**

---

## pytest 기록

| 명령 | 결과 | 시각 |
|------|------|------|
| `{pytest 명령}` | PASS / FAIL | |

---

**판정:** [ ] 세션 완료 / [ ] 다음 Command 대기
