from fastapi import APIRouter


router = APIRouter(
    prefix = "/reservation"
)


@router.get("/national", summary="Faire une réservation national")
def national():
    return {"reservation":"information"}



@router.get("/international", summary="Faire une réservation international")
def international():
    return {"réservation":"Information"}



