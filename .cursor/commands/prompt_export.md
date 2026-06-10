# /prompt_export — validate_lines RED 세션 Export

MagicSquare_1004 세션 3 · **validate_lines TDD RED** 단계 전용.
**목표:** 현재 채팅을 바탕으로 Report 보고서 + Prompt Transcript를 **한 번에** 저장한다.

**추가 입력 없이 즉시 실행.** 세션 주제·산출물·대화는 **현재 채팅**에서 자동 추출. 사용자에게 번호·주제 **추가 질문 금지**.

---

## Phase 선언 (응답 첫 줄)

```
Phase: EXPORT | Layer: command | Track: Logic | API: validate_lines | Step: RED
```

---

## 파일 규칙 (`01.XXX` 형식)

| 종류 | 경로 패턴 | 예시 |
|------|-----------|------|
| **보고서** | `Report/NN.REPORT.md` | `Report/01.REPORT.md` |
| **Transcript** | `Prompt/NN.Export-Transcript.md` | `Prompt/01.Export-Transcript.md` |

### 번호(NN) 결정

1. `Report/`·`Prompt/`에서 `^\d{2}\.` 로 시작하는 파일명 스캔
2. 최대 번호 + 1 → 2자리 (`01`, `02`, …)
3. 번호가 없으면 **`01`**
4. **기존 파일 덮어쓰기 금지** — 충돌 시 번호 +1

---

## Export 절차

1. **수집** — 현재 채팅에서 RED 관련 User/Cursor 메시지 전부, 수정·생성 파일, pytest 결과
2. **보고서 작성** — `Report/NN.REPORT.md` 생성 (아래 템플릿)
3. **Transcript 작성** — `Prompt/NN.Export-Transcript.md` 생성 (아래 템플릿)
4. **확인** — 생성된 두 파일 경로를 사용자에게 보고

---

## Report 템플릿 (`Report/NN.REPORT.md`)

```markdown
# MagicSquare_1004 — validate_lines TDD RED

| 항목 | 내용 |
|------|------|
| 프로젝트 | MagicSquare_1004 |
| 단계 | 세션 3 — validate_lines **RED** |
| Phase | RED \| Layer: command \| Track: Logic |
| 보고서 생성일 | YYYY-MM-DD |
| Test ID | T? (채팅에서 추출, 없으면 "—") |

---

## 1. 요약

| 구분 | 결과 |
|------|------|
| 목표 | `tests/`에 실패 테스트 추가 (src/ 미수정) |
| pytest | FAIL (기대) / PASS (RED 실패) |
| 판정 | RED 성공 / RED 실패 / 미실행 |

(한 단락: 무엇을 RED로 작성했는지, pytest 결과)

---

## 2. RED 산출물

| 파일 | 변경 |
|------|------|
| tests/test_validate_lines.py | (추가한 test 함수명) |
| src/validate_lines.py | **미수정** (스텁 유지) |

### 테스트 요약

| Test ID | 함수명 | 기대 status | 기대 failed_lines | pytest |
|---------|--------|-------------|-------------------|--------|
| T? | test_... | fail / incomplete | R?, C?, D? | FAIL/PASS |

---

## 3. 도메인·계약 확인

- 4×4, 마법상수 34, 10선: R1~R4, C1~C4, D1, D2
- API: `validate_lines(grid)` → `{status, failed_lines}`
- `incomplete`: `0` 포함 시, `failed_lines` = `[]`

---

## 4. 금지 사항 준수

| 항목 | 준수 |
|------|------|
| src/ 미수정 | ✅ / ❌ |
| assert 완화·skip·xfail 없음 | ✅ / ❌ |

---

## 5. 다음 단계

- **GREEN:** `src/validate_lines.py` 최소 구현
- **회귀:** `pytest tests/test_validate_lines.py -v`

---

## 관련 문서

| 문서 | 설명 |
|------|------|
| Prompt/NN.Export-Transcript.md | 본 세션 대화 Export |
| .cursor/commands/tdd-red.md | `/tdd-red` Command |
| .cursorrules | 도메인·TDD SSOT |

---

*본 문서는 Report/NN.REPORT.md — validate_lines RED 세션 보고서입니다.*
```

---

## Transcript 템플릿 (`Prompt/NN.Export-Transcript.md`)

```markdown
# MagicSquare_1004 — validate_lines TDD RED
_Exported on YYYY-MM-DD from Cursor_

---

**User**

(첫 User 메시지 — RED 요청 원문)

---

**Cursor**

(첫 Cursor 응답 요약 또는 핵심 — Phase 선언 포함)

---

(이하 User / Cursor 교대. **현재 채팅 전문**을 시간순으로. 생략·요약 금지)
```

**Transcript 규칙**
- `_Exported on {오늘 날짜} from Cursor_` 헤더 필수
- 역할 라벨: `**User**` / `**Cursor**`
- 코드 블록·pytest 출력은 원문 유지
- RED와 무관한 말도 **전문 보존** (나중 세션 맥락용)

---

## 금지

| 금지 | 이유 |
|------|------|
| 기존 `NN.REPORT.md` / `NN.Export-Transcript.md` 덮어쓰기 | 이력 보존 |
| Transcript 요약·생략 | Export 목적 상실 |
| `git commit` / `git push` | 사용자 명시 요청 시만 |
| GREEN·REFACTOR 내용을 RED 보고서에 혼입 | 단계 분리 |

---

## 완료 보고 (채팅 출력)

```markdown
## Export 완료

| 파일 | 경로 |
|------|------|
| 보고서 | Report/NN.REPORT.md |
| Transcript | Prompt/NN.Export-Transcript.md |

다음: GREEN 시 `/tdd-green` (추후) 또는 `src/validate_lines.py` 최소 구현
```

---

## 사용 예

```
/prompt_export
```

RED 작업 직후, 추가 설명 없이 Enter만으로 실행.
