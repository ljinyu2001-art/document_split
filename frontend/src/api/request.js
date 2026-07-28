import axios from "axios"


const request = axios.create({

    // FastAPI地址
    baseURL:"http://127.0.0.1:8000",

    timeout:5000

})


export default request