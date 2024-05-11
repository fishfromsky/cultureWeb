<template>
    <div class="wu-body">
        <Child @redirect="handle_redirect"></Child>
    </div>
</template>

<script>
import Child from './children/index.vue'
import Decorate from '../../../Decorate/index.vue'
import Material from '../../../Material/index.vue'
export default{
    name: 'wu',
    components: {
        Child,
        Decorate,
        Material
    },
    data(){
        return{
            
        }
    },
    methods: {
        handle_redirect(val){
            if (val == 0){
                this.$router.push({path: '/decorate', replace: true})
            }
            else{
                this.$router.push({path: '/material', replace: true})
            }
        }
    }
}
</script>

<style scoped>
.wu-body{
    width: 100%;
    box-sizing: border-box;
    color: #fff;
}
</style>