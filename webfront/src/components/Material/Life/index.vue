<template>
    <div class="life-body">
        <div class="title position1" @click="toDetail(0)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银壶</div>
        </div>
        <div class="title position2" @click="toDetail(1)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银筷</div>
        </div>
        <div class="title position3" @click="toDetail(2)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银马铃</div>
        </div>
        <div class="title position4" @click="toDetail(3)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银烟杆</div>
        </div>
        <div class="title position5" @click="toDetail(4)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银喇叭</div>
        </div>
        <div class="title position6" @click="toDetail(5)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银杯</div>
        </div>
        <div class="title position7" @click="toDetail(6)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银碗</div>
        </div>
        <div class="title position8" @click="toDetail(7)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银马鞍</div>
        </div>
        <div class="title position9" @click="toDetail(8)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银摆件</div>
        </div>
        <div class="title position10" @click="toDetail(9)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银纺轮</div>
        </div>
        <div class="title position11" @click="toDetail(10)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银盘</div>
        </div>
        <div class="title position12" @click="toDetail(11)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银耳花</div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'material',
    data(){
        return{
            selected: -1
        }
    },
    methods: {
        toDetail(val){
            this.$router.push({path: '/material/detail3', query: {id: val}, replace: true})
        }
    }
}
</script>

<style scoped>
.life-body{
    width: 100%;
    text-align: left;
}
.title{
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all .3s
}
.title:hover{
    transform: scale(1.2);
    .text{
        color: #fff;
    }
    .point{
        background-color: #fff;
    }
}
.point{
    width: 2vh;
    height: 2vh;
    border-radius: 50%;
}
.background-bg-no-active{
    background-color: #888;
}
.background-bg-active{
    background-color: #fff;
}
.text{
    margin-top: 10px;
    font-size: 3vh;
    font-family: DongfangDakai;
    writing-mode: vertical-lr;
}
.text-no-active{
    color: #888;
}
.text-active{
    color: #fff;
}
.position1{
    margin-left: 4%;
    margin-top: 8vh;
}
.position2{
    margin-left: 16%;
    margin-top: 5vh
}
.position3{
    margin-left: 29%;
    margin-top: 10vh
}
.position4{
    margin-left: 42%;
    margin-top: 13vh
}
.position5{
    margin-top: 3vh;
    margin-left: 53%
}
.position6{
    margin-top: 32vh;
    margin-left: -2%;
}
.position7{
    margin-top: 33vh;
    margin-left: 16%
}
.position8{
    margin-top: 38vh;
    margin-left: 31%
}
.position9{
    margin-top: 36vh;
    margin-left: 49%
}
.position10{
    margin-top: 54vh;
    margin-left: 7%
}
.position11{
    margin-top: 57vh;
    margin-left: 22%
}
.position12{
    margin-top: 58vh;
    margin-left: 41%;
}
</style>