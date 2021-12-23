<template>
    <div class="page-sign-up">
         <div class="columns">
             <div class="column is-4 is-offset-4">
                   
                   <h1 class="title">Registrarse</h1>

                <form @submit.prevent="submitForm">
                   <div class="field">
                       <label>Usuario</label>
                       <div class="control">
                           <input type="text" class="input" v-model="username">
                       </div>
                   </div>

                    <div class="field">
                       <label>Contraseña</label>
                       <div class="control">
                           <input type="password" class="input" v-model="password">
                       </div>
                   </div>

                    <div class="field">
                       <label>Repetir Contraseña</label>
                       <div class="control">
                           <input type="password" class="input" v-model="password2">
                       </div>
                   </div>

                   <div class="notification is-danger" v-if="errors.length">
                       <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                   </div>

                   <div class="field">
                       <div class="control">
                           <button class="button is-danger is-light">Registrar</button>
                       </div>
                   </div>
                   <hr>
                   o <router-link to="/login">presione aquí</router-link> para ingresar
                </form>

             </div>
         </div>
    </div>
</template>

<script>
import axios   from 'axios'
import {toast} from 'bulma-toast'

export default {
    name: 'SignUp',
    data(){
        return{
            username:'',
            password:'',
            password2:'',
            errors: []
        }
    },

    methods:{
        submitForm(){
            this.errors = []

            if (this.username ===''){
                this.errors.push('no existe nombre de usuario')
            }

            if (this.password ===''){
                this.errors.push('contraseña muy corta')
            }

            if (this.password !== this.password2){
                this.errors.push('las contraseñas no coinciden')
            }

            if (!this.errors.length){
                const formData ={
                    username : this.username,
                    password : this.password

                }

                axios
                  .post("/api/v1/users/", formData)
                  .then(response =>{
                      toast({
                          message     :'cuenta creada, proceda a ingresar',
                          type        :'is-success',
                          dismissible :true,
                          pauseOnHover:true,
                          duration    :2000,
                          position    :'top-left',

                      })
                      this.$router.push('/login ')
                  })
                  .catch(error =>{
                      if(error.response){
                          for(const property in error.response.data){
                              this.errors.push(`${property}: ${error.response.data[property]}`)
                          }

                          console.log(JSON.stringify(error.response.data))
                      } else if(error.message){
                             this.errors.push('hubo un problema, intentelo nuevamente')

                             console.log(JSON.stringify(error))
                      }
                  })
            }
        }
    }
}
</script>