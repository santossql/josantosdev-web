import reflex as rx
from link_bio.styles.styles import Color

# class CustomerServiceOutlined(rx.Component):
#     library="@ant-design/icons"
#     tag="CustomerServiceOutlined"


class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    href = "https://google.com"
    target = "_blank"
    badge = {"dot": True, "color": Color.PRIMARY.value}


float_button = FloatButton.create
