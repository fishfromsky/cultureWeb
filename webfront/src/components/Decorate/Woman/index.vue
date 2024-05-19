<template>
    <div class="woman-body">
        <div class="img-box">
        </div>
    </div>
</template>

<script>
export default{
    name: 'decorate_woman',
    data(){
        return{
            
        }
    }
}
</script>

<style scoped>
.woman-body{
    width: 100%;
    box-sizing: border-box;
}
.img-box{
    width: 100%;
    height: 80vh;
    background-image: url('../../../assets/Wu/woman.png');
    background-position: -24vh center;
    background-repeat: no-repeat;
    background-size: 120% 110%;
    text-align: right;
    box-sizing: border-box;
}
.text{
    color: #fff;
    font-size: 2vh;
}
.text-pos1{
    position: absolute;
    right: 21%;
    top: 27.5vh
}
</style>