from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import urllib.parse
from pyHaiku import Random_haiku

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/haiku")
async def getNyanMessage():
    #ランダム俳句返し
    #message = urllib.parse.unquote()
    replyHaiku = Random_haiku()
    
    print(replyHaiku)
    return {"message": replyHaiku,"status":"success"}
