import streamlit as st
import base64

# Function to convert local image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load your local background image
img_path = r"C:\Users\vozon\Downloads\ai.background.jpg"
  # change this to your image file path
img_base64 = get_base64_of_bin_file(img_path)

# Inject CSS with Base64 background
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{img_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0); /* Hide header background */
}}
[data-testid="stToolbar"] {{
    right: 2rem;
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("Choose Your Favorite Coding Language")

# Dropdown (selectbox)
language = st.selectbox(
    "Select your favorite language:",
    ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
)

st.write(f"✅ Your favorite language is **{language}**")
