<div align="center">

# 🌟 지혜나눔터 (Jihye Nanumteo)
### 70년의 지혜가 빛나는 순간, 세대를 이어가는 배움의 장  
**어르신이 선생님이 되는 세대교류 플랫폼 (MVP)**

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<a href="#-프로젝트-한눈에-보기">한눈에 보기</a> •
<a href="#-핵심-기능-mvp">핵심 기능</a> •
<a href="#-아키텍처--데이터-모델">아키텍처</a> •
<a href="#-로컬-실행">로컬 실행</a> •
<a href="#-공모전-참여-및-회고">공모전/회고</a>

</div>

---

## 🔎 프로젝트 한눈에 보기

> "이거 아는 사람이 나밖에 없어. 내가 가면 이 맛도 사라지는 거지."  
> — 안동 하회마을 할머니의 안동식혜 레시피를 전수하며

**지혜나눔터**는 고령자를 ‘수혜자’가 아니라 **‘선생님(멘토)’**으로 전환해  
대학생에게 전통 지식/기술을 전수하는 **세대교류 프로그램 플랫폼**의 MVP입니다.

### 해결하려는 문제
- **고령자**: 사회적 역할 상실, 경제적 어려움, 고립감
- **청년**: 지역 전통 지식 단절, 피상적인 교류
- **지역사회**: 무형문화유산/생활기술의 소멸 위험

### 솔루션(요약)
| 대상 | 역할 | 가치 |
|---|---|---|
| 어르신 멘토 | 경험/지혜 전수 | 사회적 역할 회복 + 활동비(운영 정책에 따라) |
| 대학생 멘티 | 프로그램 수강 | 실질 기술 습득 + 세대 이해 |
| 지역사회 | 지식 보존 | 지속 가능한 전통 지식 아카이브 |

---

## ✨ 핵심 기능 (MVP)

- **프로그램 목록/상세 조회**
- **프로그램 신청(Enrollment)**
- **멘토 목록/상세 조회**
- **멘토 등록(폼 기반)**
- **관리자 대시보드(승인/수료 처리)**
- **시연용 더미 데이터 자동 시드(Seed)**

> ⚠️ MVP 특성상 인증/권한(로그인)은 포함하지 않았습니다. `/admin`은 데모용입니다.

---

## 🧩 아키텍처 & 데이터 모델

### 기술 구성
- **FastAPI**: API/SSR 라우팅
- **Jinja2**: 서버사이드 템플릿 렌더링
- **SQLAlchemy + SQLite**: 관계형 데이터 모델링/저장

### 엔티티 관계(ER 개요)
- `Mentor (1) ── (N) Program`
- `Student (1) ── (N) Enrollment`
- `Program (1) ── (N) Enrollment`

---

## 🚀 로컬 실행

### 준비물
- Python **3.11+**
- Git

### 설치 & 실행
```bash
# 1) 클론
git clone https://github.com/Lova-clover/Jihye-Nanumteo.git
cd Jihye-Nanumteo

# 2) 가상환경
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# 3) 의존성 설치
python -m pip install -r mvp/requirements.txt

# 4) 실행 (중요: 템플릿 경로 때문에 mvp 폴더에서 실행 권장)
cd mvp
python main.py
````

브라우저에서 접속: [http://localhost:8000](http://localhost:8000)

### 주요 라우트

* `/` : 홈
* `/programs` : 프로그램 목록
* `/programs/{id}` : 프로그램 상세
* `/mentors` : 멘토 목록
* `/mentors/register` : 멘토 등록
* `/admin` : 관리자 대시보드(데모)

---

## 📁 폴더 구조

> 아래 구조는 “공개 레포 기준”입니다.
> 실행 시 SQLite DB 파일은 로컬에서 자동 생성될 수 있습니다.

```text
Jihye-Nanumteo/
├── mvp/
│   ├── main.py
│   ├── requirements.txt
│   └── templates/
├── LICENSE
├── .gitignore
└── README.md
```

---

## 🏆 공모전 참여 및 회고

### G-AFC 고령친화 아이디어 공모전 (2026)

* **출품 부문**: 고령자 대상 프로그램·서비스 아이디어
* **제출일**: 2026-01-25
* **주최**: 국립경국대학교 G-AFC 센터
* **결과**: **미선정**

### 회고(핵심만)

**왜 미선정이었을 가능성이 큰가**

* 정량 KPI(참여율/재참여율/성과지표) 설계가 부족했다
* 운영 관점(예산·인력·리스크·지속가능성) 설득력이 더 필요했다
* 확장(지역 확산 모델)에서 “수치 기반” 근거가 부족했다

**그럼에도 남은 성과(기술적으로)**

* FastAPI + SQLAlchemy 기반 관계형 모델 설계
* 멘토/프로그램/신청/관리자 플로우를 실제 동작 MVP로 구현
* 제출물로 끝내지 않고 “실행 가능한 프로토타입”까지 완성

---


## 👨‍💻 팀

* 팀: **실버브릿지 (SilverBridge)**
* 대표: 한성주

---

## 📄 라이선스

MIT License — 자세한 내용은 [LICENSE](LICENSE) 참고
