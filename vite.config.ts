import { fileURLToPath, URL } from 'node:url'
import { defineConfig, UserConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { createHtmlPlugin } from 'vite-plugin-html';
import viteCompression from 'vite-plugin-compression';

function handleBase(mode: string) {
  if (mode === "production") return "/newmedia/2025/dalinpo/";
  else if (mode === "staging") return "/test/dalinpo2025/";
}

// https://vite.dev/config/
export default defineConfig(({ mode, command }) => {

  const config: UserConfig = {
    base: handleBase(mode),
    plugins: [vue(),
    // 壓縮插件(.gz)
    viteCompression(),
    // ejs 插件設定
    createHtmlPlugin({
      minify: true,
      inject: {
        data: {
          title: '【獨家AI分析】大林蒲最新空汙報告：PM2.5單月超標21天 揭國營3廠汙染濃度同步升降 | 專題 | 聯合報',
          description: '民進黨政府推動高雄大林蒲遷村至今8年，進度一再延宕，卻陸續擴建燃氣發電機組與洲際天然氣接收站（七接）。本報利用AI分析大林蒲PM2.5濃度，發現今年1月高達7成天數超標，風向分析更證明臨海工業區為汙染源。我們走進現場，探究國家工業發展及能源轉型，如何犧牲居民健康？大林蒲又將何去何從？',
          twitter_description: '民進黨政府推動高雄大林蒲遷村至今8年，進度一再延宕，卻陸續擴建燃氣發電機組與洲際天然氣接收站（七接）。本報利用AI分析大林蒲PM2.5濃度，發現今年1月高達7成天數超標，風向分析更證明臨海工業區為汙染源。我們走進現場，探究國家工業發展及能源轉型，如何犧牲居民健康？大林蒲又將何去何從？',
          keywords: '大林蒲,遷村,汙染,空汙,致癌物,PM2.5,國營,能源,獨家調查,AI,聯合報',
          url: 'https://vip.udn.com/newmedia/2025/dalinpo/',
          image: 'https://vip.udn.com/newmedia/2025/dalinpo/images/meta/fb_meta.jpg'
        }
      }
    })],
    optimizeDeps: {
      include: ["@udn-digital-center/common-components > vue-scrollto"],
    },
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      },
    },
    css: {
      preprocessorOptions: {
        scss: { additionalData: `@import "@/styles/_mixins.scss";` },
      },
    },
  }

  if (command === 'serve') {
    config.server = {
      allowedHosts: true,
    }
  }

  return config
})