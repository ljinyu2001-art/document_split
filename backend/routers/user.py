from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UserCreate,UserLogin


router = APIRouter(
    prefix="/user",
    tags=["用户"]
)



# 注册

@router.post("/register")

def register(
    user:UserCreate,
    db:Session=Depends(get_db)
):


    db_user=User(

        username=user.username,

        password=user.password,

        email=user.email
    )


    db.add(db_user)

    db.commit()

    db.refresh(db_user)


    return {

        "msg":"注册成功",

        "user_id":db_user.card_id
    }





# 登录

@router.post("/login")

def login(

    user:UserLogin,

    db:Session=Depends(get_db)

):


    result=db.query(User).filter(

        User.username==user.username,

        User.password==user.password

    ).first()



    if result:


        return {

            "msg":"登录成功",

            "username":result.username
        }


    else:


        return {

            "msg":"用户名或密码错误"
        }