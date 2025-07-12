# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain_openai import OpenAI, ChatOpenAI

chat_model = ChatOpenAI()

st.title('인공지능 테스트')
contents = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청"):
    with st.spinner("Wait for it..."):
        result = chat_model.invoke(contents + "에 대한 시를 써줘")
        st.write(result.content)
#print(result)

# st.write(contents + "주제로 작성된 시")
# st.write(result)