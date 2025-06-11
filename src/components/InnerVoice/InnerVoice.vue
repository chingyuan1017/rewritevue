<script lang="ts" setup>
import { ref, onMounted } from 'vue';

const contentRef = ref();
const contentHeight = ref();
const darkImage = ref();

const props = withDefaults(
  defineProps<{
    text: string;
    cardHalf?: boolean;
    firstMainImg: string;
    firstPadImg?: string;
    firstPcImg?: string;
    secondMainImg: string;
    secondPadImg?: string;
    secondPcImg?: string;
  }>(),
  {
    cardHalf: false,
  },
);

onMounted(() => {
  contentHeight.value = contentRef.value.offsetHeight;
  const cardTriggerHeight = props.cardHalf ? 3.5 : 2;

  window.addEventListener('scroll', () => {
    const windowDistance = window.scrollY;
    const windowInnerHeight = window.innerHeight / cardTriggerHeight;
    const contentBounding =
      contentRef.value.getBoundingClientRect().top + windowDistance;
    if (windowDistance >= contentBounding - windowInnerHeight) {
      darkImage.value.style.opacity = 1;
    } else {
      darkImage.value.style.opacity = 0;
    }
  });
});
</script>

<template>
  <section
    class="inner-voice"
    :style="{ '--total-height': `calc(200dvh + ${contentHeight + 100}px)` }"
  >
    <div class="inner-voice-bg">
      <picture class="inner-voice-pic">
        <source media="(min-width: 1280px)" :srcset="firstPcImg" />
        <source media="(min-width: 768px)" :srcset="firstPadImg" />
        <img
          :src="firstMainImg"
          alt=""
          class="inner-voice-img first"
          decoding="async"
        />
      </picture>
      <picture class="inner-voice-pic">
        <source media="(min-width: 1280px)" :srcset="secondPcImg" />
        <source media="(min-width: 768px)" :srcset="secondPadImg" />
        <img
          :src="secondMainImg"
          alt=""
          class="inner-voice-img second"
          ref="darkImage"
          decoding="async"
        />
      </picture>
    </div>
    <div
      class="inner-voice-card"
      :class="{ 'inner-voice-card-half': cardHalf }"
    >
      <article class="inner-voice-content" ref="contentRef">
        <p class="inner-voice-text">
          {{ text }}
        </p>
      </article>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import './InnerVoice.scss';
</style>
