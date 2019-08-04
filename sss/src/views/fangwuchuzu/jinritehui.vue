<template>
      <div class="filter_pag">
     <heard_nav></heard_nav>
          <el-image :src=static_url+st></el-image>
<!--          <el-image  :src=static_url+todayBanner.jpg></el-image>-->
      <jinritehui></jinritehui>
      </div>
</template>

<script>
    import heard_nav from "@/components/heard_nav.vue"
    import Jinritehui from "@/components/filter/filter_model_jinritehui";
    export default {
      components:{
          Jinritehui,
          heard_nav,
      },

       name: "qingsongzhaofang",
         data(){
        return  {
            static_url:this.$settings.static_img,
            st:"todayBanner.jpg"
            }
        },
    }
</script>
<style scoped>

</style>