<template>

<div class="login-card">

    <h2>汽车租赁系统登录</h2>


    <el-form>

        <el-form-item label="用户名">

            <el-input 
                v-model="username"
                placeholder="请输入用户名"
            />

        </el-form-item>



        <el-form-item label="密码">

            <el-input

                v-model="password"

                type="password"

                placeholder="请输入密码"

            />

        </el-form-item>



        <el-button 
            type="primary"
            @click="login"
        >
            登录
        </el-button>


        <el-button 
            @click="$router.push('/register')"
        >
            注册
        </el-button>


    </el-form>


</div>


</template>



<script setup>

import {ref} from "vue"

import request from "../api/request"

import {ElMessage} from "element-plus"

import {useRouter} from "vue-router"



const router=useRouter()



const username=ref("")

const password=ref("")



function login(){


    request.post("/user/login",{

        username:username.value,

        password:password.value

    })

    .then(res=>{


        console.log(res.data)


        ElMessage.success("登录成功")


        router.push("/cars")


    })

    .catch(err=>{


        console.log(err)


        ElMessage.error("登录失败")


    })


}


</script>



<style scoped>

.login-box{

    width:400px;

    margin:100px auto;

}


h2{

    text-align:center;

    margin-bottom:30px;

}


</style>