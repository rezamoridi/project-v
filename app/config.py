import routers
from models import models
from database import engine
from fastapi import FastAPI
import routers.course
import routers.lecturer
import routers.student

app = FastAPI()

models.Base.metadata.create_all(bind = engine)


app.include_router(routers.student.router, tags=["Students"]) 
app.include_router(routers.lecturer.router, tags=["Lecturers"])
app.include_router(routers.course.router, tags=["Courses"])