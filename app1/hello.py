# streamlit run app1/hello.py           #for running any app on streamlit this command streamlit run folder_name/file_name.py

from PIL import Image
import streamlit as st

st.title('Sample App')
#st.header("This is a header")
#st.subheader("This is subheader")

#To open camera 
#st.camera_input('Camera Input', key="Camera Input")
image = st.camera_input("Take a Snap")
if image:
    im = Image.open(image)
    #adding purple gradient in image
    color = st.color_picker("Pick a color", "#00f900")
    im2 = Image.new("RGB", im.size, color)
    #overlaying two images
    im = Image.blend(im,im2, 0.5)  #Blending image 1 &2 both 50%
    #resize img by 30%
    im = im.resize((int(im.size[0]*0.3), int(im.size[1]*0.3)))
    st.image(im)

    st.sidebar.image(im)

    filename = st.text_input("Save As", "image.png")
    if st.button('Save'):   #creating a button named save
        im.save(filename)
        st.snow()