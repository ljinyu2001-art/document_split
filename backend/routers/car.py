from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Car, CarReserve


router = APIRouter(
    prefix="/car",
    tags=["车辆"]
)


# ============================
# 查询车辆列表（包含状态）
# ============================

@router.get("/list")
def car_list(
    db: Session = Depends(get_db)
):

    result = db.query(
        Car,
        CarReserve.status
    ).join(
        CarReserve,
        Car.car_id == CarReserve.car_id
    ).all()


    cars = []


    for car, status in result:

        cars.append({

            "car_id": car.car_id,

            "car_type": car.car_type,

            "capacity": car.capacity,

            "manufacturer": car.manufacturer,

            "produce_date": car.produce_date,

            "price": car.price,

            "status":
                "可预约"
                if status == "0"
                else "已预约"

        })


    return cars



# ============================
# 预约车辆
# ============================

@router.put("/reserve/{car_id}")
def reserve(

    car_id: int,

    db: Session = Depends(get_db)

):


    # 查询车辆状态

    car_status = db.query(
        CarReserve
    ).filter(
        CarReserve.car_id == car_id
    ).first()



    # 没有状态记录

    if not car_status:

        return {

            "msg":"车辆状态记录不存在"

        }



    # 已预约

    if car_status.status == "1":

        return {

            "msg":"该车辆已经被预约"

        }



    # 修改状态

    car_status.status = "1"


    db.commit()


    return {

        "msg":"预约成功",

        "car_id":car_id

    }