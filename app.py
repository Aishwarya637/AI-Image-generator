import streamlit as st
from openai import OpenAI
import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("api_key:", api_key)

if not api_key:
    st.error("API key not found. Please set OPENAI_API_KEY in your .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("Aishu's AI Image Generator")
st.write("Generate images of your imagination using our AI image generator.") 

# Prompt input
prompt = st.text_input("Enter your image prompt:", "A futuristic city with flying cars")
size = st.selectbox("Select image size:", ["1024x1024"], index=0)

if st.button("Generate Image"):
    if not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        with st.spinner("Generating image..."):
            try:
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size=size
                )
                if not response or not response.data:
                    st.error("No image returned. Check your API key, quota, or model name.")
                else:
                    image_url = response.data[0].url
                    st.image(image_url, caption="Generated Image", use_container_width=True)

                    # Download button
                    img_data = requests.get(image_url).content
                    st.download_button(
                        label="📥 Download Image",
                        data=img_data,
                        file_name="dalle3_image.png",
                        mime="image/png"
                    )
            except Exception as e:
                st.error(f"Error: {str(e)}")
