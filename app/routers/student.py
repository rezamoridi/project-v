from database import get_db, Session
from schemas import schemas
from cruds import cruds
from fastapi import Depends, APIRouter


router = APIRouter()

@router.get("/getStu{id}", response_model=schemas.Student,responses={
    404: {"model": schemas.ErrorMessage, "description": "Student Not Found"}})
def get_student(id: int, db: Session = Depends(get_db)):
    return cruds.student_exist(id, db)

@router.post('/regStu', response_model=schemas.BaseStudent, responses={
    404: {"model": schemas.ErrorMessage, "description": "Course Or Lecturer Not found"},
    409: {"model": schemas.ErrorMessage, "description": "Duplicated Student"}})
def post_stud(student: schemas.Student, db: Session = Depends(get_db)):
    cruds.register_student(db= db, student=student)
    return schemas.BaseStudent(fname=student.fname, lname=student.lname, stid=student.stid, major=student.major)


@router.patch("/updateStu{id}", response_model=schemas.Student, responses={
    404: {"model": schemas.ErrorMessage, "description": "Student Not Found"}})
def update_student(id: int, update_model: schemas.Student, db: Session = Depends(get_db)):
    return cruds.update_student(id, update_model, db)

@router.delete("/delStu{id}", response_model=schemas.BaseStudent, responses={
    404: {"model": schemas.ErrorMessage, "description": "Student Not Found"}})
def delete_student(id: int, db: Session = Depends(get_db)):
    return cruds.delete_student(id, db)



