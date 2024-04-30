from geopy.geocoders import Nominatim
from functools import lru_cache

@lru_cache(maxsize=128)  # Cache up to 128 unique city/state combinations
def get_zip_code(city, state):
  geolocator = Nominatim(user_agent="sneakerSaaS")
  location = geolocator.geocode(f"{city} {state}")

  if location:
    return (location.raw.get('display_name').split(',')[3].replace(' ', ''))
  else:
    return None, None, None, None

def validate_zip_code(zip_code):
  return True if isinstance(zip_code, str) and zip_code.isdigit() and len(zip_code) == 5 else False


