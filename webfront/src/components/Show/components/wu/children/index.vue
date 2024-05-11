<template>
    <div class="child-body">
        <div class="logo-box" @click="redirect_decorate">
            <div class="logo shi-logo"></div>
            <div class="logo-text">饰</div>
        </div>
        <div class="logo-box" @click="redirect_object">
            <div class="logo qi-logo"></div>
            <div class="logo-text">器</div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'child',
    data(){
        return{

        }
    },
    methods: {
        redirect_decorate(){
            this.$emit('redirect', 0)
        },
        redirect_object(){
            this.$emit('redirect', 1)
        }
    }
}
</script>

<style scoped>
.child-body{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
.logo-box{
    margin-top: 15vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}
.logo{
    width: 35vh;
    height: 35vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 110% 100%;
}
.shi-logo{
    background-image: url('../../../../../assets/Wu/shi.png');
}
.qi-logo{
    background-image: url('../../../../../assets/Wu/qi.png');
}
.logo-text{
    margin-top: 4vh;
    font-family: DongfangDakai;
    font-size: 5vh;
}
</style>