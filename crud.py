from sqlalchemy.orm import Session
from model import Student
from schemas import StudentSchema

# Get all student data
def get_student(db:Session, skip:int=0,limit:int=100):
    return db.query(Student).offset(skip).limit(limit).all()

# Get Students by id
def get_student_by_id(db:Session,student_id: int):
    return db.query(Student).filter(Student.id==student_id).first()

# Create student data
def create_student(db:Session, student:StudentSchema):
    _student = Student(fname=student.fname, lname=student.lname)
    db.add(_student)
    db.commit()
    db.refresh(_student)
    return _student

# Remove student by id
def remove_student(db:Session, student_id:int):
    _student = get_student_by_id(db=db, student_id=student_id)
    db.delete(_student)
    db.commit() 
# Update Student data
def update_student(db:Session, student_id:int, fname:str, lname:str):
    _student = get_student_by_id(db=db, student_id=student_id)
    _student.fname = fname
    _student.lname = lname
    db.commit()
    db.refresh(_student)
    return _student

