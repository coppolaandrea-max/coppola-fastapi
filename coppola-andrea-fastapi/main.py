# main.py - il primo server: a chi dice «ping» rispondiamo «pong»
from fastapi import FastAPI
# 1. creiamo l'applicazione, cioè il server
app = FastAPI()

# 2. quando arriva una richiesta GET all'indirizzo /ping, rispondiamo pong
@app.get("/ping")  # questa è una delle rotte del nostro server (decoratore)
def ping():
    return {"risposta": "pong"}
# 3. il colpo con GET: la parola arriva nell'indirizzo e il server decide che cosa
rispondere
@app.get("/gioca")
def gioca(parola: str):
    if parola == "ping":
        return {"risposta": "pong"}
    return {"risposta": "Non ho capito: scrivi ping"}