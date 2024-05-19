<template>
    <div class="jihuo2-body">
        <audio ref="audioPlayer" :src="audio_src"></audio>
        <div class="voice-item">
            <div v-loading="audioloading" class="voice-logo" @click="startAudio"></div>
            <div class="text">点击暂停聆听诵经祭火</div>
        </div>
        <div class="title-list">
            <div class="border-bg border-bg-left" style="margin-right: 10px;"></div>
            <div class="title-text">祭火</div>
            <div class="border-bg border-bg-right" style="margin-left: 10px;"></div>
        </div>
        <div class="main-content">
            众人从毕摩手里接过用蒿草扎成的火把，游走于田边地角，效仿阿什嫫以火驱虫的传说。
        </div>
        <div class="click-text">
            <div class="text-box" @click="nextPage">点击继续</div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'jihuo2',
    data(){
        return{
            audio_src: 'http://120.27.144.206:8000/static/voice/祭火.m4a',
            audioloading: false,
            selected1: -1,
            selected2: -1,
            selected3: -1,
            selected4: -1,
        }
    },
    methods: {
        startAudio(){
            this.$parent.$parent.$parent.$parent.$parent.$parent.$refs.audioPlayer.pause();
        },
        nextPage(){
            this.$emit('nextpage', [0, 1])
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
        }
    }
}
</script>

<style scoped>
.jihuo2-body{
    min-width: 1150px;
    width: 100%;
    overflow-x: scroll;
    overflow-x: auto;
    position: fixed;
    top: 10vh;
    left: 0;
    height: 90vh;
    background-image: url('../../../../../assets/chang/jihuo2.png');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: 100% 100%;
    box-sizing: border-box;
}
.voice-item{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 2vh;
    right: 5%;
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
.click-text{
    width: 100%;
    text-align: center;
    color: #fff;
    font-size: 2vh;
    position: absolute;
    bottom: 4vh;
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
    margin-left: 10%;
    text-align: center;
    position: absolute;
    top: 35vh;
    color: #fff;
    font-size: 3.5vh;
    font-family: DongfangDakai;
}
</style>