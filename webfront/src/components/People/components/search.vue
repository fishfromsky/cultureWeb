<template>
    <div class="search-body">
        <div class="search-text">搜索</div>
        <div class="divider"></div>
        <div class="search-box">
            <div class="input-icon-container">
                <i class="el-icon-search"></i>
                <input type="text" v-model="search_content" placeholder="请输入您想搜索的内容" @keyup.enter="search">
            </div>
        </div>
        <div class="divider"></div>
        <div class="panel-header" @click="togglePanel(index)">
            <div class="header-box">
                分类
            </div>
            <div class="up-logo" :class="{ active: panel_active }"></div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'search',
    data(){
        return{
            panel_active: true
        }
    },
    methods: {
        togglePanel(){
            this.panel_active = !this.panel_active
        }
    }
}
</script>

<style scoped>
.search-text{
    color: #fff;
    font-size: 2vh;
    text-align: left;
}
.divider{
    width: 100%;
    height: 0.5px;
    background-color: #fff;
    margin-top: 20px;
}
.search-box{
    margin-top: 20px;
    width: 100%;
    text-align: center;
    box-sizing: border-box;
}
.input-icon-container {
    box-sizing: border-box;
    width: 100%;
    display: flex;
    align-items: center;
    background-color: #131e3a;
    color: #fff;
    border: 1px solid #fff;
    border-radius: 3vh;
    font-size: 2vh;
    padding: 5px 5px;
    padding-top: 10px;
    padding-bottom: 10px
}
.input-icon-container input {
  border: none;
  outline: none;
  background-color: transparent;
  margin-left: 10px; 
  color: #fff;
  font-size: 2vh;
}
.panel-header {
    width: 100%;
    height: 5vh;
    border-bottom: 1px solid #aaa;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    box-sizing: border-box;
    padding-top: 2vh;
    padding-bottom: 2vh;
    color: #fff;
}
.header-box{
    font-size: 2vh;
}
.up-logo{
    width: 2vh;
    height: 2vh;
    background-image: url('../../../assets/up.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    transition: all .3s;
}
.up-logo.active{
    transform: rotate(180deg);
}
</style>