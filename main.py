from fastapi import FastAPI
from cuit import normalizar_cuit, cuit_checksum_valido
app = FastAPI(title="nosis-service")


@app.get("/health")
def health():
    return {"status": "ok"}
