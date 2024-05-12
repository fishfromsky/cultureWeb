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
        <div class="divider" style="margin-top: 0;"></div>
        <div class="content-box">
            <div class="panel-content" v-for="(item, idx) in category_list" :key="idx" :style="{ maxHeight: panel_active ? '500px' : '0' }" @click="selectItem(idx)">
                <div class="selected-item" :class="{ active: selected_idx==idx }"></div>
                <div class="name-box">{{ item }}</div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'search',
    props: {
        category_list: {
            type: Array,
            required: true
        }
    },
    data(){
        return{
            panel_active: true,
            selected_idx: -1,
            search_content: ''
        }
    },
    methods: {
        togglePanel(){
            this.panel_active = !this.panel_active
        },
        search(){

        },
        selectItem(idx){
            if (this.selected_idx == idx){
                this.selected_idx = -1
            }
            else{
                this.selected_idx = idx
            }
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
    padding-bottom: 10px;
    padding-left: 15px;
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
.content-box{
    width: 100%;
    max-height: 70vh;
    overflow-x: hidden;
    overflow-y: auto;
}
.content-box::-webkit-scrollbar {
  width: 6px; /* 滚动条的宽度 */
}

.content-box::-webkit-scrollbar-track {
  background: transparent; /* 滚动条轨道的颜色 */
}

.content-box::-webkit-scrollbar-thumb {
  background-color: #fff; /* 滚动条本身的颜色 */
  border-radius: 4px; /* 滚动条圆角 */
}

.content-box::-webkit-scrollbar-thumb:hover {
  background: #555; /* 滚动条鼠标悬停时的颜色 */
}
.panel-content {
    overflow: hidden;
    transition: all 0.3s;
    width: 100%;
    height: 5vh;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    cursor: pointer;
}
.selected-item{
    width: 1.5vh;
    height: 1.5vh;
    border: 1px solid #fff;
    border-radius: 50%;
    transition: all .3s;
}
.selected-item.active{
    background-color: #fff;
}
.name-box{
    font-size: 1.7vh;
    margin-left: 20px;
    color: #fff;
}
.panel.active .panel-content {
    max-height: 500px; 
    padding: 10px;
}
</style>