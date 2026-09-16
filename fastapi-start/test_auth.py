from fastapi.testclient import TestClient
from unittest.mock import AsyncMock
from db_config import get_session
from router_config.auth_router import get_obj
from main import app

client = TestClient(app)

def test_login():
    login_data={
        "email":"asdfsdfsd",
        "password":"sdfsadf"
    }
    response = client.post("/auth/login",json=login_data)
    assert response.status_code==400


def test_loginsuccess():
    mock_service = AsyncMock()

    mock_service.loginUser.return_value ="some-jwt-token"
   
    def override_get_job():
        return mock_service
    
    def override_get_session():
        return mock_service

    app.dependency_overrides[get_obj] = override_get_job
    app.dependency_overrides[get_session] = override_get_session

    login_data={
        "email":"test@gmail.com",
        "password":"test"
    }
    response = client.post("/auth/login",json=login_data)

    assert response.status_code==200

    assert response.json()=={
          "token":"some-jwt-token",
            "message":"login sucessful"
    }
    # makesure loginUser calls only once during the testcase
    mock_service.loginUser.assert_awaited_once()