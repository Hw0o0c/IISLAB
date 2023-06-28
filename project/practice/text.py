import streamlit as st

def main():
    st.title('웹 대시보드')

    name = '주일룡'

    st.text('제 이름은 {} 입니다.'.format(name))

    st.header('이 영역은 헤더 영역')

    st.subheader('이 영역은 서브헤더영역')

    st.success('작업이 성공했을때 사용')
    st.warning('경고 문구를 보여주고 싶을때 사용')
    st.info('정보를 보여주고 싶을때 사용')
    st.error('문제가 발생했을때 사용')
    # st.markdown

    st.help(sum) #함수 설명을 보여주고 싶을 때
    st.help(len)
if __name__ == '__main__':
    main()
