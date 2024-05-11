<template>
    <div class="wen-child-body">
        <div class="child-title">{{ child_title }}</div>
        <div class="child-content">{{ child_content }}</div>
    </div>
</template>

<script>
export default{
    name: 'wen_component',
    props: {
        child_title: {
            type: String,
            required: true,
            default: ''
        },
        child_content: {
            type: String,
            required: true,
            default: ''
        }
    },
    data(){
        return{
            
        }
    },
    methods: {
    }
}
</script>

<style scoped>
.wen-child-body{
    color: #fff;
    margin-top: 40px;
}
.child-title{
    font-size: 4vh;
    font-family: DongfangDakai;
    text-align: center;
}
.child-content{
    font-size: 2vh;
    margin-top: 30px;
    text-align: left;
    text-indent: 2em;
}
</style>