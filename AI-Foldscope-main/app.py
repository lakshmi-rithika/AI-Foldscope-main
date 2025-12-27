import streamlit as st
from PIL import Image


st.title("AI Foldscope Application")
st.header("Upload and View an Image")
st.subheader("This application takes a picture as input and analyzes it using AI techniques.")

uploaded_file = st.file_uploader("Chosose an image", type=["png", "jpg", "jpeg", "gif", "bmp"])

if uploaded_file is not None:
	try:
		image = Image.open(uploaded_file)
	except Exception as e:
		st.error(f"Error opening image: {e}")
	else:
		if st.button("View"):
			st.image(image, width=700)
			st.write("Uploaded Image:")