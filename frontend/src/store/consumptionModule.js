const consumptionModule = {
    namespaced: true,
    state: () => ({
        days: []
    }),

    actions: {
        getConsumption({state, commit}) {
            fetch("127.0.0.1:8000/api/v1/waypoints/get_consumptions/").then(r => r.json()).then(r => {
                commit('days', r.days);
            });
        }
    }
}

export default consumptionModule;