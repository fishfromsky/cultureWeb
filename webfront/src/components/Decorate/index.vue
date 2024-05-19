<template>
    <div class="decorate-body">
        <div class="left-navi">
            <div class="navi1 navi-position1" @click="select_id(0)">
                <div class="point" :class="[selected == 0? 'change-bg': 'original-bg']"></div>
                <div class="text" :class="[selected == 0? 'change-color': 'original-color']">
                    彝族小孩
                </div>
            </div>
            <div class="navi1 navi-position2" @click="select_id(1)">
                <div class="point" :class="[selected == 1? 'change-bg': 'original-bg']"></div>
                <div class="text" :class="[selected == 1? 'change-color': 'original-color']">彝族男子</div>
            </div>
            <div class="navi1 navi-position3" @click="select_id(2)">
                <div class="point" :class="[selected == 2? 'change-bg': 'original-bg']"></div>
                <div class="text" :class="[selected == 2? 'change-color': 'original-color']">彝族女子</div>
            </div>
        </div>
        <div class="main-content">
            <Child v-if="selected == 0"></Child>
            <Man v-if="selected == 1"></Man>
            <Woman v-if="selected == 2"></Woman>
        </div>
    </div>
</template>

<script>
import Child from './Child/index.vue'
import Man from './Man/index.vue'
import Woman from './Woman/index.vue'
export default{
    name: 'decorate',
    components: {
        Child,
        Man,
        Woman
    },
    data(){
        return{
            selected: 0
        }
    },
    methods: {
        select_id(val){
            if (val != this.selected){
                this.selected = val
            }
        }
    }
}
</script>

<style scoped>
.decorate-body{
    width: 100%;
    height: 90vh;
    background-color: #131e3a;
    background-image: url('../../assets/main_bg_yin.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    box-sizing: border-box;
    padding: 40px;
    display: flex;
    flex-direction: row;
}
.left-navi{
    margin-top: -40px;
    margin-left: -8%;
    width: 37%;
    height: 85vh;
    background-image: url('../../assets/Wu/shi_curve.png');
    background-position: center center;
    background-size: 100% 110%;
    background-repeat: no-repeat;
}
.main-content{
    width: 100%;
    min-height: 80vh;
    box-sizing: border-box;
}
.navi1{
    min-width: 100px;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    height: 20vh;
    cursor: pointer;
}
.navi-position1{
    margin-left: 71.5%;
    margin-top: 6vh
}
.navi-position2{
    margin-left: 34%;
    margin-top: 4vh;
}
.navi-position3{
    margin-left: 43%;
    margin-top: 5vh;
}
.point{
    width: 2vh;
    height: 2vh;
    border-radius: 50%;
    transition: all .3s;
}
.text{
    writing-mode: vertical-rl;
    font-family: DongfangDakai;
    font-size: 3vh;
    margin-left: 40px;
    transition: all .3s;
}
.original-color{
    color: #888;
}
.change-color{
    color: #fff;
}
.original-bg{
    background-color: #888;
}
.change-bg{
    background-color: #fff;
}
</style>