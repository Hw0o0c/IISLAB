import streamlit as st
def main():
    lang = ['운동','영화감상','음악듣기','산책하기','먹기']
    st.multiselect('당신의 취미를 선택하세요. 복수 선택 가능', lang)
if __name__ == "__main__":
    main()