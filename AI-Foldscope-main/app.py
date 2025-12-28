import streamlit as st
import numpy as np
from ultralytics import YOLO
from PIL import Image

@st.cache_resource
def load_model():
    return YOLO("best-aavi.pt")  # custom trained model

st.title("AI Foldscope Application")
st.header("Upload the File and View an Image")
st.subheader("This application takes a picture as input and analyzes it using AI techniques.")

uploaded_file = st.file_uploader("Choose an Image", type=["png", "jpg", "jpeg", "gif", "bmp"])

if uploaded_file is not None:
	try:
		image = Image.open(uploaded_file)
		img_array = np.array(image)
		model = load_model()
	except Exception as e:
		st.error(f"Error opening image: {e}")
	else:
		if st.button("View"):
			st.image(image, width=700, caption="Original Image")
			st.write("class names", model.names)
			with st.spinner("Running YOLOv8..."):
				results = model(img_array, conf=0.5)
				#results = model(uploaded_file, conf=0.01)
				st.write(results)
				for box in results[0].boxes:
					cls_id = int(box.cls[0])
					cls_name = model.names[cls_id]
					st.write(f"Detected: {cls_name}")
			annotated = results[0].plot()
			st.image(annotated, caption="Detected Objects", use_column_width=True)

