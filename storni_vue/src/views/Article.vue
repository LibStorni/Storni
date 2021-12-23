<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="article.get_image">
                </figure>
                
                <h1 class="title">{{article.title}}</h1>
                <p>{{article.description}}</p>

            </div>

        <div class="column is-3">
                <h2 class="subtitle">Informacion</h2>
                <p><strong>precio:</strong>{{article.price}}</p>
            
            
            <div class="field has-addons mt-6">
                <div class="control">
                    <input type="number" class="input" min="0" v-model="quantity">
                </div>

                <div class="control">
                    <a class="button is-light" @click="addToCart">Añadir al Carrito</a>
                </div>


            </div>
        </div>

        </div>




    </div>







</template>

<script>
import axios   from 'axios'
import {toast} from 'bulma-toast'

export default{
    name: 'Article',
    data(){
        return{
           article :{},
           quantity: 1
        }
    },
    
    mounted(){
        this.getArticle()
        
    },

    methods:{
     async getArticle(){
            
            this.$store.commit('setIsLoading',true)

            const article_slug = this.$route.params.article_slug

          await  axios
              .get(`/api/v1/articles/${article_slug}/`)

              .then(response => {
                  this.article = response.data

                  document.title = this.article.title + '|Storni'
              })
              .catch(error =>{
                  console.log(error)
              })

            this.$store.commit('setIsLoading',false)  
        },

        addToCart(){
        console.log('addToCart')
            if (isNaN(this.quantity) || this.quantity < 1){
                this.quantity = 1

            }
            const item ={
                article : this.article,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast ({
                message: " el articulo se añadio al carrito",
                type: 'is-success',
                dismissible:true,
                pauseOnHover:true,
                duration: 2000,
                position: 'bottom-right',

            })
        }
    }

}

</script>