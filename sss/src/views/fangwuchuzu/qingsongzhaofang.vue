<template>
      <div class="filter_pag">
     <heard_nav></heard_nav>
      <filter_model_qingsong></filter_model_qingsong>
      </div>
</template>

<script>
    import heard_nav from "@/components/heard_nav.vue"
    import filter_model_qingsong from "@/components/filter/filter_model_qingsong.vue"
    export default {
      components:{
          heard_nav,
          filter_model_qingsong
      },
       name: "qingsongzhaofang"
    }
</script>
<style scoped>

</style>