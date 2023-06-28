import streamlit as st

def main():
    st.title('버튼 만들기')
    st.button('버튼 클릭!')
    
    """대문자로 바꿔주는 버튼
    if st.button('대문자'):
        df['species] = df['species'].str.upper()
        st.dataframe(df)
    """

if __name__ == '__main__':
    main()
    