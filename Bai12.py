with open('fin_bai12.txt', 'r') as fin:
    data = fin.read().splitlines()
with open('fout_bai12.txt', 'w') as fout:
    fout.write(' '.join(data))