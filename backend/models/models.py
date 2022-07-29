from ctypes.wintypes import CHAR
from sqlalchemy import Boolean, Column, Integer, String, Date, Time, Text
from db.database import Base
import enum
from sqlalchemy.dialects.mysql import ENUM



class Categorie(str, enum.Enum):
    male = "M"
    femme = "F"
    autres = "Autre"

class voyage_(str, enum.Enum):
    national = "National"
    International = "International"

class national_voyage(str, enum.Enum):
    mahajanga = "Majunga"
    tamatave = "Tamatave"
    diego = "Diego"

class international_voyage(str, enum.Enum):
    paris = "Paris"
    bordeau = "Bordeau"

class payement(str, enum.Enum):
    mvola= "Mvola"
    carte_bank = "Carte_bankaire"

class categorie_(str, enum.Enum):
    vol ="Achat_vol" 
    reservation = "Réservation" 



class client_today(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), unique=False, index=False)
    prenom= Column(String(50), unique=False, index=False)
    categorie = Column(ENUM(Categorie))
    mail = Column(String(50))
    telephone = Column(String(15))
    cin = Column(String(15))
    nbr_passage = Column(Integer)
    categorie = Column(ENUM(categorie_))
    voyage = Column(ENUM(voyage_))
    date_voyage = Column(Date)
    heurre_voyage = Column(Time)
    payement = Column(ENUM(payement))


class reservation_national(Base):
    __tablename__ = "reservation_national"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), unique=False, index=False)
    prenom= Column(String(50), unique=False, index=False)
    mail = Column(String(50))
    telephone = Column(String(15))
    cin = Column(String(15))
    nbr_passage = Column(Integer)
    destination = Column(ENUM(national_voyage))
    date_voyage = Column(Date)
    heurre_voyage = Column(Time)
    payement = Column(ENUM(payement))


class reservation_international(Base):
    __tablename__ = "reservation_international"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), unique=False, index=False)
    prenom= Column(String(50), unique=False, index=False)
    mail = Column(String(50))
    telephone = Column(String(15))
    cin = Column(String(15))
    nbr_passage = Column(Integer)
    destination = Column(ENUM(international_voyage))
    date_voyage = Column(Date)
    heurre_voyage = Column(Time)
    payement = Column(ENUM(payement))


class vol_national(Base):
    __tablename__ = "vol_national"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), unique=False, index=False)
    prenom= Column(String(50), unique=False, index=False)
    mail = Column(String(50))
    telephone = Column(String(15))
    cin = Column(String(15))
    nbr_passage = Column(Integer)
    destination = Column(ENUM(national_voyage))
    date_voyage = Column(Date)
    heurre_voyage = Column(Time)
    payement = Column(ENUM(payement))


class vol_national(Base):
    __tablename__ = "vol_international"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), unique=False, index=False)
    prenom= Column(String(50), unique=False, index=False)
    mail = Column(String(50))
    telephone = Column(String(15))
    cin = Column(String(15))
    nbr_passage = Column(Integer)
    destination = Column(ENUM(international_voyage))
    date_voyage = Column(Date)
    heurre_voyage = Column(Time)
    payement = Column(ENUM(payement))