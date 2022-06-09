from sentinelsat import SentinelAPI
from decouple import config

user = config('DHUS_USER')
password = config('DHUS_PASSWORD')
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')
