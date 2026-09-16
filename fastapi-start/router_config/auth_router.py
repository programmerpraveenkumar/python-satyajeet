from fastapi import FastAPI,Depends,Header,Request,APIRouter,HTTPException,WebSocket
from db_config import get_session
from models import Employee
from data_models import EmployeeRequest,LoginRequest
from sqlmodel import Session, select
from sample_service import sample_service


auth_router= APIRouter()

def get_obj():
   return sample_service()





@auth_router.post("/login")
async def login(loginReq:LoginRequest,
           sample_service_obj=Depends(get_obj),
           session: Session = Depends(get_session)):
    try:
        token =await sample_service_obj.loginUser(loginReq,session)
        return {
            "token":token,
            "message":"login sucessful"
        }
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    
@auth_router.post("/register")
async def register(empReq:EmployeeRequest,
           sample_service_obj=Depends(get_obj),
           session: Session = Depends(get_session)):
    try:
        if sample_service_obj.checkUserEmail(empReq.email,session):
            sample_service_obj.storeUser(empReq,session)
            return {
                "message":"Register sucessful"
            }
        else:
            raise ValueError("Email is already registered")
                   
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))    