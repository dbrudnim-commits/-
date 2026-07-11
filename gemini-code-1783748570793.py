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

# 제재별 화면에 띄워줄 지문, 조건 및 [도움 질문] 데이터
TOPIC_CONTENT = {
    '스마트폰': {
        'title': "📱 우리 손안의 작은 세상 — 스마트폰의 세계",
        'text': "[학생 일기] 오늘 할머니 댁에 갔는데 할머니께서 옛날 폴더폰을 쓰고 계셨다. 내가 쓰던 스마트폰으로 유튜브 영상을 보여드리고 영상통화도 걸어드리니 눈이 휘둥그레지셨다. 문득 매일 쓰는 스마트폰이 과거의 전화기와 정확히 뭐가 다르고, 또 어떤 기능들이 숨어있는지 정리해서 할머니께 설명해 드리고 싶어졌다.",
        'q1_cond': "설명 대상인 '스마트폰'의 특성을 고려하여, 가장 효과적인 설명 방법 2가지를 계획하시오.",
        'q2_cond': "앞서 계획한 설명 방법 2가지의 특성이 문장에 명확히 드러나도록 '서론-본론-결론'을 갖춘 한 편의 글을 쓰시오.",
        'q2_bullet': ["반드시 문항 1에서 선택한 2가지 설명 방법의 표현 형식을 본문에 포함할 것", "맺음말(결론) 부분에는 스마트폰 기술의 편리함이나 미래 변화에 대한 기대감이 드러나도록 서술할 것"],
        # 학생 수준별 비계 설정을 위한 도움 질문 데이터
        'hints': {
            'q1': ["🤔 잠깐! 이 설명 방법이 쓰레기나 AI가 아닌 '스마트폰'을 설명할 때 왜 필요할까요?", "👉 혹시 과거 휴대폰과의 '차이점'을 말하고 싶나요? 아니면 스마트폰의 여러 '종류와 기능'을 나누어 보여주고 싶나요?"],
            'q2_intro': "📢 '서론'에 무엇을 쓸지 막막하다면?\n- 할머니에게 설명하듯 '우리가 매일 쓰는 스마트폰에 대해 알아볼까요?'라며 흥미를 끄는 문장으로 시작해 보세요!",
            'q2_body': "📢 '본론'을 채우기 힘들다면? 아래 질문에 답하는 문장을 이어 써 보세요.\n1. 과거 할머니의 폴더폰과 지금 나의 스마트폰은 어떤 점이 다른가요? ('~와 달리' 사용하기)\n2. 스마트폰의 기능에는 어떤 것들이 있나요? ('첫째, 둘째' 또는 '예를 들어' 사용하기)",
            'q2_conclusion': "📢 '결론' 마무리가 어렵다면?\n- 스마트폰 덕분에 우리 생활이 앞으로 얼마나 더 편리해질지, 미래에 대한 기대감을 한 문장으로 적으며 글을 마쳐보세요!"
        }
    },
    '인공지능': {
        'title': "🤖 인간을 닮은 컴퓨터 — 인공지능(AI)의 습격",
        'text': "[뉴스룸] 최근 이세돌을 이긴 알파고를 넘어, 인간처럼 글을 쓰고 그림을 그리는 생성형 AI가 등장했습니다. 하지만 많은 사람이 인공지능이 정확히 무엇인지 헷갈려하고, 단순한 자동화 기계와 혼동하곤 합니다. 이 추상적인 첨단 기술의 명확한 개념과 실제 일상 속 활약상을 독자들에게 쉽게 전달해 봅시다.",
        'q1_cond': "설명 대상인 '인공지능'의 특성을 고려하여, 가장 효과적인 설명 방법 2가지를 계획하시오.",
        'q2_cond': "앞서 계획한 설명 방법 2가지의 특성이 문장에 명확히 드러나도록 '서론-본론-결론'을 갖춘 한 편의 글을 쓰시오.",
        'q2_bullet': ["반드시 문항 1에서 선택한 2가지 설명 방법의 표현 형식을 본문에 포함할 것", "맺음말(결론) 부분에는 인공지능과 공존하는 인간의 올바른 태도나 이해의 필요성이 드러나도록 서술할 것"],
        'hints': {
            'q1': ["🤔 잠깐! 인공지능은 눈에 보이지 않는 복잡한 기술이에요.", "👉 독자들이 오해하지 않게 '인공지능이란 무엇인지 뜻풀이(정의)'를 먼저 해주거나, 일상 속 '실제 사례(예시)'를 보여주면 어떨까요?"],
            'q2_intro': "📢 '서론'에 무엇을 쓸지 막막하다면?\n- 최근 뉴스나 일상에서 자주 들리는 '인공지능 기술'을 언급하며 독자들의 호기심을 자극해 보세요!",
            'q2_body': "📢 '본론'을 채우기 힘들다면? 아래 질문에 답하는 문장을 이어 써 보세요.\n1. 교과서나 사전에서 말하는 인공지능의 진짜 뜻은 무엇인가요? ('~이란 ~을 뜻한다' 사용하기)\n2. 우리 일상(스마트폰, 네비게이션 등)에서 AI가 쓰이는 구체적인 예는 무엇이 있나요? ('예를 들면 ~이 있다' 사용하기)",
            'q2_conclusion': "📢 '결론' 마무리가 어렵다면?\n- 인공지능 기술이 발전하는 미래에 우리는 어떤 마음가짐이나 올바른 태도를 가져야 할지 다짐하는 문장으로 마쳐보세요!"
        }
    },
    '재활용': {
        'title': "♻️ 지구를 살리는 올바른 약속 — 분리배출의 정석",
        'text': "[생활 정보] 환경을 위해 분리배출을 열심히 하지만, 씻지 않은 컵라면 용기나 치킨 상자 속 기름종이는 재활용이 되지 않고 일반 쓰레기로 버려야 한다는 사실을 모르는 사람이 많습니다. 겉보기엔 비슷하지만 성격이 완전히 다른 쓰레기들을 체계적으로 알려주는 가이드라인을 작성해 봅시다.",
        'q1_cond': "설명 대상인 '쓰레기 분리배출'의 특성을 고려하여, 가장 효과적인 설명 방법 2가지를 계획하시오.",
        'q2_cond': "앞서 계획한 설명 방법 2가지의 특성이 문장에 명확히 드러나도록 '서론-본론-결론'을 갖춘 한 편의 글을 쓰시오.",
        'q2_bullet': ["반드시 문항 1에서 선택한 2가지 설명 방법의 표현 형식을 본문에 포함할 것", "맺음말(결론) 부분에는 지구와 환경을 위한 일상 속 실천의 의지가 명확히 드러나도록 서술할 것"],
        'hints': {
            'q1': ["🤔 잠깐! 쓰레기 분리배출은 우리가 매일 몸으로 실천해야 하는 구체적인 행동이에요.", "👉 수많은 쓰레기들을 재질별로 '나누어 정리(분류)'하거나, 헷갈리기 쉬운 쓰레기들의 '차이점(대조)'을 밝혀주면 독자에게 도움이 되지 않을까요?"],
            'q2_intro': "📢 '서론'에 무엇을 쓸지 막막하다면?\n- 우리가 매일 버리는 쓰레기 양이나 분리배출의 중요성을 강조하며 글을 시작해 보세요!",
            'q2_body': "📢 '본론'을 채우기 힘들다면? 아래 질문에 답하는 문장을 이어 써 보세요.\n1. 재활용 쓰레기는 재질에 따라 어떻게 나눌 수 있나요? ('종류는 크게 ~로 나뉜다' 사용하기)\n2. 겉보기엔 비슷하지만 재활용이 되는 것과 안 되는 것의 차이는 무엇인가요? ('~와 달리 종량제 봉투에' 사용하기)",
            'q2_conclusion': "📢 '결론' 마무리가 어렵다면?\n- 나부터 올바른 분리배출을 시작하겠다는 실천의 의지나 다짐을 담아 지구를 살리자는 문장으로 마쳐보세요!"
        }
    }
}

# --- [2. 채점 핵심 함수 (피드백 어조 부드럽게 개선)] ---
def normalize_method(input_text):
    for standard_method, synonyms in METHOD_SYNONYMS.items():
        if any(syn in input_text for syn in synonyms):
            return standard_method
    return None

def evaluate_q1(method_input, reason_input):
    method = normalize_method(method_input)
    if not method:
        return False, None, "💡 아직 설명 방법 명칭을 적지 않았거나 오타가 난 것 같아요. 다시 확인해 볼까요?"
    if any(kw in reason_input for kw in VALID_REASONS[method]):
        return True, method, f"✨ 멋져요! '{method}'이라는 방법의 쓰임새와 특성에 맞게 이유를 아주 잘 설명했습니다."
    else:
        return False, method, f"🌱 살짝 아쉬워요! 고른 방법은 '{method}'인데, 적어준 이유는 다른 설명 방법의 특징인 것 같아요. 위의 [도움 질문] 박스를 열어 이유를 다시 다듬어 볼까요?"

def evaluate_q2(text, method1, method2, topic_key):
    feedback = []
    paragraphs = [p for p in text.split('\n') if len(p.strip()) > 0]
    
    if len(paragraphs) >= 3:
        feedback.append("✨ 참 잘했어요! 서론, 본론, 결론의 모양새가 단락 구분을 통해 예쁘게 잘 보입니다.")
    else:
        feedback.append("💡 글의 짜임새 Tip: 서론이 끝나면 엔터(줄바꿈)를 치고, 본론이 끝나면 또 엔터를 쳐서 밤 세 단락으로 나누어 쓰면 더 보기 좋은 글이 된답니다!")
        
    for m in [method1, method2]:
        if m and any(marker in text for marker in TEXT_MARKERS[m]):
            feedback.append(f"✨ 성공! 문항 1에서 약속한 '{m}'의 서술 방식이 본문 문장에 잘 반영되었습니다.")
        elif m:
            feedback.append(f"💡 조건 확인: 본문에 '{m}'의 느낌이 잘 나지 않아요! 예를 들어 대조라면 '~와 달리', 정의라면 '~이란 ~을 말한다' 같은 힌트 단어를 본문에 쏙 넣어보세요.")
            
    conclusion_text = paragraphs[-1] if paragraphs else text
    if any(kw in conclusion_text for kw in CONCLUSION_KEYWORDS[topic_key]):
        feedback.append(f"✨ 최고예요! 조건에서 요청한 맺음말의 방향성이 결론 부분에 훌륭하게 녹아들었습니다.")
    else:
        feedback.append("💡 마무리 힌트: 글의 맨 마지막 문장에 조건이 요구한 생각(미래에 대한 기대/나의 다짐/올바른 태도)이 드러나도록 한 문장만 덧붙여 볼까요?")
        
    return feedback

# --- [3. Streamlit 웹앱 UI 설계] ---
st.set_page_config(page_title="국어과 서논술형 연습장", layout="centered")

st.title("✏️ 정기고사 대비 서논술형 답안 작성 연습")
st.write("상단의 탭을 눌러 문제를 풀고, 막힐 때는 언제든 **[💡 어려울 땐 열어보기]**를 눌러 도움을 받아보세요!")

tab1, tab2, tab3 = st.tabs(["📝 문제 세트 1 (스마트폰)", "📝 문제 세트 2 (인공지능)", "📝 문제 세트 3 (재활용)"])

def render_study_page(topic_key):
    data = TOPIC_CONTENT[topic_key]
    
    st.header(data['title'])
    st.info(data['text'])
    st.markdown("---")
    
    # 2. 문항 1 영역
    st.subheader("💡 [문항 1] 설명 방법 구상하기")
    st.caption(data['q1_cond'])
    
    # 문항 1용 도움 질문 박스 추가
    with st.expander("💡 [문항 1] 어떤 설명 방법을 골라야 할지 모르겠다면? (클릭)", expanded=False):
        for hint in data['hints']['q1']:
            st.write(hint)
            
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**[첫 번째 방법]**")
        m1 = st.text_input("설명 방법 명칭 입력", key=f"{topic_key}_m1", placeholder="예: 정의, 대조, 예시, 분류 중 선택")
        r1 = st.text_area("그 방법을 선택한 이유", key=f"{topic_key}_r1", placeholder="독자에게 왜 이 방법이 필요한지 서술하세요.", height=80)
    with col2:
        st.markdown("**[두 번째 방법]**")
        m2 = st.text_input("설명 방법 명칭 입력", key=f"{topic_key}_m2", placeholder="예: 정의, 대조, 예시, 분류 중 선택")
        r2 = st.text_area("그 방법을 선택한 이유", key=f"{topic_key}_r2", placeholder="독자에게 왜 이 방법이 필요한지 서술하세요.", height=80)
        
    st.markdown("---")
    
    # 3. 문항 2 영역
    st.subheader("✍️ [문항 2] 서론-본론-결론 갖춰 글 쓰기")
    st.write(data['q2_cond'])
    
    # 채점 조건 박스
    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 15px; border-radius: 8px; border-left: 5px solid #ff4b4b; margin-bottom: 15px;">
        <strong style="font-size: 16px;">〈채점 조건〉</strong><br>
        <ul style="margin-top: 5px; margin-bottom: 0px; padding-left: 20px;">
            <li>🎯 <b>문항 1에서 자신이 고른 설명 방법 2가지</b>를 본문에 모두 사용하여 문장을 쓸 것</li>
            <li>🎯 서론, 본론, 결론이 구분되도록 글을 쓰다가 중간에 <b>엔터(줄바꿈)를 쳐서 단락을 나눌 것</b></li>
            <li>🎯 <b>마무리 조건:</b> """ + data['q2_bullet'][1] + """</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 문항 2용 단계별 구체적 도움 질문 박스 대폭 강화
    with st.expander("🚀 [문항 2] 한 편의 글을 쓰기가 너무 막막하고 두렵다면? (클릭)", expanded=False):
        st.markdown(f"**[1단계: 서론 쓰기 도움말]**\n{data['hints']['q2_intro']}\n")
        st.markdown(f"**[2단계: 본론 쓰기 도움말]**\n{data['hints']['q2_body']}\n")
        st.markdown(f"**[3단계: 결론 쓰기 도움말]**\n{data['hints']['q2_conclusion']}")
        st.success("💡 위의 1, 2, 3단계 도움 질문에 대한 답변들을 부드럽게 이어 붙여 아래 칸에 작성하면 멋진 글이 완성돼요!")

    q2_text = st.text_area("이곳에 답안을 작성하세요.", key=f"{topic_key}_q2", height=250, placeholder="위의 단계별 도움말을 참고하여 차근차근 문장을 적어보세요.")
    
    # 4. 채점 및 피드백 출력
    if st.button("실시간 답안 채점 및 검토", key=f"{topic_key}_btn", type="primary"):
        st.markdown("### 📊 다정한 실시간 피드백 리포트")
        
        p1, ext_m1, fb1 = evaluate_q1(m1, r1)
        p2, ext_m2, fb2 = evaluate_q1(m2, r2)
        
        with st.expander("🔍 문항 1 생각 점검 결과", expanded=True):
            st.info(fb1)
            st.info(fb2)
            
        with st.expander("🔍 문항 2 글쓰기 조건 점검 결과", expanded=True):
            if not q2_text.strip():
                st.warning("아직 글을 작성하지 않았네요! 도움 질문을 보며 한 줄이라도 적어볼까요?")
            else:
                feedbacks = evaluate_q2(q2_text, ext_m1, ext_m2, topic_key)
                for fb in feedbacks:
                    if "❌" in fb or "💡" in fb:
                        st.warning(fb)
                    else:
                        st.success(fb)

# 탭 매핑 실행
with tab1:
    render_study_page('스마트폰')
with tab2:
    render_study_page('인공지능')
with tab3:
    render_study_page('재활용')
