from fastapi import APIRouter


router = APIRouter(
    prefix = "/decouvrer"
)

@router.get("/programme_vol" , summary="Savoir les progmammes du vol")
def programme_vol():
    return {"Notre programme":"national et international"}



@router.get("/reseau" , summary="Découvrer notre réseau")
def reseau():
    return {"Notre Réseau":"national et international"}



@router.get("/information_vol" , summary="Savoir les offres à proposer")
def information_vol():
    return {"Notre vol":"Information"}


@router.get("/nous" , summary="Contacter notre employés")
def nous():
    return {"Notre programme":"national et international"}
