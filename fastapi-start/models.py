from typing import Optional
from sqlmodel import SQLModel, Field

class Employee(SQLModel, table=True):
    __table_args__ = {"schema": "user_db"}
    __tablename__: str = "employees" 
    
    emp_id: int = Field(default=None, primary_key=True)
    name:str
    salary:float
