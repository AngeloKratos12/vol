from fastapi import APIRouter


router = APIRouter(
    prefix = "/reservation"
)


@router.get("/national", summary="Faire une réservation national")
def reservation_national():
    return {"reservation":"information"}



@router.get("/international", summary="Faire une réservation international")
def reservation_international():
    return {"réservation":"Information"}



