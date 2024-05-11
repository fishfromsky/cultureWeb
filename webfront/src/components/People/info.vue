<template>
    <div class="info-body">
        <el-row>
            <el-col :span="20">
                <Basic v-if="selected == 0" :infoBody="infoBody"></Basic>
                <Zuopin v-if="selected == 1"></Zuopin>
            </el-col>
            <el-col :span="4">
                <div class="nav">
                    <div class="line"></div>
                    <div class="nav-item" style="margin-bottom: 20vh;" @click="selectNav(0)">
                        <div class="point" :class="[selected == 0? 'point-color-active': 'point-color']"></div>
                        <div class="nav-text" :class="[selected == 0? 'text-color-active': 'text-color']">基本信息</div>
                    </div>
                    <div class="nav-item" style="margin-bottom: 10vh;" @click="selectNav(1)">
                        <div class="point" :class="[selected == 1? 'point-color-active': 'point-color']"></div>
                        <div class="nav-text" :class="[selected == 1? 'text-color-active': 'text-color']">银饰作品</div>
                    </div>
                    <div class="nav-item" @click="selectNav(2)">
                        <div class="point" :class="[selected == 2? 'point-color-active': 'point-color']"></div>
                        <div class="nav-text" :class="[selected == 2? 'text-color-active': 'text-color']">口口相授</div>
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Basic from './components/basic.vue'
import Zuopin from './components/zuopin.vue'
export default{
    name: 'info',
    components: {
        Basic,
        Zuopin
    },
    props: {
        infoid: {
            type: Number,
            required: true
        }
    },
    data(){
        return{
            infoBody: {},
            selected: 0
        }
    },
    methods: {
        selectNav(val){
            if (val != this.selected){
                this.selected = val
            }
        }
    },
    created(){
        let params = {
            'id': this.infoid
        }
        this.$http({
            url: 'api/get_workman_info',
            params: params,
            method: 'GET'
        }).then(res=>{
            this.infoBody = res.data.data
        }).catch(err=>{this.$message.error(err)})
    }
}
</script>

<style scoped>
.nav{
    min-width: 12%;
    height: 30vh;
    position: absolute;
    right: 3%;
}
.line{
    width: 0.2vh;
    height: 100%;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
}
.point{
    width: 2vh;
    height: 2vh;
    border-radius: 50%;
    transition: all .3s;
}
.point-color{
    background-color: #868a94;
}
.point-color-active{
    background-color: #fff;
}
.nav-item{
    position: absolute;
    bottom: -1vh;
    margin-left: -1vh;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    cursor: pointer;
}
.nav-text{
    font-family: DongfangDakai;
    font-size: 2.5vh;
    margin-left: 20px;
    transition: all .3s;
}
.text-color{
    color: #868a94;
}
.text-color-active{
    color: #fff;
}
</style>