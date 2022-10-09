from tkinter import Button, PhotoImage
from typing import Callable


class GuiButton(Button):
    image: PhotoImage

    def __init__(
        self,
        image_filename: str,
        handler: Callable[[], None],
    ) -> None:
        super().__init__()

        self.image = PhotoImage(file=image_filename)
        self.config(
            image=self.image,
            command=handler,
            borderwidth=0,
            highlightthickness=0,
        )
