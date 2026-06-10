"""MagicSquare_1004 최소 GUI 데모 — G1 격자 · 10선 검증 · Step A 힌트."""

from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget

from src.boundary.grid_ui import GridUI
from src.boundary.result_display import ResultDisplay
from src.entity.solution import solution
from src.validate_lines import validate_lines

# PRD §10.2 G1 SSOT
GRID_G1: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 10, 0, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 0],
]


class DemoWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("MagicSquare_1004 — GUI 데모")
        self.setMinimumWidth(320)

        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)

        self._grid_ui = GridUI()
        self._grid_ui.set_grid(GRID_G1)
        root.addWidget(self._grid_ui)

        buttons = QHBoxLayout()
        validate_btn = QPushButton("10선 검증")
        validate_btn.clicked.connect(self._on_validate)
        hint_btn = QPushButton("Step A 힌트")
        hint_btn.clicked.connect(self._on_hint)
        reset_btn = QPushButton("G1 초기화")
        reset_btn.clicked.connect(self._on_reset)
        buttons.addWidget(validate_btn)
        buttons.addWidget(hint_btn)
        buttons.addWidget(reset_btn)
        root.addLayout(buttons)

        self._result_display = ResultDisplay()
        root.addWidget(self._result_display)

    def _on_validate(self) -> None:
        self._result_display.show_validation(validate_lines(self._grid_ui.get_grid()))

    def _on_hint(self) -> None:
        grid = self._grid_ui.get_grid()
        self._result_display.show_solution_hint(solution(grid))

    def _on_reset(self) -> None:
        self._grid_ui.set_grid(GRID_G1)
        self._result_display.reset_message()


def main() -> None:
    app = QApplication(sys.argv)
    window = DemoWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
