"""Memeriksa stok, prioritas restock, dan nilai inventaris."""


BATAS_AMAN = 20
BATAS_RENDAH = 10

INVENTARIS = [
    {"kode": "AT001", "nama": "Buku catatan", "stok": 42, "harga": 18000},
    {"kode": "AT002", "nama": "Pulpen gel", "stok": 16, "harga": 7000},
    {"kode": "AT003", "nama": "Pensil 2B", "stok": 8, "harga": 4000},
    {"kode": "AT004", "nama": "Penghapus", "stok": 0, "harga": 3000},
    {"kode": "AT005", "nama": "Penggaris", "stok": 25, "harga": 6000},
    {"kode": "AT006", "nama": "Map plastik", "stok": 11, "harga": 5000},
    {"kode": "AT007", "nama": "Spidol", "stok": 4, "harga": 12000},
    {"kode": "AT008", "nama": "Stabilo", "stok": 31, "harga": 10000},
]


def status_stok(stok):
    if stok == 0:
        return "HABIS", "KRITIS", "Segera lakukan restock"
    if stok <= BATAS_RENDAH:
        return "RENDAH", "TINGGI", "Restock secepatnya"
    if stok <= BATAS_AMAN:
        return "PERINGATAN", "SEDANG", "Jadwalkan restock"
    return "AMAN", "RENDAH", "Stok mencukupi"


def main():
    total_nilai = 0
    jumlah_perlu_restock = 0
    statistik = {"AMAN": 0, "PERINGATAN": 0, "RENDAH": 0, "HABIS": 0}

    print("=" * 96)
    print("LAPORAN PEMANTAUAN INVENTARIS")
    print("=" * 96)
    print(f"{'Kode':<9}{'Nama barang':<19}{'Stok':>7}{'Harga':>14}{'Nilai stok':>16}  {'Status':<13}{'Prioritas'}")
    print("-" * 96)

    for item in INVENTARIS:
        status, prioritas, rekomendasi = status_stok(item["stok"])
        nilai = item["stok"] * item["harga"]
        total_nilai += nilai
        statistik[status] += 1
        if status != "AMAN":
            jumlah_perlu_restock += 1
        print(f"{item['kode']:<9}{item['nama']:<19}{item['stok']:>7}"
              f"{item['harga']:>14,}{nilai:>16,}  {status:<13}{prioritas}")
        if status != "AMAN":
            print(f"  -> {rekomendasi}")

    print("-" * 96)
    print(f"Total nilai inventaris : Rp{total_nilai:,}")
    print(f"Total barang           : {len(INVENTARIS)}")
    print(f"Barang perlu restock   : {jumlah_perlu_restock}")
    print("Ringkasan status       : " + ", ".join(f"{k}={v}" for k, v in statistik.items()))
    print("=" * 96)


if __name__ == "__main__":
    main()
