"""검증·솔버 결과 표시."""

from __future__ import annotations

from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget

from src.validate_lines import ValidationResult

_STATUS_STYLES = {
    "pass": ("통과 — 10선 합 34", "color: #1b7a3d; font-weight: bold;"),
    "fail": ("실패", "color: #c0392b; font-weight: bold;"),
    "incomplete": ("미완성 — 빈칸을 채우세요", "color: #b8860b; font-weight: bold;"),
}


class ResultDisplay(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._status_label = QLabel("「10선 검증」으로 행·열·대각선 합을 확인하세요.")
        self._detail_label = QLabel("")
        self._detail_label.setWordWrap(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self._status_label)
        layout.addWidget(self._detail_label)

    def show_validation(self, result: ValidationResult) -> None:
        status = result["status"]
        label, style = _STATUS_STYLES.get(status, (status, ""))
        self._status_label.setText(f"결과: {label}")
        self._status_label.setStyleSheet(style)

        failed_lines = result["failed_lines"]
        self._detail_label.setText(
            f"실패 줄: {', '.join(failed_lines)}" if failed_lines else ""
        )

    def reset_message(self) -> None:
        self._status_label.setText("G1 격자로 초기화했습니다.")
        self._status_label.setStyleSheet("")
        self._detail_label.setText("")

    def show_solution_hint(self, step_a: list[int]) -> None:
        parts = [
            f"({step_a[i]},{step_a[i + 1]})→{step_a[i + 2]}"
            for i in range(0, len(step_a), 3)
        ]
        self._detail_label.setText(f"Step A 힌트: {', '.join(parts)}")
