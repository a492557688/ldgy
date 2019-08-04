<template>
    <div class="detail_page">
    <heard_nav></heard_nav>
    <detail_info></detail_info>
  </div>
</template>

<script>
    import heard_nav from "@/components/heard_nav.vue"
    import detail_info from "@/components/detail_page/detail_info.vue"
    export default {
      name: "detail_page",
         components:{
          heard_nav,
          detail_info,
         },
          // created(){
          //        this.house_id = this.$route.params.course_id;
          //
          // }

    }
</script>

<style scoped>

</style>