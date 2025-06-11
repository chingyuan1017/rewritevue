<script setup lang="ts">
import {
  NmdHeader,
  NmdHeaderShare,
  NmdProgressbar,
  NmdMenu,
  NmdMenuItem,
  NmdHamburger,
  NmdFooter,
  NmdToTop,
  NmdFullReadMore,
} from '@udn-digital-center/common-components';
import InnerVoice from '@/components/InnerVoice';
import { IMG_URL_BASE } from '@/constants/path.ts';
import { shareURL_fb, shareURL_line, shareURL_twitter } from './utils/share.ts';
</script>

<template>
  <nmd-progressbar />
  <nmd-to-top />
  <nmd-menu>
    <nmd-menu-item :is-current="true" to="https://vip.udn.com/">
      篇章二
    </nmd-menu-item>
    <nmd-menu-item to="#">篇章三</nmd-menu-item>
    <nmd-menu-item to="#">篇章四</nmd-menu-item>
    <nmd-menu-item to="https://vip.udn.com/vip/index"
      >更多相關報導</nmd-menu-item
    >
  </nmd-menu>
  <nmd-header>
    <nmd-header-share
      :facebook="{ href: shareURL_fb }"
      :line="{ href: shareURL_line, target: '_blank' }"
      :twitter="{ href: shareURL_twitter }"
    />
    <nmd-hamburger></nmd-hamburger>
  </nmd-header>
  <main>
    <inner-voice
      text="(78)二次訪問，長期追蹤，大林蒲幼兒園前園長陳玉西，肺腺癌又復發，也有心血管疾病。二次訪問，長期追蹤，大林蒲幼兒園前園長陳玉西，肺腺癌又復發，也有心血管疾病。"
      :first-main-img="`${IMG_URL_BASE}/mob/webp/dalinpo2025_pic1_1_mob.webp`"
      :first-pad-img="`${IMG_URL_BASE}/pad/webp/dalinpo2025_pic1_1_pad@2x.webp`"
      :first-pc-img="`${IMG_URL_BASE}/pc/webp/dalinpo2025_pic1_1_pc@2x.webp`"
      :second-main-img="`${IMG_URL_BASE}/mob/webp/dalinpo2025_pic1_2_mob.webp`"
      :second-pad-img="`${IMG_URL_BASE}/pad/webp/dalinpo2025_pic1_2_pad@2x.webp`"
      :second-pc-img="`${IMG_URL_BASE}/pc/webp/dalinpo2025_pic1_2_pc@2x.webp`"
    />
    <inner-voice
      text="(79)二次訪問，長期追蹤，大林蒲幼兒園前園長陳玉西，肺腺癌又復發，也有心血管疾病。二次訪問，長期追蹤，大林蒲幼兒園前園長陳玉西，肺腺癌又復發，也有心血管疾病。"
      :first-main-img="`${IMG_URL_BASE}/mob/webp/dalinpo2025_pic2_1_mob@2x.webp`"
      :first-pad-img="`${IMG_URL_BASE}/pad/webp/dalinpo2025_pic2_1_pad@2x.webp`"
      :first-pc-img="`${IMG_URL_BASE}/pc/webp/dalinpo2025_pic2_1_pc@2x.webp`"
      :second-main-img="`${IMG_URL_BASE}/mob/webp/dalinpo2025_pic2_2_mob@2x.webp`"
      :second-pad-img="`${IMG_URL_BASE}/pad/webp/dalinpo2025_pic2_2_pad@2x.webp`"
      :second-pc-img="`${IMG_URL_BASE}/pc/webp/dalinpo2025_pic2_2_pc@2x.webp`"
    />
    <nmd-footer />
    <nmd-full-read-more
      title="霾葬大林蒲 獨家調查：16種致癌物圍城 694億遷村抹不去的罪"
      content="說明說明說明說明說明說明，說明說明說明說明說明說明，說明說明說明說明說明說明，說明說明說明說明說明說明，說明說明說明說明說明說明，說明說明說明說明說明說明，說明說明說明說明說明說明"
      img-src="https://fakeimg.pl/1280x720/282828/eae0d0/?retina=1&text=Dalinpo"
      href="#"
      horizontal="start"
    />
  </main>
</template>
