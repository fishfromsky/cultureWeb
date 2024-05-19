<template>
    <div class="child-body">
        <div class="img-box"></div>
    </div>
</template>

<script>
export default{
    name: 'decorate_child',
    data(){
        return{
            
        }
    }
}
</script>

<style scoped>
.child-body{
    
}
.img-box{
    width: 100%;
    height: 80vh;
    background-image: url('../../../assets/Wu/child.png');
    background-position: -24vh center;
    background-repeat: no-repeat;
    background-size: 120% 110%;
}
</style>