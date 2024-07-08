from cruds import cruds
from database import get_db, Session
from schemas import schemas
from fastapi import Depends, APIRouter

router = APIRouter()

@router.get("/getCourse{cid}", response_model=schemas.Course, responses={
    404: {"model": schemas.ErrorMessage, "description": "Course Not Found"}})
def get_course(cid: int, db: Session = Depends(get_db)):
    return cruds.course_exist(cid= cid, db= db)

@router.post("/regCours", response_model=schemas.Course, responses={
    409: {"model": schemas.ErrorMessage, "description": "Duplicated Course"}})
def reg_course(course: schemas.Course, db: Session = Depends(get_db)):
    return cruds.registr_course(course= course, db= db)

@router.patch("/updateCours{cid}", response_model=schemas.Course, responses={
    404: {"model": schemas.ErrorMessage, "description": "Course Not Found"}})
def patch_course(cid: int, new_date: schemas.Course, db: Session = Depends(get_db)):
    return cruds.update_course(cid= cid, new_data=new_date, db= db)

@router.delete("/delCours{cid}", response_model=schemas.Course, responses={
    404: {"model": schemas.ErrorMessage, "description": "Course Not Found"}})
def del_course(cid: int, db: Session = Depends(get_db)):
    return cruds.delete_course(cid= cid, db= db)

