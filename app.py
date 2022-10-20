import streamlit as st
import pandas as pd
inf = open('bible.txt', 'r', encoding="UTF-8")
st.title('Bible Verse for You')
name = st.text_input('Your name', ' ')
word = inf.readlines()
n = 0
for i in range(len(name)):
    n += int(ord(name[i]))
    pass
n = n % 50

# 이걸로 뽑기하면 굉장히 재미있을 듯 사실 재미라기 보다는 찾은 방법이긴 함.
if st.button('Bible word'):
    st.write('Bible word for', name, 'is')
    st.success(word[n])
else:
    pass
