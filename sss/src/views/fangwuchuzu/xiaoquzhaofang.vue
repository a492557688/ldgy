<template>
  <div class="filter_pag">
    <heard_nav></heard_nav>
    <filter_model_xiaoqu></filter_model_xiaoqu>
  </div>
</template>
<script>
import heard_nav from "@/components/heard_nav.vue"
import filter_model_xiaoqu from "@/components/filter/filter_model.vue"
  export default {
  name:"xiaoquzhaofang",
   components:{
      heard_nav,
      filter_model_xiaoqu,
   }
}
</script>
<style scoped>
</style>