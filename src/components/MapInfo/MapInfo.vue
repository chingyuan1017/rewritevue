<script lang="ts" setup>
import { ref, onMounted, type Ref } from 'vue';
import { useEventListener } from '@vueuse/core';

const contentRef1 = ref();
const contentRef2 = ref();
const contentRef3 = ref();

const contentHeight1 = ref();
const contentHeight2 = ref();
const contentHeight3 = ref();
const picSpace = ref();

const secondImg = ref();
const thirdImg = ref();

defineProps<{
  text1: string;
  text2: string;
  text3: string;
  firstMainImg: string;
  firstPadImg?: string;
  firstPcImg?: string;
  secondMainImg: string;
  secondPadImg?: string;
  secondPcImg?: string;
  thirdMainImg: string;
  thirdPadImg?: string;
  thirdPcImg?: string;
}>();

onMounted(() => {
  contentHeight1.value = contentRef1.value.offsetHeight;
  contentHeight2.value = contentRef2.value.offsetHeight;
  contentHeight3.value = contentRef3.value.offsetHeight;
  picSpace.value = window.innerHeight;

  useEventListener(window, 'scroll', () => {
    const windowDistance = window.scrollY;

    // 這邊先這樣處理，如果之後要加，在考慮抽象
    const contentBounding =
      contentRef1.value.getBoundingClientRect().top + windowDistance;
    if (windowDistance >= contentBounding) {
      transitionInOut(secondImg, 1, 0.5);
    } else {
      transitionInOut(secondImg, 0, 0.5);
    }

    const contentBounding2 =
      contentRef2.value.getBoundingClientRect().top + windowDistance;
    if (windowDistance >= contentBounding2) {
      transitionInOut(thirdImg, 1, 0.5);
    } else {
      transitionInOut(thirdImg, 0, 0.5);
    }
  });
});

// TODO 要怎樣過度效果，再者邊丟給CSS處理，或是直接寫在CSS，看之後PM要求
const transitionInOut = (
  imageEntity: Ref<HTMLImageElement | undefined>,
  opacity: number,
  duration: number,
) => {
  if (imageEntity.value) {
    imageEntity.value.style.opacity = `${opacity}`;
    imageEntity.value.style.transition = `all ${duration}s ease`;
  }
};
</script>

<template>
  <section
    class="map-info"
    :style="{
      '--total-height': `calc(200dvh + ${
        contentHeight2 + contentHeight3 + picSpace * 2
      }px)`,
    }"
  >
    <div class="map-info-bg">
      <picture class="map-info-pic">
        <source media="(min-width: 1280px)" :srcset="firstPcImg" />
        <source media="(min-width: 768px)" :srcset="firstPadImg" />
        <img
          :src="firstMainImg"
          alt=""
          class="map-info-img first"
          loading="lazy"
          decoding="async"
        />
      </picture>
      <picture class="map-info-pic">
        <source media="(min-width: 1280px)" :srcset="secondPcImg" />
        <source media="(min-width: 768px)" :srcset="secondPadImg" />
        <img
          :src="secondMainImg"
          alt=""
          class="map-info-img second"
          ref="secondImg"
          loading="lazy"
          decoding="async"
        />
      </picture>
      <picture class="map-info-pic">
        <source media="(min-width: 1280px)" :srcset="thirdPcImg" />
        <source media="(min-width: 768px)" :srcset="thirdPadImg" />
        <img
          :src="thirdMainImg"
          alt=""
          class="map-info-img third"
          ref="thirdImg"
          loading="lazy"
          decoding="async"
        />
      </picture>
    </div>
    <div class="map-info-card1">
      <article class="map-info-content" ref="contentRef1">
        <p class="map-info-text">
          <span v-html="text1"></span>
        </p>
      </article>
    </div>
    <div
      class="map-info-card2"
      :style="{ '--topSpace2': `calc(${picSpace * 2 + 100}px)` }"
    >
      <article class="map-info-content" ref="contentRef2">
        <p class="map-info-text">
          <span v-html="text2"></span>
        </p>
      </article>
    </div>
    <div
      class="map-info-card3"
      :style="{ '--topSpace3': `calc( ${picSpace * 3 + 100}px)` }"
    >
      <article class="map-info-content" ref="contentRef3">
        <p class="map-info-text">
          <span v-html="text3"></span>
        </p>
      </article>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import './MapInfo.scss';
</style>
