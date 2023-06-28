import streamlit as st
def main():
    lang = ['Python', 'C', 'Java','Go','PHP']
    my_choice = st.selectbox('좋아하는 언어 선택',lang)
    if my_choice == lang[0]:
        st.write('파이썬을 선택하셨습니다.')
    elif my_choice == lang[1]:
        st.write('C언어를 선택하셨습니다.')
    elif my_choice == lang[2]:
        st.write('자바을 선택하셨습니다.')
    elif my_choice == lang[3]:
        st.write('GO을 선택하셨습니다.')
    elif my_choice == lang[4]:
        st.write('PHP를 선택하셨습니다.')
if __name__ == "__main__":
    main()