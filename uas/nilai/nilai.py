def nilai():
    from texttable import Texttable
    table = Texttable()
    no = 0      
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    jawab = "y"
    while(jawab == "y"):
        nama.append(input("Masukan Nama : "))
        nim.append(input("Masukan NIM  : "))
        nilai_tugas.append(input("Nilai Tugas  : "))
        nilai_uts.append(input("Nilai UTS    : "))
        nilai_uas.append(input("Nilai UAS    : "))
        jawab = input("\nTambah data (y/t)? ")
        no += 1
    for i in range(no):
        tugas = int(nilai_tugas[i])
        uts = int(nilai_uts[i])
        uas = int(nilai_uas[i])
        akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100)
        table.set_cols_dtype(['a','i','i','i','i','i','i'])
        table.add_rows([['NO','NAMA','NIM','TUGAS','UTS','UAS','AKHIR'],
                        [i+1,nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])
    print (table.draw())
