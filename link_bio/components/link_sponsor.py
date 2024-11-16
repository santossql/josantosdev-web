import reflex as rx
from link_bio.styles.styles import Size as Size

def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            alt=alt,
            height=Size.VERY_BIG.value,
            width="auto",
        ),
        href=url,
        is_external=True
    )
