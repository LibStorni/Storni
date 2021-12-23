<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="article.get_thumbnail">
            </figure>
            
            <h3 class="is-size-4">{{article.titulo}}</h3>
            <p class="is-size-6 has-text-grey">${{article.precio}}</p>

            <router-link v-bind:to="article.get_absolute_url" class="button is-light mt4">Ver Detalles</router-link>

        </div>
    </div>
</template>

<script>
export default {
    name:'ItemCase',
    props:{
        article: Object
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