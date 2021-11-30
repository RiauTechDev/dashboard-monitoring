"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE

"""
import latestearthquake

if __name__ == '__main__':
    print('Aplikasi utama')
    result = latestearthquake.ekstraksi_data()
    latestearthquake.tampilkan_data(result)
