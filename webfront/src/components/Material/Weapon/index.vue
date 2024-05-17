<template>
    <div class="life-body">
        <div class="title position1" @click="toDetail(0)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银护肘</div>
        </div>
        <div class="title position3" @click="toDetail(1)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银匕首</div>
        </div>
        <div class="title position9" @click="toDetail(2)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银刀</div>
        </div>
        <div class="title position10" @click="toDetail(3)">
            <div class="point" :class="[selected == 0? 'background-bg-active': 'background-bg-no-active']"></div>
            <div class="text" :class="[selected == 0? 'text-active': 'text-no-active']">银箭筒</div>
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
            this.$router.push({path: '/material/detail', query: {id: val, category: '1'}, replace: true})
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