
# load module
from urllib.request import urlretrieve
import os
import pandas as pd
URL='https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename = 'Fremont.csv', url = URL, force_download = False):
    
    """Download and Cashe Fremont Bike Data
    
    Uses pandas to format timestamps and add column lableing to return a data frame ready for analysis
    
    Args:
        filename (str): CSV file of data
        url (str): URL to retireve file if not downloaded
        
    Returns:
        Pandas Data Frame
    """
    
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    
    data = pd.read_csv(filename, index_col ='Date', parse_dates = True)
    data.columns = ['East', 'West']
    data['Total'] = data['West'] + data['East']
    
    return data
# download data from URL and call it Fremont.csv