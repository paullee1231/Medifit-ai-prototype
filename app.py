
import streamlit as st

st.title("MediFit.AI - 건강 처방 시스템")

# 1. 사용자 입력
age = st.number_input("나이", min_value=0, max_value=120, value=30)
weight = st.number_input("몸무게(kg)", min_value=30, max_value=200, value=70)
height = st.number_input("키(cm)", min_value=100, max_value=220, value=170)
symptom = st.selectbox("현재 증상", ["무증상", "관절 통증", "고혈압", "당뇨", "허리 통증"])

# 2. 간단한 AI 처방 로직 (조건 기반 예시)
if st.button("처방 분석하기"):
    bmi = weight / ((height/100) ** 2)
    
    st.subheader("AI 분석 결과")

    # 운동 가이드
    if symptom == "무증상":
        st.write("- 추천 운동: 빠르게 걷기 30분/일, 요가")
    elif symptom == "관절 통증":
        st.write("- 추천 운동: 수중 운동, 스트레칭 위주")
    elif symptom == "고혈압":
        st.write("- 추천 운동: 중강도 유산소 운동 (걷기, 실내 자전거)")
    elif symptom == "당뇨":
        st.write("- 추천 운동: 유산소 + 근력 병행")
    elif symptom == "허리 통증":
        st.write("- 추천 운동: 허리 지지 운동, 가벼운 코어 근력 운동")

    # 약물 가이드 경고
    if symptom in ["고혈압", "당뇨"]:
        st.warning("※ 약물 복용 여부에 따라 의사와 상담 후 운동을 조절하세요.")
    
    # 리포트 요약
    st.write(f"당신의 BMI는 {bmi:.1f}입니다.")
