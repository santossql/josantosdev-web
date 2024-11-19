import reflex as rx
from link_bio.styles.styles import Size as Size
import link_bio.styles.styles as styles


def link_button(
    title: str, body: str, image: str, url: str, is_external=True
) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    alt=title,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style, as_="span"),
                    rx.text(body, style=styles.button_body_style, as_="span"),
                    spacing="0",
                    align="start",
                    padding_y=Size.SMALL.value,
                    padding_rigth=Size.SMALL.value,
                ),
                spacing="0",
                width="100%",
            ),
        ),
        href=url,
        is_external=is_external,
        width="100%",
    )
