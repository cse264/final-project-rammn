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
    var numUsers = 31;
    var numSearches = 65;
    return {
      numUsers,
      numSearches,
    }
  },
  setup() {
    const recentSearches = [
      {
        user: '5e91a',
        search: 'https://i.redd.it/zaqxjbuvwdx81.jpg',
        time: '2022-05-04 12:51:07',
      },
      {
        user: '5e91a',
        search: 'https://i.redd.it/0i9mv63c7la31.jpg',
        time: '2022-05-04 12:51:07',
      },
      {
        user: '5e91a',
        search: 'https://www.reddit.com/r/AskReddit/comments/uhze53/whats_stopping_you_from_having_sex/',
        time: '2022-05-04 12:51:07',
      },
      {
        user: '5e91a',
        search: 'https://i.redd.it/gzvw9bb7psw81.jpg',
        time: '2022-05-04 12:51:07',
      },
      {
        user: '5e91a',
        search: 'https://www.reddit.com/live/18hnzysb1elcs',
        time: '2022-05-04 12:51:07',
      },
      {
        user: '5e91a',
        search: 'https://v.redd.it/l0e20b6ktdx81',
        time: '2022-05-04 12:51:07',
      },
      {
        user: '86fb8',
        search: 'https://www.reddit.com/gallery/ui51zq',
        time: '2022-05-04 12:39:23',
      },
      {
        user: '86fb8',
        search: 'https://v.redd.it/s02clyst7fx81',
        time: '2022-05-04 12:39:23',
      },
      {
        user: '86fb8',
        search: 'https://www.reddit.com/r/AskReddit/comments/ui2a0b/what_is_your_goto_small_talk_topic_with_strangers/',
        time: '2022-05-04 12:39:23',
      },
      {
        user: '86fb8',
        search: 'https://itsgoingdown.org/anarchist-and-autonomous-formations-hit-the-streets-of-mexico-city-on-may-day/',
        time: '2022-05-04 12:39:23',
      },
    ]

    const recentUsers = [
      {
        id: '5e91a',
        user: 'cpattissons',
        time: '2022-05-04 12:51:07',
      },
      {
        id: '86fb8',
        user: 'gshergoldt',
        time: '2022-05-04 12:39:23',
      },
      {
        id: '540b9',
        user: 'wdater',
        time: '2022-05-04 12:39:23',
      },
      {
        id: 'ec155',
        user: 'clightbournq',
        time: '2022-05-04 12:39:23',
      },
      {
        id: 'e00cc',
        user: 'aantrago',
        time: '2022-05-04 12:39:23',
      },
      {
        id: 'd505e',
        user: 'bjukubczakn',
        time: '2022-05-04 12:39:23',
      },
      {
        id: '5e95b',
        user: 'dcoughlanm',
        time: '2022-05-04 12:39:23',
      },
      {
        id: '7370e',
        user: 'aoluneyl',
        time: '2022-05-04 12:39:23',
      },
      {
        id: '5070e',
        user: 'jdowlingj',
        time: '2022-05-04 12:39:23',
      },
      {
        id: 'f5afc',
        user: 'biacopettig',
        time: '2022-05-04 12:39:23',
      },
    ]

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
      recentSearches,
      recentUsers,
      topUsers,
    }
  },
}
</script>
