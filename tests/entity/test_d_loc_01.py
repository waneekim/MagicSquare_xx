from src.entity.find_blank_coords import find_blank_coords


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    # Then: [(2, 3), (4, 4)] 반환 (1-index, row-major)
    assert find_blank_coords(grid_g1) == [(2, 3), (4, 4)]
