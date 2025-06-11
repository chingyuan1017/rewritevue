<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue';
import { IMG_URL_BASE } from '@/constants/path';

const captionRef = ref<HTMLDivElement | null>();
const headerRef = ref<HTMLHeadElement | null>();
const captionMarginTopPosition = ref<number>();

onMounted(() => {
  nextTick(() => {
    const captionPaddingTop = window.getComputedStyle(
      captionRef.value as HTMLDivElement,
    ).paddingTop;
    const headerHeight = headerRef.value!.offsetHeight;
    captionMarginTopPosition.value = parseInt(captionPaddingTop) + headerHeight;
  });
});
</script>

<template>
  <section class="intro">
    <div class="intro-video">
      <video
        muted
        autoplay
        loop
        playsinline
        :poster="`${IMG_URL_BASE}/pc/dalinpo2025_video4_preview_pc.jpg`"
        class="intro-video"
      >
        <source
          :src="`${IMG_URL_BASE}/pc/dalinpo2025_video4_pc.mp4`"
          type="video/mp4"
        />
      </video>
    </div>
    <div
      class="intro-caption"
      ref="captionRef"
      :style="{
        '--caption-margin-top-position': `-${captionMarginTopPosition}px`,
      }"
    >
      <div class="intro-container">
        <header class="intro-header" ref="headerRef">
          <h1 class="intro-header-title">大林蒲二部曲</h1>
          <p class="intro-header-describe">
            副標副標副標副標副標副標副標副標副標副標副標副標
          </p>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="31"
            viewBox="0 0 32 31"
            fill="none"
          >
            <path
              d="M0.999634 15.0302L15.9996 30.0302L30.9996 15.0302"
              stroke="currentColor"
              stroke-linejoin="round"
            />
          </svg>
        </header>
        <footer class="intro-footer">
          <p class="intro-footer-content">
            導言導言導言導言導言導言，導言導言導言導言導言導言導言導言，導言導言導言導言導言導言導言導言導言導言導言。導言導言導言導言導言導言，導言導言導言導言導言導言導言導言，導言導言導言導言導言導言導言。
          </p>
          <p class="intro-footer-content">
            導言導言導言導言導言導言，導言導言導言導言導言導言導言導言，導言導言導言導言導言導言導言導言導言導言導言。導言導言導言導言導言導言，導言導言導言導言導言導言導言導言，導言導言導言導言導言導言導言。
          </p>
          <p class="intro-footer-content">
            導言導言導言導言導言導言，導言導言導言導言導言導言導言導言，導言導言導言導言導言導言導言導言導言導言導言。導言導言導言導言導言導言，導言導言導言導言導言導言導言導言，導言導言導言導言導言導言導言。
          </p>
        </footer>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import './IntroSection.scss';
</style>
