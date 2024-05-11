<template>
    <div class="bottom-navigate-body">
        <div class="navigator-flex">
            <div class="middle-box">
                <div class="nav-logo-box" v-for="(item, idx) in logo" :key="idx" @click="handle_click(idx)">
                    <div class="logo-bg" :class="[item.status? item.class_list[0]:item.class_list[1]]"></div>
                    <div class="logo-text" :class="[item.status? item.class_list[2]:item.class_list[3]]">{{ item.name }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'bottom_navigate',
    data(){
        return{
            selected: 0,
            logo: [
                {status: 1, class_list: ['dongwu-active', 'dongwu-no-active', 'logo-text-active', 'logo-text-noactive'], name: '动物纹'},
                {status: 0, class_list: ['zhiwu-active', 'zhiwu-no-active', 'logo-text-active', 'logo-text-noactive'], name: '植物纹'},
                {status: 0, class_list: ['nature-active', 'nature-no-active', 'logo-text-active', 'logo-text-noactive'], name: '自然现象纹'},
                {status: 0, class_list: ['jihe-active', 'jihe-no-active', 'logo-text-active', 'logo-text-noactive'], name: '几何纹'},
                {status: 0, class_list: ['else-active', 'else-no-active', 'logo-text-active', 'logo-text-noactive'], name: '其他'}
            ],
        }
    },
    methods: {
        handle_click(val){
            if (this.selected != val){
               this.logo[this.selected].status = 0
               this.logo[val].status = 1
               this.selected = val;
               this.$emit('changeWen', val)
            }
        }
    }
}
</script>

<style scoped>
.bottom-navigate-body{
    width: 80%;
    margin-left: 25%;
    margin-top: 12vh;
}
.navigator-flex{
    width: 100%;
    display: flex;
    flex-direction: row;
}
.nav-logo-box{
    min-height: 12vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: -3.5vh;
    cursor: pointer;
}
.nav-logo-box:first-child{
    margin-left: -50px;
}
.nav-logo-box:last-child{
    margin-right: -50px;
}
.middle-box{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 80%;
    height: 2px;
    background-image: linear-gradient(
    to right,
    #868a94 0%,
    #868a94 50%,
    transparent 50%
    );
    background-size: 20px 2px;
    background-repeat: repeat-x;
}
.logo-bg{
    width: 6vh;
    height: 6vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 140% 140%;
    transition: all .3s;
}
.dongwu-active{
    background-image: url('../../../assets/wen_dongwu.png');
}
.zhiwu-active{
    background-image: url('../../../assets/wen_zhiwu.png');
}
.nature-active{
    background-image: url('../../../assets/wen_nature.png');
}
.jihe-active{
    background-image: url('../../../assets/wen_jihe.png');
}
.else-active{
    background-image: url('../../../assets/wen_qita.png');
}
.dongwu-no-active{
    background-image: url('../../../assets/wen_dongwu_no_active.png');
}
.zhiwu-no-active{
    background-image: url('../../../assets/wen_zhiwu_no_active.png');
}
.nature-no-active{
    background-image: url('../../../assets/wen_nature_no_active.png');
}
.jihe-no-active{
    background-image: url('../../../assets/wen_jihe_no_active.png');
}
.else-no-active{
    background-image: url('../../../assets/wen_qita_no_active.png');
}
.logo-text{
    font-family: DongfangDakai;
    font-size: 3vh;
    margin-top: 10px;
    transition: all .3s
}
.logo-text-active{
    color: #fff;
}
.logo-text-noactive{
    color: #868a94;
}
</style>