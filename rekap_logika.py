"""Merangkum persentase status akademik, diskon, dan kebutuhan restock."""


MAHASISWA = [
    {"nama": "Alya", "ipk": 3.60, "sks": 20},
    {"nama": "Bima", "ipk": 1.70, "sks": 15},
    {"nama": "Citra", "ipk": 2.80, "sks": 18},
    {"nama": "Dafa", "ipk": 1.20, "sks": 12},
    {"nama": "Eka", "ipk": 3.90, "sks": 22},
]

# Setiap kasus berisi IPK, status anak karyawan, dan pembayaran tepat waktu.
KASUS_DISKON = [
    (3.9, False, True),
    (3.5, True, False),
    (2.8, False, True),
    (3.2, False, False),
    (3.0, False, True),
]

STOK_BARANG = [42, 16, 8, 0, 25, 11, 4, 31]


def status_mahasiswa(data):
    if data["ipk"] >= 2 and data["sks"] >= 18:
        return "Aktif"
    if 1.5 <= data["ipk"] < 2:
        return "Peringatan"
    return "Tidak Aktif"


def hitung_diskon(ipk, anak_karyawan, tepat_waktu):
    if anak_karyawan:
        utama = 0.25
    elif ipk >= 3.8:
        utama = 0.20
    elif ipk >= 3.5:
        utama = 0.15
    elif ipk >= 3.0:
        utama = 0.10
    else:
        utama = 0
    return utama + (0.05 if tepat_waktu else 0)


def main():
    total_mahasiswa = len(MAHASISWA)
    jumlah_aktif = sum(status_mahasiswa(m) == "Aktif" for m in MAHASISWA)
    jumlah_tidak_aktif = sum(status_mahasiswa(m) == "Tidak Aktif" for m in MAHASISWA)
    persen_aktif = jumlah_aktif / total_mahasiswa * 100 if total_mahasiswa else 0
    persen_tidak_aktif = jumlah_tidak_aktif / total_mahasiswa * 100 if total_mahasiswa else 0

    diskon_list = [hitung_diskon(*kasus) for kasus in KASUS_DISKON]
    rata_diskon = sum(diskon_list) / len(diskon_list) * 100 if diskon_list else 0

    jumlah_restock = sum(stok <= 20 for stok in STOK_BARANG)
    persen_restock = jumlah_restock / len(STOK_BARANG) * 100 if STOK_BARANG else 0

    baris = [
        ("Mahasiswa aktif", f"{persen_aktif:.1f}%", f"{jumlah_aktif}/{total_mahasiswa} mahasiswa"),
        ("Mahasiswa tidak aktif", f"{persen_tidak_aktif:.1f}%", f"{jumlah_tidak_aktif}/{total_mahasiswa} mahasiswa"),
        ("Rata-rata diskon SPP", f"{rata_diskon:.1f}%", f"{len(diskon_list)} kasus simulasi"),
        ("Barang perlu restock", f"{persen_restock:.1f}%", f"{jumlah_restock}/{len(STOK_BARANG)} barang"),
    ]

    print("=" * 76)
    print("RINGKASAN HASIL PENGOLAHAN DATA")
    print("=" * 76)
    print(f"{'Indikator':<30}{'Hasil':>15}   {'Keterangan':<25}")
    print("-" * 76)
    for indikator, hasil, keterangan in baris:
        print(f"{indikator:<30}{hasil:>15}   {keterangan:<25}")
    print("=" * 76)


if __name__ == "__main__":
    main()
