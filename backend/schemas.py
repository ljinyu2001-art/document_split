from pydantic import BaseModel



# 注册

class UserCreate(BaseModel):

    username:str

    password:str

    email:str



# 登录

class UserLogin(BaseModel):

    username:str

    password:str



# 返回用户

class UserOut(BaseModel):

    card_id:int

    username:str

    email:str


    class Config:

        from_attributes=True



# 返回车辆


class CarOut(BaseModel):

    car_id:int

    car_type:str

    capacity:float

    manufacturer:str

    price:float


    class Config:

        from_attributes=True