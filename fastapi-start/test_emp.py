from fastapi.testclient import TestClient
from unittest.mock import AsyncMock,MagicMock
from db_config import get_session
from router_config.auth_router import get_obj
from main import app
from models import Employee

client = TestClient(app)


def test_emp_list():

    mock_service = MagicMock()
    def override_get_session():
        return mock_service
    
    app.dependency_overrides[get_session] = override_get_session
    
    employees = [Employee(emp_id=1,name="Praveen",email="praveen@gmail.com",password="test", salary=50000),
                 Employee(emp_id=2, name="Ravi", 
                          email="ravi@gmail.com",
                          password="test@123",salary=60000) 
                          ]
    # mock_service.exec.return_value=employees
    mock_service.exec.return_value.all.return_value = employees
    headers = {
        "token": "test-token",
        "Content-Type": "application/json"
    }

    response = client.get("/user",headers=headers)
    assert response.status_code==200
    response_json = response.json()
    assert len(response_json) == 2
    assert response_json[0]['emp_id'] ==1