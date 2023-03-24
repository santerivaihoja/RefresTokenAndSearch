import requests
import json
from bs4 import BeautifulSoup

# osoitteet vain esimerkkinä se pitää saada dynaamiseksi
#url = "https://api.nettix.fi/rest/bike/ad/2918552"
url = "https://api.nettix.fi/rest/bike/search?page=1&rows=30&sortBy=price&sortOrder=asc&latitude=60.5346&longitude=25.6074&isMyFavorite=false&make=387&model=8062&includeMakeModel=true&accessoriesCondition=and&isPriced=true&taxFree=false&vatDeduct=true&tagsCondition=and"
refresh_token = ""

# funktio tokenin uudistamiseksi
def renew_access_token(refresh_token):
    # Set the URL and data for the token renewal request
    token_url = "https://auth.nettix.fi/oauth2/token"
    data = {"grant_type": "refresh_token", "refresh_token": refresh_token}

    response = requests.post(token_url, data=data)
    response.raise_for_status()
    access_token = response.json()["access_token"]
    return access_token

access_token = renew_access_token(refresh_token)

# uusi token on tässä käytössä
headers = {"X-Access-Token": access_token}
response = requests.get(url, headers=headers)
response.raise_for_status()

print(response) #printataan onnistuiko
print(access_token) #testiksi

site_json = json.loads(response.text)
keskiarvo = ([d.get('price') for d in site_json])
avg = sum(keskiarvo)/len(keskiarvo)
print("The average is ", round(avg, 2))
