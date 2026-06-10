"""pytest 픽스처 — G1 격자 SSOT (PRD §10.2)."""

import pytest

from src.entity.constants import BLANK_COUNT, GRID_SIZE

GRID_G1: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 10, 0, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 0],
]


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1 격자 — 0이 정확히 2개."""
    grid = [row[:] for row in GRID_G1]
    blank_count = sum(cell == 0 for row in grid for cell in row)
    assert blank_count == BLANK_COUNT
    assert len(grid) == GRID_SIZE
    assert all(len(row) == GRID_SIZE for row in grid)
    return grid
