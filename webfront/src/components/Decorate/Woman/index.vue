<template>
    <div class="woman-body">
        <div class="img-box"></div>
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
}
.img-box{
    width: 100%;
    height: 80vh;
    background-image: url('../../../assets/Wu/woman.png');
    background-position: -24vh center;
    background-repeat: no-repeat;
    background-size: 110% 110%;
}
</style>