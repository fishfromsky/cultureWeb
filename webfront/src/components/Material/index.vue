<template>
    <div class="material-body">
        <div class="back"></div>
        <div class="left-navi">
            <div class="navi1 navi-position1" @click="change_select(0)">
                <div class="point" :class="[selected == 0? 'change-bg': 'original-bg']"></div>
                <div class="text" style="margin-left: 40px" :class="[selected == 0? 'change-color': 'original-color']">宗教法器</div>
            </div>
            <div class="navi1 navi-position2" style="justify-content: flex-end;" @click="change_select(1)">
                <div class="text" :class="[selected == 1? 'change-color': 'original-color']">兵器武器</div>
                <div class="point" style="margin-left: 40px;" :class="[selected == 1? 'change-bg': 'original-bg']"></div>
            </div>
            <div class="navi1 navi-position3" @click="change_select(2)">
                <div class="point" :class="[selected == 2? 'change-bg': 'original-bg']"></div>
                <div class="text" style="margin-left: 40px;" :class="[selected == 2? 'change-color': 'original-color']">生活用具</div>
            </div>
        </div>
        <Zongjiao v-if="selected == 0"></Zongjiao>
        <Weapon v-if="selected == 1"></Weapon>
        <Life v-if="selected == 2"></Life>
    </div>
</template>

<script>
import Life from './Life/index.vue'
import Zongjiao from './Zongjiao/index.vue'
import Weapon from './Weapon/index.vue'
export default{
    name: 'material',
    components: {
        Life,
        Zongjiao,
        Weapon
    },
    data(){
        return{
            selected: 0
        }
    },
    methods: {
        change_select(val){
            if (val != this.selected){
                this.selected = val
            }
        }
    }
}
</script>

<style scoped>
.material-body{
    width: 100%;
    display: flex;
    flex-direction: row;
    height: 90vh;
    background-color: #131e3a;
    background-image: url('../../assets/main_bg_yin.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    box-sizing: border-box;
    padding: 40px;
}
.back{
    width: 4vh;
    height: 4vh;
    position: absolute;
    top: 1vh;
    left: 1vh;
    background-image: url('../../assets/back.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    z-index: 1000;
    cursor: pointer;
}
.left-navi{
    min-width: 35%;
    height: 85vh;
    margin-left: -6%;
    background-image: url('../../assets/Wu/qi_curve.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 110%;
    margin-top: -40px;
}
.navi1{
    min-width: 100px;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    cursor: pointer;
}
.navi-position1{
    margin-top: 15vh;
    margin-left: 36.5%;
}
.navi-position2{
    margin-top: 21vh;
    margin-right: 44.5%;
}
.navi-position3{
    margin-top: 21vh;
    margin-left: 16.5%;
}
.point{
    width: 2vh;
    height: 2vh;
    border-radius: 50%;
    transition: all .3s;
}
.text{
    font-family: DongfangDakai;
    font-size: 3vh;
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