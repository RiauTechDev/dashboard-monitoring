"""
The Latest Earthquake Detection App
Modularization With Function
Modularization With Package

"""

# Import Module and call the function

import latestearthquake

if __name__ == '__main__':
    gempa_di_indonesia = latestearthquake.GempaTerkini('https://bmkg.go.id')
    print(f'Aplikasi utama menggunakan package yang memiliki deskripsi {gempa_di_indonesia.description}')
    gempa_di_indonesia.tampilkan_keterangan()
    gempa_di_indonesia.run()
