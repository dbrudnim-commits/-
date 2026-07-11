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

# 남학생 전용 테마가 입혀진 제재 데이터베이스
TOPIC_CONTENT = {
    '스마트폰': {
        'title': "🏎️ 슈퍼카만큼 빠른 기술 — 스마트폰 제재소",
        'text': "🦖 [공룡 부대의 일기] 오늘 랩터 부대원들과 훈련을 마치고 막사에 돌아왔는데, 대장 티라노께서 옛날 구식 무전기를 쓰고 계셨다. 내가 쓰던 최신 스마트폰으로 전술 유튜브 영상을 보여드리고 영상통화를 걸어드리니 앞발을 탁 치며 놀라셨다! 매일 쓰는 스마트폰이 과거의 무전기와 정확히 뭐가 다르고, 어떤 미친 기능들이 숨어있는지 대장님께 설명해 드리는 보고서를 작성해보자.",
        'q1_cond': "설명 대상인 '스마트폰'의 무기를 분석하여, 가장 강력한 설명 방법 2가지를 장착하시오.",
        'q2_cond': "앞서 선택한 무기(설명 방법) 2가지의 특성을 살려 '서론-본론-결론'의 완벽한 3단 전술 글을 완성하시오.",
        'q2_bullet': ["선택한 2가지 설명 방법의 시그니처 표현을 본문에 반드시 장전할 것", "마무리(결론)에는 스마트폰이 바꿀 미래 세상이나 편리함에 대한 기대감을 폭발시킬 것"],
        'hints': {
            'q1': ["🦖 어이 부대원! 스마트폰을 설명할 때 어떤 기술을 쓸까?", "👉 피처폰이나 무전기랑 스펙을 비교하는 '대조'를 쓸까? 아니면 기능별로 엔진을 쪼개서 보여주는 '분류'를 쓸까?"],
            'q2_intro': "🛠️ [1단계 엔진 시동: 서론]\n- 독자들의 시선을 단번에 사로잡을 수 있게 '우리가 매일 손에 쥐고 사는 스마트폰의 무서운 비밀을 알고 있나?'처럼 강렬하게 시작해봐!",
            'q2_body': "🛠️ [2단계 풀 악셀: 본론]\n- 자, 이제 본론에서 스펙을 보여주자. 아래 질문에 답만 채워봐.\n1. 옛날 폰과 지금 스마트폰은 뭐가 다르지? ('~와 달리', '반면' 필수 사용!)\n2. 스마트폰 안에는 어떤 대단한 기능들이 숨어있지? ('예를 들어', '첫째, 둘째' 사용!)",
            'q2_conclusion': "🛠️ [3단계 피니시 라인: 결론]\n- 마지막 골인 지점이야! 스마트폰 기술이 앞으로 얼마나 더 엄청나게 발전할지, 미래 세상에 대한 기대감을 한 문장으로 멋지게 마무리해봐!"
        }
    },
    '인공지능': {
        'title': "🦖 티라노의 두뇌를 가진 컴퓨터 — 인공지능(AI) 연구소",
        'text': "🏎️ [레이싱 뉴스] 체스 챔피언을 꺾은 알파고를 넘어, 이제는 스스로 레이싱 트랙의 최적 경로를 계산하는 '인공지능(AI) 내비게이션'이 등장했습니다! 하지만 많은 사람이 AI를 단순한 자동 세차 기계 정도로 얕보곤 합니다. 이 강력한 디지털 공룡의 진짜 정체와 우리 일상 속 활약상을 친구들에게 확실하게 각인시켜 줍시다.",
        'q1_cond': "설명 대상인 '인공지능'의 특성을 고려하여, 가장 효과적인 설명 방법 2가지를 계획하시오.",
        'q2_cond': "앞서 계획한 설명 방법 2가지의 특성이 문장에 명확히 드러나도록 '서론-본론-결론'을 갖춘 한 편의 글을 쓰시오.",
        'q2_bullet': ["반드시 문항 1에서 선택한 2가지 설명 방법의 표현 형식을 본문에 포함할 것", "맺음말(결론) 부분에는 인공지능과 공존하는 인간의 올바른 태도나 이해의 필요성이 드러나도록 서술할 것"],
        'hints': {
            'q1': ["🦖 크아앙! 인공지능은 눈에 보이지 않는 초강력 두뇌야.", "👉 헷갈려하는 친구들을 위해 '인공지능이란 정확히 이런 뜻이다!(정의)'를 박아주거나, 게임/자율주행 같은 '실제 소름 돋는 사례(예시)'를 보여주면 어떨까?"],
            'q2_intro': "🛠️ [1단계 레이더 가동: 서론]\n- 요즘 롤(LoL) 핵이나 알파고처럼 핫한 '인공지능' 이야기를 툭 던지면서 친구들의 호기심을 자극해봐!",
            'q2_body': "🛠️ [2단계 터보 부스터: 본론]\n- 본격적인 설명 타임! 아래 질문에 답해보자.\n1. 인공지능의 진짜 과학적 정의가 뭐지? ('~이란 ~을 뜻한다' 사용!)\n2. 우리 일상이나 게임 속에서 AI가 활약하는 진짜 예시는? ('예를 들면 ~이 있다' 사용!)",
            'q2_conclusion': "🛠️ [3단계 깃발 체커: 결론]\n- 결론이야! 이 강력한 AI 기술과 함께 살아갈 우리 인간 레이서들은 앞으로 어떤 멋진 마음가짐이나 태도를 가져야 할지 다짐하며 끝내자!"
        }
    },
    '재활용': {
        'title': "🌋 지구 환경을 지키는 변신 로봇 — 분리배출 정비소",
        'text': "🦖 [화산지대 미션] 지구 온난화로 공룡들이 살던 화산이 폭발하기 직전입니다! 환경을 지키기 위해 분리배출을 하지만, 떡볶이가 묻은 플라스틱이나 치킨 상자 속 기름종이는 재활용 로봇이 먹지 못하고 고장 난다는 사실을 모르는 대원들이 많습니다. 완벽하게 변신하여 재태어날 쓰레기들의 계급과 정비 법칙을 깔끔하게 정리해 줍시다.",
        'q1_cond': "설명 대상인 '쓰레기 분리배출'의 특성을 고려하여, 가장 효과적인 설명 방법 2가지를 계획하시오.",
        'q2_cond': "앞서 계획한 설명 방법 2가지의 특성이 문장에 명확히 드러나도록 '서론-본론-결론'을 갖춘 한 편의 글을 쓰시오.",
        'q2_bullet': ["반드시 문항 1에서 선택한 2가지 설명 방법의 표현 형식을 본문에 포함할 것", "맺음말(결론) 부분에는 지구와 환경을 위한 일상 속 실천의 의지가 명확히 드러나도록 서술할 것"],
        'hints': {
            'q1': ["🏎️ 쓰레기 분리배출은 지구 방위대의 핵심 작전이야!", "👉 수많은 쓰레기 부품들을 재질에 따라 착착 '나누어 줄 세우는 방법(분류)'이나, 헷갈리는 녀석들의 '차이점(대조)'을 부각하면 격파하기 쉽겠지?"],
            'q2_intro': "🛠️ [1단계 사이렌 발령: 서론]\n- 매일 쏟아지는 쓰레기 더미 때문에 지구가 아파한다는 경고를 날리며 웅장하게 시작해봐!",
            'q2_body': "🛠️ [2단계 부품 분해: 본론]\n- 정확한 가이드를 주자. 아래 질문을 문장으로 만들어봐.\n1. 쓰레기 부품들은 재질에 따라 어떻게 대분류할 수 있지? ('종류는 크게 ~로 나뉜다' 사용!)\n2. 겉은 비슷해도 재활용 대장과 일반 쓰레기 졸개의 차이는 뭐지? ('~와 달리 종량제에' 사용!)",
            'q2_conclusion': "🛠️ [3단계 지구 수호 성공: 결론]\n- 승리의 마무리! 나부터 올바른 분리배출 작전을 성공시키겠다는 단단한 실천 의지와 다짐을 담아 멋지게 끝맺음해봐!"
        }
    }
}

# --- [2. 채점 핵심 함수 (남학생 스타일 어조로 변경)] ---
def normalize_method(input_text):
    for standard_method, synonyms in METHOD_SYNONYMS.items():
        if any(syn in input_text for syn in synonyms):
            return standard_method
    return None

def evaluate_q1(method_input, reason_input):
    method = normalize_method(method_input)
    if not method:
        return False, None, "⚙️ 무기(설명 방법)가 장착되지 않았거나 오타가 났어! 명칭을 다시 세팅해봐."
    if any(kw in reason_input for kw in VALID_REASONS[method]):
        return True, method, f"🔥 [임무 완료] 대박! '{method}'의 핵심 특성을 정확히 꿰뚫고 완벽한 이유를 적었어."
    else:
        return False, method, f"⚠️ [엔진 과열] 장착한 무기는 '{method}'인데, 설명은 다른 무기의 기술을 쓰고 있어! 아래 [정비소 가이드]를 열어 튜닝해볼까?"

def evaluate_q2(text, method1, method2, topic_key):
    feedback = []
    paragraphs = [p for p in text.split('\n') if len(p.strip()) > 0]
    
    if len(paragraphs) >= 3:
        feedback.append("🔥 [임무 완료] 서론-본론-결론의 3단 전술 배치가 아주 깔끔하게 정돈되었다!")
    else:
        feedback.append("⚙️ [전술 수정] 글이 통째로 뭉쳐있어! 서론 쓰고 엔터! 본론 쓰고 엔터! 단락을 딱딱 나눠줘야 가독성 부스터가 켜져.")
        
    for m in [method1, method2]:
        if m and any(marker in text for marker in TEXT_MARKERS[m]):
            feedback.append(f"🔥 [임무 완료] 문항 1에서 고른 핵심 기술 '{m}' 파워가 본문 문장에 제대로 박혔어!")
        elif m:
            feedback.append(f"⚙️ [전술 수정] 본문에 '{m}'의 파워가 안 보여! 대조라면 '~와 달리', 정의라면 '~이란 ~이다' 같은 시그니처 단어를 치트키처럼 써봐.")
            
    conclusion_text = paragraphs[-1] if paragraphs else text
    if any(kw in conclusion_text for kw in CONCLUSION_KEYWORDS[topic_key]):
        feedback.append(f"🔥 [임무 완료] 미션 요구사항인 '결론의 방향성'까지 멋지게 완파했다!")
    else:
        feedback.append("⚙️ [전술 수정] 피니시 라인 부실! 마지막 문장에 조건이 요구한 피니시 핵심(미래 기대/나의 다짐/태도)을 한 문장만 묵직하게 더 던져봐!")
        
    return feedback

# --- [3. Streamlit 웹앱 UI 설계] ---
st.set_page_config(page_title="남학생 전용 서논술형 트랙", layout="centered")

# 대문 디자인 - 강렬하고 스포티하게
st.title("🦖🏎️ 국어 서논술형 크래시 배틀 룸")
st.write("조건을 격파하고 실시간으로 미션 통과 등급을 획득하라! 막힐 땐 **[🛠️ 정비소 가이드]** 팝업을 열어봐.")

# 남학생들이 좋아하는 이름으로 탭 구성
tab1, tab2, tab3 = st.tabs(["🦖 세트 1 (티라노 스마트폰)", "🏎️ 세트 2 (AI 슈퍼카)", "🌋 세트 3 (볼케이노 분리배출)"])

def render_study_page(topic_key):
    data = TOPIC_CONTENT[topic_key]
    
    st.header(data['title'])
    # 지문 상자를 어두운 기지 느낌으로 스타일링
    st.info(data['text'])
    st.markdown("---")
    
    # 2. 문항 1 영역
    st.subheader("⚔️ [미션 1] 설명 전술 무기 고르기")
    st.caption(data['q1_cond'])
    
    with st.expander("🛠️ [무기 정비소] 어떤 무기를 장착해야 할지 고민된다면? (클릭)", expanded=False):
        for hint in data['hints']['q1']:
            st.write(hint)
            
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**[주무기 1번]**")
        m1 = st.text_input("무기 이름 (설명 방법)", key=f"{topic_key}_m1", placeholder="정의 / 대조 / 예시 / 분류 중 입력")
        r1 = st.text_area("이 무기를 고른 전술적 이유", key=f"{topic_key}_r1", placeholder="이 기술이 독자에게 왜 먹히는지 적어봐.", height=80)
    with col2:
        st.markdown("**[보조무기 2번]**")
        m2 = st.text_input("무기 이름 (설명 방법)", key=f"{topic_key}_m2", placeholder="정의 / 대조 / 예시 / 분류 중 입력")
        r2 = st.text_area("이 무기를 고른 전술적 이유", key=f"{topic_key}_r2", placeholder="이 기술이 독자에게 왜 먹히는지 적어봐.", height=80)
        
    st.markdown("---")
    
    # 3. 문항 2 영역
    st.subheader("✍️ [미션 2] 3단 전술 글로 격파하기")
    st.write(data['q2_cond'])
    
    # 레이싱 서킷 감점 방지 조건 박스 (레드 포인트)
    st.markdown("""
    <div style="background-color: #262730; padding: 15px; border-radius: 8px; border-left: 6px solid #FF4B4B; border-right: 6px solid #FF4B4B; color: #FFFFFF; margin-bottom: 15px;">
        <strong style="font-size: 16px; color: #FF4B4B;">🚨 [감점 방지] 미션 클리어 조건</strong><br>
        <ul style="margin-top: 5px; margin-bottom: 0px; padding-left: 20px; color: #E0E0E0;">
            <li>⚡ <b>방금 장착한 무기 2가지</b>의 핵심 표현 형식이 문장에 무조건 묻어나올 것</li>
            <li>⚡ 쓰다가 중간에 <b>엔터(줄바꿈)를 쾅! 쳐서 3단 구조(서론-본론-결론)</b>를 눈에 띄게 할 것</li>
            <li>⚡ <b>피니시 조건:</b> """ + data['q2_bullet'][1] + """</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🏎️ [레이싱 스태프 가이드] 글쓰기 엔진 멈춤 현상 해결법 (클릭)", expanded=False):
        st.markdown(f"{data['hints']['q2_intro']}\n")
        st.markdown(f"{data['hints']['q2_body']}\n")
        st.markdown(f"{data['hints']['q2_conclusion']}")
        st.info("💡 위의 1, 2, 3단계 가이드의 질문에 답하는 문장들을 조립해서 아래 패널에 쏴버려!")

    q2_text = st.text_area("전술 답안 입력 패널", key=f"{topic_key}_q2", height=250, placeholder="가이드를 보면서 기어 올리고 작성 시작!")
    
    # 4. 채점 및 피드백 출력
    if st.button("🏁 전술 분석 및 채점 요청", key=f"{topic_key}_btn", type="primary"):
        st.markdown("### 📊 미션 결과 스코어 보드")
        
        p1, ext_m1, fb1 = evaluate_q1(m1, r1)
        p2, ext_m2, fb2 = evaluate_q1(m2, r2)
        
        with st.expander("🔍 [분석] 무기 장착 적합도 판정", expanded=True):
            st.code(fb1)
            st.code(fb2)
            
        with st.expander("🔍 [분석] 레이싱 트랙 주행 판정", expanded=True):
            if not q2_text.strip():
                st.error("차량이 출발하지 않았어! (답안이 비어있음) 한 줄이라도 적고 엑셀을 밟아봐!")
            else:
                feedbacks = evaluate_q2(q2_text, ext_m1, ext_m2, topic_key)
                for fb in feedbacks:
                    if "🔥" in fb:
                        st.success(fb)
                    else:
                        st.warning(fb)

# 탭 작동
with tab1:
    render_study_page('스마트폰')
with tab2:
    render_study_page('인공지능')
with tab3:
    render_study_page('재활용')
