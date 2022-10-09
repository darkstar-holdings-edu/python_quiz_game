from tkinter import Canvas

from gui_theme import THEME_COLOR, THEME_FONT_FACE


class GuiQuestionBox:
    canvas: Canvas
    text_id: int

    def __init__(
        self,
        height: int,
        width: int,
    ) -> None:

        canvas = Canvas(
            height=height,
            width=width,
            background="white",
            borderwidth=0,
            highlightthickness=0,
        )

        self.text_id = canvas.create_text(
            150,
            125,
            text="Default text.",
            fill=THEME_COLOR,
            font=(THEME_FONT_FACE, 20, "italic"),
            width=width - 5,
        )

        self.canvas = canvas

    def grid(self, row: int, column: int, columnspan: int, pady: int) -> None:
        self.canvas.grid(row=row, column=column, columnspan=columnspan, pady=pady)

    def update_text(self, text: str) -> None:
        self.canvas.itemconfig(self.text_id, text=text)

    def update_background(self, color: str) -> None:
        self.canvas.config(background=color)
