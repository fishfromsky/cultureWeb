<template>
    <div class="container" id="container">
        <div class="item" v-for="(item, idx) in dataset" :key="idx" :class="[item.size_type == 1? 'item-height2': 'item-height1']">
            <img :src="item.img" class="item-img" >
        </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'dataset',
    props: {
        dataset: {
            type: Array,
            required: true
        }
    },
    data() {
      return {
       
      };
    },
    watch: {
        dataset(val){
            let item_count = val.length
            let height = (parseInt(item_count/3)+1)*40
            const container = document.getElementById('container')
            container.style.height = height.toString()+'vh'
        }
    }
  }
  </script>
  
  <style>
/* 让内容按列纵向展示 */
.container {
    margin-top: 20px;
  display: flex;
  flex-flow: column wrap;
  width: 90%;
  margin-left: 5%;
}
.item{
    width: 33%;
    overflow: hidden;
    box-sizing: border-box;
}
.item-img{
    width: 100%;
    height: 100%;
    transition: all .3s;
    cursor: pointer;
}
.item-img:hover{
    transform: scale(1.03);
}

.item-height1{
    height: 30vh;
}

.item-height2{
    height: 40vh;
}

/* 重新定义内容块排序优先级，让其横向排序 */
.item:nth-child(3n+1) { order: 1; }
.item:nth-child(3n+2) { order: 2; }
.item:nth-child(3n)   { order: 3; }

/* 强制使内容块分列的隐藏列 */
.container::before,
.container::after {
  content: "";
  flex-basis: 100%;
  width: 0;
  order: 2;
}
  </style>
  