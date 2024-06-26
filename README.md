## Задание
Требовалось реализовать класс `VehicleManager` для работы с [API](https://test.tspb.su/test-task).

Класс должен поддерживать следующий функционал:
- Получение списка автомобилей
- Получение списка автомобилей по заданным параметрам (фильтрация)
- Получение информации об автомобиле по id
- Добавление нового автомобиля
- Изменение информации об автомобиле
- Удаление автомобиля
- Расчет расстояние между двумя автомобилями (в метрах)
- Нахождение ближайшего автомобиля к заданному

Класс `VehicleManager` должен оперировать объектами класса `Vehicle`,
который хранит информацию об автомобиле.

## Описание и запуск приложения
Перед запуском проекта требуется установить виртуальное окружение. Далее 
требуется установить зависимости, которые используются в проекте, они 
вынесены для удобства в отдельный файл **requirements.txt**. Для установки 
библиотек в созданное виртуальное окружение в консоль требуется написать
команду: `pip install -r requirements.txt`. Реализация выполнена на версии python 3.12.

Для запуска приложения требуется написать команду `python main.py`.
В консоль выведется результат работы приложения, включающий себя то, что
необходимо было реализовать в задании. 

P.S. С помощью магического метода класса `Vehicle` формат вывода объектов
соответствует заданию.