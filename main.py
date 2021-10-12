"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal 12 Oktober 2021
    Waktu: 05:23:31 WIB
    Magnitudo: 3.9
    Kedalaman: 29 km
    Lokasi: LS=7.85 BT=107.28
    Pusat Gempa: Pusat gempa berada di laut 96 km baratdaya Bandung
    Dirasakan: Dirasakan (Skala MMI): II-III Garut
    """
    hasil = dict()
    hasil['tanggal'] = '12 Oktober 2021'
    hasil['waktu'] = '05:23:31 WIB'
    hasil['magnitudo'] = 3.9
    hasil['lokasi'] = {'ls':7.85, 'bt':107.28}
    hasil['pusat'] = 'Pusat gempa berada di laut 96 km baratdaya Bandung'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Garut' 

    return hasil

def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
