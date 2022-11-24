<template>
  <div class="arda">
    <p>HIIII</p>
    <div class="tmp">
      <l-map :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      </l-map>
    </div>
  </div>
</template>

<script>
// import L from "leaflet";
import { LMap, LTileLayer } from "vue2-leaflet";

export default {
  name: "ArdaMap",
  components: {
    LMap,
    LTileLayer,
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 8,
      center: [47.31322, -1.319482],
    };
  },
  methods: {},
};
</script>

<style>
.tmp {
  width: 100%;
  height: 400px;
}
</style>
