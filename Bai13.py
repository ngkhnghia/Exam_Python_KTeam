try:
    with open('fin_bai13.txt', 'r') as fin:
        data = fin.read().split()
    with open('fout_bai13.txt', 'w') as fout:
        fout.write(' '.join(data))
except FileNotFoundError:
    with open('fout_bai13.txt', 'w') as fout:
        fout.write('khong tim thay file input!')