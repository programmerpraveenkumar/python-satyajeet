from fastapi import FastAPI,Depends
from pydantic import BaseModel
from db_config import get_session
from models import Employee
from sqlmodel import Session, select


app = FastAPI()


class UserRegister(BaseModel):
    name:str
    mobile:str


@app.get("/")
def sample(session: Session = Depends(get_session)):
    emp_list = session.exec(select(Employee)).all()
    
    return emp_list

@app.get("/sample")
def sample(name:str,mobile:str):
   
    return f"name is {name} and mobile is {mobile} "

@app.get("/sample/{id}")
def user_id(id:int):
    return f"id is {id} "

@app.post("/sample")
def user_register(user_reg:UserRegister):
    return f" name {user_reg.name} and mobile {user_reg.mobile}"

@app.put("/sample")
def user_register(user_id:str,user_reg:UserRegister):
    return f" id {user_id} name {user_reg.name} and mobile {user_reg.mobile}"

@app.delete("/sample")
def delete_register(user_id:int):
    return f" id for delete {user_id}"


"""
`{
name:"",
mobile:"",
city:""
}`

class user_regiseter:
name:str
mobile:str

"""