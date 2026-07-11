import streamlit as st

# --- [1. 채점 기준 및 제재 데이터베이스] ---
METHOD_SYNONYMS = {
    '정의': ['정의', '뜻풀이', '의미', '개념'],
    '예시': ['예시', '예를 들어', '사례', '예'],
    '대조': ['대조', '비교', '차이'],
    '분류': ['분류', '구분', '종류', '나누어']
}

VALID_REASONS = {
    '정의': ['뜻', '의미', '개념', '명확'],
    '예시': ['사례', '구체적', '친숙', '이해'],
    '대조': ['차이', '부각', '선명'],
    '분류': ['나누', '체계적', '기준', '정리']
}

TEXT_MARKERS = {
    '정의': ['말한다', '뜻한다', '이란', '이다'],
    '예시': ['예를 들어', '예로', '대표적으로', '등이 있다'],
    '대조': ['달리', '반면', '차이', '비교하면'],
    '분류': ['나뉜다', '첫째', '둘째', '구분할 수', '크게']
}

CONCLUSION_KEYWORDS = {
    '스마트폰': ['기대', '발전', '미래', '변화', '편리'],
    '인공지능': ['태도', '이해', '미래', '활용', '공존'],
    '재활용': ['실천', '환경', '보호', '확인', '지구']
}

# 제재별 화면에 띄워줄 지문 및 조건 데이터
TOPIC_CONTENT = {
    '스마트폰': {
        'title': "📱 우리 손안의 작은 세상 — 스마트폰의 세계",
        'text': "[학생 일기] 오늘 할머니 댁에 갔는데 할머니께서 옛날 폴더폰을 쓰고 계셨다. 내가 쓰던 스마트폰으로 유튜브 영상을 보여드리고 영상통화도 걸어드리니 눈이 휘둥그레지셨다. 문득 매일 쓰는 스마트폰이 과거의 전화기와 정확히 뭐가 다르고, 또 어떤 기능들이 숨어있는지 정리해서 할머니께 설명해 드리고 싶어졌다.",
        'q1_cond': "설명 대상인 '스마트폰'의 특성을 고려하여, 가장 효과적인 설명 방법 2가지를 계획하시오.",
        'q2_cond': "앞서 계획한 설명 방법 2가지의 특성이 문장에 명확히 드러나도록 '서론-본론-결론'을 갖춘 한 편의 글을 쓰시오.",
        'q2_bullet': ["반드시 문항 1에서 선택한 2가지 설명 방법의 표현 형식을 본문에 포함할 것", "맺음말(결론) 부분에는 스마트폰 기술의 편리함이나 미래 변화에 대한 기대감이 드러나도록 서술할 것"]
    },
    '인공지능': {
        'title': "🤖 인간을 닮은 컴퓨터 — 인공지능(AI)의 습격",
        'text': "[뉴스룸] 최근 이세돌을 이긴 알파고를 넘어, 인간처럼 글을 쓰고 그림을 그리는 생성형 AI가 등장했습니다. 하지만 많은 사람이 인공지능이 정확히 무엇인지 헷갈려하고, 단순한 자동화 기계와 혼동하곤 합니다. 이 추상적인 첨단 기술의 명확한 개념과 실제 일상 속 활약상을 독자들에게 쉽게 전달해 봅시다.",
        'q1_cond': "설명 대상인 '인공지능'의 특성을 고려하여, 가장 효과적인 설명 방법 2가지를 계획하시오.",
        'q2_cond': "앞서 계획한 설명 방법 2가지의 특성이 문장에 명확히 드러나도록 '서론-본론-결론'을 갖춘 한 편의 글을 쓰시오.",
        'q2_bullet': ["반드시 문항 1에서 선택한 2가지 설명 방법의 표현 형식을 본문에 포함할 것", "맺음말(결론) 부분에는 인공지능과 공존하는 인간의 올바른 태도나 이해의 필요성이 드러나도록 서술할 것"]
    },
    '재활용': {
        'title': "♻️ 지구를 살리는 올바른 약속 — 분리배출의 정석",
        'text': "[생활 정보] 환경을 위해 분리배출을 열심히 하지만, 씻지 않은 컵라면 용기나 치킨 상자 속 기름종이는 재활용이 되지 않고 일반 쓰레기로 버려야 한다는 사실을 모르는 사람이 많습니다. 겉보기엔 비슷하지만 성격이 완전히 다른 쓰레기들을 체계적으로 알려주는 가이드라인을 작성해 봅시다.",
        'q1_cond': "설명 대상인 '쓰레기 분리배출'의 특성을 고려하여, 가장 효과적인 설명 방법 2가지를 계획하시오.",
        'q2_cond': "앞서 계획한 설명 방법 2가지의 특성이 문장에 명확히 드러나도록 '서론-본론-결론'을 갖춘 한 편의 글을 쓰시오.",
        'q2_bullet': ["반드시 문항 1에서 선택한 2가지 설명 방법의 표현 형식을 본문에 포함할 것", "맺음말(결론) 부분에는 지구와 환경을 위한 일상 속 실천의 의지가 명확히 드러나도록 서술할 것"]
    }
}

# --- [2. 채점 핵심 함수] ---
def normalize_method(input_text):
    for standard_method, synonyms in METHOD_SYNONYMS.items():
        if any(syn in input_text for syn in synonyms):
            return standard_method
    return None

def evaluate_q1(method_input, reason_input):
    method = normalize_method(method_input)
    if not method:
        return False, None, "❌ 설명 방법 명칭이 비어있거나 올바르지 않습니다."
    if any(kw in reason_input for kw in VALID_REASONS[method]):
        return True, method, f"✅ [통과] '{method}'의 개념적 특성에 맞게 이유를 잘 서술했습니다."
    else:
        return False, method, f"❌ [오개념 발생] '{method}'을 고르고 이유는 다른 설명 방법의 특성을 서술했습니다. (개념 혼동 우려)"

def evaluate_q2(text, method1, method2, topic_key):
    feedback = []
    paragraphs = [p for p in text.split('\n') if len(p.strip()) > 0]
    
    if len(paragraphs) >= 3:
        feedback.append("✅ [통과] 서론-본론-결론 구조가 단락 구분을 통해 잘 드러납니다.")
    else:
        feedback.append("⚠️ [구조 미흡] 서론, 본론, 결론을 작성할 때 줄바꿈(엔터)을 활용해 단락을 명확히 나눠주세요.")
        
    for m in [method1, method2]:
        if m and any(marker in text for marker in TEXT_MARKERS[m]):
            feedback.append(f"✅ [통과] 본문에 '{m}'의 서술 방식이 조건에 맞게 녹아있습니다.")
        elif m:
            feedback.append(f"❌ [조건 미흡] 문항 1에서 구상한 '{m}'의 서술 특징(표지 단어)이 글에 나타나지 않습니다.")
            
    conclusion_text = paragraphs[-1] if paragraphs else text
    if any(kw in conclusion_text for kw in CONCLUSION_KEYWORDS[topic_key]):
        feedback.append(f"✅ [통과] 조건에서 요구한 결론의 방향성이 맺음말에 잘 반영되었습니다.")
    else:
        feedback.append("❌ [결론 오류] 조건에 제시된 맺음말 필수 서술 방향(전망/의지/태도 등)이 누락되었습니다.")
        
    return feedback

# --- [3. Streamlit 웹앱 UI 설계] ---
st.set_page_config(page_title="국어과 서논술형 연습장", layout="centered")

st.title("✏️ 정기고사 대비 서논술형 답안 작성 연습")
st.write("상단의 탭을 눌러 세트별 문항을 연습하고 실시간 피드백을 받아보세요!")

# 탭 구성 (이미지처럼 문제 세트별 탑 다운 전환)
tab1, tab2, tab3 = st.tabs(["📝 문제 세트 1 (스마트폰)", "📝 문제 세트 2 (인공지능)", "📝 문제 세트 3 (재활용)"])

def render_study_page(topic_key):
    data = TOPIC_CONTENT[topic_key]
    
    # 1. 제재 글 타이틀 및 지문 박스
    st.header(data['title'])
    st.info(data['text'])
    
    st.markdown("---")
    
    # 2. 문항 1 영역
    st.subheader("💡 [문항 1] 설명 방법 구상하기")
    st.caption(data['q1_cond'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**[첫 번째 방법]**")
        m1 = st.text_input("설명 방법 명칭 입력", key=f"{topic_key}_m1", placeholder="예: 정의, 대조, 예시 등")
        r1 = st.text_area("그 방법을 선택한 이유", key=f"{topic_key}_r1", placeholder="대상의 특성과 연결 지어 서술하세요.", height=80)
    with col2:
        st.markdown("**[두 번째 방법]**")
        m2 = st.text_input("설명 방법 명칭 입력", key=f"{topic_key}_m2", placeholder="예: 정의, 대조, 예시 등")
        r2 = st.text_area("그 방법을 선택한 이유", key=f"{topic_key}_r2", placeholder="대상의 특성과 연결 지어 서술하세요.", height=80)
        
    st.markdown("---")
    
    # 3. 문항 2 영역
    st.subheader("✍️ [문항 2] 서론-본론-결론 갖춰 글 쓰기")
    st.write(data['q2_cond'])
    
    # 예시 이미지 느낌의 <조건> 박스 스타일링
    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 15px; border-radius: 8px; border-left: 5px solid #ff4b4b; margin-bottom: 20px;">
        <strong style="font-size: 16px;">〈채점 조건〉</strong><br>
        <ul style="margin-top: 5px; margin-bottom: 0px; padding-left: 20px;">
            <li>🎯 <b>문항 1에서 자신이 설계한 두 가지 설명 방법</b>을 본문에 모두 활용할 것</li>
            <li>🎯 서론, 본론, 결론의 짜임새가 보이도록 <b>단락을 구분(줄바꿈)</b>하여 서술할 것</li>
            <li>🎯 <b>조건:</b> """ + data['q2_bullet'][1] + """</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    q2_text = st.text_area("이곳에 답안을 작성하세요. (엔터를 누르면 단락이 구분됩니다)", key=f"{topic_key}_q2", height=250, placeholder="머리말(서론)로 글을 시작해 보세요...")
    
    # 4. 채점 및 피드백 출력
    if st.button("실시간 답안 채점 및 검토", key=f"{topic_key}_btn", type="primary"):
        st.markdown("### 📊 실시간 채점 리포트")
        
        # 문항 1 검증
        p1, ext_m1, fb1 = evaluate_q1(m1, r1)
        p2, ext_m2, fb2 = evaluate_q1(m2, r2)
        
        with st.expander("🔍 문항 1 개념 검증 결과 보기", expanded=True):
            st.write(f"첫 번째 방법: {fb1}")
            st.write(f"두 번째 방법: {fb2}")
            
        # 문항 2 검증
        with st.expander("🔍 문항 2 글쓰기 조건 검증 결과 보기", expanded=True):
            if not q2_text.strip():
                st.warning("문항 2 답안 글이 비어있습니다. 내용을 작성해 주세요.")
            else:
                feedbacks = evaluate_q2(q2_text, ext_m1, ext_m2, topic_key)
                for fb in feedbacks:
                    st.write(fb)

# 각 탭에 독립된 데이터 매핑하여 렌더링
with tab1:
    render_study_page('스마트폰')
with tab2:
    render_study_page('인공지능')
with tab3:
    render_study_page('재활용')
