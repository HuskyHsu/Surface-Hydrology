<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
import Vue from 'vue';

import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios);

export default {
  name: 'app',
  created() {
    Vue.axios.get('http://127.0.0.1:8000/data/all/').then((response) => {
      console.log(response.data);
    });
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
