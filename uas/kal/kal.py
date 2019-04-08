from texttable import Texttable

def kalkulator():
    
    jawab4 = "y"
    while(jawab4 == "y"):
        table4 = Texttable ()
        #---pilih---#
        print (("\n"),("_"*3),("KALKULATOR"),("_"*3))
        table4.add_rows([['NO','JENIS HITUNGAN'],['1.','(+) Penjumlahan'],['2.','(-) Pengurangan'],['3.','(x) Perkalian'],['4.','(:) Pembagian']])
        print (table4.draw()) 
        jenishitungan = (input("\n--> Masukan Pilihan JENIS HITUNGAN ?  "))

        if   jenishitungan == '1':
             print("\n+ Penjumlahan +")
             a = int(input("Masukan angka pertama : "))
             b = int(input("Masukan angka kedua   : "))
             hasil = a+b
             print("\n>",a,"+",b,"=",hasil,"\n")
            
        elif jenishitungan == '2':
             print("\n- Pengurangan -")
             a = int(input("Masukan angka pertama : "))
             b = int(input("Masukan angka kedua   : "))
             hasil = a-b
             print("\n>",a,"-",b,"=",hasil,"\n")

        elif jenishitungan == '3':
             print("\nx Perkalian x")
             a = int(input("Masukan angka pertama : "))
             b = int(input("Masukan angka kedua   : "))
             hasil = a*b
             print("\n>",a,"x",b,"=",hasil,"\n")

        elif jenishitungan == '4':
             print("\n: Pembagian :")
             a = int(input("Masukan angka pertama : "))
             b = int(input("Masukan angka kedua   : "))
             hasil = a/b
             print("\n>",a,":",b,"=",hasil,"\n")

        else:
            print (("\n        !!! WARNING !!!        "),("\n!!! Pilihan Tidak Ditemukan !!!"))

            
        jawab4 = input("\n  Tambahkan Data KALKULATOR (y/t)? ") ; print("")
