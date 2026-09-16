from jose import jwt

SECURITY_KEY = "security"
def create_jwt(user_id,email):
    return jwt.encode(
        {
            "sub":email,
            "user_id":user_id

        },SECURITY_KEY,algorithm="HS256"
    )

def jwt_verify(token):
   jwt.decode(token,SECURITY_KEY,algorithms=["HS256"])
