"""FR-SOL-01 — Step A: 빈칸 채움 계획을 int[6] 1-index로 반환."""

from src.entity.constants import GRID_SIZE, MAGIC_CONSTANT
from src.entity.find_blank_coords import find_blank_coords


def solution(grid: list[list[int]]) -> list[int]:
    coords = find_blank_coords(grid)
    result: list[int] = []
    for row_1, col_1 in coords:
        row_0, col_0 = row_1 - 1, col_1 - 1
        row_sum = sum(grid[row_0][c] for c in range(GRID_SIZE))
        value = MAGIC_CONSTANT - row_sum
        result.extend([row_1, col_1, value])
    return result
