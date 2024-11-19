import reflex as rx
from datetime import datetime
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.styles.styles import Size as Size

def experience():
    return datetime.today().year - datetime(2013, 1, 1).year


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="JS",
                size="6",
                src="/avatar.jpg",
                radius="full",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px solid",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        "Jonathan Santos", 
                        size="6"
                    ),
                    rx.text(
                        "@josantosdev",
                        color=TextColor.BODY.value,
                        margin_top=Size.ZERO.value,
                    ),
                    spacing="0",
                ),
                rx.vstack(
                    rx.hstack(
                        link_icon(
                            "/icons/linkedin.svg",
                            "https://linkedin.com",
                   "Linkedin"
                        ),
                        link_icon(
                            "/icons/github.svg",
                            "https://github.com",
                            "github"                     
                        ),
                        link_icon(
                            "/icons/x-twitter.svg",
                            "https://twitter.com",
                                     "X"                        
                        ),
                        link_icon(
                            "/icons/instagram.svg",
                            "https://instagram.com",
                            "Instagram"                        
                        ),
                        link_icon(
                            "/icons/facebook.svg",
                            "https://instagram.com",
                            "Facebook"                        
                        ),
                    ),
                ),
            ),
        ),
        rx.flex(
            info_text(f"{experience()}+", "Años de experiencia"),
            rx.spacer(),
            info_text(f"20+", "Proyectos"),
            rx.spacer(),
            info_text(f"100k+", "Seguidores"),
            width="100%",
        ),
        rx.text(
            f"""Soy ingeniero de software desde hace más de { experience() } años.
                Actualmente trabajo como freelance full-stack developer iOS y Android.
                Además creo contenido formativo sobre programación y tecnología en redes.
                Aquí podrás encontrar todos mis enlaces de interés. Bienvenid@!""",
            color=TextColor.BODY.value,
            font_size=Size.MEDIUM.value
        ),
        spacing="5",
        align_items="start",
    )
