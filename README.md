# ex3-ko-diffsinger-support
Repository that supports Korean Diffsinger development
한국어 Diffsinger 제작을 지원하는 레포지토리에요.

## 🔖1. Phonemes | 음소표 
| phoneme | type | description(EN) | 설명(KO) | Usage
|---|---|---|---|---
| **SP** | silence | Silent Pause | 조용한 공백 | 
| AP |  | Aspirate Pause (Mainly inhale breath) | 거센 공백, 주로 들숨 부분 |
| **a** | vowel | vowel with No batchim | 받침 없는 모음 | 가 \[g a\]
| i |  |  |  |
| u |  |  |  |
| e |  |  |  |
| o |  |  |  |
| eu |  |  |  |
| eo |  |  |  |
| **a1** |  | vowel with batchim - `N, P` | 받침 딸린 모음 - `ㅁ, ㅂ` | 범 \[b eo1 M\], 삽 \[s a1 P\]
| i1 |  |  |  |
| u1 |  |  |  |
| e1 |  |  |  |
| o1 |  |  |  |
| eu1 |  |  |  |
| eo1 |  |  |  |
| **a2** |  | vowel with batchim - `N, cl` | 받침 딸린 모음 - `ㄴ, ㄷ` | 빈 \[by i2 N\], 맛 \[m a2 cl\]
| i1 |  |  |  |
| u1 |  |  |  |
| e1 |  |  |  |
| o1 |  |  |  |
| eu1 |  |  |  |
| eo1 |  |  |  |
| **a3** |  | vowel with batchim - `ㅇ` | 받침 딸린 모음 - `ㅇ` | 궁 \[gw u3], 상 \[s a3\]
| i3 |  |  |  |
| u3 |  |  |  |
| e3 |  |  |  |
| o3 |  |  |  |
| eu3 |  |  |  |
| eo3 |  |  |  |
| **a4** |  | vowel with batchim - `ㄹ` | 받침 딸린 모음 - `ㄹ` | 살 \[g a4],  말\[m a4\]
| i4 |  |  |  |
| u4 |  |  |  |
| e4 |  |  |  |
| o4 |  |  |  |
| eu4 |  |  |  |
| eo4 |  |  |  |
| **N** | last consonant | batchim - `ㄴ` | 받침 - `ㄴ` | 난 \[n a2 N\]
| **M** |  | batchim - `ㅁ` | 받침 - `ㅁ` | 범 \[b eo1 M\]
| **K** |  | batchim - `ㄱ` | 받침 - `ㄱ` | 막 \[m a K\]
| **cl** |  | batchim - `ㄷ` | 받침 - `ㄷ` | 맛 \[m a2 cl\]
| **P** |  | batchim - `ㅂ` | 받침 - `ㅂ` | 난 \[n a2 N\]
| **w** | semivowel | semivowel - `w` | w계열 반모음 | 워 \[w eo\]
| y | semivowel | semivowel - `y` | j계열 반모음 | 야 \[y a\]
| **vf** | vocal fry | vocal fry | 보컬프라이 (엣지) | '아 \[vf a\], 아'\[a vf\]
| **g** | first consonant | ㄱ | ㄱ | 가 \[g a]
| gy |  |  | | 길 \[gy i4],  갸\[gy a\]
| gw |  |   | | 구 \[gw u],  궤\[gw e\]
| **n** |  | ㄴ |ㄴ | 
| ny |  |  | | 
| nw |  |   | | 
| **d** |  | ㄷ |ㄷ | 
| dy |  |  | | 
| dw |  |   | | 
| **r** |  | ㄹ |ㄹ | 
| ry |  |  | | 
| rw |  |   | | 
| **m** |  | ㅁ |ㅁ | 
| my |  |  | | 
| mw |  |   | | 
| **b** |  | ㅂ |ㅂ | 
| by |  |  | | 
| bw |  |   | | 
| **s** |  | ㅅ |ㅅ | 
| sy |  |  | | 
| sw |  |   | | 
| **j** |  | ㅈ |ㅈ | 
| jy |  |  | | 
| jw |  |   | | 
| **ch** |  | ㅊ |ㅊ | 
| chy |  |  | | 
| chw |  |   | | 
| **k** |  | ㅋ |ㅋ | 
| ky |  |  | | 
| kw |  |   | | 
| **t** |  | ㅌ |ㅌ | 
| ty |  |  | | 
| tw |  |   | | 
| **p** |  | ㅍ |ㅍ | 
| py |  |  | | 
| pw |  |   | | 
| **h** |  | ㅎ |ㅎ | 
| hy |  |  | | 
| hw |  |   | | 
| **gg** |  | ㄲ |ㄲ | 
| ggy |  |  | | 
| ggw |  |   | | 
| **dd** |  | ㄸ |ㄸ | 
| ddy |  |  | | 
| ddw |  |   | | 
| **bb** |  | ㅃ |ㅃ | 
| bby |  |  | | 
| bbw |  |   | | 
| **ss** |  | ㅆ |ㅆ | 
| ssy |  |  | | 
| ssw |  |   | | 
| **jj** |  | ㅉ |ㅉ | 
| jjy |  |  | | 
| jjw |  |   | | 
## 🔖2. How to Label | 라벨링 방법
### 📕2-1. 예사소리, ㅅ (g, d, b, s, j... + s, ss...) - consonants which are not fortis & not aspirate
- start: 자음의 시작 (start of consonant)
- end: 자음의 끝 (end of consonant)
![image](https://github.com/EX3exp/ex3-ko-diffsinger-support/assets/100339835/e72b4aa9-fb42-4a9c-b2b5-c539db720f69)
### 📕2-2. ㅅ이 아닌 된소리, 거센소리 (k, t, p, gg, dd, bb...) - consonants which are fortis or aspirate
- start: 자음의 시작으로부터 약 10ms 앞 (start of consonant, but with pre-silence(10ms))
- end: 자음의 끝 (end of consonants)
![image](https://github.com/EX3exp/ex3-ko-diffsinger-support/assets/100339835/145caca2-9000-4f38-8577-5a76d42b8326)
### 📕2-3. 받침이 딸린 모음 _ 접미사 1, 2(a1, i2...)- vowels with suffix 1, 2
- start: 주로 UTAU 프리셋 두던 지점에 두면 맞습니다 (kinda similar with UTAU's preutterance...)
- end: 받침부의 3분의 1 지점(1/3 of batchim length)
![image](https://github.com/EX3exp/ex3-ko-diffsinger-support/assets/100339835/9c479bc0-b3d3-497e-a3c9-f55f26ed379b)
### 📕2-4. 받침이 딸린 모음 _ 접미사 3, 4(a3, i4...)- vowels with suffix 3, 4
- start: 주로 UTAU 프리셋 두던 지점에 두면 맞습니다 (kinda similar with UTAU's preutterance...)
- end: 모음의 끝(end of vowel)
![image](https://github.com/EX3exp/ex3-ko-diffsinger-support/assets/100339835/ae5854af-4729-449b-81d4-fe794f966235)

