from database import Base
from sqlalchemy import Column, String, ARRAY, BigInteger, Integer, BOOLEAN
from sqlalchemy.dialects.postgresql import BIGINT, DATE



class Student(Base):
    __tablename__ = "students"

    stid = Column(BIGINT, primary_key=True)
    fname = Column(String(10))
    lname = Column(String(10))
    fathername = Column(String(10))
    birth = Column(DATE)
    address= Column(String(100))
    id = Column(BIGINT, unique=True)
    ids = Column(String, unique=True)
    born_city= Column(String(25))
    cphone = Column(String(13))
    hphone = Column(String)
    postal_code = Column(BIGINT)
    major = Column(String(30))
    department= Column(String(20))
    married= Column(BOOLEAN)
    enrolled_courses_ids= Column(ARRAY(String))
    lecturer_ids = Column(ARRAY(Integer))



class Lecturer(Base):
    __tablename__ = "lecturer"

    lid = Column(BIGINT, primary_key=True)
    fname = Column(String(10))
    lname = Column(String(10))
    id = Column(BIGINT, unique=True)
    department = Column(String(20))
    major = Column(String(30))
    birth = Column(String)
    born_city = Column(String(30))
    address = Column(String(100))
    postal_code = Column(BIGINT)
    cphone = Column(String)
    hphone = Column(String)
    l_course_ids = Column(ARRAY(Integer))



class Course(Base):
    __tablename__ = "courses"

    cid = Column(Integer, primary_key=True)
    cname = Column(String(25))
    department = Column(String(30))
    credit = Column(Integer)
