from cruds import cruds
from database import get_db, Session
from schemas import schemas
from fastapi import Depends, APIRouter

router = APIRouter()

@router.get("/getLect{lid}", response_model=schemas.Lecturer,responses={
    404: {"model": schemas.ErrorMessage, "description": "Lecturer not found"}})
def get_lecturer(lid: int, db: Session = Depends(get_db)):
    return cruds.lecturer_exist(lid= lid, db= db)



@router.post("/regLect", response_model= schemas.BaseLecturer, responses={
    404: {"model": schemas.ErrorMessage, "description": "Course Not found for Lecturer"},
    409: {"model": schemas.ErrorMessage, "description": "Duplicated Lecturer"}})
def register_lecturer(lecturer: schemas.Lecturer, db: Session = Depends(get_db)):
    return cruds.register_lecturer(lecturer= lecturer, db= db)



@router.patch("/updateLect{lid}", response_model=schemas.Lecturer, responses={
    404: {"model": schemas.ErrorMessage, "description": "Lecturer not found"}})
def updatelecturer(lid: int, update_date : schemas.Lecturer, db : Session = Depends(get_db)):
    return cruds.update_lecturer(lid= lid, new_data= update_date, db= db)




@router.delete("/delLect{lid}", response_model=schemas.BaseLecturer, responses={
    404: {"model": schemas.ErrorMessage, "description": "Lecturer not found"}})
def delete_lecturer(lid: int, db: Session = Depends(get_db)):
    return cruds.delete_lecturer(lid= lid, db= db)


