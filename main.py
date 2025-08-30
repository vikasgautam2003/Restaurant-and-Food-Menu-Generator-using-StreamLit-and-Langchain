import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    ("Italian", "Chinese", "Mexican", "Indian", "Thai", "French", "Japanese", "Greek")
)

if cuisine:
    # This now calls the real function from your helper file
    response = langchain_helper.get_name_item(cuisine)

    st.header(response['restaurant_name'])
    menu_items = response["menu_items"].split(",")

    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item.strip())


