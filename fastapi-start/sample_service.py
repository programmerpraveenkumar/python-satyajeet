from models import Employee
from data_models import EmployeeRequest,LoginRequest
import requests
class sample_service:
        
    def storeUser(self,empReq:EmployeeRequest,session):
        try:
            emp = Employee(
                name=empReq.name,
                emp_id=empReq.emp_id,
                salary=empReq.salary
            )
            session.add(emp)
            session.commit()
        except:
            raise ValueError("error while storing")

          
    def loginUser(self,loginReq:LoginRequest,session):
        #TODO connect to the login table
        if loginReq.username=="admin" and loginReq.password=="admin":
            return True
        else:
            raise ValueError("error while login")  
          
        
    def get_user_list(self):
        res =  requests.get("https://www.apirequest.in/api/user")
        return res.json()