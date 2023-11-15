"""
FAST API route implmentations

@author Anthony Epps
"""

from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import StudentSchema,RequestStudent,Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create(request:RequestStudent,db:Session=Depends(get_db)):
    _student = crud.create_student(db,student=request.parameter)
    return Response(code="200",status="OK",message="Student successfully created",result=_student).dict(exclude_none=True)

@router.get('/')
async def get(db:Session=Depends(get_db)):
    _student = crud.get_student(db, 0, 100)
    return Response(code="200",status="OK",message="All Student(s) data successfully fetched", result=_student).dict(exclude_none=True)

@router.get('/{id}')
async def get_by_id(id:int, db:Session=Depends(get_db)):
    _student = crud.get_student_by_id(db,id)
    return Response(code="200",status="OK",message="Student data successfully fetched for entered id", result=_student).dict(exclude_none=True)

@router.patch('/update')
async def udpate_student(request: RequestStudent, db:Session=Depends(get_db)):
    _student = crud.update_student(db,student_id=request.parameter.id, fname=request.parameter.fname, lname=request.parameter.lname)
    return Response(code="200",status="OK",message="Student data successfully updated", result=_student).dict(exclude_none=True)

@router.delete('/{id}')
async def delete(id:int, db:Session=Depends(get_db)):
    _student = crud.remove_student(db,student_id=id)
    return Response(code="200",status="OK",message="Student data successfully deleted for the id given", result=_student).dict(exclude_none=True)