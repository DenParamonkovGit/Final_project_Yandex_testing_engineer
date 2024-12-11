import requests
import configuration

def post_create_order(order_data): # Объявляем функцию создания заказа
    url = configuration.URL + configuration.CREATE_ORDER # Составляем запрос и присваиваем переменной url
    response = requests.post(url, #С помощью библиотеки requests отправляем post запрос
                             json=order_data) # Указываем, что данные в JSON и вставляем тело запроса
    return response # Возвращаем объект ответа

def get_order_info(track): # Объявляем функцию получения информации заказа по номеру
    url = configuration.URL + configuration.SEARCH_ORDER + str(track) # Составляем запрос и присваиваем переменной url
    response = requests.get(url) # Пользуясь библиотекой requests отправляем запрос и возвращаем инфо о результате запроса
    return response # Возвращаем объект ответа