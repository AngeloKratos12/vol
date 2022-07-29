from fastapi import APIRouter


router = APIRouter(
    prefix = "/achat"
)


@router.get("/national", summary="Faire une réservation national")
def national():
    return {"Achet":"information"}



@router.get("/international", summary="Faire une réservation international")
def international():
    return {"Achat":"Information"}

