<template>
    <div>
    <heard_nav></heard_nav>
        <shangwuhezuo></shangwuhezuo>
    </div>
</template>

<script>
    import shangwuhezuo from "@/components/fangwutuoguang/shangwuhezuo.vue"
    import heard_nav from "@/components/heard_nav"
    export default {
         components: {
             shangwuhezuo,
             heard_nav
         },
        name: "hezuo"
    }
</script>

<style scoped>

</style>