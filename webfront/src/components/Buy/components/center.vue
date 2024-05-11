<template>
    <div class="center-body">
        <div class="info-btn">
            <div class="logo person"></div>
        </div>
        <div class="info-btn">
            <div class="logo purchase"></div>
        </div>
        <div class="info-btn">
            <div class="logo save"></div>
        </div>
        <div class="info-btn">
            <div class="logo history"></div>
        </div>
        <div class="info-btn">
            <div class="logo comment"></div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'center',
    data(){
        return{

        }
    }
}
</script>

<style scoped>
.center-body{
    width: 100%;
    height: 70vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.info-btn{
    margin-top: 20px;
    width: 6vh;
    height: 6vh;
    background: #888f9e;
    border-radius: 50%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}
.logo{
    width: 4vh;
    height: 4vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    cursor: pointer;
}
.person{
    background-image: url('../../../assets/Person.png');
}
.purchase{
    background-image: url('../../../assets/purchase.png');
}
.save{
    background-image: url('../../../assets/no_save.png');
}
.history{
    background-image: url('../../../assets/history.png');
}
.comment{
    background-image: url('../../../assets/message.png');
}
</style>