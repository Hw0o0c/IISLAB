import streamlit as st

def main():
    age = st.slider('나이', 1, 120, 30, 5) # 타이틀, 최소밸류, 최대밸류, 기본값, 스텝
    st.text('제가 선택한 나이는 {} 입니다.'.format(age))

if __name__ == "__main__":
    main()