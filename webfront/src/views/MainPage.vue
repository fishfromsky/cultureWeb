<template>
    <div class="main">
        <NavBar></NavBar>
        <router-view></router-view>
    </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import Cookies from 'js-cookie'
export default{
    name: 'MainPage',
    components: {
        NavBar
    },
    data(){
        return{
           
        }
    },
    methods: {
       
    },
    mounted(){
    }
}
</script>

<style scoped lang="less">
.main{
    min-width: 1150px;
    overflow-x: scroll;
    height: 100vh;
    overflow-x: auto;
    font-family: PuhuiTi;
}
</style>