import reflex as rx
from link_bio.styles.styles import STYLESHEETS, BASE_STYLE
from link_bio.pages.index import index
from link_bio.pages.courses import courses

class State(rx.State):
    pass

app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    head_components=[
        rx.script(src="https://googletagmanager.com/gtag/js?id=XXXXXXXXXXX"),
        rx.script(
            """
            window.datalayer = window.datalayer || [];
            function gtag(){datalayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'XXXXXXXXX');
            """
        ),
    ],
)


# app.add_page(
#     index,
#     title=title,
#     description=description,
#     image="logo.png",
# )
