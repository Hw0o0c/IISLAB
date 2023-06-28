import streamlit as st

def main() :
    name = st.text_input('이름을 입력하세요!')

    if name != '':
        st.subheader(name + '님 안녕하세요??')

    address = st.text_input('주소를 입력하세요', max_chars=10)
    st.subheader(address)

    message = st.text_area('메세지를 입력하세요', height=3)
    st.subheader(message)

    st.number_input('숫자 입력',1,100)
    st.number_input('실수 입력',1.0, 100.0)

    my_date = st.date_input('약속날짜')
    st.write(my_date)

    st.write(my_date.weekday())
    st.write(my_date.strftime('%A'))

    my_time =st.time_input('시간 선택')
    st.write(my_time)

    color = st.color_picker('색을 선택하세요')
    st.write(color)

    password = st.text_input('비밀번호 입력', type='password')
    st.write(password)

if __name__ == "__main__":
    main()