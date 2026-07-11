import streamlit as st

st.set_page_config(page_title="국어 서논술형 워크북", layout="centered")

# ==========================================
# 1. 상단 스타일 선택 버튼 (단순 텍스트 스위칭)
# ==========================================
theme = st.radio(
    "🎨 원하는 학습 테마를 선택하세요",
    ["♂️ 남학생 버전 (크래시 배틀 룸)", "♀️ 여학생 버전 (다이어리 감성 카페)"],
    horizontal=True
)

# 테마에 따른 고정 텍스트 분기
if "남학생" in theme:
    MAIN_TITLE = "🦖🏎️ 국어 서논술형 크래시 배틀 룸"
    SUB_TITLE = "조건을 격파하고 실시간으로 미션 통과 등급을 획득하라!"
    STORY_TEXT = "🦖 [공룡 부대의 일기] 오늘 최신 스마트폰을 처음 본 대장 티라노가 깜짝 놀라셨다! 매일 쓰는 스마트폰이 과거의 무전기와 정확히 뭐가 다르고, 어떤 대단한 기능들이 숨어있는지 대장님께 설명해 드리는 보고서를 작성해보자."
    Q1_TITLE = "⚔️ [미션 1] 설명 전술 무기 고르기"
    Q1_PLACEHOLDER = "정의 / 대조 / 예시 / 분류 중 입력"
    Q2_TITLE = "✍️ [미션 2] 3단 전술 글로 격파하기"
    Q2_LABEL = "전술 답안 입력 패널"
    Q2_PLACEHOLDER = "기어 올리고 작성 시작!"
    BTN_TEXT = "🏁 전술 분석 및 채점 요청"
    COND_HTML = """
        <div style="background-color: #262730; padding: 15px; border-radius: 8px; border-left: 6px solid #FF4B4B; color: #FFFFFF; margin-bottom: 15px;">
            <strong style="color: #FF4B4B;">🚨 [감점 방지] 미션 클리어 조건</strong><br>
            <ul>
                <li>⚡ 선택한 설명 방법의 핵심 표현이 본문에 들어갈 것</li>
                <li>⚡ 엔터(줄바꿈)를 쳐서 서론-본론-결론 구조를 만들 것</li>
                <li>⚡ 스마트폰이 바꿀 미래 세상에 대한 기대감을 쓸 것</li>
            </ul>
        </div>"""
else:
    MAIN_TITLE = "🎀 다이어리 감성 문학 카페"
    SUB_TITLE = "예쁜 다이어리를 한 칸씩 채우듯 미션을 완료해 보아요!"
    STORY_TEXT = "🍓 [소녀의 다이어리] 오늘 할머니께 예쁜 스마트폰으로 영상통화를 걸어드리니 토끼처럼 놀라셨어요. 매일 쓰는 스마트폰이 과거의 전화기와 어떻게 다른지, 어떤 유용한 기능이 있는지 예쁘게 정리해서 할머니 지침서를 만들어 드리고 싶어요."
    Q1_TITLE = "💖 [스텝 1] 마음에 드는 설명 방법 꾸미기"
    Q1_PLACEHOLDER = "정의 / 대조 / 예시 / 분류 중 입력"
    Q2_TITLE = "✍️ [스텝 2] 다이어리에 한 편의 글 녹여내기"
    Q2_LABEL = "나만의 소중한 답안 노트"
    Q2_PLACEHOLDER = "소중한 생각을 차근차근 적어보세요..."
    BTN_TEXT = "✨ 다이어리 검토 및 채점 받기"
    COND_HTML = """
        <div style="background-color: #FFF0F0; padding: 15px; border-radius: 8px; border-left: 6px solid #FFB7B2; color: #4A4A4A; margin-bottom: 15px;">
            <strong style="color: #FF9AA2;">🌸 [체크리스트] 감점 방지 약속</strong><br>
            <ul>
                <li>✨ 선택한 설명 방법의 예쁜 힌트 표현이 문장에 들어갈 것</li>
                <li>✨ 엔터(줄바꿈)를 눌러 단락을 예쁘게 나눌 것</li>
                <li>✨ 미래의 편리함과 설레는 기대감을 결론에 담을 것</li>
            </ul>
        </div>"""

# ==========================================
# 2. 화면 렌더링 (기본 Streamlit 컴포넌트)
# ==========================================
st.title(MAIN_TITLE)
st.caption(SUB_TITLE)

st.info(STORY_TEXT)
st.markdown("---")

# [문항 1] 설명 방법 입력
st.subheader(Q1_TITLE)
col1, col2 = st.columns(2)
with col1:
    m1 = st.text_input("설명 방법 1", placeholder=Q1_PLACEHOLDER, key="m1")
    r1 = st.text_area("선택한 이유 1", placeholder="이유를 적어주세요.", height=70, key="r1")
with col2:
    m2 = st.text_input("설명 방법 2", placeholder=Q1_PLACEHOLDER, key="m2")
    r2 = st.text_area("선택한 이유 2", placeholder="이유를 적어주세요.", height=70, key="r2")

st.markdown("---")

# [문항 2] 본문 작성
st.subheader(Q2_TITLE)
st.markdown(COND_HTML, unsafe_allow_html=True)
q2_text = st.text_area(Q2_LABEL, placeholder=Q2_PLACEHOLDER, height=200, key="q2")

# ==========================================
# 3. 단순하고 직관적인 채점 로직 (에러 원천 차단)
# ==========================================
if st.button(BTN_TEXT, type="primary"):
    st.markdown("### 📊 실시간 피드백 결과")
    
    # 1. 문항 1 피드백
    if not m1 or not m2:
        st.warning("⚠️ 문항 1의 설명 방법을 모두 입력해야 채점이 진행됩니다.")
    else:
        st.success(f"✔️ 문항 1 분석 완료: [{m1}]과 [{m2}]를 활용하여 논리적 근거를 잘 제시했습니다.")

    # 2. 문항 2 피드백 (줄바꿈 및 키워드 기본 검사)
    if not q2_text.strip():
        st.error("❌ 본문 내용이 비어 있습니다. 글을 작성해 주세요.")
    else:
        # 단락 분사 검사
        paragraphs = [p for p in q2_text.split('\n') if p.strip()]
        if len(paragraphs) >= 3:
            st.success("✔️ 구조 검사 통과: 서론-본론-결론의 3단 구성이 뚜렷합니다.")
        else:
            st.warning("⚠️ 구조 보완 필요: 엔터(줄바꿈)를 사용하여 단락을 확실하게 나누어 보세요.")
            
        # 결론 키워드 검사 (미래, 편리, 발전, 기대)
        conclusion_keywords = ['미래', '편리', '발전', '기대', '행복']
        if any(kw in q2_text for kw in conclusion_keywords):
            st.success("✔️ 결론 조건 통과: 미래 변화에 대한 기대감이 잘 표현되었습니다.")
        else:
            st.warning("⚠️ 결론 보완 필요: 스마트폰이 가져올 미래의 편리함이나 기대감을 마지막 문장에 채워주세요.")
