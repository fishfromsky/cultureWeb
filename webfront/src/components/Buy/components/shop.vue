<template>
    <div class="shop-body">
        <div class="search-box">
            <div class="input-icon-container">
                <i class="el-icon-search"></i>
                <input type="text" v-model="search_content" placeholder="请输入您想搜索的内容" @keyup.enter="search">
            </div>
        </div>
        <div class="filter-box">
            <div class="condition">
                <div class="filter-item">
                    <div class="filter-text">人气</div>
                    <div class="logo-box">
                        <div class="down-logo"></div>
                    </div>
                </div>
                <div class="filter-item" style="margin-left: 40px;">
                    <div class="filter-text">销量</div>
                    <div class="logo-box">
                        <div class="down-logo"></div>
                    </div>
                </div>
                <div class="filter-item" style="margin-left: 40px;">
                    <div class="filter-text">价格</div>
                    <div class="logo-box">
                        <div class="up-logo"></div>
                        <div class="down-logo"></div>
                    </div>
                </div>
                <input type="number" v-model="low_price" class="low-price" placeholder="最低价"/>
                &nbsp &#8212 &nbsp 
                <input type="number" v-model="high_price" class="low-price" placeholder="最高价" style="margin-left: 0;"/>
            </div>
            <div class="filter-item">共{{ goods_num }}件商品</div>
        </div>
        <div class="main-shop">
            <div class="img-box" v-for="(item, idx) in goods_info" :key="idx">
                <div class="img" @click="select_goods(item)">
                    <img :src="item.src" style="width: 100%; height: 100%;" class="img-hover">
                </div>
                <div class="text-box">{{ item.name }}</div>
                <div class="price-box">
                    <div class="goods-price">
                        &yen {{ item.price }}
                    </div>
                    <div class="pay-count">
                        {{ item.pay_count }}人已付款
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Cookies from 'js-cookie'
export default{
    name: 'shop',
    props: {
        'person_id': {
            type: Array,
            required: true
        },
        'category_id': {
            type: Array,
            required: true
        }
    },
    data(){
        return{
            search_content: '',
            goods_num: 0,
            low_price: '',
            high_price: '',
            goods_info:[
            ],
            initial: true
        }
    },
    methods: {
        search(){
            
        },
        select_goods(val){
            let user_id = Cookies.get('user_id')
            if (user_id == null){
                this.$router.push({path: '/login'})
            }
            else{
                this.$emit('selectGoods', val.id)
            }
        },
        get_goods_num(){
            let that = this
            this.$http.get('api/get_goods_number').then(res=>{
                that.goods_num = res.data.data
            }).catch(e=>{this.$message.error(e)})
        },
        get_goods_info(){
            let that = this
            let data = {
                'person': this.person_id,
                'category': this.category_id
            }
            this.$http.post('api/get_goods_info', data).then(res=>{
                that.goods_info = res.data.data

            }).catch(res=>{this.$message.error(res)})
        }
    },
    watch: {
        person_id: {
            handler(new_val){
                if (this.person_id.length == 0 && this.initial){
                    
                }
                else{
                    if (this.initial){
                        this.initial = false
                    }
                    this.get_goods_info()
                }
            },
            immediate: true,
        },
        category_id: {
            handler(new_val){
                if (this.category_id.length == 0 && this.initial){
                    
                }
                else{
                    if (this.initial){
                        this.initial = false
                    }
                    this.get_goods_info()
                }
            },
            immediate: true,
        }
    },
    created(){
        this.get_goods_num()
        this.get_goods_info()
    }
}
</script>

<style scoped>
.shop-body{
    width: 100%;
    box-sizing: border-box;
    padding-left: 10%;
}
.seach-box{
    width: 100%;
    text-align: center;
}
.input-icon-container {
    width: 50%;
    margin-left: 25%;
    display: flex;
    align-items: center;
    background-color: #0c1429;
    color: #fff;
    border: 1px solid #fff;
    border-radius: 3vh;
    font-size: 2vh;
    padding: 10px 10px;
}
.input-icon-container input {
  border: none;
  outline: none;
  background-color: transparent;
  margin-left: 10px; 
  color: #fff;
  font-size: 2vh;
}
.icon {
  font-style: normal;
}
.filter-box{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    color: #fff;
    box-sizing: border-box;
    padding: 20px;
    padding-top: 30px;
}
.condition{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
}
.filter-item{
    font-size: 2vh;
    display: flex;
    flex-direction: row;
}
.logo-box{
    margin-left: 10px;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.down-logo{
    background-image: url('../../../assets/down.png');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: 100% 100%;
    width: 1.5vh;
    height: 1.5vh;
}
.up-logo{
    background-image: url('../../../assets/up.png');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: 100% 100%;
    width: 1.5vh;
    height: 1.5vh;
}
.low-price{
    width: 10%;
    height: 100%;
    background: transparent;
    color: #fff;
    border: none;
    outline: none;
    border: 1px solid #fff;
    border-radius: 1vh;
    margin-left: 10px;
}
.main-shop{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    flex-wrap: wrap;
    height: 60vh;
    overflow-x: hidden;
    overflow-y: auto;
}
.main-shop::-webkit-scrollbar {
  width: 6px; /* 滚动条的宽度 */
}

.main-shop::-webkit-scrollbar-track {
  background: transparent; /* 滚动条轨道的颜色 */
}

.main-shop::-webkit-scrollbar-thumb {
  background-color: #fff; /* 滚动条本身的颜色 */
  border-radius: 4px; /* 滚动条圆角 */
}

.main-shop::-webkit-scrollbar-thumb:hover {
  background: #555; /* 滚动条鼠标悬停时的颜色 */
}
.img-box{
    width: 30%;
    min-height: 60vh;
    margin-left: 20px;
}
.img{
    width: 100%;
    height: 45vh;
    border: 1px solid #fff;
    border-radius: 2vh;
    overflow: hidden;
}
.img-hover{
    transition: all .3s ease-out;
    cursor: pointer;
}
.img-hover:hover{
    transform: scale(1.2);
}
.text-box{
    margin-top: 10px;
    width: 100%;
    color: #fff;
    font-size: 2vh;
    text-overflow: ellipsis;
    overflow-x: hidden;
    white-space: nowrap;
    text-align: left;
}
.price-box{
    margin-top: 10px;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.goods-price{
    font-size: 2vh;
    color: #fff;
}
.pay-count{
    color: #aaa;
    font-size: 1.5vh;
}
</style>