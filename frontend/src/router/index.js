import { createRouter, createWebHistory } from "vue-router"

import Login from "../views/Login.vue"
import Register from "../views/Register.vue"
import CarList from "../views/CarList.vue"


const router = createRouter({

    history:createWebHistory(),

    routes:[

        {
            path:"/",
            redirect:"/login"
        },

        {
            path:"/login",
            component:Login
        },

        {
            path:"/register",
            component:Register
        },

        {
            path:"/cars",
            component:CarList
        }

    ]

})


export default router