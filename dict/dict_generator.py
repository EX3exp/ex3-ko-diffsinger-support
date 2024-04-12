from unicode import join_jamos

cs = {'ㄱ': 'g', 'ㄴ': 'n', 'ㄷ': 'd', 'ㄹ': 'r', 'ㅁ': 'm', 'ㅂ': 'b', 'ㅅ': 's', 'ㅇ': '', 'ㅈ': 'j', 'ㅊ': 'ch', 'ㅋ': 'k', 'ㅌ':'t', 'ㅍ': 'p', 'ㅎ': 'h', 'ㄲ': 'gg', 'ㄸ': 'dd', 'ㅃ':'bb', 'ㅆ':'ss','ㅉ':'jj'}
vs = {'ㅏ': ' a', 'ㅣ': 'y i', 'ㅜ': 'w u', 'ㅔ': ' e', 'ㅓ': ' eo', 'ㅐ': ' e', 'ㅗ': ' o', 'ㅡ': ' eu', 'ㅘ': 'w a', 'ㅟ': 'w i', 'ㅞ': 'w e', 'ㅙ': 'w e', 'ㅚ': 'w e', 'ㅝ': 'w eo', 'ㅢ': ' e', 'ㅟ': 'w i', 'ㅑ':'y a', 'ㅕ':'y eo', 'ㅛ': 'y o', 'ㅠ': 'y u', 'ㅖ': 'y e', 'ㅒ': 'y e'}
lcs = {'ㄱ': ' K', 'ㅋ': ' K', 'ㄴ': '2 N', 'ㄵ': '2 N',  'ㄶ': '2 N','ㅄ': '1 P', 'ㄿ': '1 P', 'ㄼ': '1 P', 'ㄺ': ' K', 'ㄷ':'2 cl', 'ㄳ':'2 K', 'ㅌ':'2 cl', 'ㄹ': '4','ㄽ': '4', 'ㄾ': '2 cl', 'ㅀ': '4', 'ㅁ': '1 M', 'ㄻ': '1 M', 'ㅂ': '1 P', 'ㅍ': '1 P', 'ㅅ':'2 cl','ㅈ':'2 cl', 'ㅊ':'2 cl', 'ㅎ':'2 cl', 'ㅇ': '3', '': '', 'ㄲ': ' K', 'ㅆ':'2 cl'}

phones = []
phones.append(f"sil\tSP")
phones.append(f"0\tSP")
phones.append(f"pau\tSP")
phones.append(f"br\tAP")
phones.append(f"asp\tAP")

def process(phones : list):
    for c in sorted(cs.keys()):
        for v in sorted(vs.keys()):
            if c == 'ㅇ' and (v == 'ㅣ' or v == 'ㅜ'):
                phones.append(f"{join_jamos(c + v)}\t{cs[c] + vs[v][1:]}".replace("  ", " "))
                phones.append(f"'{join_jamos(c + v)}\tvf {cs[c] + vs[v][1:]}".replace("  ", " "))
                phones.append(f"{join_jamos(c + v)}'\t{cs[c] + vs[v][1:]} vf".replace("  ", " "))
            else:
                phones.append(f"{join_jamos(c + v)}\t{cs[c] + vs[v]}".replace("  ", " "))
                phones.append(f"'{join_jamos(c + v)}\tvf {cs[c] + vs[v]}".replace("  ", " "))
                phones.append(f"{join_jamos(c + v)}'\t{cs[c] + vs[v]} vf".replace("  ", " "))
        for v in sorted(vs.keys()):
            for lc in sorted(lcs.keys()):
              if c == 'ㅇ' and (v == 'ㅣ' or v == 'ㅜ'):
                  phones.append(f"{join_jamos(c + v + lc)}\t{cs[c] + vs[v][1:] + lcs[lc]}".replace("  ", " "))
                  phones.append(f"'{join_jamos(c + v + lc)}\tvf {cs[c] + vs[v][1:] + lcs[lc]}".replace("  ", " "))
                  phones.append(f"{join_jamos(c + v + lc)}'\t{cs[c] + vs[v][1:] + lcs[lc]} vf".replace("  ", " "))
              else:
                  phones.append(f"{join_jamos(c + v + lc)}\t{cs[c] + vs[v] + lcs[lc]}".replace("  ", " "))
                  phones.append(f"'{join_jamos(c + v + lc)}\tvf {cs[c] + vs[v] + lcs[lc]}".replace("  ", " "))
                  phones.append(f"{join_jamos(c + v + lc)}'\t{cs[c] + vs[v] + lcs[lc]} vf".replace("  ", " "))

process(phones)

with open('ex3_kor_dict.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(phones))

# uncomment below if you want to generate config.json
# newlst = []
# for p in phones:
#     _ = p.split()
#     t = f'"{_[0]}": ['
#     ind = 0

#     for __ in _[1:]:
#         t+=f'"{__}"'
#         if ind != len(_[1:]) - 1:
#             t+= ", "
        
#         ind+=1
#     t += "]"
#     newlst.append(t)

# with open('config.json', 'w', encoding='utf-8') as f:
#      # "息": ["br"],
     
#      f.write(',\n'.join(newlst))