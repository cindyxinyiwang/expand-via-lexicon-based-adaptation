import random
import sys

tgt_langs = ["bam", "glv", "gsw", "myv", "wol", "mlt", "grc"]

tgt_lang = sys.argv[1]
# [pos|panx]
task = sys.argv[2]
calc_stats = 0
total_words = 0
swapped = 0

for split in ["train"]:
    en_tsv = "download/{}/{}-en.tsv".format(task, split)
    tgt_output = "download/{}/{}-en2{}.tsv".format(task, split, tgt_lang)
    lexicon = "data/lexicons/eng_{}_lexicon.txt".format(tgt_lang)
    dic = {}
    total_words, swapped = 0, 0
    with open(lexicon, "r") as myfile:
      for line in myfile:
        words = line.strip().split("\t")
        if words[0] not in dic:
          dic[words[0]] = []
        dic[words[0]].append(words[1])
    if not calc_stats:
        print("writing to {}".format(tgt_output))
        tgt_output = open(tgt_output, "w")
    
    with open(en_tsv, "r") as myfile:
        for line in myfile:
            line = line.strip()
            if not line:
                if not calc_stats:
                    tgt_output.write("\n")
            else:
                toks = line.split("\t")
                sent, label = toks[0], toks[1]
                pseudo_sent = []
                for w in sent.split():
                    total_words += 1
                    if w in dic:
                        swapped += 1
                        pseudo_sent.append(random.choice(dic[w]))
                    else:
                        pseudo_sent.append(w)
                if not calc_stats:
                    tgt_output.write(" ".join(pseudo_sent) + "\t" + label + "\n")
    print("for {}, the swapped percent is {}".format(tgt_lang, swapped/total_words))
        
           
