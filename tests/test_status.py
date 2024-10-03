import requests

# %%
def test_jph1():
    param = {'id': [1, 2, 3]}
    response = requests.get('https://jsonplaceholder.typicode.com/posts', params=param)
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  

# %%
def test_jph1():
    param = {'username': ['Bret', 'Kamren', 'Delphine']}
    response = requests.get('https://jsonplaceholder.typicode.com/users', params=param)
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  

# %%
def test_jph3():
    response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  

# %%
def test_jph2():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  

# %%
def test_jph4():
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1')
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  
# %%
def test_jph5():
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/1')
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  

# %%
# из списка всех пивоварен беру идентификатор очередной пивоварни, конкретно про эту пивоварню формирую тестовый запрос и проверяю контент, который возвращает мне сервис
def test_id_bre():
    response_bre = requests.get('https://api.openbrewerydb.org/v1/breweries')
    for i in response_bre.json():
    bre_id = i['id']
    r = requests.get(f"https://api.openbrewerydb.org/v1/breweries/{bre_id}")
    assert r.status_code == 200

def test_city_bre(): #Тестовый запрос про пивоварни в каждом городе
    #Составляю список названий городов без повторений
    city_id=[]
    response_city = requests.get('https://api.openbrewerydb.org/v1/breweries')

    for i in response_city.json():
        city_id.append(i['city'])
    unique_city = list(set(city_id))

    #Формирую тестовый запрос про каждый город и проверяю контент, который возвращает мне сервис
    for i in unique_city:
        response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_city={i}")
        assert response.json().get("status") == "success"

        assert response.headers['Content-Encoding'] == "gzip"
        assert response.headers['Connection'] == "keep-alive"
        assert response.headers['Server'] == "cloudflare"
        assert 'Date' in response.headers
        assert 'Via' in response.headers
        assert 'Content-Type' in response.headers
        assert 'Vary' in response.headers
        assert 'Cache-Control' in response.headers
        assert 'Age' in response.headers
        assert 'Report-To' in response.headers
        assert 'CF-RAY' in response.headers
        
        assert response.status_code == requests.codes.ok
        assert response.history == []
        assert response.reason == "OK"
        assert 'elapsed' in response.__attrs__
        assert 'request' in response.__attrs__
        assert '_content' in response.__attrs__
        assert 'url' in response.__attrs__
        assert 'encoding' in response.__attrs__
        assert 'cookies' in response.__attrs__  

def test_country_bre(): #Тестовый запрос про пивоварни в каждой стране
    #Составляю список стран без повторений
    response_country = requests.get('https://api.openbrewerydb.org/v1/breweries')

    country_id=[]
    for i in response_country.json():    
        country_id.append(i['country'])
    unique_country = list(set(country_id))

    #Формирую тестовый запрос про каждую страну и проверяю контент, который возвращает мне сервис
    for i in unique_country:
        response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_country={i}")
        assert response.json().get("status") == "success"

        assert response.headers['Content-Encoding'] == "gzip"
        assert response.headers['Connection'] == "keep-alive"
        assert response.headers['Server'] == "cloudflare"
        assert 'Date' in response.headers
        assert 'Via' in response.headers
        assert 'Content-Type' in response.headers
        assert 'Vary' in response.headers
        assert 'Cache-Control' in response.headers
        assert 'Age' in response.headers
        assert 'Report-To' in response.headers
        assert 'CF-RAY' in response.headers
        
        assert response.status_code == requests.codes.ok
        assert response.history == []
        assert response.reason == "OK"
        assert 'elapsed' in response.__attrs__
        assert 'request' in response.__attrs__
        assert '_content' in response.__attrs__
        assert 'url' in response.__attrs__
        assert 'encoding' in response.__attrs__
        assert 'cookies' in response.__attrs__  

def test_state_bre(): #Тестовый запрос про пивоварни в каждом штате
    #Составляю список штатов без повторений
    state_id=[]
    response_state = requests.get('https://api.openbrewerydb.org/v1/breweries')
    for i in response_state.json():
        state_id.append(i['state'])
    unique_state = list(set(state_id))

    #Формирую тестовый запрос про каждый штат и проверяю контент, который возвращает мне сервис
    for i in unique_state:
        r = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_state={i}")
        assert response.json().get("status") == "success"

        assert response.headers['Content-Encoding'] == "gzip"
        assert response.headers['Connection'] == "keep-alive"
        assert response.headers['Server'] == "cloudflare"
        assert 'Date' in response.headers
        assert 'Via' in response.headers
        assert 'Content-Type' in response.headers
        assert 'Vary' in response.headers
        assert 'Cache-Control' in response.headers
        assert 'Age' in response.headers
        assert 'Report-To' in response.headers
        assert 'CF-RAY' in response.headers
        
        assert response.status_code == requests.codes.ok
        assert response.history == []
        assert response.reason == "OK"
        assert 'elapsed' in response.__attrs__
        assert 'request' in response.__attrs__
        assert '_content' in response.__attrs__
        assert 'url' in response.__attrs__
        assert 'encoding' in response.__attrs__
        assert 'cookies' in response.__attrs__  

def test_bre1():
    param = {'name': ['Texas Ale Project', 'Basement Brewers of Texas', 'Texas Leaguer Brewing Company']}
    response = requests.get('https://api.openbrewerydb.org/v1/breweries/autocomplete?query=texas', params=param)
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__    

# %%
def test_bre2():
    param = {'brewery_type': ['nano', 'micro', 'bar']}

    response = requests.get('https://api.openbrewerydb.org/v1/breweries?by_country=south%20korea', params=param)
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  

# %%
def test_bre3():
    param = {'state': ['Wisconsin','Texas']}

    response = requests.get('https://api.openbrewerydb.org/v1/breweries', params=param)
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  
# %%
def test_bre4():
    param = {'state': ['Wisconsin','Texas']}

    response = requests.get('https://api.openbrewerydb.org/v1/breweries', params=param)
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__    

# %%
def test_bre5():
    response = requests.get(' https://api.openbrewerydb.org/v1/breweries/meta?by_type=micro')
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__   

# %%
def test_dog1():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  
# %%
def test_dog2():
    response = requests.get('https://dog.ceo/api/breed/hound/list')
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  
    assert response.json().get("status") == "success"


# %%
def test_dog3():
    response = requests.get('https://dog.ceo/api/breed/hound/plott/images')
    assert response.headers['Content-Encoding'] == "gzip"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['Server'] == "cloudflare"
    assert 'Date' in response.headers
    assert 'Via' in response.headers
    assert 'Content-Type' in response.headers
    assert 'Vary' in response.headers
    assert 'Cache-Control' in response.headers
    assert 'Age' in response.headers
    assert 'Report-To' in response.headers
    assert 'CF-RAY' in response.headers
    
    assert response.status_code == requests.codes.ok
    assert response.history == []
    assert response.reason == "OK"
    assert 'elapsed' in response.__attrs__
    assert 'request' in response.__attrs__
    assert '_content' in response.__attrs__
    assert 'url' in response.__attrs__
    assert 'encoding' in response.__attrs__
    assert 'cookies' in response.__attrs__  
    assert response.json().get("status") == "success"
    

#Запрашиваю названия всех пород и потом для каждой породы проверяю контент, который возвращает мне сервис
def test_dog4():
    response_list = requests.get('https://dog.ceo/api/breeds/list/all')
    lis = response_list.json().get("message")
    for key, value in lis.items():
        response = requests.get(f"https://dog.ceo/api/breed/{key}/images/random")
        assert response.json().get("status") == "success"

        assert response.headers['Content-Encoding'] == "gzip"
        assert response.headers['Connection'] == "keep-alive"
        assert response.headers['Server'] == "cloudflare"
        assert 'Date' in response.headers
        assert 'Via' in response.headers
        assert 'Content-Type' in response.headers
        assert 'Vary' in response.headers
        assert 'Cache-Control' in response.headers
        assert 'Age' in response.headers
        assert 'Report-To' in response.headers
        assert 'CF-RAY' in response.headers
        
        assert response.status_code == requests.codes.ok
        assert response.history == []
        assert response.reason == "OK"
        assert 'elapsed' in response.__attrs__
        assert 'request' in response.__attrs__
        assert '_content' in response.__attrs__
        assert 'url' in response.__attrs__
        assert 'encoding' in response.__attrs__
        assert 'cookies' in response.__attrs__  
