<template>
    <div class="main-body">
        <el-row :gutter="20">
            <el-col :span="21">
                <Wen v-if="navigator == 0"></Wen>
                <Wu v-if="navigator == 1"></Wu>
                <Detail v-if="navigator == 2"></Detail>
                <Shi v-if="navigator == 3"></Shi>
                <Chang v-if="navigator == 4"></Chang>
            </el-col>
            <el-col :span="3">
                <Navigate @navigator="handle_navigate"></Navigate>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Navigate from './components/navigate.vue'
import Detail from './components/detail.vue'
import Wen from './components/wen.vue'
import Wu from './components/wu/index.vue'
import Shi from './components/shi/index.vue'
import Chang from './components/change/index.vue'
export default {
    name: 'Show',
    components: {
        Navigate,
        Detail,
        Wen,
        Wu,
        Shi,
        Chang
    },
    data(){
        return{
            navigator: 0
        }
    },
    methods: {
        handle_navigate(val){
            this.navigator = val
        }
    }
}
</script>

<style scoped>
.main-body{
    width: 100%;
    min-height: 90vh;
    background-color: #131e3a;
    background-image: url('../../assets/main_bg_yin.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    box-sizing: border-box;
    padding: 40px;
}
</style>