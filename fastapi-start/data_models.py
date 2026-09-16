from pydantic import BaseModel

class EmployeeRequest(BaseModel):
    emp_id: int
    name:str
    salary:float
    email:str
    password:str

class LoginRequest(BaseModel):
   email:str
   password:str

