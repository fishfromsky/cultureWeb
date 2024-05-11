<template>
    <div class="shi-body">
        <div class="circle-body circle-position1">
            <div class="circle">
                <div class="point point-pos1"></div>
                <div class="point point-pos2"></div>
                <div class="point point-pos3"></div>
                <div class="bg bg1"></div>
            </div>
            <div class="title">[&nbsp公元937年&nbsp]</div>
        </div>
        <div class="content">
            {{ content1 }}
        </div>
        <div class="shi-divider"></div>
        <div class="content" style="left: 38%; top: 6vh;">
            {{ content2 }}
        </div>
        <div class="circle-body circle-position2">
            <div class="title" style="margin-top: -1vh;">[&nbsp1840年&nbsp鸦片战争前后&nbsp]</div>
            <div class="circle" style="margin-top: 2vh;">
                <div class="point point-pos1"></div>
                <div class="point point-pos2"></div>
                <div class="point point-pos3"></div>
                <div class="bg bg2"></div>
            </div>
        </div>
        <div class="content" style="top: 32vh; left: 64%;">
            {{ content3 }}
        </div>
        <div class="nav-box circle-position3">
            <div class="nav-circle">
                <div class="circle" style="margin-top: 2vh;">
                    <div class="point point-pos1"></div>
                    <div @click="toBook" class="point point-pos2 point-ani"></div>
                    <div class="bg bg3" style="margin-top: -9.2vh; margin-left: -0.4vh"></div>
                </div>
                <div class="title">[&nbsp至今&nbsp]</div>
            </div>
            <div class="nav-title" @click="toBook">《岳西县志》</div>
            <div class="url-list" @click="toBook">
                <div class="url-text">点击查看具体内容</div>
                <div class="icon-box">
                    <i class="el-icon-arrow-down" style="font-size: 1.5vh;"></i>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'shi',
    data(){
        return{
            content1: '彝族人民把银作为一种货币进行交易和流通，通过铸造银币或使用现成的银锭来进行交易和存储财富。',
            content2: '鸦片交易让大量白银流入彝区，据有关记录显示，在当时五两鸦片可换一银锭(约十两)。彝族人民逐渐将银子做成器具以及将银用于起义工具中，银饰种类不断丰富。',
            content3: '1956年，凉山彝族的奴隶社会制度废除，凉山进入社会主义社会。银也被广泛应用于彝族生活的各个方面，在彝族人的生活和信仰中有着崇高的地位。'
        }
    },
    methods: {
        toBook(){
            this.$router.push({path: '/history', replace: true})
        }
    }
}
</script>

<style scoped>
.shi-body{
    width: 100%;
    color: #fff;
}
.nav-box{
    position: absolute;
    display: flex;
    flex-direction: row;
}
.nav-circle{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.circle-body{
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.circle-position1{
    top: 10vh;
    left: 13%;
}
.circle-position2{
    top: 44vh;
    left: 35%;
}
.circle-position3{
    top: 8vh;
    left: 65%;
}
.circle {
    width: 18vh;
    height: 18vh;
    border: 1px solid #d09935;
    border-radius: 50%;
}
.title{
    margin-top: 1.5vh;
    font-size: 3vh;
    font-family: DongfangDakai;
}
.content{
    left: 9%;
    position: absolute;
    width: 15%;
    font-size: 2vh;
    text-align: left;
    margin-top: 10vh;
    overflow: hidden;
    word-wrap: break-word;
    word-break: normal;
}
.point {
    width: 2vh;
    height: 2vh;
    border-radius: 50%;
    background-color: #d09935;
}
.point-pos1{
    margin-left: 22%;
    margin-top: 0vh
}
.point-pos2{
    margin-left: 95%;
    margin-top: 6vh;
}
.point-ani{
    background-color: #fff;
    animation: animated-border 1s ease-out infinite;
    cursor: pointer;
}
@keyframes animated-border {
    0% {
        box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.4);
    }
    100% {
        box-shadow: 0 0 0 10px rgba(255, 255, 255, 0);
    }
}

.point-pos3{
    margin-left: 0%;
    margin-top: 2vh;
}
.shi-divider{
    margin-top: 32vh;
    width: 100%;
    height: 10vh;
    background-image: url('../../../../assets/Wu/shi_divider.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
.bg{
    border-radius: 50%;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    margin-left: -0.3vh;
    margin-top: -13.5vh;
    width: 19vh;
    height: 17vh;
}
.bg1{
    background-image: url('../../../../assets/Wu/shi1.png');
}
.bg2{
    background-image: url('../../../../assets/Wu/shi2.png');
}
.bg3{
    background-image: url('../../../../assets/Wu/shi3.png');
}
.nav-title{
    writing-mode: vertical-lr;
    font-size: 2.2vh;
    font-family: DongfangDakai;
    margin-top: -10vh;
    margin-left: 15px;
    cursor: pointer;
}
.url-list{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    margin-left: 15px;
    cursor: pointer;
}
.url-text{
    writing-mode: vertical-lr;
    border: 1px solid #fff;
    box-sizing: border-box;
    padding: 5px;
    border-radius: 3vh;
    padding-top: 10px;
    padding-bottom: 10px;
}
.icon-box{
    width: 2vh;
    height: 2vh;
    background-color: #fff;
    border-radius: 50%;
    color: #0c1429;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: -1vh;
}
</style>