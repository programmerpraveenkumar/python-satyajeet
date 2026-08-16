from fastapi import FastAPI,Request,HTTPException,Depends,Header
from fastapi.responses import JSONResponse
import time
from router_config import user_router,product_router,auth_router

app = FastAPI()

@app.middleware("http")
async def timing_middlware(request:Request,call_next):
    starttime = time.time()
    # print(request.url)

    # print(request.url.path)
    if request.url.path.startswith("/auth"):
            response = await call_next(request)
    else:
        # print(request.headers.get("session"))
        auth_token = request.headers.get("auth_token")
        if auth_token is None:
            # return the error response
            return JSONResponse(
                status_code=401,
                content={"detail": "Token is not found"}
            )
        else:
            response = await call_next(request)
    
    endtime = time.time()
    print(f"total time taken {endtime} {starttime} {endtime-starttime} seconds")
    return response




app.include_router(auth_router.auth_router,prefix="/auth")
app.include_router(user_router.router,prefix="/user")
app.include_router(product_router.router,prefix="/product")



# authentication
# login->username,password->valid->token
                        #   ->not vlaid->not token  

#store the token in front-end app

# 17.0.0.1/inbox
# 17.0.0.1/sentbox
# JWT->id,expiry,encoding algorithm+securekey
# movie