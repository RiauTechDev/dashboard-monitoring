"""
The Latest Earthquake Detection App
Modularization With Function
Modularization With Package

"""

# Import Module and call the function

import latestearthquake

if __name__ == '__main__':
    print('Main Application')
    result = latestearthquake.data_extraction()
    latestearthquake.show_data(result)
