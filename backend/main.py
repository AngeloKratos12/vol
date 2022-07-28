from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from rooters import achat, reservation, article, decouvrer, avis



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(achat.router)
app.include_router(reservation.router)
app.include_router(article.router)
app.include_router(decouvrer.router)
app.include_router(avis.router)


@app.get("/", tags=["root"], summary="Acceuil")
async def acc():
    return {"message":"hello"}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info", workers= 10, reload = True)