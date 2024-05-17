<template>
  <div id="app">
    <audio ref="audioPlayer" :src="audio_src"></audio>
    <router-view/>
  </div>
</template>

<script>
export default{
  data(){
    return{
      audio_src: 'http://120.27.144.206:8000/static/voice/祭火.m4a',
    }
  }
}
</script>

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body{
  margin: 0;
}

</style>
