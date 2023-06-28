import streamlit as st
import pandas as pd

def main() :
    df = pd.read_csv('D:\data\iris.csv')
    my_order = ['오름차순정렬', '내림차순정렬']

    status = st.radio('정렬방법 선택', my_order)

    if status == my_order[0]:
        df = df.sort_values('PetalLengthCm')
        st.dataframe(df)
    elif status == my_order[1]:
        df = df.sort_values('PetalLengthCm', ascending=False)
        st.dataframe(df)

    st.header('평점을 선택하세요!!')
    st.radio(label='Radio buttons', options=['5점','4점','3점','2점','1점'])
    
    # 라디오 버튼 가로로 놓기
    st.write('<style>div.row-widget.stRadio> div{flex-direction:row;}</style>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()