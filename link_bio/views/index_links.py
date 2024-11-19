import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.constants as const
from link_bio.routes import Route


def index_links() -> rx.Component:
    return rx.vstack(
        # Comunidad
        title("Comunidad"),
        link_button(
            "Cursos gratis",
            "Consulta mis tutoriales para aprender programación",
            "/icons/linkedin.svg",
            Route.COURSES.value,
            is_external=False,
        ),
        link_button(
            "Linkedin",
            "Red social profesional",
            "/icons/linkedin.svg",
            const.LINKEDIN_URL,
        ),
        link_button(
            "GitHub", "Repositorios proyectos", "/icons/github.svg", const.GITHUB_URL
        ),
        link_button(
            "X", "Red social personal", "/icons/x-twitter.svg", const.TWITTER_X_URL
        ),
        link_button(
            "Instagram",
            "Red social personal",
            "/icons/instagram.svg",
            const.INSTAGRAM_URL,
        ),
        link_button(
            "Facebook", "Red social personal", "/icons/facebook.svg", const.FACEBOOK_URL
        ),
        # Recursos
        title("Recursos y más"),
        link_button(
            "YouTube",
            "Tutoriales sobre desarrollo de software y más",
            "/icons/youtube.svg",
            const.YOUTUBE_URL,
        ),
        # Contacto
        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia",
            "/icons/email.svg",
            const.MY_PUBLICINBOX_URL,
        ),
        link_button("Email", const.EMAIL, "/icons/email.svg", f"mailto:{const.EMAIL}"),
        spacing="3",
        width="100%",
    )
