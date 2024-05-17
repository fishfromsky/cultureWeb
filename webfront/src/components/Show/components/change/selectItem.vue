<template>
    <div class="menu-body">
        <div class="item-list">
            <div class="item-box-container" @click="handle_click">
                <div class="item-box item-bg"></div>
                <div class="item-text">火把节</div>
            </div>
            <div class="item-box-container">
                <div class="item-box item-bg-text">
                    <div class="item-text">敬请期待</div>
                </div>
                <div class="item-text">敬请期待</div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'selectItem',
    data(){
        return{

        }
    },
    methods: {
        handle_click(){
            this.$emit('handleClick', 0)
        }
    }
}
</script>

<style scoped>
.menu-body{
    width: 100%;
}
.item-list{
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    margin-top: 20vh;
}
.item-box-container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.item-box{
    width: 35vh;
    height: 35vh;
    border: 1.5px solid #fff;
    border-radius: 5vh;
}
.item-bg{
    background-image: url('../../../../assets/chang/huobajie.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    transition: all .3s;
    cursor: pointer;
}
.item-bg:hover{
    transform: scale(1.05);
}
.item-bg-text{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.item-text{
    margin-top: 20px;
    font-size: 6vh;
    font-family: DongfangDakai;
    color: #fff;
}
</style>