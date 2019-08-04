<template>
   <div class="home">
   <heard_nav></heard_nav>
   <banner></banner>
      <welocome></welocome>
   <fangjianhuxing></fangjianhuxing>
   <jingpinfangyuan></jingpinfangyuan>
   <remenquyu></remenquyu>
   <bottom></bottom>

   </div>
</template>

<script>
import heard_nav from "@/components/heard_nav.vue"
import banner from "@/components/home/banner.vue"
import fangjianhuxing from "@/components/home/fangjianhuxing.vue"
import welocome from "@/components/home/welocome.vue"
import jingpinfangyuan from "@/components/home/jingpinfangyuan.vue"
import remenquyu from "@/components/home/remenquyu.vue"
import dibu from "@/components/home/dibu.vue"
import bottom from "@/components/home/bottom.vue"
export default {
   components:{
      heard_nav,
      banner,
      fangjianhuxing,
      welocome,
      jingpinfangyuan,
      remenquyu,
      dibu,
      bottom,
   }
}

</script>

<style scoped>

   *{
   text-decoration: none;color: blue
   }
</style>