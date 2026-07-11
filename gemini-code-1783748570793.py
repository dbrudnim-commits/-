import streamlit as st
import re

# --- [1. 채점 기준 데이터베이스] ---
# 1-1. 의미 기반 허용 용어 사전
METHOD_SYNONYMS = {
    '정의': ['정의', '뜻풀이', '의미', '개념'],
    '예시': ['예시', '예를 들어', '사례', '예'],
    '대조': ['대조', '비교', '차이'],
    '분류': ['분류', '구분', '종류', '나누어']
}

# 1-2. 오개념 방지를 위한 방법별 필수 '이유' 키워드
VALID_REASONS = {
    '정의': ['뜻', '의미', '개념', '명확'],
    '예시': ['사례', '구체적', '친숙', '이해'],
    '대조': ['차이', '부각', '선명'],
    '분류': ['나누', '체계적', '기준', '정리']
}

# 1-3. 문항 2 연계성 확인을 위한 방법별 본문 필수 표지
TEXT_MARKERS = {
    '정의': ['말한다', '뜻한다', '이란', '이다'],
    '예시': ['예를 들어', '예로', '대표적으로', '등이 있다'],
    '대조': ['달리', '반면', '차이', '비교하면'],
    '분류': ['나뉜다', '첫째', '둘째', '구분할 수', '크게']
}

# 1-4. 제재별 결론 방향성 필수 키워드
CONCLUSION_KEYWORDS = {
    '스마트폰': ['기대', '발전', '미래', '변화', '편리'],
    '인공지능': ['태도', '이해', '미래', '활용', '공존'],
    '재활용': ['실천', '환경', '보호', '확인', '지구']
}

# 1-5. 선택지별 모범 답안 데이터베이스
MODEL_ANSWERS = {
    '정의': "대상: 정의 / 이유: 핵심 개념을 명확히 하여 독자의 오해를 막기 위함 / 본문 적용: '~은 ~을 뜻한다' 형식 사용 / 영상: 대상의 핵심 단어 부각 자막",
    '예시': "대상: 예시 / 이유: 구체적인 사례를 들어 친숙하고 쉽게 설명하기 위함 / 본문 적용: '예를 들면 ~등이 있다' 형식 사용 / 영상: 실제 사례 사진이나 영상 제시",
    '대조': "대상: 대조 / 이유: 차이점을 부각하여 독자적인 특성을 선명히 드러내기 위함 / 본문 적용: '~와 달리 ~한 반면' 형식 사용 / 영상: 화면 2분할, O/X 등 시각적 대조 연출",
    '분류': "대상: 분류(구분) / 이유: 하위 종류를 나누어 체계적으로 정리하기 위함 / 본문 적용: '첫째, 둘째' 형식 사용 / 영상: 번호 표지, 아이콘 나열 등 인포그래픽 연출"
}

# --- [2. 채점 로직 함수] ---
def normalize_method(input_text):
    """입력된 텍스트에서 의미상 허용되는 설명 방법 공식 명칭을 추출합니다."""
    for standard_method, synonyms in METHOD_SYNONYMS.items():
        if any(syn in input_text for syn in synonyms):
            return standard_method
    return None

def evaluate_q1(method_input, reason_input):
    method = normalize_method(method_input)
    if not method:
        return False, None, "❌ 유효한 설명 방법이 작성되지 않았거나 파악할 수 없습니다."
    
    # 오개념 검사: 선택한 방법의 특성이 이유에 맞게 서술되었는지 확인
    if any(kw in reason_input for kw in VALID_REASONS[method]):
        return True, method, f"✅ [통과] '{method}'의 특성이 이유에 올바르게 서술되었습니다."
    else:
        return False, method, f"❌ [오개념 발생] '{method}'을 선택했으나, 이유 서술 시 해당 방법의 본래 목적(특성)이 드러나지 않았습니다."

def evaluate_q2(text, method1, method2, topic):
    feedback = []
    score = 0
    
    # 1. 분량 및 구조 검사 (단순 길이 및 단락 기준)
    paragraphs = [p for p in text.split('\n') if len(p.strip()) > 0]
    if len(paragraphs) >= 3:
        feedback.append("✅ [통과] 서론-본론-결론의 3단 구조(줄바꿈)를 갖추었습니다.")
        score += 1
    else:
        feedback.append("⚠️ [감점] 줄바꿈이 부족하여 서-본-결 구조가 시각적으로 불명확합니다.")
        
    # 2. 설명 방법 연계성 검사 (문항 1의 방법이 쓰였는지)
    for m in [method1, method2]:
        if m and any(marker in text for marker in TEXT_MARKERS[m]):
            feedback.append(f"✅ [통과] 본문에 '{m}'의 특성을 담은 표현이 명확히 드러났습니다.")
            score += 2
        elif m:
            feedback.append(f"❌ [감점] 문항 1에서 계획한 '{m}'의 특성이나 표현이 본문에 나타나지 않습니다.")
            
    # 3. 결론 방향성 검사
    conclusion_text = paragraphs[-1] if paragraphs else text
    if any(kw in conclusion_text for kw in CONCLUSION_KEYWORDS[topic]):
        feedback.append(f"✅ [통과] 조건에서 요구한 결론 방향(제재 관련 다짐/전망 등)이 명확히 드러났습니다.")
        score += 2
    else:
        feedback.append("❌ [감점] 맺음말에 제재에 맞는 올바른 결론 방향이 제시되지 않았습니다.")
        
    return score, feedback

# --- [3. Streamlit UI 구성] ---
st.set_page_config(page_title="서논술형 자동 채점 시스템", layout="wide")
st.title("📝 국어과 서논술형 문항 자동 채점기")
st.markdown("---")

# 제재 선택
topic = st.selectbox("📌 채점할 제재(세트)를 선택하세요", ["스마트폰", "인공지능", "재활용"])

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("학생 답안 입력")
    st.markdown("**[문항 1] 설명 방법 계획**")
    m1 = st.text_input("설명 방법 1 (명칭 또는 의미)")
    r1 = st.text_area("설명 방법 1 선택 이유", height=68)
    m2 = st.text_input("설명 방법 2 (명칭 또는 의미)")
    r2 = st.text_area("설명 방법 2 선택 이유", height=68)
    
    st.markdown("**[문항 2] 설명하는 글 쓰기**")
    q2_text = st.text_area("완성된 글 작성 (서론-본론-결론)", height=200)

with col2:
    st.subheader("📊 채점 결과 및 피드백")
    if st.button("채점 실행하기", type="primary"):
        with st.spinner("채점 로직 구동 중..."):
            
            # Q1 채점
            st.markdown("### 1️⃣ 문항 1 평가 (오개념 및 허용 범위 확인)")
            pass1, ext_m1, fb1 = evaluate_q1(m1, r1)
            pass2, ext_m2, fb2 = evaluate_q1(m2, r2)
            st.write(fb1)
            st.write(fb2)
            
            # Q2 채점
            st.markdown("### 2️⃣ 문항 2 평가 (연계성 및 결론 방향 확인)")
            if q2_text.strip() == "":
                st.warning("문항 2 답안이 입력되지 않았습니다.")
            else:
                score2, fbs2 = evaluate_q2(q2_text, ext_m1, ext_m2, topic)
                for fb in fbs2:
                    st.write(fb)
            
            # 선택지별 모범 답안 출력
            st.markdown("---")
            st.markdown("### 💡 선택한 설명 방법에 따른 모범 답안 (참고용)")
            if ext_m1 in MODEL_ANSWERS:
                st.info(f"**[{ext_m1} 모범 답안]**\n{MODEL_ANSWERS[ext_m1]}")
            if ext_m2 in MODEL_ANSWERS:
                st.info(f"**[{ext_m2} 모범 답안]**\n{MODEL_ANSWERS[ext_m2]}")