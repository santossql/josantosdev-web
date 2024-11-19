import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor
import link_bio.constants as const

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Certificaciónes"),
        rx.hstack(
            link_sponsor(
                "/icons/hyland_onbase_admin.png",
                const.HYLAND_URL,
                "Hylan Onbase"
            ),
            link_sponsor(
                "/icons/oracle_certifier.png",
                const.ORACLE_URL,
                "Oracle"
            ),
            # columns=rx.breakpoints(initial="1", xs="2"),
            spacing="5",
            width="100%",
        ),
        aling_items="start",
        width="100%"
    )