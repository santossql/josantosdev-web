import reflex as rx

from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.links import links
from link_bio.components.footer import footer
from link_bio.views.sponsors import sponsors
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


title = "JosantosDev | Te enseño programación y desarrollo de software."
description = "Hola, mi nombre es Jonathan Santos. Soy ingeniero de software, desarrollo freelancer full-stack y divulgador."
preview = "https://josantosdev.com/preview.jpg"

app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=False,
        radius="large",
        accent_color="gray",
    ),
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://googletagmanager.com/gtag/js?id=XXXXXXXXXXX"),
        rx.script(
            """
            windows.datalayer = window.datalayer || [];
            function gtag(){datalayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'XXXXXXXXX');
            """
        ),
    ],
)
app.add_page(
    index,
    title=title,
    description=description,
    image="logo.png",
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "sumamary_large_image"},
        {"name": "twitter:site", "content": "@josantosdev"},
    ],
)
