from src.validate_lines import validate_lines


def test_t1_pass_on_complete_answer_grid():
    # Given: PRD §2.4 과제 슬라이드 정답 4×4 (빈칸 없음)
    grid = [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]

    # When
    result = validate_lines(grid)

    # Then: T1 Green — status=pass, failed_lines=[]
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


def test_t2_fail_r2_and_c2_when_intersection_cell_changed():
    # Given: T1 기준, R2∩C2 교차 셀 (1,1) 값 10→11
    grid = [
        [16,  3,  2, 13],
        [ 5, 11, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]

    # When
    result = validate_lines(grid)

    # Then: T2 Red — status=fail, R2·C2 ∈ failed_lines
    assert result["status"] == "fail"
    assert "R2" in result["failed_lines"]
    assert "C2" in result["failed_lines"]


def test_t3_incomplete_when_blank_cell_exists():
    # Given: 빈칸(0) 1개 이상 — (1,3)
    grid = [
        [16,  3,  2, 13],
        [ 5, 10, 11,  0],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]

    # When
    result = validate_lines(grid)

    # Then: T3 Red — status=incomplete, failed_lines=[]
    assert result["status"] == "incomplete"
    assert result["failed_lines"] == []


def test_t4_fail_diagonals_when_rows_and_cols_are_34():
    # Given: 반마방진 — 행·열 34, D1=31, D2=49
    grid = [
        [ 7, 12,  1, 14],
        [14,  8, 11,  1],
        [ 2, 13,  8, 11],
        [11,  1, 14,  8],
    ]

    # When
    result = validate_lines(grid)

    # Then: T4 Red — 대각선 검사 누락 방지 (Mom Test)
    assert result["status"] == "fail"
    assert "D1" in result["failed_lines"]
    assert "D2" in result["failed_lines"]


def test_t5_fail_multiple_lines_all_reported():
    # Given: T1 기준, (0,0) 16→15 → R1·C1·D1 동시 ≠34
    grid = [
        [15,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]

    # When
    result = validate_lines(grid)

    # Then: T5 Red — 틀린 줄 ID 전부 반환 (누락 없음)
    assert result["status"] == "fail"
    assert set(result["failed_lines"]) >= {"R1", "C1", "D1"}
