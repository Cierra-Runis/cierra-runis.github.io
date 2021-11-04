---
layout: article
titles:
  # @start locale config
  en      : &EN       About
  en-GB   : *EN
  en-US   : *EN
  en-CA   : *EN
  en-AU   : *EN
  zh-Hans : &ZH_HANS  关于
  zh      : *ZH_HANS
  zh-CN   : *ZH_HANS
  zh-SG   : *ZH_HANS
  zh-Hant : &ZH_HANT  關於
  zh-TW   : *ZH_HANT
  zh-HK   : *ZH_HANT
  ko      : &KO       소개
  ko-KR   : *KO
  fr      : &FR       À propos
  fr-BE   : *FR
  fr-CA   : *FR
  fr-CH   : *FR
  fr-FR   : *FR
  fr-LU   : *FR
  # @end locale config
key: page-about
---

<script>
  fetch('https://v1.hitokoto.cn')
    .then(response => response.json())
    .then(data => {
      const hitokoto = document.getElementById('hitokoto_text')
      hitokoto.href = 'https://hitokoto.cn/?uuid=' + data.uuid
      hitokoto.innerText = data.hitokoto
    })
    .catch(console.error)
</script>

# 鸣谢

- [Jekyll](http://jekyllrb.com/) & [TeXt Theme](https://github.com/kitian616/jekyll-TeXt-theme).

# 友链

- [青空域](https://halc.top)

