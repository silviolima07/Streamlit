import streamlit as st
import os
#import app

def main():
    """ A simple iris EDA App """

    st.title("Iris EDA App with streamlit")
    st.subheader("Streamlit is a python server for web apps")
    #port = int(os.environ.get('PORT', 5000))

    port = int(os.environ.get('PORT', 5000))
    print(port)

if __name__ == '__main__':
    main()
