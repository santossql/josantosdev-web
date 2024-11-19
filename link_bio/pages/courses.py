import reflex as rx
import link_bio.utils as utils
from link_bio.routes import Route

from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.components.footer import footer
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles


@rx.page(
    route=Route.COURSES.value,
    title=utils.cursos_title,
    description=utils.cursos_description,
    image=utils.preview,
    meta=utils.cursos_meta,
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
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
    )
