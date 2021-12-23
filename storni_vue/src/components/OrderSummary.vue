<template>
    <div class="box mb-4">
        <h3 class="is-size-4 mb-6">Orden #{{order.id}}</h3>
        <h4 class="is-size-5">Articulos</h4>

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
                v-for="item in order.items"
                v-bind:key="item.article.id"
                >

                <td>{{item.article.title}}</td>
                <td>{{item.article.price}}</td>
                <td>{{item.quantity}}</td>
                <td>${{getItemTotal(item).toFixed(2)}}</td>
                </tr>

            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'OrderSummary',
    props:{
        order: Object
    },

    methods:{
        getItemTotal(item){
            return item.quantity * item.article.price
        },
        orderTotalLength(order){
            return order.items.reduce((acc,curVal) => {
                return acc += curVal.quantity
            },0)
        }
    },

}
</script>