<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Busqueda</h1>

                <h2 class="is-size-5 has-text-grey">Termino Buscado: "{{ query }}"</h2>
            </div>


            <ItemCase 
                v-for="article in articles"
                v-bind:key="article.id"
                v-bind:article="article" />
      
         
      </div>
    </div>
</template>

<script>
import ItemCase from '@/components/ItemCase.vue'
import axios from 'axios'


export default {
    name: 'Search',
   
    components: {
        ItemCase
    },
    data() {
        return {
            articles: [],
            query   : ''
        }
    },
    mounted() {
        document.title = 'Search | Storni'

        let uri    = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')
            this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)
            await axios
                .post('/api/v1/articles/search/', {'query': this.query})
                .then(response => {
                    this.articles = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>