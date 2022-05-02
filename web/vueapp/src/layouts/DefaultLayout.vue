<template>
  <div>
    <!-- <AppSidebar /> -->
    <div class="wrapper d-flex flex-column min-vh-100 bg-light">
      <AppHeader />
      <div class="body flex-grow-1 px-3">
        <CContainer lg>
          <router-view />
        </CContainer>
      </div>
      <AppFooter />
    </div>
  </div>
</template>
<script>
import { CContainer } from '@coreui/vue'
import AppFooter from '@/components/AppFooter.vue'
import AppHeader from '@/components/AppHeader.vue'

export default {
  name: 'DefaultLayout',
  components: {
    AppFooter,
    AppHeader,
    CContainer,
  },
}
</script>
