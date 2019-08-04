<template>
    <div>
    <heard_nav></heard_nav>
    <banner></banner>
<!--        <yijiantuoguan></yijiantuoguan>-->
    </div>
</template>

<script>
      import banner from "@/components/fangwutuoguang/banner.vue"
      import heard_nav from "@/components/heard_nav"
      // import heard_nav from "@/components/heard_nav"
    export default {
        name: "fangwutuoguan",

        components: {
          banner,
          heard_nav
        },

    }

</script>

<style scoped>

</style>