try:
    with open("fin_bai11.txt", 'r') as fin:
        ten = fin.readline().rstrip('\n')
        tuoi = int(fin.readline().rstrip('\n'))
    with open('fout_bai11.txt', "w") as fout:
        fout.write('Vao 20 nam nua, tuoi cua {} se la {}'.format(ten, tuoi + 20))
except FileNotFoundError:
    with open('fout_bai11.txt', "w") as fout:
        fout.write('khong tim thay file input!')
except:
    with open('fout_bai11.txt', "w") as fout:
        fout.write('dinh dang dau vao khong hop le!')