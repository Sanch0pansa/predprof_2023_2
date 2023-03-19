import { createApp } from 'vue'
import { createStore } from 'vuex'
import planModule from "@/store/planModule";
import consumptionModule from "@/store/consumptionModule";

// Create a new store instance.
const store = createStore({
    state () {
        return {
            plan: [],
            consumptions: {
                resources: {},
                waypoints: [
                    [

                    ]
                ]
            }
        }
    },

    modules: {
        plan: planModule,
        consumptions: consumptionModule
    }
})

const app = createApp({ /* your root component */ })

// Install the store instance as a plugin
app.use(store)