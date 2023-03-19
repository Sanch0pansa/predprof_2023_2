<script>
import {mapActions, mapState} from "vuex";

export default {
  name: "HomeView",
  methods: {
    ...mapActions({
      getWaypoints: "plan/getWaypoints"
    }),

  },

  state: {
    ...mapState({
      waypoints: "plan/waypoints"
    })
  },

  mounted() {
    this.getWaypoints();
  }
}
</script>

<template>
  <div class="row">
  <div class="col-6">
    <h1>Инициализация плана</h1>
    <div class="mt-3 mb-3">
      <button class="btn btn-primary">Получить новый план</button>
    </div>
    <h1>
      Сохранить и пересчитать расход
    </h1>
    <div class="mt-3 mb-3">
      <button class="btn btn-primary">Сохранить и пересчитать</button>
    </div>
  </div>
  <div class="col-6">
    <h1>Полётный план</h1>

    <ul class="list-group list-group-numbered my-3">
      <li v-for="(waypoint, i) in waypoints" class="list-group-item d-flex justify-content-between align-items-start">
        <div class="ms-2 me-auto">
          <div class="fw-bold">Пункт {{ i }}</div>
          <div class="d-flex">
            <span class="badge bg-primary rounded-pill">{{ waypoint.sh }} SH</span>
            <span class="badge bg-success rounded-pill">{{ waypoint.distance }} LY</span>
          </div>
        </div>
        <button class="btn btn-primary">Добавить пункт после
        </button>
      </li>
    </ul>
  </div>
  </div>
</template>
