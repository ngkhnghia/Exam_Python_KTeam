with open("fin_bai10.txt", 'r') as fin:
    ten = fin.readline().rstrip('\n')
    tuoi = int(fin.readline().rstrip('\n'))
with open('fout_bai10.txt', "w") as fout:
    fout.write('Vao 20 nam nua, tuoi cua {} se la {}'.format(ten, tuoi + 20))