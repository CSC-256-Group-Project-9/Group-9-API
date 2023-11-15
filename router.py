"""
FAST API route implmentations

@author Anthony Epps
"""

from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import StudentSchema,RequestStudent,Response
import crud

# Initialize the APIRouter object
router = APIRouter()

# Try/Catch to make connection to database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#POST: Create Student , return RESPONSE object
@router.post('/create')
async def create(request:RequestStudent,db:Session=Depends(get_db)):
    _student = crud.create_student(db,student=request.parameter)
    return Response(code="201",status="Created",message="Student %s successfully created" %(_student.fname),result=_student).dict(exclude_none=True)

#GET: Get all Students from database, return RESPONSE object
@router.get('/')
async def get(db:Session=Depends(get_db)):
    _student = crud.get_student(db, 0, 100)
    return Response(code="200",status="OK",message="All Student(s) data successfully fetched", result=_student).dict(exclude_none=True)

#GET: Get Student with passed ID passed (IN URL), return RESPONSE object
@router.get('/{id}')
async def get_by_id(id:int, db:Session=Depends(get_db)):
    _student = crud.get_student_by_id(db,id)
    return Response(code="200",status="OK",message="Student data successfully fetched for entered id", result=_student).dict(exclude_none=True)

#PATCH: Update Student with ID passed IN THE BODY (NOT URL), return RESPONSE object
@router.patch('/update')
async def udpate_student(request: RequestStudent, db:Session=Depends(get_db)):
    _student = crud.update_student(db,student_id=request.parameter.id, fname=request.parameter.fname, lname=request.parameter.lname)
    return Response(code="204",status="OK",message="Student data successfully updated", result=_student).dict(exclude_none=True)

#DELETE: Deletes Student with passed ID (IN URL), return RESPONSE object
@router.delete('/{id}')
async def delete(id:int, db:Session=Depends(get_db)):
    _student = crud.remove_student(db,student_id=id)
    return Response(code="204",status="OK",message="Student data successfully deleted for ID", result=_student).dict(exclude_none=True)