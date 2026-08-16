from fastapi import FastAPI,Depends,Header,Request,APIRouter
from db_config import get_session
from models import Employee
from data_models import EmployeeRequest
from sqlmodel import Session, select
from sample_service import sample_service


router= APIRouter()


def get_obj( req: Request):
    print(req.headers)#accessing the http headers
    return sample_service()

@router.get("/")
def sample(session: Session = Depends(get_session)):
    emp_list = session.exec(select(Employee)).all()
    return emp_list

@router.get("/get_user_api")
def sample(sample_service_obj=Depends(get_obj)):
    # sample_service_obj = sample_service()
    user_list = sample_service_obj.get_user_list()
    return user_list


@router.post("/")
def sample(empReq:EmployeeRequest,
           sample_service_obj=Depends(get_obj),
           session: Session = Depends(get_session)):
#    sample_service_obj = sample_service()
   sample_service_obj.storeUser(empReq,session)
   return {"message":"user stored"} 