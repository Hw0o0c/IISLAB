import streamlit as st
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates


col1, col2 = st.columns(2)

with col1:
    st.write("## Url example")

    with st.echo("below"):
        value = streamlit_image_coordinates(
            "https://placekitten.com/200/300",
            key="url",
        )

        st.write(value)

with col2:
    st.write("## Url example")

    with st.echo("below"):
        value = streamlit_image_coordinates(
            "https://placekitten.com/200/300",
            key="url",
        )

        st.write(value)