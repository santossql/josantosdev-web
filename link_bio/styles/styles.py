import reflex as rx
from enum import Enum
from .colors import Color
from .colors import TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px"

# Stylesheets

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
]


# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


# Styles

BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "font_family": Font.DEFAULT,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    },
    rx.button: {
        "background_color": Color.CONTENT.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "height": "100%",
        "padding": Size.SMALL.value,
        "text_align": "start",
        "white_space": "normal",
        "width": "100%",
        "_hover": {
            "background_color": Color.SECONDARY.value,
        },
    },
    rx.link: {
        "text_decoration":"none", 
        "_hover": {},
    },
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value,
)

title_style = dict(
    padding_top=Size.DEFAULT.value, 
    width="100%"
)

button_title_style = dict(
    color=TextColor.HEADER.value,
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
)

button_body_style = dict(
    color=TextColor.BODY.value,
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
)
