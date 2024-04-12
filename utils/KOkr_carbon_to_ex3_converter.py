from os import path as Path
from os import walk as Walk

consonants = ["gg", "dd", "bb", "ss", "jj", "g", "n", "d", "r", "m", "b", "s", "j", "ch", "k", "t", "p", "h"]
vowels = ["eu", "eo", "a", "i", "u", "e", "o"]
vowels_ = ["\teu", "\teo", "\ta", "y\ti", "w\tu", "\te", "\to"]

semivowels = ["y", "w"]
semivowels_ = ["$", "$"]

batchims = ["NG", "K", "N", "T", "L", "M", "P"]
batchims_ = ["3\t$", "\tK", "2\tN", "2\tcl", "4\t$", "1\tM", "1\tP"]
fortis_tbl = {"kk": "gg", "tt": "dd", "pp": "bb"}
conv_tbl = {}

for c in consonants:
    for v, v_ in list(zip(vowels ,vowels_)):
        conv_tbl[f"{c}\t{v}"] = f"{c}{v_}"
    
    for s, s_ in list(zip(semivowels, semivowels_)):
        conv_tbl[f"{c}\t{s}"] = f"{c}{s}\t{s_}" # $ will be deleted

for v in vowels:
    for b, b_ in list(zip(batchims, batchims_)):
        conv_tbl[f"{v}\t{b}"] = f"{v}{b_}"


def __process__(_lines: list) -> list:
    lines = []
    starts = []
    ends = []
    _phones = []
    for i, line in enumerate(_lines):
        start, end, phone = line.split()

        if phone in fortis_tbl.keys():
            phone = fortis_tbl[phone]       

        starts.append(start)
        ends.append(end)
        _phones.append(phone)
    
    phones_ = "\t".join(_phones)
    
    for from_, to_ in conv_tbl.items():
        phones_ = phones_.replace(from_, to_)

    phones = phones_.split("\t")

    for i, phone in enumerate(phones):
        if phone == "$":
            ends[i - 1] = ends[i]
            continue

    for start, end, phone in list(zip(starts, ends, phones)):
        if phone != "$":
            lines.append(f"{start} {end} {phone}")

    return lines

corpus_path = input("변환할 .lab들이 있는 폴더의 경로를 입력해 주세요 >>> ")

if Path.exists(corpus_path):
    print("\n변환이 시작되었어요")
    for (path, dir, files) in Walk("./corpus/"):
        for filename in files:
            if Path.splitext(filename)[-1] == '.lab':
                lab_path = Path.join(path, filename)
                with open(lab_path, 'r', encoding='utf-8') as f:
                    lines = __process__(f.readlines())
            
                with open(lab_path, 'w', encoding='utf-8') as f:
                    f.write("\n".join(lines))

                print(f"[CONVERTED LAB]\t{filename}")
    print("\n변환이 끝났어요!")
else:
    print("∑(;°Д°) 존재하지 않는 경로를 입력받았어요")
input("\n종료하려면 엔터를 누르세요...")