import streamlit as st

def main():
    st.title("Text Editor")

    st.markdown("""<style>
                .css-2trqyj {
                    width: 500px !important;
                    height: 100px !important;
                }
                </style>""", unsafe_allow_html=True)


    text = st.text_area("Enter your text here", height=500)


    words = text.split()
    st.write(f"Word count: {len(words)}")

    if st.button("Download File"):
        download_link = f'<a href="data:text/plain;charset=utf-8,{text}" download="text_editor_content.txt">Download File</a>'
        st.markdown(download_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
