from pydantic import BaseModel, Field, condate, field_validator
from .consts import IRAN_PROVINCE_CAPITALS, VALID_DEPARTMENTS, VALID_ENGI_DEPARTMENT_MAJORS



 
class BaseUser(BaseModel):
    fname : str = Field(min_length=3, max_length=10 ,pattern=r"^[\u0600-\u06FF]+$", default="نام")
    lname : str = Field(min_length=3, max_length=10 ,pattern=r"^[\u0600-\u06FF]+$", default="فامیلی")
    birth : str = Field(pattern = r"^1[3-4]\d{2}-(0[1-6]-(0[1-9]|[1-2][0-9]|[3][0-1])|(?:1[0-2]|(?:0[7-9]))-(0[1-9]|[1-2][0-9]|[3][0]))$")
    address: str = Field(min_length=3, max_length=100, pattern=r"^[\u0600-\u06FF\.\- ]+$", default="آدرس")
    id : int  = Field(default=1234567890, description="کد ملی معتبر")
    born_city: str = Field(default="مرکز استان")
    cphone : str = Field(pattern=r"^09[0-9]{9}$")
    hphone : str = Field(pattern=r"^0\d{2}-\d{8}")
    postal_code : int = Field(ge=1000000000, le=9999999999, default=1234567890)
    major : str = Field(default="یکی از رشته های فنی مهندسی")
    department: str = Field(min_length=3, max_length=30)

    @field_validator('id')
    @classmethod
    def valid_id_number(cls, v):
        if not check_code_meli(v):
            raise ValueError("invalid id number")
        return v

    @field_validator('born_city')
    @classmethod
    def valid_born_city(cls, v):
        if not v in IRAN_PROVINCE_CAPITALS:
            raise ValueError("invalid born city. born city must be a capital of the iran provinces")
        return v

    @field_validator('department')
    @classmethod
    def valid_department(cls, v):
        if not v in VALID_DEPARTMENTS:
            raise ValueError("invalid department, it must be one of valid departments")
        return v
    
    @field_validator('major')
    @classmethod
    def valid_major(cls, v):
        if not v in VALID_ENGI_DEPARTMENT_MAJORS:
            raise ValueError("major must be one of the enineering department")
        return v
    





class Student(BaseUser):
    stid : str = Field(pattern=r"40[0-2]114150\d{2}")

    fathername : str = Field(min_length=3, max_length=20 ,pattern=r"^[\u0600-\u06FF]+$", default="نام پدر")

    ids : str = Field(pattern=r"^\d{8}[\u0600-\u06FF]$", default='12345678ش')

    married: bool = False

    enrolled_courses_ids: list[int]

    lecturer_ids : list[int]







class Lecturer(BaseUser):
    lid: int

    l_course_ids: list[int]





class Course(BaseModel):
    cid : int = Field(ge=0, le=99999, default=12345)
    cname : str = Field(pattern=r"^[\u0600-\u06FF 1-9۱-۹]{2,25}$", default="نام درس")
    department : str = Field(default="یکی از دانشکده های مجاز")
    credit : int = Field(ge=1, le=4, default=4)

    @field_validator('department')
    def valid_department(cls, v):
        if not v in VALID_DEPARTMENTS:
            raise ValueError("invalid Department for course")
        return v




class ErrorMessage(BaseModel):
  message: str



class BaseStudent(BaseModel):
    fname: str
    lname: str
    stid : str
    major: str

class BaseLecturer(BaseModel):
    fname: str
    lname: str
    lid: str
    major: str


# Validation check algorithm
def check_code_meli(code):
            code1 = str(code)
            L = len(code1)
        
            if L < 8 or int(code) == 0:
                return False
        
            code1 = ('0000' + code1)[-10:]
        
            if int(code1[3:9]) == 0:
                return False
        
            c = int(code1[9])
            s = 0
            for i in range(9):
                s += int(code1[i]) * (10 - i)
        
            s = s % 11
            return (s < 2 and c == s) or (s >= 2 and c == (11 - s))



