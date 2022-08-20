conv_dic = {"A": "T", "T": "A", "G": "C", "C": "G"}


def compstrand(strand):
    return "".join([conv_dic[bp] for bp in strand])


def read_input_stick():
    with open(input()) as f:
        seqs = [line.rstrip('\n') for line in f]
        plasmid = seqs[0]
        rest_plasm = seqs[1]
        gfp = seqs[2]
        res, res2 = seqs[3].split()
        p5_pl, p3_pl = cut(plasmid, rest_plasm)
        p5_gfp, p3_gfp = cut(gfp, res, res2, flag=False)
        return p5_pl[0] + p5_gfp + p5_pl[1], p3_pl[0] + p3_gfp + p3_pl[1]


def cut(seq, *args, flag=True):
    if flag:
        i = seq.find(args[0])
        origin = (seq[:i + 1], seq[i + 1:])
        compl = (compstrand(seq[:i + 5]), compstrand(seq[i + 5:]))

    else:
        i = seq.find(args[0])
        j = seq.rfind(args[1])
        origin = seq[i + 1:j + 1]

        comp = compstrand(seq)
        i = comp.find(compstrand(args[0]))
        j = comp.rfind(compstrand(args[1]))
        compl = comp[i + 5:j + 5]
    return origin, compl


def main():
    origin, compl = read_input_stick()
    print(origin)
    print(compl)

if __name__ == '__main__':
    main()
