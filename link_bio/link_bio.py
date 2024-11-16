import reflex as rx

from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
from link_bio.views.sponsors.sponsors import sponsors
import link_bio.styles.styles as styles

# Backend
# class State(rx.State):
#     pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                align="center",
                direction="column",
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value,
            ),
        ),
        footer(),
        # margin_bottom=styles.Size.BIG.value
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=False,
        radius="large",
        accent_color="gray",
    ),
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="JosantosDev | Te enseño programación y desarrollo de software.",
    description="Hola, mi nombre es Jonathan Santos. Soy ingeniero de software, desarrollo freelancer full-stack y divulgador.",
)
