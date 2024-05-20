<template>
    <div class="main">
        <div v-if="selected==0">
            <NavBar></NavBar>
            <router-view></router-view>
        </div>
        <div v-else class="video-container">
            <video autoplay loop style="width: 100%; height: 100%; object-fit: fill;">
                <source src="../assets/introduction.mp4" type="video/mp4">
            </video>
            <div class="mask">
                <div class="mask-text" @click="selected=0">点击跳过</div>
            </div>
        </div>
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
           selected: 1
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
.video-container{
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
}
.mask{
    width: 100%;
    height: 20%;
    position: absolute;
    left: 0;
    bottom: 0;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    background-image: linear-gradient(to top, rgba(0, 0, 0, 0.7), transparent);
}
.mask-text{
    color: #fff;
    font-family: DongfangDakai;
    font-size: 3vh;
    cursor: pointer;
}
</style>