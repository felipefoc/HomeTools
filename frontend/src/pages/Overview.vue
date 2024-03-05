<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xl-2">
          <stats-card @click="openInNewTab('http://casadofocky.ddns.net:8989')">
            <div slot="header" class="icon-warning">
              <i class="nc-icon nc-chart text-warning"></i>
            </div>
            <div slot="content">
              <h4 class="card-title">Sonarr</h4>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-2">
          <stats-card @click="openInNewTab('http://casadofocky.ddns.net:7878')">
            <div slot="header" class="icon-success">
              <i class="nc-icon nc-light-3 text-success"></i>
            </div>
            <div slot="content">
              <h4 class="card-title">Radarr</h4>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-2">
          <stats-card @click="openInNewTab('http://casadofocky.ddns.net:8096')"><
            <div slot="header" class="icon-danger">
              <i class="nc-icon nc-vector text-danger"></i>
            </div>
            <div slot="content">
              <h4 class="card-title">Jellyfin</h4>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-2">
          <stats-card @click="openInNewTab('http://casadofocky.ddns.net:8989')">
            <div slot="header" class="icon-info">
              <i class="nc-icon nc-favourite-28 text-primary"></i>
            </div>
            <div slot="content">
              <h4 class="card-title">Teste</h4>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-2">
          <stats-card>
            <div slot="header" class="icon-info">
              <i class="nc-icon nc-favourite-28 text-primary"></i>
            </div>
            <div slot="content">
              <h4 class="card-title">Teste</h4>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-2">
          <stats-card>
            <div slot="header" class="icon-info">
              <i class="nc-icon nc-favourite-28 text-primary"></i>
            </div>
            <div slot="content">
              <h4 class="card-title">Teste</h4>
            </div>
          </stats-card>
        </div>

      </div>
    
    </div>
  </div>
</template>
<script>
  import ChartCard from 'src/components/Cards/ChartCard.vue'
  import StatsCard from 'src/components/Cards/StatsCard.vue'
  import LTable from 'src/components/Table.vue'

  export default {
    components: {
      LTable,
      ChartCard,
      StatsCard
    },
    methods: {
      openInNewTab(url) {
        window.open(url, '_blank');
      }
    },
  }
</script>
<style>

</style>
