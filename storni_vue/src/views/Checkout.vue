<template>
    <div class="checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Facturar</h1>
            
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Articulo</th>
                            <th>Precio</th>
                            <th>Cantidad</th>
                            <th>Total</th>
                        </tr>
                    </thead>

                    <tbody>
                       <tr 
                       v-for="item in cart.items"
                       v-bind:key="item.article.id"
                       >

                       <td>{{item.article.title}}</td>
                       <td>${{item.article.price}}</td>
                       <td>{{item.quantity}}</td>
                       <td>${{getItemTotal(item).toFixed(2)}}</td>

                       </tr>
                    </tbody>

                    <tfoot>
                        <tr>

                            <td colspan="2">Total</td>
                            <td>{{cartTotalLength}}</td>
                            <td>${{cartTotalPrice.toFixed(2)}}</td>
                   
                        </tr>


                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Detalles de envio</h2>
                <p class="has-text-grey mb-4">*Todos los campos son obligatorios</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        
                        <div class="field">
                            <label >Nombre*</label>
                        
                        <div class="control">
                            <input type="text" class="input" v-model="name">
                        </div>
                        </div>

                        <div class="field">
                            <label >Correo*</label>
                        
                        <div class="control">
                            <input type="email" class="input" v-model="email">
                        </div>
                        </div>

                        <div class="field">
                            <label >Direccion*</label>
                        
                        <div class="control">
                            <input type="text" class="input" v-model="address">
                        </div>
                        </div>

                        <div class="field">
                            <label >Lugar*</label>
                        
                        <div class="control">
                            <input type="text" class="input" v-model="place">
                        </div>
                        </div>

                    </div>

                </div>
                 <div class="notification is-danger" v-if="errors.length">
                       <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                    </div>
                    
                    <hr>

                    <div id="card-element" class="mb-5"></div>

                    <template v-if="cartTotalLength">
                        <hr>
                        <button class="button is-dark" @click="submitForm">Realizar pago</button>
                    </template>

            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Checkout',
    data(){
        return{
            cart:{
                items:[]
            },
            stripe:{},
            card:{},
            name:'',
            email:'',
            address:'',
            place:'',
            errors:[]
        }
    },
    mounted(){
        document.title = 'Checkout|Storni'

        this.cart = this.$store.state.cart

        if(this.cartTotalLength > 0){
            this.stripe = Stripe('pk_test_51K9BRoDRr1m4RcswZbisCgz07GW05dCAIwgQhhdDNNzMSNRO6lxTWrnMoJ1kCme60hL3kK6WROXoWxDN0W9Y1U4n00A1xSBxMZ')
            const elements = this.stripe.elements();
            this.card  = elements.create('card',{hidePostalCode:true})

            this.card.mount('#card-element')
        }
    },

    methods:{
        getItemTotal(item){
            return item.quantity * item.article.price
        },
        submitForm(){
            this.errors =[]

            if(this.name === ''){
                this.errors.push('campo faltante')
            }

            if(this.email === ''){
                this.errors.push('campo faltante')
            }

            if(this.address === ''){
                this.errors.push('campo faltante')
            }
            
            if(this.place === ''){
                this.errors.push('campo faltante')
            }

            if(!this.errors.length){
                this.$store.commit('setIsLoading',true)

                this.stripe.createToken(this.card).then(result =>{
                    if(result.error){
                        this.$store.commit('setIsLoading',false)

                        this.errors.push('Algo salió mal con stripe. Vuelva a intentarlo')

                        console.log(result.error.message)
                    } else{
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
    async stripeTokenHandler(token){
        const items = []

        for(let i=0;i < this.cart.items.length; i++){
            const item = this.cart.items[i]
            const obj  = {
                article  : item.article.id,
                quantity : item.quantity,
                price    : item.article.price * item.quantity
            }

            items.push(obj)
        }

        const data = {
            'name'    :this.name,
            'email'   :this.email,
            'address' :this.address,
            'place'   :this.place,
            'items'   :items,
            'stripe_token':token.id,
        }
     await axios
        .post('/api/v1/checkout/',data)
        .then(response =>{
            this.$store.commit("clearCart")
            this.$route.push('/cart/success')

        })
        .catch(error =>{
            this.errors.push('algo salio mal, vuelva intentarlo')

            console.log(error)
        })

        this.$store.commit('setIsLoading',false)
        


        }
    },
    computed:{
        cartTotalPrice(){
            return this.cart.items.reduce((acc,curVal) =>{
                return acc += curVal.article.price * curVal.quantity
            },0)
        },
        
        cartTotalLength(){
            return this.cart.items.reduce((acc,curVal)=>{
                return acc += curVal.quantity
            },0)
        }
    }
}
</script>