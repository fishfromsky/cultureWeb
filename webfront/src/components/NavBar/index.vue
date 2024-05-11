<template>
    <div class="main-body">
        <div class="header">
            <div class="logo-box">
                <div class="logo-container">
                    <div class="logo-item">
                        <img src="../../assets/logo.png" style="width: 100%; height: 100%;"/>
                    </div>
                </div>
                <div class="title-box">
                    <div class="title-text">彝山有银</div>
                </div>
            </div>
            <ul class="menu">
                <li v-for="(item, idx) in nav_list" class="menu-item" @click="selectPage(idx)">{{ item.name }}</li>
            </ul>
            <div class="personal">
                <div class="divider"></div>
                <div class="icon-box">
                    <i class="el-icon-search"></i>
                </div>
                <div class="input-container">
                    <input
                    type="text"
                    v-model="inputValue"
                    @focus="isActive = true"
                    @blur="isActive = false"
                    :class="{ 'active': isActive }"
                    >
                    <span class="underline" v-if="isActive"></span>
                </div>
                <div class="login">
                    <i class="el-icon-user"></i>
                </div>
            </div>
        </div>
        <div class="bottom-line"></div>
    </div>
</template>

<script>
export default {
    name: 'NavBar',
    data(){
        return{
            nav_list: [
                {name: '银', path: '/show'},
                {name: '匠', path: '/people'},
                {name: '闻', path: '/wen'},
                {name: '肆', path: '/buy'},
                {name: '嬉', path: '/game'},
                {name: '谈', path: '/talk'}
            ],
            inputValue: '',
            isActive: false,
        }
    },
    methods: {
        selectPage(id){
            this.$router.push({path: this.nav_list[id].path, replace: true})
        }
    }
}
</script>

<style scoped>
.main-body{
    width: 100%;
    height: 10vh;
    top: 0;
    left: 0;
    background-color: #080e26;
}
.header{
    width: 100%;
    height: 99%;
    display: flex;
    flex-direction: row;
    font-family: DongfangDakai;
}
.bottom-line{
    width: 96%;
    margin-left: 2%;
    height: 1%;
    background-color: #696969;
}
.logo-box{
    width: 20%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
}
.logo-container{
    width: 35%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.logo-item{
    width: 100%;
    height: 6vh;
    margin-left: 40px;
}
.title-box{
    width: 70%;
    height: 100%;
    margin-left: 30px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
}
.title-text{
    color: #fff;
    font-size: 4vh;
}
.menu{
    width: 60%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 0;
    list-style: none;
    margin: 0;
}
.menu-item{
    margin-left: 10%;
    position: relative;
    color: #fff;
    font-size: 4vh;
    padding-bottom: 5px;
    cursor: pointer;
}
.menu-item:after{
    content: "";
    width: 0;
    height: 0.3vh;
    background: #fff;
    position: absolute;
    border-radius: 2px;
    top: 100%;
    left: 50%;
    transition: width 0.3s ease, left 0.3s ease;
}
.active{
    border-bottom: solid 2px #fff;
}
.menu-item:hover:after {
    width: 100%; 
    left: 0; 
}
.personal{
    width: 30%;
    height: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-end;
}
.icon-box{
    font-size: 2vh;
    color: #fff;
    margin-left: 10px;
}

.input-container{
    position: relative;
    display: inline-block;
    margin-right: 10px;
    margin-left: 10px;
    width: 30%;
}
.input-container input {
    width: 100%;
    border: none;
    outline: none;
    padding: 10px 0;
    background-color: #080e26;
    color: #fff;
    font-size: 2vh;
}

.underline {
  position: absolute;
  bottom: 0;
  left: 50%;
  height: 1px;
  width: 0;
  background-color: #fff;
  transition: all .8s;
}

.input-container input.active + .underline {
  width: 100%;
  left: 0;
}
.login{
    font-size: 2vh;
    color: #fff;
    margin-left: 10px;
    margin-right: 40px;
    cursor: pointer;
}
</style>