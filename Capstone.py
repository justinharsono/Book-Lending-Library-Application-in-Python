# ID Buku, Nama Buku, Author, Kategory, Stock
list_buku = [
    ['A21', 'DORAEMON', 'FUJIKO FUJIO', 'KOMIK', '5'],
    ['P12', 'KESEJAHTERAAN SOSIAL', 'ISBANDI RUKMINTO', 'PENGETAHUAN', '3'],
    ['P22', 'STRATEGIC MANAGEMENT', 'SOFJAN ASSAURI', 'PENGETAHUAN', '3'],
    ['N50', 'MOBY-DICK', 'HERMAN MELVILLE', 'NOVEL', '5'],
    ['N19', 'WAR AND PEACE', 'TOLSTOY', 'NOVEL', '4'],
]


def read():
    sub_menu = 0

    while(True):
        print('''
            ===== Menampilkan Data Buku =====
            1. Tampilkan Semua
            2. Cari Dengan ID Buku
            3. Kembali ke Menu Utama
            =================================
    ''')
        sub_menu = int(input("Silakan Pilih Menu Tampilan Data [1-3] : "))

        if sub_menu == 1:
            print("Daftar Buku :")
            for row in list_buku:
                print("ID : {}, Nama : {}, Author : {}, Kategori : {}, Stock : {}".format(row[0], row[1], row[2], row[3], row[4]))
        elif sub_menu == 2:
            id = input("Masukkan ID : ")
            exists = False
            data = []
            
            for row in list_buku:
                if row[0] == id:
                    exists = True
                    data = row
            
            if exists:
                print("Data Buku dengan ID : {}".format(id))
                print("ID : {}, Nama : {}, Author : {}, Kategori : {}, Stock : {}".format(data[0], data[1], data[2], data[3], data[4]))
            else:
                print("===== Tidak ada Data Buku =====")
        elif sub_menu == 3:
            break
        else:
            pass
        print()


def create():
    sub_menu = 0

    while(True):
        print('''
            ===== Menambahkan Data Buku ====
            1. Tambah Data Buku
            2. Kembali Ke Menu Utama
            ====================================
        ''')
        sub_menu = int(input("Silakan Pilih Menu Menambah Data [1-2] : "))

        if sub_menu == 1:
            id = input("Masukkan ID : ")
            exists = False

            for row in list_buku:
                if row[0] == id:
                    exists = True
            
            if exists:
                print("Data Sudah Ada")
            else:
                nama = input("Masukkan Nama Buku : ")
                author = input("Masukkan Author : ")
                kategori = input("Masukkan Kategori : ")
                stock = input("Masukkan Stock : ")

                while(True):
                    konfirmasi = input("Apakah Data akan disimpan? (Y/N) : ")

                    if konfirmasi == "Y":
                        row = [id, nama, author, kategori, stock]
                        list_buku.append(row)
                        print("Data Tersimpan")
                        break
                    
                    if konfirmasi == "N":
                        break
                print()
                                        
        elif sub_menu == 2:
            break
        else:
            pass


def update():
    sub_menu = 0

    while(True):
        print('''
            ===== Mengubah Data Buku =====
            1. Ubah Data Buku
            2. Kembali Ke Menu Utama
        ''')
        sub_menu = int(input("Silakan Pilih Sub Menu Update Data [1-2] : "))

        if sub_menu == 1:
            id = input("Masukkan ID : ")
            exists = False
            index = 0

            i = 0
            for row in list_buku:
                if row[0] == id:
                    exists = True
                    index = i
                    break
                i = i + 1
            
            if exists:
                data = list_buku[index]
                print("ID : {}, Nama : {}, Author : {}, Kategori : {}, Stock : {}".format(data[0], data[1], data[2], data[3], data[4]))
                while(True):
                    konfirmasi = input("Tekan Y jika ingin update data atau N jika ingin cancel update (Y/N) : ")

                    if konfirmasi == "Y":
                        kolom = input("Masukkan Kolom yang ingin di edit\n(Nama/Author/Kategori/Stock): ")

                        if kolom == "Nama":
                            nama_baru = input("Masukkan Nama Buku yang Baru : ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N) : ")
                                if konfirmasi2 == "Y":
                                    list_buku[index][1] = nama_baru
                                    print("Data Updated")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass
                        elif kolom == "Author":
                            author_baru = input("Masukkan Author Baru : ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N) : ")
                                if konfirmasi2 == "Y":
                                    list_buku[index][2] = author_baru
                                    print("Data Updated")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass
                        elif kolom == "Kategori":
                            kategori_baru = input("Masukkan Kategori Baru : ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N) : ")
                                if konfirmasi2 == "Y":
                                    list_buku[index][3] = kategori_baru
                                    print("Data Updated")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass
                        elif kolom == "Stock":
                            stock_baru = input("Masukkan Stock Baru : ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N) : ")
                                if konfirmasi2 == "Y":
                                    list_buku[index][4] = stock_baru
                                    print("Data Updated")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass

                        break
                    
                    if konfirmasi == "N":
                        print("Data Tidak Terhapus")
                        break
                print()
            else:
                print("Data Tidak Ada")
                print()
        elif sub_menu == 2:
            break
        else:
            pass


def delete():
    sub_menu = 0

    while(True):
        print('''
            ===== Menghapus Data Buku =====
            1. Hapus Data Buku
            2. Kembali Ke Menu Utama
            ===================================
        ''')
        sub_menu = int(input("Silakan Pilih Sub Menu Hapus Data [1-2] : "))

        if sub_menu == 1:
            id = input("Masukkan ID : ")
            exists = False
            index = 0

            i = 0
            for row in list_buku:
                if row[0] == id:
                    exists = True
                    index = i
                    break
                i = i + 1
            
            if exists:
                while(True):
                    konfirmasi = input("Apakah Data akan dihapus? (Y/N) : ")

                    if konfirmasi == "Y":
                        list_buku.pop(index)
                        print("Data Deleted")
                        break
                    
                    if konfirmasi == "N":
                        print("Data Tidak Terhapus")
                        break
                print()
            else:
                print("Data Tidak Ada")
                print()
        elif sub_menu == 2:
            break
        else:
            pass


       
main_menu = 0 


def show_menu():
    print('''
            ===== Stock Peminjaman Buku Perpustakaan =====
            1. Menampilkan Data Buku
            2. Menambahkan Data Buku
            3. Mengubah Data Buku
            4. Menghapus Data Buku
            5. Exit Program
            ==============================================
    ''') 

while(True):
    show_menu()
    main_menu = int(input("Silakan Pilih Menu Utama [1-5] : "))
    print()

    if main_menu == 1:
        read()
    elif main_menu == 2:
        create()
    elif main_menu == 3:
        update()
    elif main_menu == 4:
        delete()
    elif main_menu == 5:
        print("===== Terimakasih =====")
        break
    else:
        print("Menu yang anda pilih tidak tersedia. Silahkan dicoba lagi.")
    print()