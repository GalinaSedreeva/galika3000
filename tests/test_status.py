# def test_status(check_status):
#     assert check_status == 200

import requests

# %%
def test_jph1():
    param = {'id': [1, 2, 3]}
    response = requests.get('https://jsonplaceholder.typicode.com/posts', params=param)
    print(response.text)
    assert response.status_code == 200
#test_jph1()    

# %%
def test_jph1():
    param = {'username': ['Bret', 'Kamren', 'Delphine']}
    response = requests.get('https://jsonplaceholder.typicode.com/users', params=param)
    print(response.text)
    assert response.status_code == 200
#test_jph1()    

# %%
def test_jph3():
    response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
    print(response.text)
    assert response.status_code == 200
#test_jph3()    

# %%
def test_jph2():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print(response.text)
    assert response.status_code == 200
#test_jph2()    

# %%
def test_jph4():
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1')
    print(response.text)
    assert response.status_code == 200
    print(response.cookies)
#test_jph4()    

# %%
def test_jph5():
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/1')
    print(response.text)
    assert response.status_code == 200
#test_jph5()    

# %%
def test_bre1():
    param = {'name': ['Texas Ale Project', 'Basement Brewers of Texas', 'Texas Leaguer Brewing Company']}

    response = requests.get('https://api.openbrewerydb.org/v1/breweries/autocomplete?query=texas', params=param)
    print(response.text)
    assert response.status_code == 200
#test_bre1()    

# %%
def test_bre2():
    param = {'brewery_type': ['nano', 'micro', 'bar']}

    response = requests.get('https://api.openbrewerydb.org/v1/breweries?by_country=south%20korea', params=param)
    print(response.json())
    assert response.status_code == 200
#test_bre2()  

# %%
def test_bre3():
    param = {'state': ['Wisconsin','Texas']}

    response = requests.get('https://api.openbrewerydb.org/v1/breweries', params=param)
    print(response.json())
    assert response.status_code == 200
    print(response.cookies)
#test_bre3()  

# %%
def test_bre4():
    param = {'state': ['Wisconsin','Texas']}

    response = requests.get('https://api.openbrewerydb.org/v1/breweries', params=param)
    print(response.json())
    assert response.status_code == 200
#test_bre4()  

# %%
def test_bre5():
    response = requests.get(' https://api.openbrewerydb.org/v1/breweries/meta?by_type=micro')
    print(response.text)
    assert response.status_code == 200
#test_bre5()    

# %%
def test_dog1():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    print(response.text)
    assert response.status_code == 200
#test_dog1()    

# %%
def test_dog2():
    response = requests.get('https://dog.ceo/api/breed/hound/list')
    print(response.json())
    assert response.status_code == 200
    assert response.json().get("status") == "success"
#test_dog2()    

# %%
def test_dog3():
    response = requests.get('https://dog.ceo/api/breed/hound/plott/images')
    print(response.json())
    assert response.status_code == 200
    assert response.json().get("status") == "success"
    print(response.cookies)
#test_dog3() 

#Запрашиваю названия всех пород и потом у каждой породы проверяю код
def test_dog4():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    lis = response.json().get("message")
    for key, value in lis.items():
        r = requests.get(f"https://dog.ceo/api/breed/{key}/images/random")
        assert r.status_code == 200

#test_dog4()



# %%
#response = requests.get('https://dog.ceo/api/breed/hound/plott/images')

# Получение заголовков ответа
#headers = response.headers

# Вывод заголовков
#for key, value in headers.items():
 #   print(f'{key}: {value}')

# %% [markdown]
# Реализуйте в отдельном модуле (файле) тестовую функцию, которая будет принимать 2 параметра:
# 
# url - значение по умолчанию https://ya.ru
# status_code - значение по умолчанию 200
# 
# Параметры должны быть реализованы через pytest.addoption. Можно положить фикcтуру и тестовую функцию в один файл. Основная задача чтобы ваш тест проверял статус ответа по переданному URL. Например, по несуществующему адресу https://ya.ru/sfhfh должен быть валидным ответ 404
# 
# Пример запуска pytest:
# 
# test_module.py --url=https://mail.ru --status_code=200

# %%
# def pytest_addoption(parser):
#     parser.addoption(
#         "--url",
#         default='https://ya.ru'
#     )

#     parser.addoption(
#         "--status_code",
#         default=200
#     )

# # %%
# @pytest.fixture
# def check_status(request):
#     return request.config.getoption("--url")


