from src.entity.solution import solution
from tests._approval import assert_matches_golden, format_int6

GOLDEN_D_SOL_01 = "d_sol_01_g1_step_a.approved.txt"


def test_d_sol_01_step_a_success(grid_g1):
    # Given: G1 격자
    # When: solution(grid_g1) Step A 호출
    # Then: int[6] 1-index — row,col,val × 2 (row-major)
    actual = solution(grid_g1)
    assert_matches_golden(format_int6(actual), GOLDEN_D_SOL_01)
