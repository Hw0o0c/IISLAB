import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('D:/data/iris.csv')

    with st.expander('데이터프레임 보기'):
        
        st.dataframe(df)

if __name__ == "__main__":
    main()