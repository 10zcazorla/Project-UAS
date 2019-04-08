from texttable import Texttable


def gaji ():
    table = Texttable ()
    no = 0
    nama = []
    jabatan = []
    gaji = []
    jawab = "y"
    while (jawab =="y"):
        nama.append(input("Masukan Nama :"))
        print("1. operator ")
        print("2. leader ")
        print("3. supervisor ")
        print("4. manager ")
        jab = input("jabatan :")
        jabatan.append(jab)
        if (jab == 'operator'):
            gaji.append('Rp.6.000.000')
            
           
            
        elif (jab == 'leader'):
            gaji.append('Rp.10.000.000')
            
            
        elif (jab == 'supervisor'):
            gaji.append('Rp.15.000.000')
           
            
        elif (jab == 'manager'):
            gaji.append('Rp.20.000.000')
            
        else:
            break
        no += 1
        jawab = input ("\n Tambahkan Lagi (y/t)?")
    for i in range (no) :
        table.add_rows([['NO', 'NAMA', 'JABATAN', 'GAJI'],
                        [i+1,nama[i],jabatan[i],gaji[i]]])
    print(table.draw())


