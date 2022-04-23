const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
})

const path = require('path')

module.exports = {
  assetsDir: '../static',
  publicPath: undefined,
  outputDir: path.resolve(__dirname, '../../backend/RAMMN/templates'),
  runtimeCompiler: undefined,
  productionSourceMap: undefined,
  parallel: undefined,
  css: undefined,
}
