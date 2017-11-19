<template>
<el-container>
  <el-header>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1"><a href="http://hydro.ihs.ncu.edu.tw/" target="_blank">Surface Hydrology Lab.</a></el-menu-item>
        <el-menu-item index="2"><a href="/" target="_blank">Home</a></el-menu-item>
        <el-submenu index="3">
          <template slot="title">上傳檔案</template>
          <el-menu-item index="3-1">蓮華池</el-menu-item>
        </el-submenu>
    </el-menu>
  </el-header>
  <el-container>
    <el-aside width="200px">Aside</el-aside>
    <el-container>
      <el-main>Main</el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </el-container>
</el-container>
</template>

<script>
import Vue from 'vue';

import axios from 'axios';
import VueAxios from 'vue-axios';
// import ElementUI from 'element-ui';
// import 'element-ui/lib/theme-chalk/index.css';

Vue.use(VueAxios, axios);

export default {
  name: 'app',
  data() {
    return {
      activeIndex: '1',
      activeIndex2: '1',
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
  },
  created() {
    Vue.axios.get('http://127.0.0.1:8000/data/all/').then((response) => {
      console.log(response.data);
    });
  },
};
</script>

<style>

html, body {
  margin: 0;
  padding: 0;
}

.el-header,
.el-footer {
  /* background-color: #b3c0d1; */
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  /* background-color: #d3dce6; */
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  /* background-color: #e9eef3; */
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>