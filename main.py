"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 25 November 2021
    Waktu: 00:10:30 WIB
    Magnitudo: 2.8
    Kedalaman: 11 km
    Lokasi: LS: 7.30 BT: 110.41
    Pusat Gempa: Pusat gempa berada di darat 10 Km Barat Laut Kota Salatiga
    Dirasakan: Dirasakan (Skala MMI): II Banyubiu, II Ambarawa, II Temenggungan,
    II Pojoksari, II Brongkol, II Kalipawon, II Tegalrejo,
    II Jambu, II Losari, II Gondorio, II Semilir, II Garung, II Bejalen
    :return:
    """
    hasil =  dict()
    hasil['tanggal'] = '25 November 2021'
    hasil['waktu'] = '00:10:30 WIB'
    hasil['magnitudo'] = 2.8
    hasil['kedalaman'] = '11 km'
    hasil['lokasi'] = {'ls': 7.30, 'bt': 110.41}
    hasil['pusat'] = 'Pusat gempa berada di darat 10 Km Barat Laut Kota Salatiga'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Banyubiu, II Ambarawa, II Temenggungan,' \
                         ' II Pojoksari, II Brongkol, II Kalipawon, II Tegalrejo,' \
                         'II Jambu, II Losari, II Gondorio, II Semilir, II Garung, II Bejalen'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
