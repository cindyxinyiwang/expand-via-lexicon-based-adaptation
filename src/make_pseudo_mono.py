import random
import sys

max_count = 200000
lan = sys.argv[1]

#for lan in ["wol", "luo", "hau", "lug", "ibo", "kin"]:
src_file = "data/enwiki.tok.txt"
lexicon = "data/lexicons/tat_eng_lexicon.txt"
trg_file = "data/pseudo_mono/en2{}.200k.txt".format(lan)

count = 0
dic = {}
with open(lexicon, "r") as myfile:
  for line in myfile:
    words = line.strip().split("\t")
    if words[0] not in dic:
      dic[words[0]] = []
    dic[words[0]].append(words[1])
if use_bible_lexicon:
  with open(bible_lexicon, "r") as myfile:
    for line in myfile:
      words = line.strip().split("\t")
      if words[0] not in dic:
        dic[words[0]] = []
      dic[words[0]].append(words[1])

trg_file = open(trg_file, "w")
replaced_data = []
with open(src_file, "r") as myfile:
  for line in myfile:
    toks = line.split()
    new_toks = []
    replaced = 0
    for t in toks:
      if t in dic:
        new_t = random.choice(dic[t])
        new_toks.append(new_t)
        replaced += 1
      else:
        new_toks.append(t)
    if replaced >= 3:
      trg_file.write(" ".join(new_toks) + "\n")
      count += 1
      if count >= max_count: break

