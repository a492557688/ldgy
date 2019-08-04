<template>
    <div class="home">
        <!--<Header :aaa="msg" @bbb="ac"></Header>-->
        <Header></Header>
        <Banner></Banner>
        <Footer></Footer>
    </div>
</template>

<script>
    import Header from "@/components/Header"
    import Banner from "@/components/home/banner"
    import Footer from "@/components/Footer"

    export default {
        name: "Home",
        data() {
            return {
                msg: ''
            }
        },
        methods: {},
        components: {
            'Header': Header,
            Footer,
            Banner,
        }
    }
</script>

<style scoped>

</style>