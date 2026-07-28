<template>

<div class="register-box">


    <h2>汽车租赁系统注册</h2>


    <el-form>


        <el-form-item label="用户名">

            <el-input
                v-model="username"
                placeholder="请输入用户名"
            />

        </el-form-item>



        <el-form-item label="邮箱">

            <el-input
                v-model="email"
                placeholder="请输入邮箱"
            />

        </el-form-item>



        <el-form-item label="密码">

            <el-input
                v-model="password"
                type="password"
                placeholder="请输入密码"
            />

        </el-form-item>



        <el-form-item label="确认密码">

            <el-input
                v-model="confirmPassword"
                type="password"
                placeholder="请再次输入密码"
            />

        </el-form-item>



        <el-button
            type="primary"
            @click="register"
        >

            注册

        </el-button>



        <el-button
            @click="goLogin"
        >

            返回登录

        </el-button>



    </el-form>


</div>


</template>



<script setup>

import {ref} from "vue"

import request from "../api/request"

import {ElMessage} from "element-plus"

import {useRouter} from "vue-router"



const router = useRouter()



const username = ref("")

const email = ref("")

const password = ref("")

const confirmPassword = ref("")




// 注册

function register(){


    if(
        !username.value ||
        !password.value ||
        !email.value
    ){

        ElMessage.warning(
            "用户名、邮箱、密码不能为空"
        )

        return

    }



    if(password.value !== confirmPassword.value){


        ElMessage.error(
            "两次密码不一致"
        )

        return

    }



    request.post(
        "/user/register",
        {

            username:username.value,

            password:password.value,

            email:email.value

        }

    )

    .then(res=>{


        console.log(res.data)


        ElMessage.success(
            "注册成功"
        )


        router.push("/login")


    })

    .catch(err=>{


        console.log(err)


        ElMessage.error(
            "注册失败"
        )


    })


}




// 返回登录

function goLogin(){

    router.push("/login")

}


</script>



<style scoped>


.register-box{


    width:420px;


    padding:40px;


    background:white;


    border-radius:15px;


    box-shadow:
    0 10px 30px rgba(0,0,0,.1);


    margin:100px auto;


}



h2{


    text-align:center;


    margin-bottom:30px;


}


</style>