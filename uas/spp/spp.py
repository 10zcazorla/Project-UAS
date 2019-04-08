from texttable import Texttable
def spp():
    table= Texttable (max_width=900)
    no=0
    nama=[]
    nim=[]
    kelas=[]
    bay_uts=[]
    bay_uas=[]
    bay_bulan=[]
    bay_seminar=[]
    bay_kas=[]
    admin=[]

    print("_"*40)
    print("      Program Pembayaran Mahasiswa")
    print("_"*40)  
    nama=(input("Masukan Nama  : "))
    nim=(input("Masukan NIM   : "))
    kelas=(input("Masukan Kelas : "))        
    print ("Pilih jenis pembayaran")
    print ("1.UTS (Rp.250.000)")
    print ("2.UAS (Rp.500.000")
    pilih1 = (input("Pilih (1/2) ? "))
    if  pilih1 == '1':
        uts_uas = 'UTS'
        bay_uts=250000
        bay_uas=0
        jawab = 't'
    elif pilih1 == '2':
         uts_uas = 'UAS'
         bay_uas=500000
         bay_uts=0
         jawab = 't'

    else  :
            print ("\n!!! Failed ,Please Try Again !!!")
    
    pilih = (input("Apakah Anda mau membayar BULANAN (Rp.500.000/bulan) (y/t) ? "))
    if pilih == 'y':
        bulanan =int(input("\nPembayaran BULANAN \nDi bayar untuk berapa bulan ? "))
        d_bulanan = 'BULANAN'
        bay_bulan=5000000*bulanan
    else :
        bulanan_ = ''
        bay_bulan=0
    pilih = (input("Apakah Anda mau membayar SEMINAR (Rp.100.000) (y/t) ? "))
    if  pilih == 'y':
        seminar  = 'SEMINAR'
        bay_seminar=100000
    else:
        seminar = ''
        bay_seminar=0
    pilih = (input("Apakah Anda mau membayar KAS (Rp.20.000/bulan) (y/t) ? "))
    if  pilih == 'y':
        d_kas = 'KAS'
        kas = int(input("\nPembayaran KAS \nDi bayar untuk berapa bulan ? "))
        bay_kas=20000*kas
    else :
        kas = ''
        bay_kas=0
    print ("Anda Akan dikenakan Biaya Admin sebesar (Rp.5.000)");input('')
    admin=5000
    no=+1
    for ia in range(no):
        total_bayar = bay_uts+bay_uas+bay_bulan+bay_seminar+bay_kas
        grand_total = total_bayar+admin
    table.set_cols_dtype(['a','i','i','i','i','i','i','i','i','i','i','i'])
    table.add_rows([['NO','NAMA','NIM','KELAS','UTS','UAS','BULAN','SEMINAR','KAS','TOTAL','ADMIN','GRAND TOTAL'],
                    [ia+1,nama,nim,kelas,bay_uts,bay_uas,bay_bulan,bay_seminar,bay_kas,total_bayar,admin,grand_total]])
    print("_"*30)
    print("     Rincian Pembayaran")
    print("_"*30)
    print (table.draw())
    jawab3 = input("\n  Tambahkan Data PEMBAYARAN (y/t)? ") ; print("")
