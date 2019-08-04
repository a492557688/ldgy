<template>
    <div class="block">
    <el-carousel height="500px">
      .0
        <el-carousel-item  v-for="banner in banner_list"  v-bind:key="banner">
        <img :src="banner.img" alt="..." style="width: 1890px;height: 500px">
        A</el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
    export default {
        name: "banner",
        data() {
        return  {
          banner_list:[],
            }
        },
        created(){
      this.$axios.get(this.$settings.Host+"/home/benner/").then(res =>{
        this.banner_list=res.data
      })
    }
    }

</script>

<style scoped>
.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }
</style>