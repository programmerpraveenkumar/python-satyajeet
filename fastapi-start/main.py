from fastapi import FastAPI,Request,HTTPException,Depends,Header,WebSocket,WebSocketDisconnect
from fastapi.responses import JSONResponse,StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import time
from router_config import user_router,product_router,auth_router
import asyncio
from security_config.jwt_config import jwt_verify

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ConnectionManager:
    def __init__(self):
        # self.active_connections: list[WebSocket] = []
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self,client_id, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[client_id]=websocket

    def disconnect(self, client_id):
        # self.active_connections.remove(websocket)
        self.active_connections.pop(client_id, None)

    async def send_personal_message(self, message: str, client_id):
        # await websocket.get("client_id").send_text(message)
        connection = self.active_connections.get(client_id)
        if connection:
            await connection.send_text(message)
        else:
            print("No connect found")

    async def broadcast(self, message: str):
        for websocket in self.active_connections.values():
            await websocket.send_text(message)


manager = ConnectionManager()

# @app.websocket("/my-ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         # recv the text from the client
#         message = await websocket.receive_text()
#         await websocket.send_text(f"Server received: {message}")

async def generate_data():
    for i in range(5):
        yield f"message is {i}"
        await asyncio.sleep(3)

@app.websocket("/my-ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(client_id,websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(client_id)
        await manager.broadcast(f"Client #{client_id} left the chat")


@app.post("/my-ws/broadcast")
async def websocket_endpoint(message:str):
    try:
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(message)
    except Exception:
        print("Error")


@app.post("/my-ws/send-individual")
async def websocket_endpoint(client_id:int,message:str):
    try:
        for connetion in manager.active_connections:
            #  print(connetion.client)
            await manager.send_personal_message(message,client_id)
            # await manager.broadcast(message)
    
    except Exception:
        print("Error")        
       

@app.get("/streaming")
async def streaming_endpoint():
    return StreamingResponse(
        generate_data(),media_type="text/plain"
    )


# @app.middleware("http")
# async def timing_middlware(request:Request,call_next):
#     starttime = time.time()
#     # print(request.url)

#     # print(request.url.path)
#     if request.url.path.startswith("/auth"):
#             response = await call_next(request)
#     else:
#         # print(request.headers.get("session"))
#         auth_token = request.headers.get("auth_token")
#         if auth_token is None:
#             # return the error response
#             return JSONResponse(
#                 status_code=401,
#                 content={"detail": "Token is not found"}
#             )
#         else:
#             response = await call_next(request)
    
#     endtime = time.time()
#     print(f"total time taken {endtime} {starttime} {endtime-starttime} seconds")
#     return response


def user_token_validation_middleware(token:str=Header(None)):
    try:
        # # if tokn is not aviable return the error in json format
        # if token is None:
        #     raise HTTPException(
        #         status_code=401,
        #         detail="Token is not found"
        #     )
        # else:
        #         jwt_verify(token)
        return True
    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(
                status_code=401,
                detail=str(e)
            ) 


app.include_router(auth_router.auth_router,prefix="/auth")
app.include_router(user_router.router,prefix="/user",dependencies=[Depends(user_token_validation_middleware)])
app.include_router(product_router.router,prefix="/product",dependencies=[Depends(user_token_validation_middleware)])



# authentication
# login->username,password->valid->token
                        #   ->not vlaid->not token  

#store the token in front-end app

# 17.0.0.1/inbox
# 17.0.0.1/sentbox
# JWT->id,expiry,encoding algorithm+securekey
# movie