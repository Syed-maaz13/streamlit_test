import streamlit as st

# set maximum upload size to 500MB
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('server.maxUploadSize', 500 * 1024 * 1024)

def main():
    st.title("Privacy Preserving Data Mining using Transformation Based Noise Addition")
    uploaded_file = st.file_uploader("Choose an excel file", type=["xlsx"])
    if uploaded_file is not None:
        # do something with the uploaded file
        st.write("File uploaded successfully.")

if __name__ == '__main__':
    main()
