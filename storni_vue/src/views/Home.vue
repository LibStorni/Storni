<template>
<div class="home"> 
   <section class="hero is-light ">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Storni
            </p>
            <p class="subtitle">
                tienda de libros en linea
            </p>
        </div>
    </section>

   <div class="columns is-multiline"> 
     <div class="column is-12"> 
     
     <h2 class="is-size-4 has-text-centered"> Ultimos Ejemplares</h2>
     </div>
     
     <div class="column is-3" 
     v-for="article in latestArticles"
     v-bind:key="article.id">

     <div class="box">
       <figure class="image mb-4">
         <img :src="article.get_thumbnail">
       </figure>
       <h3 class="is-size-4">{{article.title}}</h3>
       <p class="is-size-6 has-text-grey">{{article.price}}</p>
       
     </div>
        <router-link v-bind:to="article.get_absolute_url" class="button is-light ">ver detalles</router-link>
     </div>
   
   </div>
</div>
</template>

<script>
import axios from 'axios'

export default{
  name       : 'Home',
  data(){
    return{
      latestArticles:[]
    }
  },
  components : {

  },
  mounted(){
    this.getLatestArticles()
    document.title = 'Home|Storni'
  },

  methods:{
  async  getLatestArticles(){

    this.$store.commit('setIsLoading',true)

    await  axios
        .get('api/v1/latest-articles/')
        .then(response => {
          this.latestArticles = response.data
        })
        .catch(error => {
          console.log(error)

        })

    this.$store.commit('setIsLoading',false)
    }
  }

}

 
</script>

<style scoped>
  .image{
     margin-top  :-1.25rem ;
     margin-left :-1.25rem ;
     margin-right:-1.25rem ;
     }

</style>
