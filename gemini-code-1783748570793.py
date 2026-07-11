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

# --- [2. 테마별 텍스트 및 디자인 데이터 백업] ---
THEME_DATA = {
    '남학생': {
        'page_title': "🦖🏎️ 국어 서논술형 크래시 배틀 룸",
        'page_sub': "조건을 격파하고 실시간으로 미션 통과 등급을 획득하라! 막힐 땐 [🛠️ 정비소 가이드]를 열어봐.",
        'tabs': ["🦖 세트 1 (티라노 스마트폰)", "🏎️ 세트 2 (AI 슈퍼카)", "🌋 세트 3 (볼케이노 분리배출)"],
        'topics': {
            '스마트폰': {
                'title': "🏎️ 슈퍼카만큼 빠른 기술 — 스마트폰 제재소",
                'text': "🦖 [공룡 부대의 일기] 오늘 랩터 부대원들과 훈련을 마치고 막사에 돌아왔는데, 대장 티라노께서 옛날 구식 무전기를 쓰고 계셨다. 내가 쓰던 최신 스마트폰으로 전술 유튜브 영상을 보여드리고 영상통화를 걸어드리니 앞발을 탁 치며 놀라셨다! 매일 쓰는 스마트폰이 과거의 무전기와 정확히 뭐가 다르고, 어떤 미친 기능들이 숨어있는지 대장님께 설명해 드리는 보고서를 작성해보자.",
                'q1_title': "⚔️ [미션 1] 설명 전술 무기 고르기",
                'q1_guide_title': "🛠️ [무기 정비소] 어떤 무기를 장착해야 할지 고민된다면?",
                'q1_hints': ["🦖 어이 부대원! 스마트폰을 설명할 때 어떤 기술을 쓸까?", "👉 피처폰이나 무전기랑 스펙을 비교하는 '대조'를 쓸까? 아니면 기능별로 엔진을 쪼개서 보여주는 '분류'를 쓸까?"],
                'q1_box1': "**[주무기 1번]**", 'q1_box2': "**[보조무기 2번]**",
                'q2_title': "✍️ [미션 2] 3단 전술 글로 격파하기",
                'cond_box': """
                    <div style="background-color: #262730; padding: 15px; border-radius: 8px; border-left: 6px solid #FF4B4B; color: #FFFFFF; margin-bottom: 15px;">
                        <strong style="font-size: 16px; color: #FF4B4B;">🚨 [감점 방지] 미션 클리어 조건</strong><br>
                        <ul style="margin-top: 5px; margin-bottom: 0px; padding-left: 20px; color: #E0E0E0;">
                            <li>⚡ <b>방금 장착한 무기 2가지</b>의 핵심 표현 형식이 문장에 무조건 묻어나올 것</li>
                            <li>⚡ 중간에 <b>엔터(줄바꿈)를 쾅! 쳐서 3단 구조(서론-본론-결론)</b>를 눈에 띄게 할 것</li>
                            <li>⚡ <b>피니시 조건:</b> 스마트폰이 바꿀 미래 세상이나 편리함에 대한 기대감을 폭발시킬 것</li>
                        </ul>
                    </div>""",
                'q2_guide_title': "🏎️ [레이싱 스태프 가이드] 글쓰기 엔진 멈춤 현상 해결법",
                'q2_hints': ["🛠️ [1단계 엔진 시동: 서론]\n- '우리가 매일 손에 쥐고 사는 스마트폰의 무서운 비밀을 알고 있나?'처럼 강렬하게 시작해봐!", "🛠️ [2단계 풀 악셀: 본론]\n- 1. 옛날 폰과 지금 스마트폰은 뭐가 다르지? ('~와 달리' 사용)\n- 2. 스마트폰 안에는 어떤 대단한 기능들이 있지? ('예를 들어' 사용)", "🛠️ [3단계 피니시 라인: 결론]\n- 스마트폰 기술이 앞으로 얼마나 더 엄청나게 발전할지 기대감을 한 문장으로 멋지게 마무리해봐!"],
                'q2_placeholder': "가이드를 보면서 기어 올리고 작성 시작!",
                'btn_text': "🏁 전술 분석 및 채점 요청",
                'q2_label': "전술 답안 입력 패널"
            },
            '인공지능': {
                'title': "🦖 티라노의 두뇌를 가진 컴퓨터 — 인공지능(AI) 연구소",
                'text': "🏎️ [레이싱 뉴스] 체스 챔피언을 꺾은 알파고를 넘어, 이제는 스스로 레이싱 트랙의 최적 경로를 계산하는 '인공지능(AI) 내비게이션'이 등장했습니다! 하지만 많은 사람이 AI를 단순한 자동 세차 기계 정도로 얕보곤 합니다. 이 강력한 디지털 공룡의 진짜 정체와 우리 일상 속 활약상을 친구들에게 확실하게 각인시켜 줍시다.",
                'q1_title': "⚔️ [미션 1] 설명 전술 무기 고르기",
                'q1_guide_title': "🛠️ [무기 정비소] 어떤 무기를 장착해야 할지 고민된다면?",
                'q1_hints': ["🦖 크아앙! 인공지능은 눈에 보이지 않는 초강력 두뇌야.", "👉 뜻풀이를 해주는 '정의'를 박아주거나, 게임/자율주행 같은 '실제 소름 돋는 사례(예시)'를 보여주면 어떨까?"],
                'q1_box1': "**[주무기 1번]**", 'q1_box2': "**[보조무기 2번]**",
                'q2_title': "✍️ [미션 2] 3단 전술 글로 격파하기",
                'cond_box': """
                    <div style="background-color: #262730; padding: 15px; border-radius: 8px; border-left: 6px solid #FF4B4B; color: #FFFFFF; margin-bottom: 15px;">
                        <strong style="font-size: 16px; color: #FF4B4B;">🚨 [감점 방지] 미션 클리어 조건</strong><br>
                        <ul style="margin-top: 5px; margin-bottom: 0px; padding-left: 20px; color: #E0E0E0;">
                            <li>⚡ <b>방금 장착한 무기 2가지</b>의 핵심 표현 형식이 문장에 무조건 묻어나올 것</li>
                            <li>⚡ 중간에 <b>엔터(줄바꿈)를 쾅! 쳐서 3단 구조</b>를 눈에 띄게 할 것</li>
                            <li>⚡ <b>피니시 조건:</b> 인공지능과 공존하는 인간의 올바른 태도나 이해의 필요성을 적을 것</li>
                        </ul>
                    </div>""",
                'q2_guide_title': "🏎️ [레이싱 스태프 가이드] 글쓰기 엔진 멈춤 현상 해결법",
                'q2_hints': ["🛠️ [1단계 레이더 가동: 서론]\n- 요즘 롤(LoL) 핵이나 알파고처럼 핫한 '인공지능' 이야기를 툭 던지면서 시작해봐!", "🛠️ [2단계 터보 부스터: 본론]\n- 1. 인공지능의 진짜 과학적 정의가 뭐지? ('~이란 ~을 뜻한다' 사용)\n- 2. 우리 일상 속에서 AI가 활약하는 진짜 예시는? ('예를 들면' 사용)", "🛠️ [3단계 깃발 체커: 결론]\n- 이 강력한 AI 기술과 함께 살아갈 우리 인간 레이서들은 앞으로 어떤 멋진 태도를 가져야 할지 다짐하자!"],
                'q2_placeholder': "가이드를 보면서 기어 올리고 작성 시작!",
                'btn_text': "🏁 전술 분석 및 채점 요청",
                'q2_label': "전술 답안 입력 패널"
            },
            '재활용': {
                'title': "🌋 지구 환경을 지키는 변신 로봇 — 분리배출 정비소",
                'text': "🦖 [화산지대 미션] 지구 온난화로 공룡들이 살던 화산이 폭발하기 직전입니다! 환경을 지키기 위해 분리배출을 하지만, 재활용 로봇이 먹지 못하고 고장 난다는 사실을 모르는 대원들이 많습니다. 완벽하게 변신하여 재태어날 쓰레기들의 계급과 정비 법칙을 깔끔하게 정리해 줍시다.",
                'q1_title': "⚔️ [미션 1] 설명 전술 무기 고르기",
                'q1_guide_title': "🛠️ [무기 정비소] 어떤 무기를 장착해야 할지 고민된다면?",
                'q1_hints': ["🏎️ 쓰레기 분리배출은 지구 방위대의 핵심 작전이야!", "👉 수많은 쓰레기 부품들을 재질에 따라 착착 '나누어 줄 세우는 방법(분류)'이나 '차이점(대조)'을 부각해보자."],
                'q1_box1': "**[주무기 1번]**", 'q1_box2': "**[보조무기 2번]**",
                'q2_title': "✍️ [미션 2] 3단 전술 글로 격파하기",
                'cond_box': """
                    <div style="background-color: #262730; padding: 15px; border-radius: 8px; border-left: 6px solid #FF4B4B; color: #FFFFFF; margin-bottom: 15px;">
                        <strong style="font-size: 16px; color: #FF4B4B;">🚨 [감점 방지] 미션 클리어 조건</strong><br>
                        <ul style="margin-top: 5px; margin-bottom: 0px; padding-left: 20px; color: #E0E0E0;">
                            <li>⚡ <b>방금 장착한 무기 2가지</b>의 핵심 표현 형식이 문장에 무조건 묻어나올 것</li>
                            <li>⚡ 중간에 <b>엔터(줄바꿈)를 쾅! 쳐서 3단 구조</b>를 눈에 띄게 할 것</li>
                            <li>⚡ <b>피니시 조건:</b> 지구와 환경을 위한 일상 속 실천의 의지가 명확히 드러나도록 할 것</li>
                        </ul>
                    </div>""",
                'q2_guide_title': "🏎️ [레이싱 스태프 가이드] 글쓰기 엔진 멈춤 현상 해결법",
                'q2_hints': ["🛠️ [1단계 사이렌 발령: 서론]\n- 매일 쏟아지는 쓰레기 더미 때문에 지구가 아파한다는 경고를 날리며 웅장하게 시작해봐!", "🛠️ [2단계 부품 분해: 본론]\n- 1. 쓰레기 부품들은 재질에 따라 어떻게 대분류할 수 있지? ('종류는 크게 ~로 나뉜다' 사용)\n- 2. 겉은 비슷해도 재활용 대장과 일반 쓰레기 졸개의 차이는 뭐지? ('~와 달리 종량제에' 사용)", "🛠️ [3단계 지구 수호 성공: 결론]\n- 나부터 올바른 분리배출 작전을 성공시키겠다는 단단한 실천 의지와 다짐을 담아 끝내자!"],
                'q2_placeholder': "가이드를 보면서 기어 올리고 작성 시작!",
                'btn_text': "🏁 전술 분석 및 채점 요청",
                'q2_label': "전술 답안 입력 패널"
            }
        },
        'fb_pass_q1': "🔥 [임무 완료] 대박! 특성을 정확히 꿰뚫고 완벽한 이유를 적었어.",
        'fb_fail_q1': "⚠️ [엔진 과열] 장착한 무기와 설명 내용이 매칭되지 않아! 다시 튜닝해볼까?",
        'fb_pass_struct': "🔥 [임무 완료] 서론-본론-결론의 3단 전술 배치가 아주 깔끔하다!",
        'fb_fail_struct': "⚙️ [전술 수정] 글이 통째로 뭉쳐있어! 단락을 딱딱 나눠줘야 가독성 부스터가 켜져.",
        'fb_pass_marker': "🔥 [임무 완료] 선택한 핵심 기술 파워가 본문 문장에 제대로 박혔어!",
        'fb_fail_marker': "⚙️ [전술 수정] 본문에 핵심 표현이 안 보여! 시그니처 단어를 치트키처럼 써봐.",
        'fb_pass_concl': "🔥 [임무 완료] 미션 요구사항인 '결론의 방향성'까지 멋지게 완파했다!",
        'fb_fail_concl': "⚙️ [전술 수정] 피니시 라인 부실! 조건이 요구한 핵심 마무리를 한 문장만 묵직하게 더 던져봐!",
        'empty_msg': "차량이 출발하지 않았어! (답안이 비어있음) 한 줄이라도 적고 엑셀을 밟아봐!"
    },
    '여학생': {
        'page_title': "🎀 다이어리 감성 문학 카페",
        'page_sub': "예쁜 다이어리를 한 칸씩 채우듯 미션을 완료해 보아요! 막막할 땐 [🧸 테디베어 가이드] 팝업을 열어주세요.",
        'tabs': ["🍓 세트 1 (딸기 수플레 스마트폰)", "🧸 세트 2 (테디베어 AI 친구)", "🌱 세트 3 (허브티 분리배출)"],
        'topics': {
            '스마트폰': {
                'title': "🍓 달콤하고 편리한 세상 — 우리들의 스마트폰 스토리",
                'text': "[소녀의 다이어리] 오늘 할머니 댁에 놀러 갔는데, 할머니께서 아직도 옛날 폴더폰을 소중히 쓰고 계셨어요. 내가 쓰던 예쁜 스마트폰으로 아기자기한 브이로그 영상도 보여드리고 화질 좋은 영상통화도 걸어드리니 눈이 토끼처럼 커지셨답니다! 매일 쓰는 스마트폰이 과거의 전화기와 어떻게 다른지, 어떤 유용한 기능이 있는지 예쁘게 정리해서 할머니 지침서를 만들어 드리고 싶어요.",
                'q1_title': "💖 [스텝 1] 마음에 드는 설명 방법 꾸미기",
                'q1_guide_title': "🧸 [다꾸 가이드] 설명 방법을 고르기 막막한가요?",
                'q1_hints': ["🤔 스마트폰이라는 멋진 선물을 할머니께 어떻게 소개해 드릴까요?", "👉 과거 폴더폰과의 차이점을 속닥속닥 보여주는 '대조'를 쓸까요? 아니면 숨겨진 예쁜 기능들을 묶어서 보여주는 '분류'가 좋을까요?"],
                'q1_box1': "**[첫 번째 감성 방법]**", 'q1_box2': "**[두 번째 감성 방법]**",
                'q2_title': "✍️ [스텝 2] 다이어리에 한 편의 글 녹여내기",
                'cond_box': """
                    <div style="background-color: #FFF0F0; padding: 15px; border-radius: 8px; border-left: 6px solid #FFB7B2; color: #4A4A4A; margin-bottom: 15px;">
                        <strong style="font-size: 16px; color: #FF9AA2;">🌸 [체크리스트] 감점 방지 약속</strong><br>
                        <ul style="margin-top: 5px; margin-bottom: 0px; padding-left: 20px; color: #555555;">
                            <li>✨ <b>내가 고른 예쁜 설명 방법 2가지</b>의 예쁜 표지 단어가 문장에 꼭 들어가야 해요.</li>
                            <li>✨ 글을 쓰다가 <b>엔터(줄바꿈)를 사뿐히 눌러 서론, 본론, 결론</b>의 단락을 나누어 보아요.</li>
                            <li>✨ <b>마무리 약속:</b> 스마트폰 덕분에 우리 일상이 얼마나 더 따뜻하고 편리해질지, 미래의 기대감을 담아주세요.</li>
                        </ul>
                    </div>""",
                'q2_guide_title': "🧸 [스태프 비밀 노트] 글쓰기가 스르륵 풀리는 마법",
                'q2_hints': ["🌱 [서론 마중물 물음]\n- '우리의 일상을 핑크빛 편리함으로 채워주는 스마트폰, 그 속에 숨겨진 이야기를 아시나요?'처럼 다정하게 시작해봐요.", "🌱 [본론 채우기 대화]\n- 1. 할머니의 옛날 폰과 내 스마트폰은 어떤 점이 다를까요? ('~와 달리' 사용하기)\n- 2. 스마트폰에는 어떤 신기한 아이콘 기능들이 있나요? ('예를 들어' 사용하기)", "🌱 [결론 마무리 일기]\n- 스마트폰이 앞으로 우리 삶을 얼마나 더 행복하고 편리하게 바꿔줄지, 설레는 기대감을 담아 마무리 문장을 완성해요!"],
                'q2_placeholder': "소중한 생각을 차근차근 적어보세요...",
                'btn_text': "✨ 다이어리 검토 및 채점 받기",
                'q2_label': "나만의 소중한 답안 노트"
            },
            '인공지능': {
                'title': "🧸 내 마음을 읽는 똑똑한 친구 — 인공지능(AI) 라이프",
                'text': "[감성 뉴스] 사람처럼 예쁜 그림을 그리고, 따뜻한 위로의 글을 써주는 감성 인공지능(AI)이 우리 곁에 찾아왔습니다. 하지만 많은 사람이 인공지능을 그저 딱딱하고 차가운 기계로만 오해하곤 해요. 이 친근하고 스마트한 디지털 친구의 진짜 의미와 일상 속 다정한 활약상을 친구들에게 친절하게 가르쳐 줄래요?",
                'q1_title': "💖 [스텝 1] 마음에 드는 설명 방법 꾸미기",
                'q1_guide_title': "🧸 [다꾸 가이드] 설명 방법을 고르기 막막한가요?",
                'q1_hints': ["🤔 인공지능이라는 보이지 않는 다정한 마인드를 어떻게 표현할까요?", "👉 오해하는 친구들을 위해 '인공지능의 진짜 뜻(정의)'을 차분히 읊어주거나, 일상 속 '귀여운 사례(예시)'를 보여주면 참 좋겠죠?"],
                'q1_box1': "**[첫 번째 감성 방법]**", 'q1_box2': "**[두 번째 감성 방법]**",
                'q2_title': "✍️ [스텝 2] 다이어리에 한 편의 글 녹여내기",
                'cond_box': """
                    <div style="background-color: #FFF0F0; padding: 15px; border-radius: 8px; border-left: 6px solid #FFB7B2; color: #4A4A4A; margin-bottom: 15px;">
                        <strong style="font-size: 16px; color: #FF9AA2;">🌸 [체크리스트] 감점 방지 약속</strong><br>
                        <ul style="margin-top: 5px; margin-bottom: 0px; padding-left: 20px; color: #555555;">
                            <li>✨ <b>내가 고른 예쁜 설명 방법 2가지</b>의 표지 단어가 문장에 꼭 들어가야 해요.</li>
                            <li>✨ 글을 쓰다가 <b>엔터(줄바꿈)를 사뿐히 눌러</b> 단락을 나누어 보아요.</li>
                            <li>✨ <b>마무리 약속:</b> 인공지능과 함께 살아갈 우리들의 올바른 마음가짐이나 이해의 마음을 적어주세요.</li>
                        </ul>
                    </div>""",
                'q2_guide_title': "🧸 [스태프 비밀 노트] 글쓰기가 스르륵 풀리는 마법",
                'q2_hints': ["🌱 [서론 마중물 물음]\n- 요즘 우리 생활 깊숙이 다가온 '인공지능 친구' 이야기를 따뜻하게 건네며 시작해 볼까요?", "🌱 [본론 채우기 대화]\n- 1. 인공지능이란 단어의 정확하고 예쁜 의미는 무엇일까요? ('~이란 ~을 뜻한다' 사용하기)\n- 2. 우리 일상에서 AI가 돕고 있는 소소한 예는 무엇이 있죠? ('예를 들면 ~이 있다' 사용하기)", "🌱 [결론 마무리 일기]\n- 이 똑똑한 AI 친구와 함께 공존하며 살아갈 우리들의 아름다운 태도를 다짐하며 마무리해요!"],
                'q2_placeholder': "소중한 생각을 차근차근 적어보세요...",
                'btn_text': "✨ 다이어리 검토 및 채점 받기",
                'q2_label': "나만의 소중한 답안 노트"
            },
            '재활용': {
                'title': "🌱 푸른 지구를 만드는 소소한 약속 — 분리배출 다이어리",
                'text': "[초록빛 일기] 아름다운 지구를 위해 매일 분리배출을 정성껏 실천하고 있어요. 하지만 겉보기엔 비슷해 보여도 떡볶이 국물이 물든 컵라면 용기는 아쉽게도 재활용 예쁜이로 변신하지 못하고 일반 쓰레기로 가야 한대요. 우리 소중한 지구를 아프지 않게 지켜줄 올바른 쓰레기들의 분리 법칙 꿀팁 가이드를 정성스레 채워보아요.",
                'q1_title': "💖 [스텝 1] 마음에 드는 설명 방법 꾸미기",
                'q1_guide_title': "🧸 [다꾸 가이드] 설명 방법을 고르기 막막한가요?",
                'q1_hints': ["🤔 우리가 실천할 소중한 약속들을 어떻게 독자에게 전할까요?", "👉 다양한 쓰레기들을 재질별로 예쁘게 '바구니에 담아 나누는 방법(분류)'이나 '헷갈리는 차이점(대조)'을 다정하게 가르쳐 줄까요?"],
                'q1_box1': "**[첫 번째 감성 방법]**", 'q1_box2': "**[두 번째 감성 방법]**",
                'q2_title': "✍️ [스텝 2] 다이어리에 한 편의 글 녹여내기",
                'cond_box': """
                    <div style="background-color: #FFF0F0; padding: 15px; border-radius: 8px; border-left: 6px solid #FFB7B2; color: #4A4A4A; margin-bottom: 15px;">
                        <strong style="font-size: 16px; color: #FF9AA2;">🌸 [체크리스트] 감점 방지 약속</strong><br>
                        <ul style="margin-top: 5px; margin-bottom: 0px; padding-left: 20px; color: #555555;">
                            <li>✨ <b>내가 고른 예쁜 설명 방법 2가지</b>의 표지 단어가 문장에 꼭 들어가야 해요.</li>
                            <li>✨ 글을 쓰다가 <b>엔터(줄바꿈)를 사뿐히 눌러</b> 단락을 나누어 보아요.</li>
                            <li>✨ <b>마무리 약속:</b> 푸른 지구와 환경을 지키기 위한 나의 소중한 실천 의지가 고스란히 담기게 해주세요.</li>
                        </ul>
                    </div>""",
                'q2_guide_title': "🧸 [스태프 비밀 노트] 글쓰기가 스르륵 풀리는 마법",
                'q2_hints': ["🌱 [서론 마중물 물음]\n- 매일 조금씩 아파하는 지구를 위해 우리가 할 수 있는 작은 기적, 분리배출 이야기로 시작해봐요.", "🌱 [본론 채우기 대화]\n- 1. 우리가 모은 재활용 아이들은 재질에 따라 어떻게 나누어 담기나요? ('종류는 크게 ~로 나뉜다' 사용하기)\n- 2. 겉은 비슷해도 재활용이 되는 착한 아이와 안 되는 아이의 차이는 뭐죠? ('~와 달리 종량제에' 사용하기)", "🌱 [결론 마무리 일기]\n- 나부터 시작하는 작은 초록빛 실천이 세상을 바꿀 수 있도록, 단단한 환경 다짐 문장으로 마쳐보아요!"],
                'q2_placeholder': "소중한 생각을 차근차근 적어보세요...",
                'btn_text': "✨ 다이어리 검토 및 채점 받기",
                'q2_label': "나만의 소중한 답안 노트"
            }
        },
        'fb_pass_q1': "✨ [솜씨 발휘 성공!] 와아! 설명 방법의 쓰임새와 뜻을 예쁘게 매칭하여 정답을 완성했어요.",
        'fb_fail_q1': "🌱 [다이어리 수정 중...] 골라준 방법과 적어준 이유가 살짝 어긋난 것 같아요. 가이드 노트를 다시 읽어볼까요?",
        'fb_pass_struct': "✨ [솜씨 발휘 성공!] 서론-본론-결론의 삼단 단락 구분이 무척이나 가지런하고 예쁩니다.",
        'fb_fail_struct': "📝 [노트 수정 중...] 글이 한 덩어리로 뭉쳐 있어요! 서론 쓰고 사뿐히 엔터! 단락을 예쁘게 갈라보아요.",
        'fb_pass_marker': "✨ [솜씨 발휘 성공!] 선택했던 설명 방법의 예쁜 힌트 표현들이 문장 안에 쏙쏙 잘 들어갔습니다.",
        'fb_fail_marker': "📝 [노트 수정 중...] 본문에서 선택한 방법의 느낌이 잘 나지 않아요! 치트키 단어들을 문장 사이에 예쁘게 심어보아요.",
        'fb_pass_concl': "✨ [솜씨 발휘 성공!] 약속했던 맺음말의 다정한 생각과 방향성이 결론에 가득 차 있네요. 최고예요!",
        'fb_fail_concl': "📝 [노트 수정 중...] 마지막 엔딩 문장이 아쉬워요! 조건이 속닥속닥 부탁한 소중한 생각(미래 기대/나의 의지)을 한 줄만 덧붙여봐요.",
        'empty_msg': "아직 일기장에 아무 글도 적히지 않았어요! (답안이 비어있음) 다정한 마음을 담아 한 줄이라도 써보아요!"
    }
}

# --- [3. 채점 백엔드 범용 함수] ---
def normalize_method(input_text):
    for standard_method, synonyms in METHOD_SYNONYMS.items():
        if any(syn in input_text for syn in synonyms):
            return standard_method
    return None

def evaluate_q1(method_input, reason_input, active_theme):
    t_cfg = THEME_DATA[active_theme]
    method = normalize_method(method_input)
    if not method:
        return False, None, "⚙️" if active_theme == '남학생' else "📝" + " 아직 설명 방법을 적지 않았거나 오타가 난 것 같아요!"
    if any(kw in reason_input for kw in VALID_REASONS[method]):
        return True, method, t_cfg['fb_pass_q1']
    else:
        return False, method, t_cfg['fb_fail_q1']

def evaluate_q2(text, method1, method2, topic_key, active_theme):
    t_cfg = THEME_DATA[active_theme]
    feedback = []
    paragraphs = [p for p in text.split('\n') if len(p.strip()) > 0]
    
    if len(paragraphs) >= 3:
        feedback.append(t_cfg['fb_pass_struct'])
    else:
        feedback.append(t_cfg['fb_fail_struct'])
        
    for m in [method1, method2]:
        if m and any(marker in text for marker in TEXT_MARKERS[m]):
            feedback.append(t_cfg['fb_pass_marker'].replace('{m}', m))
        elif m:
            feedback.append(t_cfg['fb_fail_marker'].replace('{m}', m))
            
    conclusion_text = paragraphs[-1] if paragraphs else text
    if any(kw in conclusion_text for kw in CONCLUSION_KEYWORDS[topic_key]):
        feedback.append(t_cfg['fb_pass_concl'])
    else:
        feedback.append(t_cfg['fb_fail_concl'])
        
    return feedback

# --- [4. Streamlit UI 메인 웹앱 설계] ---
# 학생의 선택에 따라 테마를 스위칭할 수 있도록 상단 라디오 버튼 배치
st.set_page_config(page_title="국어과 맞춤형 서논술형 워크북", layout="centered")

# 🔥 핵심 터치: 테마 스위칭 버튼 탑재
user_theme = st.radio(
    "🎨 나의 맞춤 공부방 스타일을 골라보세요!",
    ["♂️ 남학생 전용 트랙 (공룡 & 레이싱카)", "♀️ 여학생 감성 카페 (다꾸 & 파스텔)"],
    horizontal=True
)

# 내부 변수용 키 세팅
active_theme = '남학생' if "남학생" in user_theme else '여학생'
cfg = THEME_DATA[active_theme]

# 타이틀 및 인트로 변경
st.title(cfg['page_title'])
st.write(cfg['page_sub'])

# 탭 메뉴 구성
tab1, tab2, tab3 = st.tabs(cfg['tabs'])

def render_study_page(topic_key):
    data = cfg['topics'][topic_key]
    
    st.header(data['title'])
    st.info(data['text'])
    st.markdown("---")
    
    # 문항 1 영역
    st.subheader(data['q1_title'])
    
    with st.expander(f"{data['q1_guide_title']} (클릭하여 힌트 열기)", expanded=False):
        for hint in data['hints']['q1']:
            st.write(hint)
            
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(data['q1_box1'])
        m1 = st.text_input("설명 방법 이름", key=f"{active_theme}_{topic_key}_m1", placeholder="정의 / 대조 / 예시 / 분류 중 선택")
        r1 = st.text_area("선택한 이유 서술하기", key=f"{active_theme}_{topic_key}_r1", placeholder="나만의 논리로 적어보아요.", height=80)
    with col2:
        st.markdown(data['q1_box2'])
        m2 = st.text_input("설명 방법 이름 ", key=f"{active_theme}_{topic_key}_m2", placeholder="정의 / 대조 / 예시 / 분류 중 선택")
        r2 = st.text_area("선택한 이유 서술하기 ", key=f"{active_theme}_{topic_key}_r2", placeholder="나만의 논리로 적어보아요.", height=80)
        
    st.markdown("---")
    
    # 문항 2 영역
    st.subheader(data['q2_title'])
    
    # 커스텀 테마 조건 박스 삽입
    st.markdown(data['cond_box'], unsafe_allow_html=True)
    
    with st.expander(f"{data['q2_guide_title']} (클릭하여 힌트 열기)", expanded=False):
        for hint in data['hints']['q2_hints']:
            st.markdown(hint)
        st.caption("💡 위 가이드 박스의 질문들에 하나씩 답변을 다는 기분으로 글을 합치면 아주 완벽해요!")

    q2_text = st.text_area(data['q2_label'], key=f"{active_theme}_{topic_key}_q2", height=250, placeholder=data['q2_placeholder'])
    
    # 채점 및 피드백 핸들러
    if st.button(data['btn_text'], key=f"{active_theme}_{topic_key}_btn", type="primary"):
        st.markdown("### 📊 실시간 피드백 검토 결과")
        
        p1, ext_m1, fb1 = evaluate_q1(m1, r1, active_theme)
        p2, ext_m2, fb2 = evaluate_q1(m2, r2, active_theme)
        
        with st.expander("🔍 문항 1 생각 조건 분석", expanded=True):
            if active_theme == '남학생':
                st.code(fb1)
                st.code(fb2)
            else:
                st.info(fb1)
                st.info(fb2)
            
        with st.expander("🔍 문항 2 조건 완수 여부 분석", expanded=True):
            if not q2_text.strip():
                st.error(cfg['empty_msg']) if active_theme == '남학생' else st.warning(cfg['empty_msg'])
            else:
                feedbacks = evaluate_q2(q2_text, ext_m1, ext_m2, topic_key, active_theme)
                for fb in feedbacks:
                    if "🔥" in fb or "✨" in fb:
                        st.success(fb)
                    else:
                        st.warning(fb)

# 탭 작동 유도
with tab1:
    render_study_page('스마트폰')
with tab2:
    render_study_page('인공지능')
with tab3:
    render_study_page('재활용')
