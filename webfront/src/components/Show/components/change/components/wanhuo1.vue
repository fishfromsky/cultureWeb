<template>
    <div class="wanhuo1-body">
        <audio ref="audioPlayer" :src="audio_src"></audio>
        <div class="voice-item">
            <div v-loading="audioloading" class="voice-logo" @click="startAudio"></div>
            <div class="text">点击开始聆听玩火</div>
        </div>
        <div class="title-list">
            <div class="border-bg border-bg-left" style="margin-right: 10px;"></div>
            <div class="title-text">玩火</div>
            <div class="border-bg border-bg-right" style="margin-left: 10px;"></div>
        </div>
        <div class="focus focus-pos1" @mouseleave="deleteSelect(1)" @mouseover="changeSelect(1)" :class="[selected1 == 0? 'focus-active': 'focus-bg']"></div>
        <div class="focus-text focus-text-pos1" :class="[selected1 == 0? 'focus-text-active': 'focus-text-bg']">银领饰</div>
        <div class="focus focus-pos2" @mouseleave="deleteSelect(2)" @mouseover="changeSelect(2)" :class="[selected2 == 0? 'focus-active': 'focus-bg']"></div>
        <div class="focus-text focus-text-pos2" :class="[selected2 == 0? 'focus-text-active': 'focus-text-bg']">银耳饰</div>
        <div class="focus focus-pos3" @mouseleave="deleteSelect(3)" @mouseover="changeSelect(3)" :class="[selected3 == 0? 'focus-active': 'focus-bg']"></div>
        <div class="focus-text focus-text-pos3" :class="[selected3 == 0? 'focus-text-active': 'focus-text-bg']">哦尔</div>
        <div class="focus focus-pos4" @mouseleave="deleteSelect(4)" @mouseover="changeSelect(4)" :class="[selected4 == 0? 'focus-active': 'focus-bg']"></div>
        <div class="focus-text focus-text-pos4" :class="[selected4 == 0? 'focus-text-active': 'focus-text-bg']">银扣</div>
        <div class="main-content">
            是节日的高潮，热闹而隆重。一大早，村村寨寨的男女老幼穿上节日盛装，成群结队，从四面八方汇聚到火把节集会地，在祭台圣火下，举行各式各样的传统节日活动。
        </div>
        <div class="click-text">
            <div class="text-box" @click="nextPage">点击继续</div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'wanhuo1',
    data(){
        return{
            audioloading: false,
            selected1: -1,
            selected2: -1,
            selected3: -1,
            selected4: -1,
            audio_src: 'http://120.27.144.206:8000/static/voice/玩火1.m4a',
        }
    },
    methods: {
        startAudio(){
            this.$refs.audioPlayer.play()
        },
        nextPage(){
            this.$emit('nextpage', [4, 2])
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
            else{
                this.selected4 = 0
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
            else {
                this.selected4 = -1
            }
        }
    }
}
</script>

<style scoped>
.wanhuo1-body{
    min-width: 1150px;
    width: 100%;
    overflow-x: scroll;
    overflow-x: auto;
    position: fixed;
    top: 10vh;
    left: 0;
    height: 90vh;
    background-image: url('../../../../../assets/chang/wanhuo1.png');
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
    bottom: 20vh;
    left: 7%;
}
.focus-text{
    font-size: 2vh;
    color: #fff;
    transition: all .5s;
}
.focus-text-pos1{
    position: absolute;
    bottom: 23vh;
    left: 14%;
}
.focus-text-bg{
    opacity: 0;
}
.focus-text-active{
    opacity: 1;
}
.focus-pos2{
    position: absolute;
    bottom: 32vh;
    left: 29%;
}
.focus-text-pos2{
    position: absolute;
    bottom: 35vh;
    left: 36%;
}
.focus-pos3{
    position: absolute;
    right: 27%;
    top: 40vh;
}
.focus-text-pos3{
    position: absolute;
    right: 25%;
    top: 48vh;
}
.focus-pos4{
    position: absolute;
    bottom: 20vh;
    right: 4%;
}
.focus-text-pos4{
    position: absolute;
    bottom: 21vh;
    right: 11%;
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