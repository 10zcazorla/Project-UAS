from gaji.gaji import gaji
from nilai.nilai import nilai
from kal.kal import kalkulator
from spp.spp import spp
import getpass


def login():
      print("_"*40)
      print("Selamat Datang Di STT Pelita Bangsa ")
      print("Silahkan Login Terlebih Dahulu")
      print("_"*40)
      username = input("Username : ")
      password = getpass.getpass("Password : ")
      if username == "zain" and password =="123":
       menu()
      else:
          print("Login Failed!")
def menu ():       
            print ("Menu")
            print ("1.Penggajian")
            print ("2.Penilaian")
            print ("3.Kalkulator")
            print ("4.Pembayaran")
            Ychoice = int(input("Masukan Pilihan : "))
            if Ychoice == 1:
               gaji ()
            elif Ychoice == 2:
               nilai ()
            elif Ychoice == 3:
               kalkulator()
            elif Ychoice == 4:
               spp()
            else:
                print("pilian tidak ada.")
            choice()
def end():
    print("Terimakasih")
    logout()
def choice():
            choice = input("Kembali Ke Menu (y/t)? ")
            if choice == 'y':
                menu()
            else:
                end()
def logout():
            auth = input("Kembali Ke Login (y/t)? ")
            if auth == 'y':
                login()
            else:
                print("Sampai Jumpa")
                
login()
