from models import Employee
from data_models import EmployeeRequest,LoginRequest
from security_config.jwt_config import create_jwt,jwt_verify
import requests
from sqlmodel import Session, select
class sample_service:
        
    def storeUser(self,empReq:EmployeeRequest,session):
        try:
            emp = Employee(
                name=empReq.name,
                emp_id=empReq.emp_id,
                salary=empReq.salary,
                email=empReq.email,
                password=empReq.password,
            )
            session.add(emp)
            session.commit()
        except:
            raise ValueError("error while storing")
    def checkUserEmail(self,email:str,session):
      emp_db =  session.exec(select(Employee).where(Employee.email==email))
      emp_data =  emp_db.first()    
      if emp_data is None:
          return True
      else:
          return False

    async def loginUser(self,loginReq:LoginRequest,session):
        emp_db =  session.exec(select(Employee).where(Employee.email==loginReq.email,Employee.password==loginReq.password))
        emp_data =  emp_db.first()
        if emp_data is not None:
            return  create_jwt(emp_data.emp_id,emp_data.email)
        else:
            raise ValueError("username or password is wrong!!")  
          
        
    def get_user_list(self):
        res =  requests.get("https://www.apirequest.in/api/user")
        return res.json()