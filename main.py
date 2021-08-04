from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import urllib.parse
from pyHaiku import Random_haiku,Kisetsu_haiku

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

@app.get("/haiku/{message}")
async def getNyanMessage(message):
    #ランダム俳句返し
    message = urllib.parse.unquote(message)
    if "春" in message or "夏" in message or "秋" in message or "冬" in message:
        haikufirst,haikusecond,haikuthird = Kisetsu_haiku(message)
        season = message
    else:
        haikufirst,haikusecond,haikuthird = Random_haiku()
        season = "季節なし"
    
    print(f"{season}:{haikufirst} {haikusecond} {haikuthird}")
    return {"message1": haikufirst,"message2": haikusecond,"message3": haikuthird,"season": season,"status":"success"}
