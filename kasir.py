# kasir_barcode.py

# --- 1. Data Aplikasi dengan Barcode ---
# Key: Kode Barcode/SKU (String)
# Value: Dictionary detail item
MENU_BARCODE = {
    "1001": {"nama": "Mie Ayam", "harga": 12000},
    "1002": {"nama": "Es Teh", "harga": 5000},
    "1003": {"nama": "Kopi Susu", "harga": 8000},
    "1004": {"nama": "Ayam Bakar", "harga": 25000},
    "1005": {"nama": "Bakso", "harga": 10000},
    "1006": {"nama": "Nasi Goreng", "harga": 15000},
    "1007": {"nama": "Ayam Geprek", "harga": 18000},
    "1008": {"nama": "Soto Ayam", "harga": 10000},
    "1009": {"nama": "Sate Kambing", "harga": 13000},
    "1010": {"nama": "Gurame Bakar", "harga": 12000}
}

# List global untuk menyimpan pesanan
pesanan = []

# --- 2. Fungsi Tampilan Menu ---
def tampilkan_menu():
    """Menampilkan daftar menu yang tersedia dengan kodenya."""
    print("\n================= DAFTAR MENU & KODE BARCODE =================")
    print("KODE \tITEM \t\tHARGA")
    print("----------------------------------------------------------")
    
    for kode, detail in MENU_BARCODE.items():
        nama = detail["nama"]
        harga = detail["harga"]
        # Menyesuaikan spasi
        spasi = "\t\t" if len(nama) < 10 else "\t"
        print(f"{kode} \t{nama}{spasi}Rp {harga:,.0f}")
        
    print("----------------------------------------------------------")

# --- 3. Fungsi Pemrosesan Kasir (Input Barcode) ---
def proses_kasir():
    """Loop utama untuk menerima input Barcode."""
    print("--- SELAMAT DATANG DI APLIKASI KASIR BARCODE CLI ---")
    
    while True:
        tampilkan_menu()
        
        # Menerima input: Barcode Scanner otomatis akan memasukkan kode
        barcode = input("SCAN BARCODE (atau ketik 'BAYAR' untuk selesai): ").strip()
        
        if barcode.upper() == "BAYAR":
            break # Keluar dari loop pemesanan

        if barcode in MENU_BARCODE:
            detail_item = MENU_BARCODE[barcode]
            menu_ditemukan = detail_item["nama"]
            harga_satuan = detail_item["harga"]
            
            # Asumsi default: Barcode Scanner membaca satu item (jumlah = 1)
            jumlah = 1 
            
            # *Opsional*: Tanyakan jumlah jika lebih dari 1
            tanya_jumlah = input(f"Menu: {menu_ditemukan}. Tambahkan {jumlah} item? (Tekan ENTER untuk YA, atau masukkan jumlah > 1): ").strip()
            
            if tanya_jumlah.isdigit() and int(tanya_jumlah) > 0:
                jumlah = int(tanya_jumlah)

            # Tambahkan pesanan ke list
            pesanan.append({
                "menu": menu_ditemukan,
                "jumlah": jumlah,
                "harga_satuan": harga_satuan,
                "subtotal": jumlah * harga_satuan
            })
            print(f"✅ Berhasil: {jumlah} '{menu_ditemukan}' ditambahkan. Total pesanan saat ini: {len(pesanan)} item.")

        else:
            print(f"❌ Gagal: Kode Barcode '{barcode}' tidak ditemukan. Mohon cek kode atau menu.")

    # Pindah ke tahap perhitungan dan pembayaran
    hitung_total()

# --- 4. Fungsi Perhitungan dan Struk ---
def hitung_total():
    """Menghitung total harga dan memproses pembayaran (Fungsi ini tidak berubah)."""
    if not pesanan:
        print("\nTidak ada pesanan yang dibuat. Aplikasi selesai.")
        return

    # Hitung total semua pesanan
    total_semua = sum(item["subtotal"] for item in pesanan)
    
    # Cetak Header Struk
    print("\n\n===================== STRUK PEMBAYARAN =====================")
    print("ITEM \t\tQTY \tHARGA SATUAN \tSUBTOTAL")
    print("------------------------------------------------------------")
    
    # Cetak Detail Pesanan
    for item in pesanan:
        menu = item["menu"]
        # Menyesuaikan spasi untuk tampilan yang rapi
        spasi = "\t\t" if len(menu) < 8 else "\t"
        print(f"{menu}{spasi}{item['jumlah']} \tRp {item['harga_satuan']:,.0f} \tRp {item['subtotal']:,.0f}")
        
    print("------------------------------------------------------------")
    print(f"TOTAL \t\t\t\t\t\t\tRp {total_semua:,.0f}")
    
    # Proses Pembayaran
    while True:
        try:
            bayar = int(input("💰 Masukkan jumlah pembayaran (Rp): "))
            
            if bayar < total_semua:
                print(f"❌ Pembayaran Gagal: Uang yang dibayarkan kurang. Kurang Rp {(total_semua - bayar):,.0f}")
            else:
                kembalian = bayar - total_semua
                print(f"UANG DIBAYAR \t\t\t\t\t\tRp {bayar:,.0f}")
                print(f"KEMBALIAN \t\t\t\t\t\tRp {kembalian:,.0f}")
                print("============================================================")
                print("🎉 TERIMA KASIH TELAH BERBELANJA! 🎉")
                break
        except ValueError:
            print("❌ Input pembayaran tidak valid. Harap masukkan angka.")

# --- 5. Titik Masuk Program ---
if __name__ == "__main__":
    proses_kasir()