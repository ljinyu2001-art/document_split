<template>


<div class="car-box">


    <h2>
        汽车租赁车辆查询
    </h2>



    <!-- 搜索区域 -->

    <div class="search-box">


        <el-input

            v-model="keyword"

            placeholder="请输入搜索内容"

            clearable

            style="width:250px"

        />



        <el-select

            v-model="filterType"

            placeholder="筛选条件"

            style="width:150px"

        >


            <el-option

                label="车型"

                value="car_type"

            />



            <el-option

                label="厂家"

                value="manufacturer"

            />



            <el-option

                label="状态"

                value="status"

            />


        </el-select>



        <el-button

            type="primary"

            @click="search"

        >

            搜索

        </el-button>



        <el-button

            @click="reset"

        >

            重置

        </el-button>



    </div>





    <!-- 车辆表格 -->


    <el-table

        :data="showCars"

        border

        style="width:100%"

    >


        <el-table-column

            prop="car_type"

            label="车型"

        />



        <el-table-column

            prop="capacity"

            label="排量"

        />



        <el-table-column

            prop="manufacturer"

            label="厂家"

        />



        <el-table-column

            prop="produce_date"

            label="生产日期"

        />



        <el-table-column

            prop="price"

            label="价格"

        />



        <el-table-column

            prop="status"

            label="状态"

        />



        <el-table-column

            label="操作"

        >


            <template #default="scope">


                <el-button

                    type="primary"

                    :disabled="
                    scope.row.status==='已预约'
                    "

                    @click="
                    reserve(scope.row.car_id)
                    "

                >


                    {{
                        scope.row.status==="已预约"
                        ?
                        "已预约"
                        :
                        "预约"
                    }}


                </el-button>


            </template>


        </el-table-column>


    </el-table>



</div>


</template>





<script setup>


import {
    ref,
    onMounted,
    computed
} from "vue"



import request from "../api/request"


import {
    ElMessage
} from "element-plus"




// 所有车辆

const cars = ref([])



// 搜索关键词

const keyword = ref("")


// 筛选字段

const filterType = ref("")





// 查询车辆

function getCars(){


    request.get("/car/list")

    .then(res=>{


        cars.value = res.data


    })


}




// 计算显示数据

const showCars = computed(()=>{


    if(
        !keyword.value ||
        !filterType.value
    ){

        return cars.value

    }



    return cars.value.filter(car=>{


        return String(
            car[filterType.value]
        )

        .includes(
            keyword.value
        )


    })


})





// 搜索

function search(){


    if(!filterType.value){


        ElMessage.warning(
            "请选择筛选条件"
        )


    }


}





// 重置

function reset(){


    keyword.value=""


    filterType.value=""


}




// 预约

function reserve(id){



    request.put(
        `/car/reserve/${id}`
    )

    .then(res=>{


        ElMessage.success(
            res.data.msg
        )


        getCars()


    })


}




// 页面加载

onMounted(()=>{


    getCars()


})



</script>





<style scoped>


.car-box{


    width:90%;


    margin:50px auto;


    padding:30px;


    background:white;


    border-radius:15px;


    box-shadow:
    0 5px 20px rgba(0,0,0,.08);


}



h2{


    text-align:center;


    margin-bottom:30px;


}



.search-box{


    display:flex;


    gap:15px;


    margin-bottom:25px;


}



</style>