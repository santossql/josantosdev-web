import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.routes import Route
from link_bio.components.ant_components import float_button


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("josantos", color=Color.PRIMARY.value, as_="span"),
                rx.text("dev", color=Color.SECONDARY.value, as_="span"),
                style=styles.navbar_title_style,
            ),
            href=Route.INDEX.value,
        ),
        # float_button(),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )
