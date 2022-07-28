from fastapi import APIRouter


router = APIRouter(
    prefix = "/avis"
)


@router.get("/modifier_reservation")
def modifier_reservation():
    return {"reservation":"modifier"}

@router.get("/recherche")
def recherche():
    return {"objet":"recherche"}