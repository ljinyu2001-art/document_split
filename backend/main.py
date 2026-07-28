from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routers import user,car



app=FastAPI(

    title="汽车租赁查询系统"

)



# 允许Vue访问

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_methods=["*"],

    allow_headers=["*"],

)



app.include_router(
    user.router
)


app.include_router(
    car.router
)



@app.get("/")

def root():

    return {

        "msg":"汽车租赁系统启动成功"

    }