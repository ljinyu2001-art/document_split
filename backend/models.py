from sqlalchemy import Column,Integer,String,Float,Date,ForeignKey
from database import Base



class User(Base):

    __tablename__="users"


    card_id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    username = Column(
        String(50)
    )


    password = Column(
        String(50)
    )


    email = Column(
        String(50)
    )


    vip_id = Column(
        String(7)
    )



class Car(Base):

    __tablename__="car_info"


    car_id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    car_type = Column(
        String(20)
    )


    capacity = Column(
        Float
    )


    manufacturer = Column(
        String(200)
    )


    produce_date = Column(
        Date
    )


    price = Column(
        Float
    )



class CarReserve(Base):

    __tablename__="car_reserver"


    reserver_id = Column(
        Integer,
        primary_key=True
    )


    car_id = Column(
        Integer,
        ForeignKey("car_info.car_id")
    )


    status = Column(
        String(2)
    )