<template>
    <div class="wanhuo2-body">
        <audio ref="audioPlayer" :src="audio_src"></audio>
        <div class="voice-item">
            <div v-loading="audioloading" class="voice-logo" @click="startAudio"></div>
            <div class="text">点击开始唱歌跳舞</div>
        </div>
        <div class="title-list">
            <div class="border-bg border-bg-left" style="margin-right: 10px;"></div>
            <div class="title-text">玩火</div>
            <div class="border-bg border-bg-right" style="margin-left: 10px;"></div>
        </div>
        <div class="focus focus-pos1" @mouseleave="deleteSelect(1)" @mouseover="changeSelect(1)" :class="[selected1 == 0? 'focus-active': 'focus-bg']"></div>
        <div class="focus-text focus-text-pos1" :class="[selected1 == 0? 'focus-text-active': 'focus-text-bg']">银扣</div>
        <div class="focus focus-pos2" @mouseleave="deleteSelect(2)" @mouseover="changeSelect(2)" :class="[selected2 == 0? 'focus-active': 'focus-bg']"></div>
        <div class="focus-text focus-text-pos2" :class="[selected2 == 0? 'focus-text-active': 'focus-text-bg']">银头饰</div>
        <div class="focus focus-pos3" @mouseleave="deleteSelect(3)" @mouseover="changeSelect(3)" :class="[selected3 == 0? 'focus-active': 'focus-bg']"></div>
        <div class="focus-text focus-text-pos3" :class="[selected3 == 0? 'focus-text-active': 'focus-text-bg']">银耳饰</div>
        <div class="focus focus-pos4" @mouseleave="deleteSelect(4)" @mouseover="changeSelect(4)" :class="[selected4 == 0? 'focus-active': 'focus-bg']"></div>
        <div class="focus-text focus-text-pos4" :class="[selected4 == 0? 'focus-text-active': 'focus-text-bg']">银领饰</div>
        <div class="focus focus-pos5" @mouseleave="deleteSelect(5)" @mouseover="changeSelect(5)" :class="[selected5 == 0? 'focus-active': 'focus-bg']"></div>
        <div class="focus-text focus-text-pos5" :class="[selected5 == 0? 'focus-text-active': 'focus-text-bg']">银手饰</div>
        <div class="focus focus-pos6" @mouseleave="deleteSelect(6)" @mouseover="changeSelect(6)" :class="[selected6 == 0? 'focus-active': 'focus-bg']"></div>
        <div class="focus-text focus-text-pos6" :class="[selected6 == 0? 'focus-text-active': 'focus-text-bg']">银胸饰</div>
        <div class="main-content">
            人们将手中的火把聚在一起，形成一堆堆巨大的篝火，并围在篝火四周尽情地歌唱、舞蹈。
        </div>
        <div class="click-text">
            <div class="text-box" @click="nextPage">点击继续</div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'wanhuo2',
    data(){
        return{
            audioloading: false,
            selected1: -1,
            selected2: -1,
            selected3: -1,
            selected4: -1,
            selected5: -1,
            selected6: -1,
            audio_src: 'http://120.27.144.206:8000/static/voice/玩火2.m4a',
        }
    },
    methods: {
        startAudio(){
            this.$refs.audioPlayer.play()
        },
        nextPage(){
            this.$emit('nextpage', [0, 2])
        },
        changeSelect(val){
            if (val == 1){
                this.selected1 = 0
            }
            else if (val == 2){
                this.selected2 = 0
            }
            else if (val == 3){
                this.selected3 = 0
            }
            else if (val == 4){
                this.selected4 = 0
            }
            else if (val == 5){
                this.selected5 = 0
            }
            else{
                this.selected6 = 0
            }
        },
        deleteSelect(val){
            if (val == 1){
                this.selected1 = -1
            }
            else if (val == 2){
                this.selected2 = -1
            }
            else if (val == 3){
                this.selected3 = -1
            }
            else if (val == 4) {
                this.selected4 = -1
            }
            else if (val == 5){
                this.selected5 = -1
            }
            else{
                this.selected6 = -1
            }
        }
    }
}
</script>

<style scoped>
.wanhuo2-body{
    min-width: 1150px;
    width: 100%;
    overflow-x: scroll;
    overflow-x: auto;
    position: fixed;
    top: 10vh;
    left: 0;
    height: 90vh;
    background-image: url('../../../../../assets/chang/wanhuo2.png');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: 100% 100%;
    box-sizing: border-box;
    z-index: 1;
}
.voice-item{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 2vh;
    right: 5%;
    z-index: 100;
}
.voice-logo{
    cursor: pointer;
    width: 15vh;
    height: 15vh;
    background-image: url('../../../../../assets/chang/voice.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
.text{
    color: #fff;
    font-size: 2.2vh;
}
.voice-item /deep/ .el-loading-mask{
    background-color: transparent;
}
.voice- /deep/ .el-loading-spinner .path{
    stroke: #fff;
}
.title-list{
    margin-top: 5vh;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    z-index: 100;
}
.border-bg{
    width: 5vh;
    height: 5vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    transition: all .3s;
}
.border-bg-left{
    background-image: url('../../../../../assets/chang/text_border_left.png');
}
.border-bg-right{
    background-image: url('../../../../../assets/chang/text_border_right.png');
}
.title-text{
    color: #fff;
    font-size: 4vh;
    font-family: DongfangDakai;
}
.focus{
    width: 13vh;
    height: 13vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    cursor: pointer;
    transition: all .5s;
    z-index: 100
}
.focus-bg{
    background-image: url('../../../../../assets/chang/circle.png');
}
.focus-active{
    background-image: url('../../../../../assets/chang/circle_active.png');
}
.focus-pos1{
    position: absolute;
    bottom: 41vh;
    left: 6%;
}
.focus-text{
    font-size: 2vh;
    color: #fff;
    transition: all .5s;
}
.focus-text-pos1{
    position: absolute;
    bottom: 43vh;
    left: 13%;
}
.focus-text-bg{
    opacity: 0;
}
.focus-text-active{
    opacity: 1;
}
.focus-pos2{
    position: absolute;
    top: 9vh;
    left: 10%;
}
.focus-text-pos2{
    position: absolute;
    top: 16vh;
    left: 17%;
}
.focus-pos3{
    position: absolute;
    left: 31%;
    top: 16vh;
}
.focus-text-pos3{
    position: absolute;
    left: 38%;
    top: 23vh;
}
.focus-pos4{
    position: absolute;
    bottom: 42vh;
    right: 27%;
}
.focus-text-pos4{
    position: absolute;
    bottom: 45vh;
    right: 25%;
}
.focus-pos5{
    position: absolute;
    top: 40vh;
    right: 17%;
}
.focus-text-pos5{
    position: absolute;
    top: 48vh;
    right: 15%;
}
.focus-pos6{
    position: absolute;
    bottom: 21vh;
    right: 3%
}
.focus-text-pos6{
    position: absolute;
    bottom: 24vh;
    right: 10%;
}
.click-text{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    position: absolute;
    bottom: 4vh;
}
.text-box{
    color: #fff;
    font-size: 3.5vh;
    font-family: DongfangDakai;
    cursor: pointer;
    transition: all .3s;
}
.text-box:hover{
    transform: scale(1.1);
}
.main-content{
    width: 80%;
    left: 10%;
    text-align: center;
    position: absolute;
    top: 35vh;
    color: #fff;
    font-family: DongfangDakai;
    font-size: 3.5vh;
}
</style>