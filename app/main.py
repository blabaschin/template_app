from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import streamlit as st
import os.path as op
from sys import path

path.append(op.abspath(op.join(op.dirname(__file__), "..")))

from app.pages import home as home


app = FastAPI()


# Generate sidebar elements
def generate_sidebar_elements():
    pages = {
        "Home": home
    }

    # Sidebar -- Image/Title
    st.sidebar.image(
        "docs/static/workhelix.png",
        use_column_width=True,
    )

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    st.sidebar.title("Contribute!")
    st.sidebar.info(
        "WorkHelix Repo:"
        "\n\n:question: [Issues]()"
        "\n\n:handshake: [Pull Requests]()"
        "\n\n:book: [Source Code]()"
    )

    page = pages[selection]
    page.run()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


if __name__ == "__main__":
    generate_sidebar_elements()
