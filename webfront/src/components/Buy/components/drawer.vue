<template>
    <div class="drawer-body">
        <div class="panel" v-for="(panel, index) in panels" :key="index" :class="{ active: panel.active }">
            <div class="panel-header" @click="togglePanel(index)">
                <div class="header-box">
                    {{ panel.title }}
                </div>
                <div class="up-logo" :class="{ active: panel.active }"></div>
            </div>
            <div class="content-box">
                <div class="panel-content" v-for="(item, idx) in panel.content" :key="idx" :style="{ maxHeight: panel.active ? '500px' : '0' }" @click="select_item(index, idx)">
                    <div class="selected-item" :class="{ active: item.selected }"></div>
                    <div class="name-box">{{ item.name }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'drawer',
    data(){
        return{
            panels: [
            {   title: '手工艺人', 
                content: [
                ], 
                active: true
            },
            {   title: '银饰品', 
                content: [
                ], 
                active: true
            },
            { 
                title: '银器物', 
                content: [
                ], 
                active: true
            }
            ]
        }
    },
    methods: {
        togglePanel(index) {
            this.panels[index].active = !this.panels[index].active;
        },
        select_item(index, idx){
            if (this.panels[index].content[idx].selected == true){
                this.panels[index].content[idx].selected = false
                if (index == 0){
                    this.$emit('person', -this.panels[index].content[idx].id)
                }
                else if (index == 1){
                    this.$emit('decorate', -this.panels[index].content[idx].id)
                }
                else{
                    this.$emit('material', -this.panels[index].content[idx].id)
                }
            }
            else{
                this.panels[index].content[idx].selected = true
                if (index == 0){
                    this.$emit('person', this.panels[index].content[idx].id)
                }
                else if (index == 1){
                    this.$emit('decorate', this.panels[index].content[idx].id)
                }
                else{
                    this.$emit('material', this.panels[index].content[idx].id)
                }
            }
        },
        get_categories(){
            let that = this
            this.$http.get('api/get_goods_categories').then(res=>{
                let categories = res.data.data
                for (let i=0; i<categories.length; i++){
                    if (categories[i].main_class == '银饰品'){
                        categories[i].selected = false
                        that.panels[1].content.push(categories[i])
                    }
                    else if (categories[i].main_class == '银器物'){
                        categories[i].selected = false
                        that.panels[2].content.push(categories[i])
                    }
                }
            }).catch(e=>{this.$message.error(e)})
        },
        get_workman(){
            let that = this
            this.$http.get('api/get_workmans').then(res=>{
                let person = res.data.data
                for (let i=0; i<person.length; i++){
                    person[i].selected = false
                }
                that.panels[0].content = person
            }).catch(e=>{this.$message.error(e)})
        }
    },
    created(){
        this.get_categories()
        this.get_workman()
    }
}
</script>

<style scoped>
.drawer-body{
    width: 100%;
    height: 75vh;
    color: #fff;
}
.panel {
    margin-bottom: 10px;
}
.panel-header {
    width: 100%;
    height: 3vh;
    border-bottom: 1px solid #aaa;
    border-top: 1px solid #aaa;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    box-sizing: border-box;
    padding-top: 2vh;
    padding-bottom: 2vh;
}
.header-box{
    font-size: 1.5vh;
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
    max-height: 20vh;
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
    height: 3vh;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    cursor: pointer;
}
.selected-item{
    width: 1.3vh;
    height: 1.3vh;
    border: 1px solid #fff;
    transition: all .3s;
}
.selected-item.active{
    background-color: #fff;
}
.name-box{
    font-size: 1.5vh;
    margin-left: 20px;
}
.panel.active .panel-content {
    max-height: 500px; 
    padding: 10px;
}
</style>