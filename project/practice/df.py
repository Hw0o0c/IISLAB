import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('data2/iris.csv')

    st.datafram(df)
    species = df['species'].unique()

    st.text('아이리스 꽃은 ' + species + '으로 되어있다.')

    df.head()

    st.dataframe( df.head()) # 두 함수는 같은 목적으로 사용 가능
    st.write(df.head())

if __name__ == '__main__':
    main()