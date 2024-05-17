<template>
    <div class="play-body">
        <div class="back" @click="backPage"></div>
        <div class="text-box">{{ content }}</div>
        <div class="colored-text">
            <div >火把节历时三天三夜，分为</div>
            <div style="color: red;">祭火、玩火、送火</div>
            <div>三个阶段</div>
        </div>
        <div class="nav-list">
            <div class="nav-item1" @click="selectedItem(1)">
                <div class="nav-text">祭火</div>
            </div>
            <div class="dashed-line"></div>
            <div class="nav-item1" @click="selectedItem(2)">
                <div class="nav-text">玩火</div>
            </div>
            <div class="dashed-line"></div>
            <div class="nav-item1" @click="selectedItem(3)">
                <div class="nav-text">送火</div>
            </div>
            <div id="person" class="person person-pos1"></div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'play_fire',
    props: {
        selected: {
            type: Number,
            required: true,
            default: 1
        }
    },
    data(){
        return{
            content: '凉山彝族火把节起源于彝族对火的崇拜，彝族先民手持火把绕行大山，将火把、松明子插于田间，意在用火驱虫除害，保护庄稼，祈求风调雨顺。青年男女围绕火堆弹唱、跳舞，彻夜不息。',
            
        }
    },
    methods: {
        backPage(){
            this.$emit('back', 0)
        },
        selectedItem(val){
            var box = document.getElementById('person')
            if (this.selected == 1 & val == 2){
                box.classList.add('move')
            }
            else if (this.selected == 2 && val == 3){
                box.classList.add('move')
            }
            else if (this.selected == 1 && val == 3){
                box.classList.add('move1')
            }
            else if (this.selected == 2 && val == 1){
                box.classList.add('move-reverse')
            }
            else if (this.selected == 3 && val == 2){
                box.classList.add('move-reverse')
            }
            else if (this.selected == 3 && val == 1){
                box.classList.add('move-reverse1')
            }
            setTimeout(() => {
                if (val == 1){
                    this.$emit('toPage', [1, 1])
                }
                else if (val == 2){
                    this.$emit('toPage', [3, 2])
                }
                else{
                    this.$emit('toPage', [5, 3])
                }
            }, 1500);
        }
    },
    mounted(){
        var box = document.getElementById('person')
        if (this.selected == 1){
            if (box.classList.contains('person-pos2')){
                box.classList.remove('person-pos2')
            }
            if (box.classList.contains('person-pos3')){
                box.classList.remove('person-pos3')
            }
            box.classList.add('person-pos1')
        }
        else if (this.selected == 2){
            if (box.classList.contains('person-pos1')){
                box.classList.remove('person-pos1')
            }
            if (box.classList.contains('person-pos3')){
                box.classList.remove('person-pos3')
            }
            box.classList.add('person-pos2')
        }
        else{
            if (box.classList.contains('person-pos1')){
                box.classList.remove('person-pos1')
            }
            if (box.classList.contains('person-pos2')){
                box.classList.remove('person-pos2')
            }
            box.classList.add('person-pos3')
        }
    }
}
</script>

<style scoped>
.play-body{
    min-width: 1150px;
    position: fixed;
    top: 10vh;
    left: 0;
    height: 90vh;
    background-image: url('../../../../assets/chang/wanhuo_bg.png');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: 100% 100%;
    box-sizing: border-box;
    padding: 60px;
    padding-top: 13vh;
}
.back{
    width: 5vh;
    height: 5vh;
    background-image: url('../../../../assets/back.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    position: absolute;
    top: 2vh;
    left: 2%;
    cursor: pointer;
}
.text-box{
    width: 100%;
    text-align: center;
    color: #fff;
    font-family: DongfangDakai;
    font-size: 3vh;
    line-height: 5vh;
}
.colored-text{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    color: #fff;
    font-family: DongfangDakai;
    font-size: 3vh;
}
.nav-list{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-top: 23vh;
}
.nav-item1{
    cursor: pointer;
    width: 16vh;
    height: 16vh;
    border-radius: 50%;
    border: 1.5px dashed #aaa;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.dashed-line{
    width: 25vh;
    color: #aaa;
    height: 0;
    border-bottom: 1.5px dashed #aaa;
}
.nav-text{
    font-size: 5vh;
    color: #fff;
    font-family: DongfangDakai;
}
.person{
    position: absolute;
    width: 20vh;
    height: 20vh;
    background-image: url('../.././../../assets/chang/person.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 120%;
    transition: all 1s ease-out;
}
.person-pos1{
    left: 28%;
}
.person-pos2{
    left: 52%;
}
.person-pos3{
    right: 14%;
}
.move{
    transform: translateX(42vh);
}
.move1{
    transform: translateX(85vh);
}
.move-reverse{
    transform: translateX(-42vh);
}
.move-reverse1{
    transform: translateX(-85vh);
}
</style>