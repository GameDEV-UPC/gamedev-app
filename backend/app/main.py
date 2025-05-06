from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import threading

app = FastAPI()

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes poner solo tu dominio en lugar de '*'
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Player(BaseModel):
    nick: str
    color: str

players = []


@app.post("/join")
def join(player: Player):
    
    players.append(player)
    return {"message": "Jugador añadido"}

@app.get("/players")
def get_players():
    
    playerslist = players.copy()  # Copia de la lista de jugadores
    players.clear()
    return playerslist

@app.delete("/players")
def delete_players():
   
    players.clear()
    return {"message": "Jugadores borrados"}