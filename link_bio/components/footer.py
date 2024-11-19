import reflex as rx
from datetime import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

now_year = datetime.today().year

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="//icons/logo_dev.svg",
            alt="Logo",
            height=Size.VERY_BIG.value,
        ),
        rx.link(
            f"© 2013-{now_year} JosantosDev by Jonathan Santos v4.",
            href="https://josantosdev.com",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM RD TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value       
        ),
        align="center",
        # margin_bottom=Size.BIG.value,
        spacing="1",
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color=TextColor.FOOTER.value,
    )
