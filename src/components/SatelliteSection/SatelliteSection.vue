<script lang="ts" setup>
import { useTemplateRef, onMounted, ref, nextTick, watch } from 'vue';
import {
  useIntersectionObserver,
  useEventListener,
  type MaybeElement,
} from '@vueuse/core';

import { IMG_URL_BASE } from '@/constants/path';

const emptyCount = ref<number>(0);
const videoDevice = ref<string>('');
const scrollCardHeightSet = ref<number[]>([]);

const emptyTotalRef = useTemplateRef<HTMLElement[]>('emptyTotalRef');
const bgRef = useTemplateRef<HTMLElement | null>('bgRef');
const taiwanIn = useTemplateRef<HTMLVideoElement | null>('taiwanIn');
const dalinpoIn = useTemplateRef<HTMLVideoElement | null>('dalinpoIn');
const threeDigitalIn = useTemplateRef<HTMLVideoElement | null>(
  'threeDigitalIn',
);
const zoomOut = useTemplateRef<HTMLVideoElement | null>('zoomOut');
const satellite = useTemplateRef<null>('satellite');

const isSatelliteShow = ref<boolean>(false);

// IntersectionObserver Config
const observerRoot = {
  root: bgRef.value,
  rootMargin: '0px 0px -100% 0px',
};

const observerCallback = ([entry]: IntersectionObserverEntry[]) => {
  const { index } = (entry.target as HTMLElement).dataset;
  const { isIntersecting, boundingClientRect } = entry;

  const currentIndex = Number(index);

  if (isIntersecting && boundingClientRect.top <= 0) {
    if (currentIndex === 0) {
      (bgRef.value!.children[1] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[2] as HTMLElement).style.opacity = '0';
    }

    if (currentIndex === 1) {
      (bgRef.value!.children[1] as HTMLElement).style.opacity = '1';
      (bgRef.value!.children[2] as HTMLElement).style.opacity = '1';
      (bgRef.value!.children[3] as HTMLElement).style.opacity = '0';
    }

    if (currentIndex === 2) {
      (bgRef.value!.children[1] as HTMLElement).style.opacity = '1';
      (bgRef.value!.children[2] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[3] as HTMLElement).style.opacity = '1';
      (bgRef.value!.children[4] as HTMLElement).style.opacity = '0';
    }

    if (currentIndex === 3) {
      (bgRef.value!.children[1] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[2] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[3] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[5] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[4] as HTMLElement).style.opacity = '1';
    }

    if (currentIndex === 4) {
      (bgRef.value!.children[4] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[7] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[8] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[5] as HTMLElement).style.opacity = '0';

      const { duration, currentTime } = taiwanIn.value as HTMLVideoElement;

      if (duration === currentTime || currentTime !== 0) {
        taiwanIn.value?.pause();
        const taiwanInInterval = setInterval(() => {
          taiwanIn.value!.currentTime -= 0.1;

          if (taiwanIn.value!.currentTime === 0) {
            (bgRef.value!.children[5] as HTMLElement).style.opacity = '0';
            clearInterval(taiwanInInterval);
          }
        }, 50);
      }
    }

    if (currentIndex === 5) {
      const { duration, currentTime } = taiwanIn.value as HTMLVideoElement;
      (bgRef.value!.children[5] as HTMLElement).style.opacity = '0';
      if (duration !== currentTime) {
        taiwanIn.value?.play();
      }
    }

    if (currentIndex === 6) {
      (bgRef.value!.children[0] as HTMLElement).style.zIndex = '-2';
      (bgRef.value!.children[6] as HTMLElement).style.zIndex = '-3';
      const { duration, currentTime } = taiwanIn.value as HTMLVideoElement;

      if (duration !== currentTime) {
        taiwanIn.value?.play();
        const taiwanVideoListener = useEventListener(
          taiwanIn.value,
          'ended',
          () => {
            (bgRef.value!.children[5] as HTMLElement).style.opacity = '1';

            taiwanVideoListener();
          },
        );
      }

      if (duration === currentTime) {
        (bgRef.value!.children[5] as HTMLElement).style.opacity = '1';
      }
    }

    if (currentIndex === 7) {
      const { duration: dalinpoDuration, currentTime: dalinpoTime } =
        dalinpoIn.value as HTMLVideoElement;
      const { duration: taiwanDuration, currentTime: taiwanCurrent } =
        taiwanIn.value as HTMLVideoElement;

      (bgRef.value!.children[5] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[0] as HTMLElement).style.zIndex = '-3';
      (bgRef.value!.children[6] as HTMLElement).style.zIndex = '-2';

      if (dalinpoDuration === dalinpoTime || dalinpoTime !== 0) {
        dalinpoIn.value!.pause();
        const dalinpoInInterval = setInterval(() => {
          dalinpoIn.value!.currentTime -= 0.1;

          if (dalinpoIn.value!.currentTime === 0) {
            clearInterval(dalinpoInInterval);
          }
        }, 50);
      }

      if (taiwanDuration !== taiwanCurrent) {
        taiwanIn.value!.currentTime = taiwanIn.value!.duration;
      }
    }

    if (currentIndex === 8) {
      const { duration, currentTime } = dalinpoIn.value as HTMLVideoElement;
      (bgRef.value!.children[5] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[0] as HTMLElement).style.zIndex = '-3';
      (bgRef.value!.children[6] as HTMLElement).style.zIndex = '-2';
      (bgRef.value!.children[7] as HTMLElement).style.opacity = '0';

      if (duration !== currentTime) {
        dalinpoIn.value?.play();
        const taiwanVideoListener = useEventListener(
          dalinpoIn.value,
          'ended',
          () => {
            taiwanVideoListener();
          },
        );
      }
    }

    if (currentIndex === 9) {
      const { duration, currentTime } = dalinpoIn.value as HTMLVideoElement;
      (bgRef.value!.children[0] as HTMLElement).style.zIndex = '-3';
      (bgRef.value!.children[6] as HTMLElement).style.zIndex = '-2';
      (bgRef.value!.children[7] as HTMLElement).style.opacity = '1';
      (bgRef.value!.children[8] as HTMLElement).style.opacity = '0';

      if (duration !== currentTime) {
        dalinpoIn.value?.play();
        const taiwanVideoListener = useEventListener(
          dalinpoIn.value,
          'ended',
          () => {
            taiwanVideoListener();
          },
        );
      }
    }

    if (currentIndex === 10) {
      const { duration, currentTime } = dalinpoIn.value as HTMLVideoElement;
      (bgRef.value!.children[0] as HTMLElement).style.zIndex = '-3';
      (bgRef.value!.children[6] as HTMLElement).style.zIndex = '-2';
      (bgRef.value!.children[9] as HTMLElement).style.zIndex = '-3';

      (bgRef.value!.children[7] as HTMLElement).style.opacity = '1';
      (bgRef.value!.children[8] as HTMLElement).style.opacity = '1';

      if (duration !== currentTime) {
        dalinpoIn.value?.play();
        const taiwanVideoListener = useEventListener(
          dalinpoIn.value,
          'ended',
          () => {
            taiwanVideoListener();
          },
        );
      }
    }

    if (currentIndex === 11) {
      const { duration, currentTime } =
        threeDigitalIn.value as HTMLVideoElement;
      (bgRef.value!.children[7] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[8] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[6] as HTMLElement).style.zIndex = '-3';
      (bgRef.value!.children[9] as HTMLElement).style.zIndex = '-2';

      if (duration === currentTime || currentTime !== 0) {
        threeDigitalIn.value?.pause();

        const threeDigitalInterval = setInterval(() => {
          threeDigitalIn.value!.currentTime -= 0.1;

          if (threeDigitalIn.value!.currentTime === 0) {
            clearInterval(threeDigitalInterval);
          }
        }, 50);
      }
    }

    if (currentIndex === 12) {
      (bgRef.value!.children[9] as HTMLElement).style.zIndex = '-2';
      (bgRef.value!.children[10] as HTMLElement).style.opacity = '0';
      const { duration, currentTime } =
        threeDigitalIn.value as HTMLVideoElement;

      if (duration !== currentTime) {
        threeDigitalIn.value?.play();
        const taiwanVideoListener = useEventListener(
          threeDigitalIn.value,
          'ended',
          () => {
            taiwanVideoListener();
          },
        );
      }
    }

    if (currentIndex === 13) {
      (bgRef.value!.children[9] as HTMLElement).style.zIndex = '-2';
      (bgRef.value!.children[10] as HTMLElement).style.opacity = '1';
      (bgRef.value!.children[11] as HTMLElement).style.opacity = '0';

      const { duration, currentTime } =
        threeDigitalIn.value as HTMLVideoElement;

      if (duration !== currentTime) {
        threeDigitalIn.value?.play();
        const taiwanVideoListener = useEventListener(
          threeDigitalIn.value,
          'ended',
          () => {
            taiwanVideoListener();
          },
        );
      }
    }

    if (currentIndex === 14) {
      (bgRef.value!.children[9] as HTMLElement).style.zIndex = '-2';
      (bgRef.value!.children[10] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[11] as HTMLElement).style.opacity = '1';
      (bgRef.value!.children[12] as HTMLElement).style.opacity = '0';
    }

    if (currentIndex === 15) {
      (bgRef.value!.children[9] as HTMLElement).style.zIndex = '-2';
      (bgRef.value!.children[13] as HTMLElement).style.zIndex = '-3';
      (bgRef.value!.children[11] as HTMLElement).style.opacity = '1';
      (bgRef.value!.children[12] as HTMLElement).style.opacity = '1';
    }

    if (currentIndex === 16) {
      (bgRef.value!.children[9] as HTMLElement).style.zIndex = '-3';
      (bgRef.value!.children[13] as HTMLElement).style.zIndex = '-2';
      (bgRef.value!.children[11] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[12] as HTMLElement).style.opacity = '0';

      const { duration, currentTime } = zoomOut.value as HTMLVideoElement;

      if (duration === currentTime || currentTime !== 0) {
        zoomOut.value?.pause();

        const zoomOutInterval = setInterval(() => {
          zoomOut.value!.currentTime -= 0.1;

          if (zoomOut.value!.currentTime === 0) {
            clearInterval(zoomOutInterval);
          }
        }, 60);
      }
    }

    if (currentIndex === 17) {
      (bgRef.value!.children[14] as HTMLElement).style.opacity = '0';
      (bgRef.value!.children[13] as HTMLElement).style.zIndex = '-2';
      const { duration, currentTime } = zoomOut.value as HTMLVideoElement;

      if (duration !== currentTime) {
        zoomOut.value?.play();
        const zoomOutVideoListener = useEventListener(
          zoomOut.value,
          'ended',
          () => {
            zoomOutVideoListener();
          },
        );
      }
    }

    if (currentIndex === 18) {
      (bgRef.value!.children[13] as HTMLElement).style.zIndex = '-2';
      const { duration, currentTime } = zoomOut.value as HTMLVideoElement;

      if (duration !== currentTime) {
        zoomOut.value?.play();
        const zoomOutVideoListener = useEventListener(
          zoomOut.value,
          'ended',
          () => {
            (bgRef.value!.children[14] as HTMLElement).style.opacity = '1';
            zoomOutVideoListener();
          },
        );
      }

      if (duration === currentTime) {
        (bgRef.value!.children[14] as HTMLElement).style.opacity = '1';
      }
    }
  }
};

// Video Device Height
const handleVideoDevice = (width: number) => {
  if (width >= 1280) {
    videoDevice.value = 'pc';
  } else if (width >= 768) {
    videoDevice.value = 'pad';
  } else {
    videoDevice.value = 'mob';
  }
};
handleVideoDevice(window.innerWidth);

onMounted(() => {
  emptyCount.value = bgRef.value!.childElementCount + 4;
  scrollCardHeightSet.value = Array(emptyCount.value).fill(0);

  nextTick(() => {
    emptyTotalRef.value!.forEach((el, index) => {
      if (el.classList.contains('satellite-empty-content')) {
        const cardHeight = (el.children[0] as HTMLElement).offsetHeight;

        scrollCardHeightSet.value[index] = cardHeight;
      }

      useIntersectionObserver(
        el as MaybeElement,
        observerCallback,
        observerRoot,
      );
    });

    useIntersectionObserver(
      satellite.value as MaybeElement,
      ([entry]) => {
        if (entry.isIntersecting) {
          isSatelliteShow.value = true;
        }

        if (entry.isIntersecting && entry.boundingClientRect.top >= 0) {
          const video = [...Array.from(bgRef.value!.children)].filter((el) =>
            el.classList.contains('satellite-bg-video'),
          );
          const bgImage = [...Array.from(bgRef.value!.children)].filter(
            (el) => !el.classList.contains('satellite-bg-video'),
          );
          video.forEach((el) => {
            (el.firstChild as HTMLVideoElement)!.currentTime = 0;
            if (el.classList.contains('first')) {
              (el as HTMLElement).style.zIndex = '-2';
            } else {
              (el as HTMLElement).style.zIndex = '-3';
            }
          });

          bgImage.forEach((el) => {
            (el as HTMLElement).style.opacity = '0';
          });
        }
      },
      {
        rootMargin: '0px 0px 150% 0px',
      },
    );
  });
});

watch(isSatelliteShow, async (value) => {
  if (value) {
    await nextTick();
    await taiwanIn.value?.play();
    await taiwanIn.value?.pause();
  }
});

onMounted(() => {
  nextTick(() => {
    useEventListener(window, 'resize', (e: UIEvent) => {
      const innerWidth = (e.target as Window).innerWidth;
      handleVideoDevice(innerWidth);
    });
  });
});
</script>

<template>
  <section ref="satellite">
    <div class="satellite">
      <div class="satellite-container" ref="bgRef">
        <div class="satellite-bg satellite-bg-video first" data-bg>
          <video
            :key="videoDevice"
            muted
            playsinline
            preload="auto"
            ref="taiwanIn"
            v-if="isSatelliteShow"
          >
            <source
              :src="`${IMG_URL_BASE}/${videoDevice}/scroll/dalinpo2025_video5-6_${videoDevice}.mp4`"
              type="video/mp4"
            />
          </video>
        </div>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1280px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic5_2_mark_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic5_2_mark_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic5_2_mark_mob.svg`"
            loading="lazy"
            decoding="async"
            alt="衛星圖簡易標記"
          />
        </picture>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1024px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic5_3_mark_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic5_3_mark_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic5_3_mark_mob.svg`"
            loading="lazy"
            decoding="async"
            alt="衛星圖文字簡易標記"
          />
        </picture>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1280px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic5_4_mark_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic5_4_mark_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic5_4_mark_mob.svg`"
            loading="lazy"
            decoding="async"
            alt="衛星圖文字複雜標記"
          />
        </picture>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1280px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic5_5_chart_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic5_5_chart_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic5_5_chart_mob.svg`"
            class="bg-mask"
            loading="lazy"
            decoding="async"
            alt="折線表"
          />
        </picture>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1280px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic6_2_mark_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic6_2_mark_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic6_2_mark_mob.svg`"
            class="bg-mask"
            loading="lazy"
            decoding="async"
            alt="折線表"
          />
        </picture>
        <div class="satellite-bg satellite-bg-video second" data-bg>
          <video
            :key="videoDevice"
            muted
            playsinline
            preload="auto"
            ref="dalinpoIn"
            v-if="isSatelliteShow"
          >
            <source
              :src="`${IMG_URL_BASE}/${videoDevice}/scroll/dalinpo2025_video6-3_${videoDevice}.mp4`"
              type="video/mp4"
            />
          </video>
        </div>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1280px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic7_2_mark_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic7_2_mark_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic7_2_mark_mob.svg`"
            class="bg-mask"
            loading="lazy"
            decoding="async"
            alt="鳳林國中測站"
          />
        </picture>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1280px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic7_3_chart_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic7_3_chart_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic7_3_chart_mob.svg`"
            class="bg-mask"
            loading="lazy"
            decoding="async"
            alt="鳳林國中測站"
          />
        </picture>
        <div class="satellite-bg satellite-bg-video second" data-bg>
          <video
            :key="videoDevice"
            muted
            playsinline
            preload="auto"
            ref="threeDigitalIn"
            v-if="isSatelliteShow"
          >
            <source
              :src="`${IMG_URL_BASE}/${videoDevice}/scroll/dalinpo2025_video7-4_${videoDevice}.mp4`"
              type="video/mp4"
            />
          </video>
        </div>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1280px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic8_2_mark_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic8_2_mark_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic8_2_mark_mob.svg`"
            class="bg-mask"
            loading="lazy"
            decoding="async"
            alt="鳳林國中測站"
          />
        </picture>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1280px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic8_3_chart_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic8_3_chart_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic8_3_chart_mob.svg`"
            class="bg-mask"
            loading="lazy"
            decoding="async"
            alt="鳳林國中測站"
          />
        </picture>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1280px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic8_4_chart_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic8_4_chart_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic8_4_chart_mob.svg`"
            class="bg-mask"
            loading="lazy"
            decoding="async"
            alt="鳳林國中測站"
          />
        </picture>
        <div class="satellite-bg satellite-bg-video second" data-bg>
          <video
            :key="videoDevice"
            muted
            playsinline
            preload="auto"
            ref="zoomOut"
            v-if="isSatelliteShow"
          >
            <source
              :src="`${IMG_URL_BASE}/${videoDevice}/scroll/dalinpo2025_video8-5_${videoDevice}.mp4`"
              type="video/mp4"
            />
          </video>
        </div>
        <picture class="satellite-bg" data-bg>
          <source
            media="(min-width: 1280px)"
            :srcset="`${IMG_URL_BASE}/pc/scroll/dalinpo2025_pic9_2_mark_pc.svg`"
          />
          <source
            media="(min-width: 768px)"
            :srcset="`${IMG_URL_BASE}/pad/scroll/dalinpo2025_pic9_2_mark_pad.svg`"
          />
          <img
            :src="`${IMG_URL_BASE}/mob/scroll/dalinpo2025_pic9_2_mark_mob.svg`"
            class="bg-mask"
            loading="lazy"
            decoding="async"
            alt="鳳林國中測站"
          />
        </picture>
      </div>
      <!-- EMPTY -->
      <div class="satellite-empty">
        <template v-for="(_, index) in emptyCount" :key="index">
          <div
            v-if="index === 2"
            class="satellite-empty-item satellite-empty-content"
            ref="emptyTotalRef"
            :data-index="index"
            :style="{
              '--card-content-height': `calc(100dvh + ${scrollCardHeightSet[index]}px)`,
            }"
          >
            <p class="satellite-empty-card">
              (100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。
            </p>
            <!-- <p style="font-size: 64px; color: red">{{ index }}</p> -->
          </div>

          <div
            v-else-if="index === 3"
            class="satellite-empty-item satellite-empty-content"
            ref="emptyTotalRef"
            :data-index="index"
            :style="{
              '--card-content-height': `calc(100dvh + ${scrollCardHeightSet[index]}px)`,
            }"
          >
            <p class="satellite-empty-card bottom">
              (100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。
            </p>
            <!-- <p style="font-size: 64px; color: red">{{ index }}</p> -->
          </div>

          <div
            v-else-if="index === 6"
            class="satellite-empty-item satellite-empty-content"
            ref="emptyTotalRef"
            :data-index="index"
            :style="{
              '--card-content-height': `calc(100dvh + ${scrollCardHeightSet[index]}px)`,
            }"
          >
            <p class="satellite-empty-card bottom">
              (100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。
            </p>
            <!-- <p style="font-size: 64px; color: red">{{ index }}</p> -->
          </div>

          <div
            v-else-if="index === 10"
            class="satellite-empty-item satellite-empty-content"
            ref="emptyTotalRef"
            :data-index="index"
            :style="{
              '--card-content-height': `calc(100dvh + ${scrollCardHeightSet[index]}px)`,
            }"
          >
            <p class="satellite-empty-card bottom">
              (100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。
            </p>
            <!-- <p style="font-size: 64px; color: red">{{ index }}</p> -->
          </div>
          <div
            v-else-if="index === 13"
            class="satellite-empty-item satellite-empty-content"
            ref="emptyTotalRef"
            :data-index="index"
            :style="{
              '--card-content-height': `calc(100dvh + ${scrollCardHeightSet[index]}px)`,
            }"
          >
            <p class="satellite-empty-card bottom">
              (100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。
            </p>
            <!-- <p style="font-size: 64px; color: red">{{ index }}</p> -->
          </div>
          <div
            v-else-if="index === 15"
            class="satellite-empty-item satellite-empty-content"
            ref="emptyTotalRef"
            :data-index="index"
            :style="{
              '--card-content-height': `calc(100dvh + ${scrollCardHeightSet[index]}px)`,
            }"
          >
            <p class="satellite-empty-card">
              (100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。
            </p>
            <!-- <p style="font-size: 64px; color: red">{{ index }}</p> -->
          </div>
          <div
            v-else-if="index === 18"
            class="satellite-empty-item satellite-empty-content"
            ref="emptyTotalRef"
            :data-index="index"
            :style="{
              '--card-content-height': `calc(100dvh + ${scrollCardHeightSet[index]}px)`,
            }"
          >
            <p class="satellite-empty-card bottom">
              (100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。(100)大林蒲位於高雄小港區西南沿海，俗稱沿海六里，人口1萬9千多人，1960年代起，台電、中油、中鋼等陸續在周圍設立工廠，居民長期飽受環境汙染。
            </p>
            <!-- <p style="font-size: 64px; color: red">{{ index }}</p> -->
          </div>

          <div
            v-else
            class="satellite-empty-item"
            ref="emptyTotalRef"
            :data-index="index"
          >
            <!-- <p style="font-size: 64px; color: red">{{ index }}</p> -->
          </div>
        </template>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import './SatelliteSection.scss';
</style>
