import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[1]
        waktu = result[0]

        result = soup.find('div', {'class', 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan

        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak menemukan data gempa terkini')
        return
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")
