<template>
  <div>
    <CRow>
      <CCol :xs="6">
        <CWidgetStatsF color="primary" :padding="false" title="Users" value="31">
          <template #icon>
            <CIcon icon="cil-user" size="xl" />
          </template>
        </CWidgetStatsF>
      </CCol>
      <CCol :xs="6">
        <CWidgetStatsF color="secondary" :padding="false" title="Searches" value="65">
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
                    <div>{{ item.id }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.user }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.time }}</div>
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
                    <div>{{ item.user }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.searches }}</div>
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
                    <div>{{ item.user }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.search }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.time }}</div>
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
  async data() {
    var numUsers = await fetch("/users/count").then(response => response.json()).then(data => data);
    console.log(numUsers);
    var numSearches = await fetch("/users/searches").then(response => response.json()).then(data => data);
    console.log(numSearches);

    var recentSearches = []
    var temp1 = await fetch("/users/search/history").then(response => response.json()).then(data => data);
    console.log(temp1);
    for (let i = 0; i < temp1.length; i++) {
      recentSearches.push({});
      recentSearches[i].user = temp1[i][0];
      recentSearches[i].search = temp1[i][1];
      recentSearches[i].time = temp1[i][2];
    }
    var recentUsers = []
    var temp2 = await fetch("/users/activity").then(response => response.json()).then(data => data);
    console.log(temp2);
    for (let i = 0; i < temp2.length; i++) {
      recentUsers.push({});
      recentUsers[i].id = temp2[i][0];
      recentUsers[i].user = temp2[i][1];
      recentUsers[i].time = temp2[i][2];
    }
    // var topUsers = []
    // var temp3 = await fetch("/users/volume").then(response => response.json()).then(data => data);
    // console.log(temp3);
    return {
      numUsers,
      numSearches,
      recentSearches,
      recentUsers,
      // topUsers,
    }
  },
  setup() {

    const topUsers = [
      {
        user: '5e91a',
        searches: 4,
      },
      {
        user: '86fb8',
        searches: 2,
      },
      {
        user: '540b9',
        searches: 2,
      },
      {
        user: 'ec155',
        searches: 2,
      },
      {
        user: 'e00cc',
        searches: 1,
      },
      {
        user: 'd505e',
        searches: 1,
      },
      {
        user: '5e95b',
        searches: 1,
      },
      {
        user: '7370e',
        searches: 1,
      },
      {
        user: '5070e',
        searches: 1,
      },
      {
        user: 'f5afc',
        searches: 1,
      },
    ]

    return {
      topUsers,
    }
  },
}
</script>
