import streamlit as st
import time

st.title("Streamlit入門")

st.write("Interactive widgets")
"Start!!"

latest_iteration = st.empty()

bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.03)

"Done!!!!!"


# text = st.text_input("あなたを趣味を教えてください")
# "あなたのしゅみ：" ,text

# condistion = st.slider("あなたの調子は？",0,100,50)
# "コンディション：" , condistion

