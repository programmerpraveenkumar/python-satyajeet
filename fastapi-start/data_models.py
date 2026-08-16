from pydantic import BaseModel

class EmployeeRequest(BaseModel):
    emp_id: int
    name:str
    salary:float

class LoginRequest(BaseModel):
   username:str
   password:str
