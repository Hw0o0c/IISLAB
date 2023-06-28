import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('D:/data/iris.csv')

    if st.checkbox('헤드 5개보기'):
        st.dataframe(df.head())
    else:
        st.text('헤드 숨겼습니다.')
if __name__ == "__main__":
    main()