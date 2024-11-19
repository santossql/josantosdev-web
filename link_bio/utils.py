import reflex as rx


# Comun
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "https://josantosdev.com/preview.jpg"

__meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "sumamary_large_image"},
    {"name": "twitter:site", "content": "@josantosdev"},
]


# Index
index_title = "JosantosDev | Te enseño programación y desarrollo de software."
index_description = "Hola, mi nombre es Jonathan Santos. Soy ingeniero de software, desarrollo freelancer full-stack y divulgador."
index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]

index_meta.extend(__meta)

# Cursos
cursos_title = "JosantosDev | Mis cursos"
cursos_description = "Cursos de programación gratuita."
cursos_meta = [
    {"name": "og:title", "content": cursos_title},
    {"name": "og:description", "content": cursos_description},
]

cursos_meta.extend(__meta)
