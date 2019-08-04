<template>
  <el-menu
  :class="el-menu-demo"
  mode="horizontal"
  background-color="##AEEEEE"
  >
<!--  { "name": "房屋出租", "rank": 0, "content": [ { "title": "轻松找房", "nav_url": "/list", "ordering": 1 }, { "title": "小区租房", "nav_url": "/xiaoqu", "ordering": 2 }, { "title": "今日特惠", "nav_url": "todaySpecial", "ordering": 3 } ] }-->
<!--{ "name": "地图找房", "rank": 0, "content": [ { "title": "null", "nav_url": "/map/", "ordering": 1 } ] }-->
<el-submenu index="1">
  <template slot="title">{{biaoti_list[0].name}}</template>

  <router-link to="/qingsongzhaofang"><el-menu-item index="1-1">{{biaoti_list[0].content[0].title}}</el-menu-item></router-link>
  <router-link to="/xiaoquzhaofang"><el-menu-item index="1-2">{{biaoti_list[0].content[1].title}}</el-menu-item></router-link>
  <router-link to="/jinritehui"> <el-menu-item index="1-2">{{biaoti_list[0].content[2].title}}</el-menu-item></router-link>
</el-submenu>
<el-submenu index="2">
  <template slot="title" >地图找房</template>
</el-submenu>
<el-submenu index="3">
  <template slot="title">房屋托管与商业合作</template>
      <router-link to="/fangwutuoguan"> <el-menu-item index="3-1">房屋托管</el-menu-item>  </router-link>
    <el-menu-item index="3-2">政府视窗</el-menu-item>
    <router-link to="/shangwuhezuo"><el-menu-item index="3-3">商务合作</el-menu-item></router-link>


</el-submenu>
  <el-submenu index="5">
  <template slot="title">灵动公寓快讯</template>
  <el-menu-item index="5-1">博客</el-menu-item>
</el-submenu>
      <el-submenu index="6">
  <template slot="title">移动青客</template>
  <el-menu-item index="6-1">房客app</el-menu-item>
  <el-menu-item index="6-2">房东app</el-menu-item>
</el-submenu>


  <h2>
    上海租房看房热线 看房热线： 8:00~22:00
        120-110-119
    </h2>
</el-menu>
</template>


<script>
  export default {
    name:"HelloWorld",
    data() {
      return {
        biaoti_list:""

      };
    },
    methods: {
    },
    created(){
      this.$axios.get(this.$settings.Host+"/home/nav/head/").then(res =>{
        this.biaoti_list=res.data
      })
    }

  }
</script>
<style scoped>
  h1{
    background: aqua;
  }
</style>