<template>
    <div class="change-body">
        <SelectItem v-if="selected == -1" @handleClick="redirectPage"></SelectItem>
        <Play v-if="selected == 0" :selected="select_item" @toPage="toPage" @back="handleBack"></Play>
        <jihuo1 v-if="selected == 1" @nextpage="toPage"></jihuo1>
        <jihuo2 v-if="selected == 2" @nextpage="toPage"></jihuo2>
        <wanhuo1 v-if="selected == 3" @nextpage="toPage"></wanhuo1>
        <wanhuo2 v-if="selected == 4" @nextpage="toPage"></wanhuo2>
        <songhuo v-if="selected == 5" @nextpage="toPage"></songhuo>
    </div>
</template>

<script>
import SelectItem from './selectItem.vue'
import Play from './play.vue'
import jihuo1 from './components/jihuo1.vue'
import jihuo2 from './components/jihuo2.vue'
import wanhuo1 from './components/wanhuo1.vue'
import wanhuo2 from './components/wanhuo2.vue'
import songhuo from './components/songhuo.vue'
export default{
    name: 'change',
    components: {
        SelectItem,
        Play,
        jihuo1,
        jihuo2,
        wanhuo1,
        wanhuo2,
        songhuo
    },
    data(){
        return{
            selected: -1,
            select_item: 1
        }
    },
    methods: {
        redirectPage(val){
            this.selected = 0
        },
        handleBack(val){
            this.selected = -1
        },
        toPage(val){
            this.selected = val[0]
            this.select_item = val[1]
        }
    }
}
</script>

<style scoped>
.change-body{
    width: 100%;
}

</style>