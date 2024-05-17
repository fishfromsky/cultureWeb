<template>
    <div class="shi-body">
        <div class="circle-body circle-position1">
            <div class="circle">
                <div class="bg bg1"></div>
                <div class="point point-pos1 point-ani-ori" @click="changeSelect(1)"></div>
                <div class="point point-pos2 point-ani-ori" @click="changeSelect(0)"></div>
                <div class="point point-pos3 point-ani-ori" @click="changeSelect(2)"></div>
            </div>
            <div class="nav-title nav-title-pos1" v-if="selected == 0">《勒俄特依》</div>
            <div class="url-list url-list-pos1" v-if="selected == 0" @click="toBook(0)">
                <div class="url-text">点击查看具体内容</div>
                <div class="icon-box">
                    <i class="el-icon-arrow-down" style="font-size: 1.5vh;"></i>
                </div>
            </div>
            <div class="nav-title-horizon nav-title-pos2" v-if="selected == 1">《建国前四川凉山彝族的白银流通》</div>
            <div class="url-list-horizon url-list-pos2" v-if="selected == 1" @click="toBook(1)">
                <div class="url-text-horizon">点击查看具体内容</div>
                <div class="icon-box" style="margin-top: 0.1vh; margin-left: -4%;">
                    <i class="el-icon-arrow-right" style="font-size: 1.5vh;"></i>
                </div>
            </div>
            <div class="nav-title nav-title-pos3" v-if="selected == 2">凉山彝族奴隶社会博物馆</div>
            <div class="url-list url-list-pos3" v-if="selected == 2" @click="toBook(2)">
                <div class="url-text">点击查看具体内容</div>
                <div class="icon-box">
                    <i class="el-icon-arrow-down" style="font-size: 1.5vh;"></i>
                </div>
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
                <div class="point point-pos4 point-ani-ori" @click="changeSelect(5)"></div>
                <div class="point point-pos5 point-ani-ori" @click="changeSelect(4)"></div>
                <div class="point point-pos6 point-ani-ori" @click="changeSelect(6)"></div>
                <div class="bg bg2"></div>
            </div>
            <div class="nav-title nav-title-pos4" v-if="selected == 4">凉山彝族奴隶社会博物馆</div>
            <div class="url-list url-list-pos4" v-if="selected == 4" @click="toBook(3)">
                <div class="url-text">点击查看具体内容</div>
                <div class="icon-box">
                    <i class="el-icon-arrow-down" style="font-size: 1.5vh;"></i>
                </div>
            </div>
            <div class="nav-title-horizon nav-title-pos5" v-if="selected == 5">《探析凉山非物质文化遗产——彝族银饰艺术》</div>
            <div class="url-list-horizon url-list-pos5" v-if="selected == 5" @click="toBook(4)">
                <div class="url-text-horizon">点击查看具体内容</div>
                <div class="icon-box" style="margin-top: 0.1vh; margin-left: -4%;">
                    <i class="el-icon-arrow-right" style="font-size: 1.5vh;"></i>
                </div>
            </div>
            <div class="nav-title nav-title-pos6" v-if="selected == 6">《雷波县志》</div>
            <div class="url-list url-list-pos6" v-if="selected == 6" @click="toBook(5)">
                <div class="url-text">点击查看具体内容</div>
                <div class="icon-box">
                    <i class="el-icon-arrow-down" style="font-size: 1.5vh;"></i>
                </div>
            </div>
        </div>
        <div class="content" style="top: 32vh; left: 64%;">
            {{ content3 }}
        </div>
        <div class="nav-box circle-position3">
            <div class="nav-circle">
                <div class="circle" style="margin-top: 2vh;">
                    <div class="point point-pos2 point-ani-ori" @click="changeSelect(8)"></div>
                    <div class="point point-pos7 point-ani-ori" @click="changeSelect(7)"></div>
                    <div class="bg bg3" style="margin-top: 0.8vh; margin-left: -0.4vh"></div>
                </div>
                <div class="title">[&nbsp至今&nbsp]</div>
            </div>
            <div class="nav-title nav-title-pos7" v-if="selected == 7">《越西县志》</div>
            <div class="url-list url-list-pos7" v-if="selected == 7" @click="toBook(7)">
                <div class="url-text">点击查看具体内容</div>
                <div class="icon-box">
                    <i class="el-icon-arrow-down" style="font-size: 1.5vh;"></i>
                </div>
            </div>
            <div class="nav-title nav-title-pos8" v-if="selected == 8">《布拖县志》</div>
            <div class="url-list url-list-pos8" v-if="selected == 8" @click="toBook(6)">
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
            selected: -1,
            content1: '彝族人民把银作为一种货币进行交易和流通，通过铸造银币或使用现成的银锭来进行交易和存储财富。',
            content2: '鸦片交易让大量白银流入彝区，据有关记录显示，在当时五两鸦片可换一银锭(约十两)。彝族人民逐渐将银子做成器具以及将银用于起义工具中，银饰种类不断丰富。',
            content3: '1956年，凉山彝族的奴隶社会制度废除，凉山进入社会主义社会。银也被广泛应用于彝族生活的各个方面，在彝族人的生活和信仰中有着崇高的地位。'
        }
    },
    methods: {
        toBook(val){
            this.$router.push({path: '/history', query: {id: val}, replace: true})
        },
        changeSelect(val){
            if (this.selected != val){
                this.selected = val
            }
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
.nav-title-pos1{
    position: absolute;
    left: -26%;
    bottom: 2vh;
}
.nav-title-horizon{
    font-size: 2.2vh;
    font-family: DongfangDakai;
    cursor: pointer;
}
.nav-title-pos2{
    position: absolute;
    top: -8vh;
    left: 0;
}
.nav-title-pos3{
    position: absolute;
    right: -40%;
    bottom: 6vh
}
.nav-title-pos4{
    position: absolute;
    left: -1%;
    top: 5vh;
}
.url-list-pos3{
    position: absolute;
    right: -72%;
    bottom: 2vh;
}
.url-list-pos4{
    position: absolute;
    bottom: -2vh;
    left: -20%;
}
.nav-title-pos5{
    position: absolute;
    bottom: -8vh;
    right: 0;
}
.nav-title-pos6{
    position: absolute;
    top: 4vh;
    right: 7%
}
.nav-title-pos7{
    position: absolute;
    right: -21%;
    top: 0
}
.nav-title-pos8{
    position: absolute;
    left: -18%;
    bottom: 0;
}
.url-list-pos5{
    position: absolute;
    bottom: -14vh;
    right: 8%;
}
.url-list-pos6{
    position: absolute;
    right: -12%;
    top: 3vh;
}
.url-list-pos7{
    position: absolute;
    right: -55%;
    top: 0
}
.url-list-pos8{
    position: absolute;
    bottom: 0;
    left: -50%;
}
.url-list-pos1{
    position: absolute;
    bottom: 0;
    left: -60%;
}
.url-list-pos2{
    position: absolute;
    top: -13vh;
    left: 0;
}

.url-list-horizon{
    min-width: 22vh;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    cursor: pointer;
}
.url-text-horizon{
    font-size: 2.2vh;
    border: 1px solid #fff;
    box-sizing: border-box;
    border-radius: 3vh;
    padding: 5px;
    padding-left: 7px;
    padding-right: 7px;
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
    position: absolute;
    top: 0;
    left: 23%
}
.point-pos2{
    position: absolute;
    bottom: 9.5vh;
    left: 0;
}
.point-pos4{
    position: absolute;
    left: 51%;
    bottom: -0.8vh;
}
.point-pos5{
    position: absolute;
    left: 20%;
    top: 10vh;
}
.point-pos6{
    position: absolute;
    top: 10vh;
    right: 20%
}
.point-pos7{
    position: absolute;
    top: 5vh;
    right: 2%;
}
.point-ani-ori{
    animation: animated-border 1s ease-out infinite;
    cursor: pointer;
    background-color: #d09935;
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
    position: absolute;
    right: -1%;
    top: 4.5vh
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
    margin-top: 0.5vh;
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
    cursor: pointer;
}
.url-list{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
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
    font-size: 2.2vh;
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