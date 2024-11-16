import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=Color.PRIMARY.value,
        ),
        f" {body}",
        font_size=styles.Size.MEDIUM.value,
        color=TextColor.BODY.value,
    )
