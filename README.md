# ex3-ko-diffsinger-support
Repository that supports Korean Diffsinger development
한국어 Diffsinger 제작을 지원하는 레포지토리에요.

## 🔖1. Phonemes | 음소표 
https://github.com/EX3exp/ex3-ko-diffsinger-support/blob/main/dict/Readme.md
## 🔖2. How to Label | 라벨링 방법
### 📕2-1. 예사소리, ㅅ (g, d, b, s, j... + s, ss...) - consonants which are not fortis & not aspirate
- start: 자음의 시작 (start of consonant)
- end: 자음의 끝 (end of consonant)
![image](https://github.com/EX3exp/ex3-ko-diffsinger-support/assets/100339835/e72b4aa9-fb42-4a9c-b2b5-c539db720f69)
### 📕2-2. ㅅ이 아닌 된소리, 거센소리 (k, t, p, gg, dd, bb...) - consonants which are fortis or aspirate
- start: 자음의 시작으로부터 약 10ms 앞 (start of consonant, but with pre-silence(about 10ms is OK))
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
### 📕2-5. 반모음 (w, y...)- semivowels
- 스펙트럼을 보며 라벨링합시다. (please see Spectrum)
- start: 전체 반모음 스펙트럼의 3분의 1 지점 (1/3 of semivowel's spectrum)
- end: 전체 반모음 스펙트럼의 3분의 2 지점 (2/3 of semivowel's spectrum)

![image](https://github.com/EX3exp/ex3-ko-diffsinger-support/assets/100339835/6ea60343-23a1-420d-bbc7-9fb2352e07ce)
![image](https://github.com/EX3exp/ex3-ko-diffsinger-support/assets/100339835/62d7a192-5126-4c1b-b1bb-9bc24787a09f)

