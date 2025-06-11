function detectMob() {
  if (
    navigator.userAgent.match(/Android/i) ||
    navigator.userAgent.match(/webOS/i) ||
    navigator.userAgent.match(/iPhone/i) ||
    navigator.userAgent.match(/iPad/i) ||
    navigator.userAgent.match(/iPod/i) ||
    navigator.userAgent.match(/BlackBerry/i) ||
    navigator.userAgent.match(/Windows Phone/i)
  ) {
    return true;
  } else {
    return false;
  }
}

const metaTitle_content =
  document.querySelector('meta[property="og:title"]')?.content || '';
const metaDescription_content =
  document.querySelector('meta[property="og:description"]')?.content || '';
const metaUrl_content =
  document.querySelector('meta[property="og:url"]')?.content || '';

const encodeTitle = encodeURI(metaTitle_content);
const encodeDescription = encodeURI(metaDescription_content);
const encodeUrl = encodeURI(metaUrl_content);

// const shareText = `${encodeTitle}%0D%0A%0D%0A${encodeDescription}`;

// 因一般的description過長，特別弄這段
// const metaTwitterDescription_content =
//   "請輸入文字";
// const encodeTwitterDescription = encodeURI(metaTwitterDescription_content);
const shareTwitterText = `${encodeTitle}%0D%0A%0D%0A${encodeDescription}`;

export const shareURL_line = (() =>
  detectMob()
    ? `https://line.naver.jp/R/msg/text/?${encodeUrl}`
    : `https://social-plugins.line.me/lineit/share?url=${encodeUrl}`)();

export const shareURL_fb = (() =>
  `https://www.facebook.com/dialog/share?app_id=1010324812347164&display=popup&href=${encodeUrl}&redirect_uri=${encodeUrl}`)();

export const shareURL_twitter = (() =>
  `https://twitter.com/intent/tweet/?text=${shareTwitterText}%0D%0A%0D%0A${encodeUrl}`)();

export default {
  shareURL_fb,
  shareURL_line,
  shareURL_twitter,
};
