from schemas import schemas

from models import models
from sqlalchemy.orm import Session
from fastapi import HTTPException



"""sumary_line

                                           ------------------- Students CRUDS -------------------

"""



def register_student(student: schemas.Student, db: Session):
    not_existed_courses = []
    not_existed_lecturers = []

    for cid in student.enrolled_courses_ids:
        course = db.query(models.Course).filter(models.Course.cid == cid).first()
        if not course:
            not_existed_courses.append(cid)  
    if not_existed_courses:
        raise HTTPException(status_code=404, detail=f"Courses not found Student: {not_existed_courses}")

    for lid in student.lecturer_ids:
        lecturer = db.query(models.Lecturer).filter(models.Lecturer.lid == lid)
        if not lecturer:
            not_existed_lecturers.append(lecturer)
        if not_existed_lecturers:
            raise HTTPException(status_code=404, detail=f"Lecturers not found Student: {not_existed_lecturers}")


    if student_exist(student.id, db):
        raise HTTPException(status_code=409, detail="student exists")
    
    reg_student = models.Student(stid = student.stid,
                                fname = student.fname,
                                lname = student.lname,
                                fathername= student.fathername,
                                birth = student.birth,
                                address= student.address,
                                id = student.id,
                                ids = student.ids,
                                born_city= student.born_city,
                                cphone = student.cphone,
                                hphone = student.hphone,
                                postal_code = student.postal_code,
                                major = student.major,
                                department= student.department,
                                married= student.married,
                                enrolled_courses_ids= student.enrolled_courses_ids,
                                lecturer_ids = student.lecturer_ids
                                )
    
    
    db.add(reg_student)
    db.commit()
    return reg_student



def student_exist(id: int, db: Session):
    student = db.query(models.Student).filter(models.Student.stid == str(id)).first()
    if not student:
        return None
    return student



def delete_student(id: int, db: Session):
    student = student_exist(id, db)
    if not student:
        raise HTTPException(status_code=404, detail="Student doesn't exist")
    db.delete(student)
    db.commit()
    return student
    


def update_student(id: int, update_data: schemas.Student, db: Session):
    student_query = db.query(models.Student).filter(models.Student.stid == id)
    if not student_query.first():
        raise HTTPException(status_code=404, detail="Student not found")
    student_query.update(update_data.model_dump())
    db.commit()
    return update_data
    



    


"""sumary_line

                                           ------------------- Lecturer CRUDS -------------------

"""



def lecturer_exist(lid: int, db: Session):
    lecturer = db.query(models.Lecturer).filter(models.Lecturer.lid == lid).first()
    if not lecturer:
        return None
    return lecturer



def register_lecturer(lecturer: schemas.Lecturer, db: Session):

    not_existed_courses = []
    for cid in lecturer.l_course_ids:
        course = db.query(models.Course).filter(models.Course.cid == cid).first()
        if not course:
            not_existed_courses.append(cid)  
    if not_existed_courses:
        raise HTTPException(status_code=404, detail=f"Courses not found for lecturer: {not_existed_courses}")

    if lecturer_exist(lid = lecturer.lid, db = db):
        raise HTTPException(status_code=409, detail="same lecturer id exists")
    
    add_lecturer = models.Lecturer(lid = lecturer.lid,
                              fname = lecturer.fname,
                              lname = lecturer.lname,
                              id = lecturer.id,
                              department = lecturer.department,
                              major = lecturer.major,
                              birth = lecturer.birth,
                              born_city = lecturer.born_city,
                              address = lecturer.address,
                              postal_code = lecturer.postal_code,
                              cphone = lecturer.cphone,
                              hphone = lecturer.hphone,
                              l_course_ids = lecturer.l_course_ids,
    )
    db.add(add_lecturer)
    db.commit()
    return add_lecturer


def update_lecturer(lid: int, new_data: schemas.Lecturer, db: Session):
    lecturer_query = db.query(models.Lecturer).filter(models.Lecturer.lid == lid)

    if not lecturer_query.first():
        raise HTTPException(status_code=404, detail="lecturer id does not exist")
    
    lecturer_query.update(new_data.model_dump())
    db.commit()
    return new_data

def delete_lecturer(lid: int, db: Session):
    lecturer = db.query(models.Lecturer).filter(models.Lecturer.lid == lid).first()
    if not lecturer:
        raise HTTPException(status_code=404, detail="Lecturer id does not exist")

    db.delete(lecturer)
    db.commit()
    return lecturer







"""sumary_line

                                                ------------------- Courses CRUDS -------------------

"""
def course_exist(cid: int, db: Session):
    course_query = db.query(models.Course).filter(models.Course.cid == cid)

    if not course_query.first():
        raise HTTPException(status_code=404, detail="Course not found")

    return course_query



def registr_course(course: schemas.Course, db: Session):
    if db.query(models.Course).filter(models.Course.cid == course.cid).first():
        raise HTTPException(status_code=409, detail="Course with same id exists")

    course_db = models.Course(cid = course.cid,
                             cname = course.cname,
                             department = course.department,
                             credit = course.credit
                            )

    db.add(course_db)
    db.commit()
    return course



def update_course(cid: int, new_data: schemas.Course, db: Session):
    course_exist(cid= cid, db= db)
    course_exist(cid= cid, db= db).update(new_data.model_dump())
    db.commit()
    return new_data
    

def delete_course(cid: int, db: Session):
    course_exist(cid= cid, db= db)
    db.delete(course_exist(cid= cid, db= db).first())
    db.commit()
    return cid
