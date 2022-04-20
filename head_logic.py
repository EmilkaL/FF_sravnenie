import parser_msu
import parser_FRTK
import re

def main():
    msu = parser_msu.main()
    frtk, lfi = parser_FRTK.main()
    all = msu.upper() + frtk.upper() + lfi.upper()
    msu, frtk, lfi = msu.upper(), frtk.upper(), lfi.upper()
    f = open('list.txt', 'w', encoding='utf-8')
    lines = all.splitlines()
    lines_wo_r = list(set(lines))
    lines_wo_r.sort()
    l = 0
    lines_l = []
    for line in lines_wo_r:
        lines_l.append([])
        lines_l[l].append(line)
        if frtk.count(line) >= 1:
            lines_l[l].append("'+")
        else:
            lines_l[l].append('-')
        if lfi.count(line) >= 1:
            lines_l[l].append("'+")
        else:
            lines_l[l].append('-')
        if msu.count(line) >= 1:
            lines_l[l].append("'+")
        else:
            lines_l[l].append('-')
        l += 1
    f.write(str(lines_l))
    return lines_l