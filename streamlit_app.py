import streamlit as st
import random

# [기존 코드 데이터 유지]
summer = ["반팔", "반바지", "셔츠"]
spring = ["맨투맨", "긴바지", "셔츠"]
winter = ["패딩", "코트", "목도리"]
my_closet = []

# 스트림릿 앱 제목 설정
st.title("☀️ 오늘의 날씨별 코디 추천 앱")

# 기존 input()을 스트림릿의 숫자 입력창(number_input)으로 대체합니다.
# 웹 앱 특성상 화면을 끄면 종료되므로, while True와 999 종료 조건은 제외했습니다.
Temp = st.number_input("온도를 입력하세요:", value=20, step=1)

# [기존 조건문 논리 그대로 유지]
if Temp >= 25:
    my_closet = summer
    st.info("여름 옷이 선택 되었습니다.")
elif Temp >= 15:
    my_closet = spring
    st.info("봄 옷이 선택 되었습니다.")
else:
    my_closet = winter
    st.info("겨울 옷이 선택 되었습니다.")

# 결과 출력 부분 (print 대신 st.write와 st.subheader 사용)
st.write("---")
st.subheader("👕 오늘의 최종 코디")

for clothing in my_closet:
    st.write(f"- **{clothing}**")