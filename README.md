<div align="center">

# 🌟 지혜나눔터(Jihye Nanumteo)

### 70년의 지혜가 빛나는 순간, 세대를 이어가는 배움의 장

**어르신이 선생님이 되는 세대교류 플랫폼**

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[🎯 프로젝트 소개](#-프로젝트-소개) • [✨ 핵심 가치](#-핵심-가치) • [🚀 시작하기](#-시작하기) • [📊 기술 스택](#-기술-스택) • [🏆 수상 내역](#-수상-내역)

</div>

---

## 📖 프로젝트 소개

> "이거 아는 사람이 나밖에 없어. 내가 가면 이 맛도 사라지는 거지."  
> — 안동 하회마을 할머니의 안동식혜 레시피를 전수하며

**지혜나눔터**는 고령자를 '수혜자'가 아닌 '선생님'으로 전환하는 혁신적인 세대교류 프로그램입니다.

### 🎯 해결하고자 하는 문제

- **고령자**: 사회적 역할 상실, 경제적 어려움, 고립감
- **청년 세대**: 전통 지식 단절, 피상적인 세대교류
- **지역사회**: 무형문화유산의 소멸 위기

### 💡 우리의 솔루션

| 구분 | 역할 | 혜택 |
|------|------|------|
| **어르신 멘토** | 70년 경험과 지혜 전수 | 활동비 지급 + 사회적 역할 회복 |
| **대학생 멘티** | 진심 어린 배움 | 실질적 기술 습득 + 세대 이해 |
| **지역사회** | 문화유산 보존 | 전통 지식의 지속 가능성 확보 |

---

## ✨ 핵심 가치

### 🔄 관점의 전환
```
어르신 = 돌봄 대상 ❌
어르신 = 지혜를 나누는 선생님 ✅
3. 🌱 텃밭 농사 체험
4. 📜 전통 공예 워크숍
```

### 🏛️ 안동·예천 특화 프로그램

<table>
<tr>
<td align="center">🍲<br><b>전통 음식</b><br>안동찜닭, 헛제사밥<br>간고등어, 안동식혜</td>
<td align="center">🎎<br><b>예절·다도</b><br>종갓집 예절<br>전통 다도</td>
<td align="center">🌱<br><b>텃밭 농사</b><br>제철 농사법<br>발효식품</td>
<td align="center">🎨<br><b>전통 공예</b><br>한지공예, 매듭<br>목공예</td>
</tr>
</table>

### 🎓 참여 방식 (자발적 참여)

- **대학생**: 수강 신청 형태로 프로그램 선택
- **어르신**: 활동비를 받으며 멘토로 참여
- **운영**: G-AFC 센터가 품질 관리 및 매칭

---

## 🚀 시작하기

### Prerequisites

- Python 3.11 이상
- Git

### Installation

```bash
# 1. 저장소 클론
git clone https://github.com/yourusername/jihye-nanumteo.git
cd jihye-nanumteo

# 2. 가상환경 생성 및 활성화
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate

# 3. 의존성 설치
pip install -r mvp/requirements.txt
```

### Running the Application

```bash
# MVP 서버 실행
cd mvp
python main.py
```

브라우저에서 [http://localhost:8000](http://localhost:8000) 접속

### 🎬 데모 영상

> 실제 작동하는 프로토타입을 약 50초 동안 시연한 영상입니다.

*(영상 링크 또는 GIF 추가 예정)*

---

## 📊 기술 스택

### Backend
- **FastAPI** 0.104.1 - 고성능 웹 프레임워크
- **SQLAlchemy** 2.0.23 - ORM
- **SQLite** - 경량 데이터베이스
- **Jinja2** - 템플릿 엔진

### Frontend
- **Tailwind CSS** - 유틸리티 기반 CSS
- **Vanilla JavaScript** - 경량화된 프론트엔드

### Design
- **Python-PPTX** - PPT 자동 생성
- **Python-DOCX** - 문서 자동 생성
- **Color Palette**: 
  - NAVY `#1A2A4E`
  - CORAL `#E5736A`
  - CREAM `#FAF7F2`
  - GOLD `#C69C52`

---

## 📁 프로젝트 구조

```
jihye-nanumteo/
├── mvp/                           # MVP 웹 애플리케이션
│   ├── main.py                   # FastAPI 메인 서버 (모델 포함)
│   ├── requirements.txt          # Python 의존성
│   ├── wisdom_sharing.db         # SQLite 데이터베이스
│   └── templates/                # HTML 템플릿
│       ├── home.html            # 메인 페이지
│       ├── programs/            # 프로그램 관련 페이지
│       ├── mentors/             # 멘토 관련 페이지
│       └── admin/               # 관리자 페이지
├── 제출한 것/                      # 공모전 제출 파일
│   ├── 최종_PPT.pptx             # 최종 PPT (10슬라이드)
│   ├── 최종_제안서.docx          # 최종 제안서 (A4 5매)
│   ├── 최종_PPT.pdf
│   ├── 최종_제안서.pdf
│   ├── 고령친화 아이디어_한성주(실버브릿지).pdf  # 병합된 최종 제출본
│   ├── 지혜나눔터_MVP_시연.mp4   # 데모 영상
│   └── G-AFC 고령친화 아이디어 공모전 신청서.*
├── .gitignore                    # Git 제외 파일 목록
├── LICENSE                       # MIT 라이선스
└── README.md                     # 프로젝트 문서
```

---

## 🎯 주요 기능

### 👥 사용자 유형
- **어르신 멘토**: 프로필 등록, 프로그램 개설, 수강생 관리
- **대학생 멘티**: 프로그램 검색, 신청, 수강 이력 관리
- **관리자**: 전체 프로그램 관리, 매칭 조율, 품질 관리

### ⚙️ 핵심 기능
- ✅ 프로그램 검색 및 필터링
- ✅ 실시간 신청 및 매칭
- ✅ 멘토-멘티 프로필 관리
- ✅ 관리자 대시보드
- ✅ 참여 이력 추적

---

## 🏆 수상 내역

### G-AFC 고령친화 아이디어 공모전 (2026)

- **출품 부문**: 고령자 대상 프로그램·서비스 아이디어
- **제출일**: 2026년 1월 25일
- **주최**: 국립경국대학교 G-AFC 센터

*(결과 발표 대기 중)*

---

## 📈 향후 계획

### Phase 1: MVP 고도화 (2026 Q1-Q2)
- [ ] 사용자 인증 시스템 추가
- [ ] 모바일 반응형 UI 개선
- [ ] 결제 시스템 통합 (활동비 지급)
- [ ] 실시간 알림 기능

### Phase 2: 파일럿 운영 (2026 Q3)
- [ ] 국립경국대학교에서 8주 파일럿 테스트
- [ ] 멘토 5명, 멘티 20명 모집
- [ ] 프로그램 4개 운영
- [ ] 만족도 조사 및 피드백 수집

### Phase 3: 지역 확장 (2026 Q4~)
- [ ] 안동·예천 지역 평생교육원 연계
- [ ] 다른 대학 및 지역사회센터 확장
- [ ] 온라인 강의 기능 추가
- [ ] 전통 지식 아카이브 구축

---

## 👨‍💻 팀 정보

**팀 실버브릿지** (Team SilverBridge)

- **대표**: 한성주
- **소속**: 연세대학교 미래캠퍼스
- **이메일**: woeg0226@naver.com

---

## 📄 라이선스

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 감사의 말

이 프로젝트는 G-AFC 고령친화 아이디어 공모전을 위해 제작되었으며,  
안동·예천 지역 어르신들의 소중한 지혜를 보존하고  
세대 간 진정한 교류를 만들어가고자 하는 마음으로 시작되었습니다.

---

<div align="center">

**Made with ❤️ by Team SilverBridge**

*70년의 지혜가 빛나는 순간, 세대를 이어가는 배움의 장*

</div>
