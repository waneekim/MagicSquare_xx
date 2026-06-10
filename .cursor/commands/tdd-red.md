# /tdd-red — validate_lines RED 단계

MagicSquare_1004 세션 3 · Command `validate_lines` 전용.
**목표:** 실패하는 테스트를 `tests/`에만 추가·수정한다. 구현은 GREEN까지 미룬다.

---

## Phase 선언 (응답 첫 줄 필수)

```
Phase: RED | Layer: command | Track: Logic | API: validate_lines
```

선택: Test ID를 함께 표기 — `| ID: T2` (T1~T5, `.cursorrules` 참고)

---

## RED 절차

1. **대상 확인** — Test ID(T1~T5)와 기대 `status` / `failed_lines`를 한 줄로 적는다.
2. **AAA 작성** — `tests/test_validate_lines.py`에 함수 1개 추가 (또는 지정된 1개만 수정).
3. **실행** — `pytest tests/test_validate_lines.py -v`
4. **RED 확인** — 해당 테스트가 **FAIL**이면 성공. PASS면 RED 실패(기대값·격자 재검토).
5. **보고** — 아래 보고 형식으로 출력한다.

---

## AAA 절차

| 단계 | 내용 |
|------|------|
| **Arrange** | 4×4 `grid` literal. 주석에 **어느 줄을 깨는지**(R*/C*/D*) 명시 |
| **Act** | `result = validate_lines(grid)` |
| **Assert** | `result["status"]`, `result["failed_lines"]` — 구체적·엄격하게 |

**격자 작성 규칙**
- 완성 격자: 1~16 값, `0` 없음
- `incomplete`용: `0` 1개 이상
- 마법 상수 **34**, 10선 ID: `R1`~`R4`, `C1`~`C4`, `D1`, `D2`

---

## pytest 예시

### T2 — 행·열 합 ≠ 34 → `fail`

```python
def test_t2_fail_r2_and_c2_when_intersection_cell_changed():
    # Arrange: 완성 격자, (2,2) 셀 10→11 → R2·C2 동시 실패
    grid = [
        [16,  3,  2, 13],
        [ 5, 11, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "fail"
    assert "R2" in result["failed_lines"]
    assert "C2" in result["failed_lines"]
```

### T3 — 빈칸(0) 포함 → `incomplete`

```python
def test_t3_incomplete_when_blank_cell_exists():
    grid = [
        [16,  3,  2, 13],
        [ 5, 10, 11,  0],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]

    result = validate_lines(grid)

    assert result["status"] == "incomplete"
    assert result["failed_lines"] == []
```

### T4 — 대각선만 ≠ 34 → `fail` + `D1` 또는 `D2`

```python
def test_t4_fail_d2_when_anti_diagonal_sum_not_34():
    # Arrange: 행·열·D1은 34, D2만 깨지도록 한 셀 조정
    grid = [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  2],  # (0,3): 1→2 등 — D2 합 ≠ 34
    ]

    result = validate_lines(grid)

    assert result["status"] == "fail"
    assert "D2" in result["failed_lines"]
```

---

## 금지 (RED)

| 금지 | 이유 |
|------|------|
| `src/` **어떤 파일도** 수정 | GREEN 전용 |
| `src/validate_lines.py`에 본문 구현 | 스텁(`...`) 유지 |
| assert 완화 (`==` → `in` 축소, 조건 삭제) | 가짜 GREEN 방지 |
| `@pytest.mark.skip`, `xfail`, 테스트 삭제 | RED 우회 |
| `validate_lines` 시그니처·반환 키 변경 | API 계약 고정 |

---

## 보고 형식

작업 후 아래만 출력한다.

```markdown
## RED 보고

| 항목 | 내용 |
|------|------|
| Phase | RED \| Layer: command \| Track: Logic |
| Test ID | T2 (예) |
| 파일 | tests/test_validate_lines.py |
| 함수 | test_t2_... |
| pytest | FAIL (기대) / PASS (RED 실패) |
| 실패 메시지 | (한 줄 요약) |

### 기대 vs 실제
- 기대 status: `fail`
- 기대 failed_lines: `R2`, `C2` 포함
- 실제: (pytest 출력 요약)

### 다음
GREEN: `src/validate_lines.py` 최소 구현
```

---

## 사용 예

```
/tdd-red
T4: 대각선만 ≠ 34인 Red 테스트. tests/만 수정.
```
