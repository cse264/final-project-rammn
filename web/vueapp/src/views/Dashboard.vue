<template>
  <div>
    <CRow>
      <CCol :xs="6">
        <CWidgetStatsF color="primary" :padding="false" title="Users" :value="numUsers">
          <template #icon>
            <CIcon icon="cil-user" size="xl" />
          </template>
        </CWidgetStatsF>
      </CCol>
      <CCol :xs="6">
        <CWidgetStatsF color="secondary" :padding="false" title="Searches" :value="numSearches">
          <template #icon>
            <CIcon icon="cil-magnifying-glass" size="xl" />
          </template>
        </CWidgetStatsF>
      </CCol>
    </CRow>
    <br />
    <CRow>
      <CCol :md="6">
        <CCard class="mb-4">
          <CCardHeader>Recent Users</CCardHeader>
          <CCardBody>
            <CTable align="middle" class="mb-0 border" hover responsive>
              <CTableHead color="light">
                <CTableRow>
                  <CTableHeaderCell>User ID</CTableHeaderCell>
                  <CTableHeaderCell>Username</CTableHeaderCell>
                  <CTableHeaderCell>Last Access</CTableHeaderCell>
                </CTableRow>
              </CTableHead>
              <CTableBody>
                <CTableRow v-for="item in recentUsers" :key="item.name">
                  <CTableDataCell>
                    <div>{{ item[0] }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item[1] }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item[2] }}</div>
                  </CTableDataCell>
                </CTableRow>
              </CTableBody>
            </CTable>
          </CCardBody>
        </CCard>
      </CCol>
      <CCol :md="6">
        <CCard class="mb-4">
          <CCardHeader>Most Searches</CCardHeader>
          <CCardBody>
            <CTable align="middle" class="mb-0 border" hover responsive>
              <CTableHead color="light">
                <CTableRow>
                  <CTableHeaderCell>User ID</CTableHeaderCell>
                  <CTableHeaderCell>Number of Searches</CTableHeaderCell>
                </CTableRow>
              </CTableHead>
              <CTableBody>
                <CTableRow v-for="item in topUsers" :key="item.name">
                  <CTableDataCell>
                    <div>{{ item[0] }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item[1] }}</div>
                  </CTableDataCell>
                </CTableRow>
              </CTableBody>
            </CTable>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
    <CRow>
      <CCol :md="12">
        <CCard class="mb-4">
          <CCardHeader>Recent Searches</CCardHeader>
          <CCardBody>
            <CTable align="middle" class="mb-0 border" hover responsive>
              <CTableHead color="light">
                <CTableRow>
                  <CTableHeaderCell>User ID</CTableHeaderCell>
                  <CTableHeaderCell>Search</CTableHeaderCell>
                  <CTableHeaderCell>Time</CTableHeaderCell>
                </CTableRow>
              </CTableHead>
              <CTableBody>
                <CTableRow v-for="item in recentSearches" :key="item.name">
                  <CTableDataCell>
                    <div>{{ item[0] }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item[1] }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item[2] }}</div>
                  </CTableDataCell>
                </CTableRow>
              </CTableBody>
            </CTable>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      numUsers: 0,
      numSearches: 0,
      recentSearches: [],
      recentUsers: [],
      topUsers: [],
      timer: "",
    }
  },
  created() {
    this.fetchData();
    this.timer = setInterval(this.fetchData, 60000);
  }, 
  methods: {
    async fetchData() {
      this.numUsers = await fetch("/users/count").then(response => response.json()).then(data => data);
      this.numSearches = await fetch("/users/searches").then(response => response.json()).then(data => data);
      this.recentSearches = await fetch("/users/search/history").then(response => response.json()).then(data => data);
      this.recentUsers = await fetch("/users/activity").then(response => response.json()).then(data => data);
      this.topUsers = await fetch("/users/volume").then(response => response.json()).then(data => data);
    },
    cancelAutoUpdate() {
      clearInterval(this.timer);
    },
  },
  beforeUnmount() {
    this.cancelAutoUpdate();
  },
}
</script>
