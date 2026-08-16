from fastapi import FastAPI,Depends,Header,Request,APIRouter,HTTPException
from db_config import get_session
from models import Employee
from data_models import EmployeeRequest,LoginRequest
from sqlmodel import Session, select
from sample_service import sample_service


auth_router= APIRouter()

def get_obj():
   return sample_service()

@auth_router.post("/login")
def login(loginReq:LoginRequest,
           sample_service_obj=Depends(get_obj),
           session: Session = Depends(get_session)):
    try:
        sample_service_obj.loginUser(loginReq,session)
        return {"message":"user loggedin"} 
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))