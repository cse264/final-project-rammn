<template>
  <div>
    <CRow class="justify-content-center">
      <CCol :xs="8">
        <div class="d-grip gap-2">
          <CButton color="secondary" shape="rounded-pill" size="lg">
            <CRow>
              <CCol :xs="2">
                <CImage :src="die" height="100"/>
              </CCol>
              <CCol :xs="10">
                <p color="primary">Roll the die to find something fun!</p>
              </CCol>
            </CRow>
          </CButton>
        </div>
      </CCol>
    </CRow>
  </div>
</template>

<script>
import die from '@/assets/images/die.png'
export default {
  name: 'AppHeader',
  components: {},
  setup() {
    return {
      die,
    }
  },
}
</script>
