<template>
  <div class="arda">
    <p>HIIII</p>
    <div class="tmp">
      <l-map style="height: 350px" :crs="crs" :options="{ zoomControl: false }">
        <l-image-overlay :url="url" :bounds="bounds"></l-image-overlay>
      </l-map>
    </div>
  </div>
</template>

<script>
import L from "leaflet";
import { LMap, LImageOverlay } from "vue2-leaflet";

export default {
  name: "ArdaMap",
  components: {
    LMap,
    LImageOverlay,
  },
  data() {
    return {
      url: "https://images.unsplash.com/photo-1524661135-423995f22d0b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1174&q=80",
      bounds: [
        [-26.5, -25],
        [1021.5, 1023],
      ],
      crs: L.CRS.Simple,
    };
  },
  methods: {},
};
</script>

<style>
.tmp {
  width: 500px;
  height: 500px;
}
</style>
