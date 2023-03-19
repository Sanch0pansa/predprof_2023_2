const planModule = {
    namespaced: true,
    state: () => ({
        waypoints: []
    }),

    actions: {
        getWaypoints({state, commit}) {
            fetch("127.0.0.1:8000/api/v1/waypoints/get_waypoints/").then(r => r.json()).then(r => {
                commit('waypoints', r);
            });
        },

        initWaypoints({state, commit}) {
            fetch("127.0.0.1:8000/api/v1/waypoints/init_waypoints/").then(r => r.json()).then(r => {
                commit('waypoints', r);
            });
        }
    }
}

export default planModule;