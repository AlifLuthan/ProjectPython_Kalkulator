  # © Muhammad Alif Luthan Mahasiswa STT Nurul Fikri 2020
print("----------------------------------------------------------------------------------")
print("----------------Fitur 2: Kalkulator biaya kuliah bagi mahasiswa-------------------")
print("---------------------NIM ditulis dengan format 01102XXYYY-------------------------")
print("----------------------------------------------------------------------------------")
nim = input("Masukan NIM: ") # Masukan NIM Mahasiswa sesuai angkatan 20.19.18.17
if nim[5:7] == "20": # jika nim mahasiswa merupakan angkatan 2020 maka akan keluar inputan sebagai berikut
    bop = 4000000  
    biaya_sks = 200000
    print("BOP mahasiswa angkatan 2020 adalah 4000000")
    print("Anda mahasiswa tahun pertama. Anda bisa mengambil paling banyak 20 SKS.")
elif nim[5:7] == "19": # jika nim mahasiswa merupakan angkatan 2019 maka akan keluar inputan sebagai berikut
    bop = 3500000
    biaya_sks = 175000
    print("BOP mahasiswa angkatan 2019 adalah 3500000")
    print("Anda mahasiswa tahun kedua. Anda bisa mengambil paling banyak 22 SKS.")
elif nim[5:7] == "18": # jika nim mahasiswa merupakan angkatan 2018 maka akan keluar inputan sebagai berikut
    bop = 3200000
    biaya_sks = 150000
    print("BOP mahasiswa angkatan 2018 adalah 3200000")
    print("Anda mahasiswa tahun ketiga. Anda bisa mengambil paling banyak 24 SKS.")
elif nim[5:7] == "17": # jika nim mahasiswa merupakan angkatan 2017 maka akan keluar inputan sebagai berikut
    bop = 2800000
    biaya_sks = 130000
    print("BOP mahasiswa angkatan 2017 adalah 2800000")
    print("Anda mahasiswa tahun keempat. Anda bisa mengambil paling banyak 26 SKS.")
else: 
    print("NIM TIDAK VALID!") # JIKA NIM MAHASISWA TIDAK BENAR SAAT PENGINPUTAN MAKA AKAN MUNCUL CETAKAN BERIKUT
print("----------------------------------------------------------------------------------")  #pemisah
sks = int(input("Jumlah SKS yang diambil semester ini: ")) # Input Jumlah sks yang diambil oleh mahasiswa
sksambil = 15 #maksimal imputan adalah sama dengan 15
totalsksambil = sks - sksambil #perhitungan sks yang diambil
Biayatambahan = totalsksambil * biaya_sks #perhitungan biaya tambahan
total = bop + Biayatambahan #total dari biaya tambahan dan bop
if sks > sksambil:
    print("Biaya tambahan untuk",totalsksambil,"SKS: ",Biayatambahan)
    #akan mencetak apa yang sebelumnya diolah oleh totalsksambil dan Biayatambahan
    print("Total biaya kuliah: ",total)
    #akan mencetak total yang sebelumnya di kalkulasi
else:
    ()
print("----------------------------------------------------------------------------------") #pemisah
ajukan = input("Apakah anda ingin mengajukan subsidi biaya kuliah? (Y/N): ") #pengajuan biaya subsidi dan penginputan
semester = [] 
if ajukan == "Y": #jika pengajuannya memiliki nilai Y maka program akan berjalan
    semester = int(input("Semester berapa anda sekarang? ")) #nilai Y diproses dan menampilkan inputan ini
if semester == 8:  #jika inputan sebelumnya adalah angka 8 yang menandakan anda mahasiswa semester 8 maka
    i1 = float(input("Masukan IP semester 1: ")) #masukan IP semester 1
    i2 = float(input("Masukan IP semester 2: ")) #masukan IP semester 2
    i3 = float(input("Masukan IP semester 3: ")) #masukan IP semester 3   
    i4 = float(input("Masukan IP semester 4: ")) #masukan IP semester 4    
    i5 = float(input("Masukan IP semester 5: ")) #masukan IP semester 5
    i6 = float(input("Masukan IP semester 6: ")) #masukan IP semester 6
    i7 = float(input("Masukan IP semester 7: ")) #masukan IP semester 7
#tipe data float digunakan karena Menyatakan bilangan yang mempunyai koma , karena nilai IPK yang saya tau itu berbentuk float 
    jum = i1 + i2 + i3 + i4 + i5 + i6 + i7  #kalkulasikan perhitungan penjumlahan i1 sd i7
    a = (jum / 7)                    # hasil dari jum sebelumnya di bagi dengan 7 dan masuk dan tersimpan ke variabel a      
    hasil = "%0.2f" % (a)            # di variabel hasi ini kita mengelolah nilai yang dimasukan sebelumnya
    # Tanda % menunjukkan bahwa di sana adalah lokasi penempatan nilai variabel dari 0.2f dan juga (a)
    # dan Angka 0.2 merupakan lebar karakter, dan jumlah angka di belakang koma.
    # Sedangkan tanda f merupakan format karakter dari nilai yang akan disisipkan        
    subsidi = float(hasil) / 4.0 * 1000000 # di variabel subsidi ini kita olah lagi dari hasil sebelumnya
    # lalu (hasil) akan dibagi dengan 4.0 dan dikalikan dengan 1000000
    hitung_total = total - subsidi         #selanjutnya hitung total dengan cara total - subsidi
    print("Anda mendapatkan subsidi sebesar ",round(subsidi))
    # cetakan diatas akan menampilkan data yang disimpan oleh subsidi 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("Total biaya kuliah: ",round(hitung_total))
    # cetakan diatas akan menampilkan data yang disimpan oleh hitung_total 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("perhitungan biaya kuliah berakhir.")
    print("----------------------------------------------------------------------------------") #pemisah
elif semester == 7: #jika inputan sebelumnya adalah angka 7 yang menandakan anda mahasiswa semester 7 maka
    i1 = float(input("Masukan IP semester 1: ")) #masukan IP semester 1
    i2 = float(input("Masukan IP semester 2: ")) #masukan IP semester 2
    i3 = float(input("Masukan IP semester 3: ")) #masukan IP semester 3   
    i4 = float(input("Masukan IP semester 4: ")) #masukan IP semester 4    
    i5 = float(input("Masukan IP semester 5: ")) #masukan IP semester 5
    i6 = float(input("Masukan IP semester 6: ")) #masukan IP semester 6
#tipe data float digunakan karena Menyatakan bilangan yang mempunyai koma , karena nilai IPK yang saya tau itu berbentuk float
    jum = i1 + i2 + i3 + i4 + i5 + i6 #kalkulasikan perhitungan penjumlahan i1 sd i6
    a = (jum / 6)                   # hasil dari jum sebelumnya di bagi dengan 6 dan masuk dan tersimpan ke variabel a
    hasil = "%0.2f" % (a)           #di variabel hasi ini kita mengelolah nilai yang dimasukan sebelumnya
    # Tanda % menunjukkan bahwa di sana adalah lokasi penempatan nilai variabel dari 0.2f dan juga (a)
    # dan Angka 0.2 merupakan lebar karakter, dan jumlah angka di belakang koma.
    # Sedangkan tanda f merupakan format karakter dari nilai yang akan disisipkan        
    subsidi = float(hasil) / 4.0 * 1000000 # di variabel subsidi ini kita olah lagi dari hasil sebelumnya
    hitung_total = total - subsidi         # selanjutnya hitung total dengan cara total - subsidi
    print("Anda mendapatkan subsidi sebesar ",round(subsidi))
    # cetakan diatas akan menampilkan data yang disimpan oleh subsidi 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("Total biaya kuliah: ",round(hitung_total))
    # cetakan diatas akan menampilkan data yang disimpan oleh hitung_total 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("perhitungan biaya kuliah berakhir.")
    print("----------------------------------------------------------------------------------") #pemisah
elif semester == 6: #jika inputan sebelumnya adalah angka 6 yang menandakan anda mahasiswa semester 6 maka
    i1 = float(input("Masukan IP semester 1: ")) #masukan IP semester 1
    i2 = float(input("Masukan IP semester 2: ")) #masukan IP semester 2
    i3 = float(input("Masukan IP semester 3: ")) #masukan IP semester 3   
    i4 = float(input("Masukan IP semester 4: ")) #masukan IP semester 4    
    i5 = float(input("Masukan IP semester 5: ")) #masukan IP semester 5
#tipe data float digunakan karena Menyatakan bilangan yang mempunyai koma , karena nilai IPK yang saya tau itu berbentuk float
    jum = i1 + i2 + i3 + i4 + i5 #kalkulasikan perhitungan penjumlahan i1 sd i5
    a = (jum / 5)                # hasil dari jum sebelumnya di bagi dengan 5 dan masuk dan tersimpan ke variabel a
    hasil = "%0.2f" % (a)        # di variabel hasi ini kita mengelolah nilai yang dimasukan sebelumnya
    # Tanda % menunjukkan bahwa di sana adalah lokasi penempatan nilai variabel dari 0.2f dan juga (a)
    # dan Angka 0.2 merupakan lebar karakter, dan jumlah angka di belakang koma.
    # Sedangkan tanda f merupakan format karakter dari nilai yang akan disisipkan
    subsidi = float(hasil) / 4.0 * 1000000 # di variabel subsidi ini kita olah lagi dari hasil sebelumnya
    hitung_total = total - subsidi         # selanjutnya hitung total dengan cara total - subsidi
    print("Anda mendapatkan subsidi sebesar ",round(subsidi))
    # cetakan diatas akan menampilkan data yang disimpan oleh subsidi 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("Total biaya kuliah: ",round(hitung_total))
    # cetakan diatas akan menampilkan data yang disimpan oleh hitung_total 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("perhitungan biaya kuliah berakhir.")
    print("----------------------------------------------------------------------------------") #pemisah
elif semester == 5: #jika inputan sebelumnya adalah angka 5 yang menandakan anda mahasiswa semester 5 maka
    i1 = float(input("Masukan IP semester 1: ")) #masukan IP semester 1
    i2 = float(input("Masukan IP semester 2: ")) #masukan IP semester 2
    i3 = float(input("Masukan IP semester 3: ")) #masukan IP semester 3   
    i4 = float(input("Masukan IP semester 4: ")) #masukan IP semester 4 
#tipe data float digunakan karena Menyatakan bilangan yang mempunyai koma , karena nilai IPK yang saya tau itu berbentuk float
    jum = i1 + i2 + i3 + i4 #kalkulasikan perhitungan penjumlahan i1 sd i4
    a = (jum / 4)           # hasil dari jum sebelumnya di bagi dengan 4 dan masuk dan tersimpan ke variabel a
    hasil = "%0.2f" % (a)   # di variabel hasi ini kita mengelolah nilai yang dimasukan sebelumnya
    # Tanda % menunjukkan bahwa di sana adalah lokasi penempatan nilai variabel dari 0.2f dan juga (a)
    # dan Angka 0.2 merupakan lebar karakter, dan jumlah angka di belakang koma.
    # Sedangkan tanda f merupakan format karakter dari nilai yang akan disisipkan
    subsidi = float(hasil) / 4.0 * 1000000 # di variabel subsidi ini kita olah lagi dari hasil sebelumnya
    hitung_total = total - subsidi         # selanjutnya hitung total dengan cara total - subsidi
    print("Anda mendapatkan subsidi sebesar ",round(subsidi))
    # cetakan diatas akan menampilkan data yang disimpan oleh subsidi 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("Total biaya kuliah: ",round(hitung_total))
    # cetakan diatas akan menampilkan data yang disimpan oleh hitung_total 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("perhitungan biaya kuliah berakhir.")
    print("----------------------------------------------------------------------------------") #pemisah
elif semester == 4: #jika inputan sebelumnya adalah angka 4 yang menandakan anda mahasiswa semester 4 maka
    i1 = float(input("Masukan IP semester 1: ")) #masukan IP semester 1
    i2 = float(input("Masukan IP semester 2: ")) #masukan IP semester 2
    i3 = float(input("Masukan IP semester 3: ")) #masukan IP semester 3
#tipe data float digunakan karena Menyatakan bilangan yang mempunyai koma , karena nilai IPK yang saya tau itu berbentuk float
    jum = i1 + i2 + i3 #kalkulasikan perhitungan penjumlahan i1 sd i3
    a = (jum / 3)      # hasil dari jum sebelumnya di bagi dengan 3 dan masuk dan tersimpan ke variabel a
    hasil = "%0.2f" % (a)   # di variabel hasi ini kita mengelolah nilai yang dimasukan sebelumnya
    # Tanda % menunjukkan bahwa di sana adalah lokasi penempatan nilai variabel dari 0.2f dan juga (a)
    # dan Angka 0.2 merupakan lebar karakter, dan jumlah angka di belakang koma.
    # Sedangkan tanda f merupakan format karakter dari nilai yang akan disisipkan
    subsidi = float(hasil) / 4.0 * 1000000 # di variabel subsidi ini kita olah lagi dari hasil sebelumnya
    hitung_total = total - subsidi         # selanjutnya hitung total dengan cara total - subsidi
    print("Anda mendapatkan subsidi sebesar ",round(subsidi))
    # cetakan diatas akan menampilkan data yang disimpan oleh subsidi 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("Total biaya kuliah: ",round(hitung_total))
    # cetakan diatas akan menampilkan data yang disimpan oleh hitung_total 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("perhitungan biaya kuliah berakhir.")
    print("----------------------------------------------------------------------------------") #pemisah
elif semester == 3: #jika inputan sebelumnya adalah angka 3 yang menandakan anda mahasiswa semester 3 maka
    i1 = float(input("Masukan IP semester 1: ")) #masukan IP semester 1
    i2 = float(input("Masukan IP semester 2: ")) #masukan IP semester 2
#tipe data float digunakan karena Menyatakan bilangan yang mempunyai koma , karena nilai IPK yang saya tau itu berbentuk float
    jum = i1 + i2      #kalkulasikan perhitungan penjumlahan i1 sd i2
    a = (jum / 2)      # hasil dari jum sebelumnya di bagi dengan 2 dan masuk dan tersimpan ke variabel a
    hasil = "%0.2f" % (a)   # di variabel hasi ini kita mengelolah nilai yang dimasukan sebelumnya
    # Tanda % menunjukkan bahwa di sana adalah lokasi penempatan nilai variabel dari 0.2f dan juga (a)
    # dan Angka 0.2 merupakan lebar karakter, dan jumlah angka di belakang koma.
    # Sedangkan tanda f merupakan format karakter dari nilai yang akan disisipkan
    subsidi = float(hasil) / 4.0 * 1000000 # di variabel subsidi ini kita olah lagi dari hasil sebelumnya
    hitung_total = total - subsidi         # selanjutnya hitung total dengan cara total - subsidi
    print("Anda mendapatkan subsidi sebesar ",round(subsidi))
    # cetakan diatas akan menampilkan data yang disimpan oleh subsidi 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("Total biaya kuliah: ",round(hitung_total))
    # cetakan diatas akan menampilkan data yang disimpan oleh hitung_total 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("perhitungan biaya kuliah berakhir.")
    print("----------------------------------------------------------------------------------") #pemisah
elif semester == 2: #jika inputan sebelumnya adalah angka 2 yang menandakan anda mahasiswa semester 2 maka
    i1 = float(input("Masukan IP semester 1: ")) #masukan IP semester 1
#tipe data float digunakan karena Menyatakan bilangan yang mempunyai koma , karena nilai IPK yang saya tau itu berbentuk float
    jum = i1 # variabel jum bernilai i1
    a = (jum / 1) # hasil dari jum sebelumnya di bagi dengan 1 dan masuk dan tersimpan ke variabel a
    hasil = "%0.2f" % (a)# di variabel hasi ini kita mengelolah nilai yang dimasukan sebelumnya
    # Tanda % menunjukkan bahwa di sana adalah lokasi penempatan nilai variabel dari 0.2f dan juga (a)
    # dan Angka 0.2 merupakan lebar karakter, dan jumlah angka di belakang koma.
    # Sedangkan tanda f merupakan format karakter dari nilai yang akan disisipkan
    subsidi = float(hasil) / 4.0 * 1000000 # di variabel subsidi ini kita olah lagi dari hasil sebelumnya
    hitung_total = total - subsidi         # selanjutnya hitung total dengan cara total - subsidi
    print("Anda mendapatkan subsidi sebesar ",round(subsidi))
    # cetakan diatas akan menampilkan data yang disimpan oleh subsidi 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("Total biaya kuliah: ",round(hitung_total))
    # cetakan diatas akan menampilkan data yang disimpan oleh hitung_total 
    # lalu membulatkan suatu bilangan desimal berkoma menggunakan round
    print("perhitungan biaya kuliah berakhir.")
    print("----------------------------------------------------------------------------------") #pemisah
elif semester == 1: #jika inputan sebelumnya adalah angka 1 yang menandakan anda mahasiswa semester 1 maka
    print("Anda tidak bisa mengajukan subsidi biaya kuliah.")
    # cetakan diatas akan menampilkan bahwa mahasiswa semester 1 tidak dapat mengajukan subsidi
    print("----------------------------------------------------------------------------------") #pemisah
    print("perhitungan biaya kuliah berakhir.")
    print("----------------------------------------------------------------------------------") #pemisah
else: 
    print("----------------------------------------------------------------------------------") #pemisah
    print("perhitungan biaya kuliah berakhir.")
    # cetakan diatas akan menampilkan perhitungan sudah berakhir jika tidak ada inputan yang dijalankan
    print("----------------------------------------------------------------------------------") #pemisah

      # © Mahasiswa STT Nurul Fikri 2020
