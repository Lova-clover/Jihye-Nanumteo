"""
지혜나눔터 MVP - 어르신이 선생님이 되는 세대교류 플랫폼
G-AFC 고령친화 아이디어 공모전 출품작
"""

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime, timedelta
import os

# 데이터베이스 설정
DATABASE_URL = "sqlite:///./wisdom_sharing.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Mentor(Base):
    """어르신 멘토"""
    __tablename__ = "mentors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    phone = Column(String(20))
    profile_image = Column(String(200), default="👨‍🏫")
    introduction = Column(Text)
    expertise = Column(String(200))
    experience_years = Column(Integer)
    available_days = Column(String(100))
    location = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    
    programs = relationship("Program", back_populates="mentor")


class Student(Base):
    """대학생 멘티"""
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    student_id = Column(String(20))
    department = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    interest = Column(String(200))
    created_at = Column(DateTime, default=datetime.now)
    
    enrollments = relationship("Enrollment", back_populates="student")


class Program(Base):
    """교육 프로그램"""
    __tablename__ = "programs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    category = Column(String(50))
    description = Column(Text)
    mentor_id = Column(Integer, ForeignKey("mentors.id"))
    location = Column(String(100))
    schedule = Column(String(100))
    max_students = Column(Integer, default=10)
    current_students = Column(Integer, default=0)
    credit_hours = Column(Float, default=1.0)
    status = Column(String(20), default="모집중")
    image_emoji = Column(String(10), default="📚")
    created_at = Column(DateTime, default=datetime.now)
    start_date = Column(DateTime)
    
    mentor = relationship("Mentor", back_populates="programs")
    enrollments = relationship("Enrollment", back_populates="program")


class Enrollment(Base):
    """수강 신청"""
    __tablename__ = "enrollments"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    program_id = Column(Integer, ForeignKey("programs.id"))
    status = Column(String(20), default="신청")
    enrolled_at = Column(DateTime, default=datetime.now)
    completed_at = Column(DateTime, nullable=True)
    review = Column(Text, nullable=True)
    rating = Column(Integer, nullable=True)
    
    student = relationship("Student", back_populates="enrollments")
    program = relationship("Program", back_populates="enrollments")


Base.metadata.create_all(bind=engine)

app = FastAPI(title="지혜나눔터", description="어르신이 선생님이 되는 세대교류 플랫폼")
templates = Jinja2Templates(directory="templates")


def seed_demo_data():
    """시연용 데이터"""
    db = SessionLocal()
    if db.query(Mentor).count() > 0:
        db.close()
        return
    
    mentors = [
        Mentor(name="김순자", age=72, phone="010-1234-5678", profile_image="👵",
               introduction="50년간 안동 하회마을에서 전통 음식을 만들어 왔습니다. 안동찜닭과 헛제사밥의 진짜 맛을 가르쳐 드릴게요.",
               expertise="전통음식", experience_years=50, available_days="화,목,토", location="안동시 풍천면"),
        Mentor(name="박영수", age=78, phone="010-2345-6789", profile_image="👴",
               introduction="퇴직 전 40년간 농사를 지었습니다. 제철 농사법과 토종 씨앗 관리법을 알려드립니다.",
               expertise="농사/텃밭", experience_years=40, available_days="월,수,금", location="예천군 용문면"),
        Mentor(name="이정희", age=68, phone="010-3456-7890", profile_image="👵",
               introduction="안동 양반가의 다도를 30년간 이어오고 있습니다. 차의 정신과 예절을 함께 배워요.",
               expertise="다도/예절", experience_years=30, available_days="수,토", location="안동시 도산면"),
        Mentor(name="최동진", age=75, phone="010-4567-8901", profile_image="👴",
               introduction="한지공예 명장입니다. 전통 한지로 생활용품 만드는 법을 가르칩니다.",
               expertise="한지공예", experience_years=45, available_days="월,화,목", location="안동시 서후면"),
        Mentor(name="정미옥", age=70, phone="010-5678-9012", profile_image="👵",
               introduction="어머니에게 배운 전통 발효식품의 비법을 전수합니다. 된장, 간장, 고추장의 진짜 맛.",
               expertise="발효식품", experience_years=35, available_days="화,금,토", location="예천군 호명면"),
    ]
    for m in mentors:
        db.add(m)
    db.commit()
    
    programs = [
        Program(title="안동찜닭의 비밀", category="음식", description="진짜 안동찜닭은 간장 양념부터 다릅니다. 할머니의 50년 노하우로 본고장의 맛을 배워봅시다.",
                mentor_id=1, location="G-AFC 조리실습실", schedule="매주 토요일 10:00-13:00", max_students=8, current_students=5, image_emoji="🍗", start_date=datetime.now()+timedelta(days=7)),
        Program(title="우리 집 텃밭 가꾸기", category="농사", description="아파트 베란다에서도 가능한 텃밭 농사. 상추, 고추, 토마토를 직접 키워봅시다.",
                mentor_id=2, location="캠퍼스 텃밭", schedule="매주 수요일 14:00-16:00", max_students=12, current_students=8, image_emoji="🌱", start_date=datetime.now()+timedelta(days=5)),
        Program(title="전통 다도 입문", category="예절", description="차 한 잔에 담긴 우리 문화의 정신. 다도를 통해 예절과 마음가짐을 배웁니다.",
                mentor_id=3, location="G-AFC 다례실", schedule="매주 토요일 14:00-16:00", max_students=6, current_students=4, image_emoji="🍵", start_date=datetime.now()+timedelta(days=14)),
        Program(title="한지로 만드는 생활소품", category="공예", description="전통 한지의 아름다움. 필통, 보석함 등 실용적인 한지 소품을 만들어 봅시다.",
                mentor_id=4, location="G-AFC 공예실습실", schedule="매주 목요일 10:00-12:00", max_students=10, current_students=7, image_emoji="📜", start_date=datetime.now()+timedelta(days=3)),
        Program(title="집에서 담그는 발효식품", category="음식", description="된장, 간장, 고추장... 우리 음식의 기본. 전통 방식 그대로 담가봅시다.",
                mentor_id=5, location="G-AFC 조리실습실", schedule="매주 금요일 10:00-13:00", max_students=8, current_students=6, image_emoji="🫙", start_date=datetime.now()+timedelta(days=10)),
        Program(title="헛제사밥과 안동식혜", category="음식", description="제사 음식의 정수. 정갈하고 담백한 안동의 전통 음식을 배웁니다.",
                mentor_id=1, location="안동 하회마을", schedule="매주 화요일 10:00-14:00", max_students=6, current_students=3, image_emoji="🍚", start_date=datetime.now()+timedelta(days=12)),
    ]
    for p in programs:
        db.add(p)
    db.commit()
    
    students = [
        Student(name="이지현", student_id="20210001", department="식품영양학과", phone="010-1111-1111", email="jihyun@gknu.ac.kr", interest="전통음식"),
        Student(name="박준호", student_id="20220015", department="원예학과", phone="010-2222-2222", email="junho@gknu.ac.kr", interest="농사"),
        Student(name="김민서", student_id="20230042", department="문화콘텐츠학과", phone="010-3333-3333", email="minseo@gknu.ac.kr", interest="공예"),
        Student(name="정다은", student_id="20210088", department="사회복지학과", phone="010-4444-4444", email="daeun@gknu.ac.kr", interest="예절"),
    ]
    for s in students:
        db.add(s)
    db.commit()
    
    enrollments = [
        Enrollment(student_id=1, program_id=1, status="승인"),
        Enrollment(student_id=1, program_id=5, status="신청"),
        Enrollment(student_id=2, program_id=2, status="승인"),
        Enrollment(student_id=3, program_id=4, status="승인"),
        Enrollment(student_id=4, program_id=3, status="승인"),
    ]
    for e in enrollments:
        db.add(e)
    db.commit()
    db.close()
    print("✅ 시연용 데이터 생성 완료")


seed_demo_data()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    db = SessionLocal()
    programs = db.query(Program).filter(Program.status == "모집중").limit(4).all()
    # 관계 데이터 미리 로드
    for p in programs:
        _ = p.mentor
    mentors = db.query(Mentor).filter(Mentor.is_active == True).limit(4).all()
    stats = {"mentors": db.query(Mentor).count(), "students": db.query(Student).count(),
             "programs": db.query(Program).count(), "enrollments": db.query(Enrollment).filter(Enrollment.status.in_(["승인", "수료"])).count()}
    db.close()
    return templates.TemplateResponse("home.html", {"request": request, "programs": programs, "mentors": mentors, "stats": stats})


@app.get("/programs", response_class=HTMLResponse)
async def programs_list(request: Request, category: str = None):
    db = SessionLocal()
    query = db.query(Program)
    if category:
        query = query.filter(Program.category == category)
    programs = query.all()
    for p in programs:
        _ = p.mentor
    db.close()
    return templates.TemplateResponse("programs/list.html", {"request": request, "programs": programs, "categories": ["음식", "예절", "농사", "공예"], "current_category": category})


@app.get("/programs/{program_id}", response_class=HTMLResponse)
async def program_detail(request: Request, program_id: int):
    db = SessionLocal()
    program = db.query(Program).filter(Program.id == program_id).first()
    if not program:
        db.close()
        raise HTTPException(status_code=404)
    _ = program.mentor
    db.close()
    return templates.TemplateResponse("programs/detail.html", {"request": request, "program": program})


@app.post("/programs/{program_id}/enroll")
async def enroll_program(program_id: int, name: str = Form(...), student_id: str = Form(...), phone: str = Form(...)):
    db = SessionLocal()
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        student = Student(name=name, student_id=student_id, phone=phone)
        db.add(student)
        db.commit()
        db.refresh(student)
    program = db.query(Program).filter(Program.id == program_id).first()
    if not program:
        db.close()
        raise HTTPException(status_code=404)
    existing = db.query(Enrollment).filter(Enrollment.student_id == student.id, Enrollment.program_id == program_id).first()
    if existing:
        db.close()
        return RedirectResponse(url=f"/programs/{program_id}?error=이미신청함", status_code=303)
    if program.current_students >= program.max_students:
        db.close()
        return RedirectResponse(url=f"/programs/{program_id}?error=정원마감", status_code=303)
    enrollment = Enrollment(student_id=student.id, program_id=program_id)
    db.add(enrollment)
    program.current_students += 1
    db.commit()
    db.close()
    return RedirectResponse(url=f"/programs/{program_id}?success=신청완료", status_code=303)


@app.get("/mentors", response_class=HTMLResponse)
async def mentors_list(request: Request):
    db = SessionLocal()
    mentors = db.query(Mentor).filter(Mentor.is_active == True).all()
    db.close()
    return templates.TemplateResponse("mentors/list.html", {"request": request, "mentors": mentors})


@app.get("/mentors/register", response_class=HTMLResponse)
async def mentor_register_form(request: Request):
    return templates.TemplateResponse("mentors/register.html", {"request": request})


@app.post("/mentors/register")
async def mentor_register(name: str = Form(...), age: int = Form(...), phone: str = Form(...), expertise: str = Form(...),
                          experience_years: int = Form(...), available_days: str = Form(...), location: str = Form(...), introduction: str = Form(...)):
    db = SessionLocal()
    mentor = Mentor(name=name, age=age, phone=phone, expertise=expertise, experience_years=experience_years,
                    available_days=available_days, location=location, introduction=introduction, profile_image="👨‍🏫")
    db.add(mentor)
    db.commit()
    db.close()
    return RedirectResponse(url="/mentors?success=등록완료", status_code=303)


@app.get("/mentors/{mentor_id}", response_class=HTMLResponse)
async def mentor_detail(request: Request, mentor_id: int):
    db = SessionLocal()
    mentor = db.query(Mentor).filter(Mentor.id == mentor_id).first()
    if not mentor:
        db.close()
        raise HTTPException(status_code=404)
    programs = db.query(Program).filter(Program.mentor_id == mentor_id).all()
    db.close()
    return templates.TemplateResponse("mentors/detail.html", {"request": request, "mentor": mentor, "programs": programs})


@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    db = SessionLocal()
    stats = {"mentors": db.query(Mentor).count(), "students": db.query(Student).count(), "programs": db.query(Program).count(),
             "enrollments": db.query(Enrollment).count(), "pending": db.query(Enrollment).filter(Enrollment.status == "신청").count()}
    recent = db.query(Enrollment).order_by(Enrollment.enrolled_at.desc()).limit(5).all()
    for e in recent:
        _ = e.student
        _ = e.program
        _ = e.program.mentor
    programs = db.query(Program).all()
    for p in programs:
        _ = p.mentor
    db.close()
    return templates.TemplateResponse("admin/dashboard.html", {"request": request, "stats": stats, "recent_enrollments": recent, "programs": programs})


@app.get("/admin/enrollments", response_class=HTMLResponse)
async def admin_enrollments(request: Request):
    db = SessionLocal()
    enrollments = db.query(Enrollment).order_by(Enrollment.enrolled_at.desc()).all()
    for e in enrollments:
        _ = e.student
        _ = e.program
        _ = e.program.mentor
    db.close()
    return templates.TemplateResponse("admin/enrollments.html", {"request": request, "enrollments": enrollments})


@app.post("/admin/enrollments/{enrollment_id}/approve")
async def approve_enrollment(enrollment_id: int):
    db = SessionLocal()
    e = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if e:
        e.status = "승인"
        db.commit()
    db.close()
    return RedirectResponse(url="/admin/enrollments", status_code=303)


@app.post("/admin/enrollments/{enrollment_id}/complete")
async def complete_enrollment(enrollment_id: int):
    db = SessionLocal()
    e = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if e:
        e.status = "수료"
        e.completed_at = datetime.now()
        db.commit()
    db.close()
    return RedirectResponse(url="/admin/enrollments", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
