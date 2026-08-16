from fastapi import FastAPI,Depends,Header,Request,APIRouter
from db_config import get_session
from models import Employee
from data_models import EmployeeRequest
from sqlmodel import Session, select
from sample_service import sample_service


router= APIRouter()

@router.get("/")
def sample(session: Session = Depends(get_session)):
    emp_list = session.exec(select(Employee)).all()
    return emp_list