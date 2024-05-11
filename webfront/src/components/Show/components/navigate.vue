<template>
    <div class="navigate-body">
        <div class="logo-box" v-for="(item, idx) in navigator" :key="idx" @click="handleClick(idx)">
            <div class="logo" :class="[navigator[idx].status? navigator[idx].class_list[0]: navigator[idx].class_list[1]]"></div>
            <div class="logo-text" :class="[navigator[idx].status? navigator[idx].class_list[2]: navigator[idx].class_list[3]]">{{ item.name }}</div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'navigate',
    data(){
        return{
            selected: 0,
            navigator: [
                {status: 1, class_list: ['wen-active', 'wen-no-active', 'logo-text-active', 'logo-text-noactive'], name: '纹'},
                {status: 0, class_list: ['wu-active', 'wu-no-active', 'logo-text-active', 'logo-text-noactive'], name: '物'},
                {status: 0, class_list: ['ji-active', 'ji-no-active', 'logo-text-active', 'logo-text-noactive'], name: '技'},
                {status: 0, class_list: ['shi-active', 'shi-no-active', 'logo-text-active', 'logo-text-noactive'], name: '史'},
                {status: 0, class_list: ['chang-active', 'chang-no-active', 'logo-text-active', 'logo-text-noactive'], name: '场'}
            ]
        }
    },
    methods: {
        handleClick(idx){
            if (idx != this.selected){
                this.navigator[this.selected].status = 0
                this.navigator[idx].status = 1
                this.selected = idx
                this.$emit('navigator', idx)
            }
        }
    }
}
</script>

<style scoped>
.navigate-body{
    margin-top: 18vh;
    width: 100%;
}
.logo-box{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}
.logo{
    width: 6vh;
    height: 6vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 150% 140%;
    cursor: pointer;
    transition: all .3s;
}
.logo-text{
    font-family: DongfangDakai;
    font-size: 4vh;
    margin-left: 20px;
    transition: all .3s;
}
.logo-box:hover{
    .logo{
        transform: scale(1.2);
    }
}
.logo-text-noactive{
    color: #868a94;
}
.logo-text-active{
    color: #fff
}
.wen-active{
    background-image: url('../../../assets/ji_navi1.png');
}
.wu-active{
    background-image: url('../../../assets/ji_navi2.png');
}
.ji-active{
    background-image: url('../../../assets/ji_navi3.png');
}
.shi-active{
    background-image: url('../../../assets/ji_navi4.png');
}
.chang-active{
    background-image: url('../../../assets/ji_navi5.png')
}
.wen-no-active{
    background-image: url('../../../assets/ji_navi1_no_active.png');
}
.wu-no-active{
    background-image: url('../../../assets/ji_navi2_no_active.png');
}
.ji-no-active{
    background-image: url('../../../assets/ji_navi3_no_active.png');
}
.shi-no-active{
    background-image: url('../../../assets/ji_navi4_no_active.png')
}
.chang-no-active{
    background-image: url('../../../assets/ji_navi5_no_active.png');
}
</style>