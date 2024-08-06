# Berisi beberapa menu pilihan dan fungsi
# 1. Tambah daftar siswa    = Menambahkan siswa ke daftar
# 2. Hapus daftar siswa     = Menghapus siswa ke daftar
# 3. Lihat daftar siswa     = Melihat daftar siswa
# 4. Hapus semua daftar     = Menghapus semua siswa dalam daftar
# 5. Keluar                 = Keluar dari loop

kelas = []

while True:
    print("1. Tambah daftar siswa\n2. Hapus daftar siswa\n3. Lihat daftar siswa\n4. Hapus semua daftar\n5. Keluar")
    menu = input("Masukkan pilihan anda: ")
    if menu not in ["1", "2", "3", "4", "5"]:
        print()
        print("Pilihan tidak tersedia")
        print("Silahkan pilih angka sesuai pilihan")
        print()
    elif menu == "1":
        print()
        nama_tambah = input("Masukkan nama siswa: ").capitalize()
        if any(char.isdigit() for char in nama_tambah):
            print("Nama tidak boleh mengandung angka")
        elif any(not char.isalnum() and not char.isspace() for char in nama_tambah):
            print("Nama tidak boleh mengandung karakter & spasi")
        else:
            kelas.append(nama_tambah)
            print("Berhasil menambahkan", nama_tambah)
        print()
    elif menu == "2":
        print()
        nama_kurang = input("Masukkan nama yang ingin dikeluarkan: ").capitalize()
        if nama_kurang in kelas:
            kelas.remove(nama_kurang)
            print(nama_kurang, "berhasil dikeluarkan")
            print()
        else:
            print("Nama tidak ditemukan")
            print("Silahkan lihat nama di daftar siswa")
            print()
    elif menu == "3":
        if kelas:
            print()
            print("Daftar Siswa:")
            kelas.sort()
            for i in kelas:
                print("-",i)
            print()
        else:
            print()
            print("Kelas kosong")
            print("Silahkan tambahkan siswa")
            print()
    elif menu == "4":
        if kelas:
            kelas.clear()
            print()
            print("Semua siswa telah dikeluarkan dari kelas")
            print()
        else:
            print()
            print("Kelas kosong")
            print("Silahkan tambahkan siswa")
            print()
    elif menu == "5":
        break
print()
print("Anda keluar")