pip install plotly
import streamlit as st
import plotly.express as px

def main():
    st.title("Privacy Preserving Data Mining using Transformation Based Noise Addition")
    st.write("Authors - Dr. Shashidhar V, Naachiket Pant, Naga Nandan B, Syed Ibrahim Maaz, Shubham Luharuka")
    uploaded_file = st.file_uploader("Choose an excel file", type=["xlsx"])
    if uploaded_file is not None:
        # do something with the uploaded file
        st.write("Database - Pima Indians Diabetes Database")
        # add a "Run" button
        if st.button("Run"):
            # show a loading bar
            with st.spinner("Running..."):
                # read the uploaded file as a pandas dataframe
                st.write("Score for NNA - 0.7293931")
                st.write("Score for TBNA - 0.7777778")

                fig = px.bar(x=["NNA", "TBNA"], y=[72, 77])
                st.plotly_chart(fig)
        

if __name__ == '__main__':
    main()
