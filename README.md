# Сайт "Куда пойти - интересные места Москвы".

Вы можете выбрать места на карте и получить больше информации по каждой точке.

Демо-версия сайта: [v1ztep.pythonanywhere.com](https://v1ztep.pythonanywhere.com/)
![png](github_preview/where_to_go.png)

## Настройки

Для запуска у вас уже должен быть установлен [Python 3](https://www.python.org/downloads/release/python-379/).

### Переменные окружения

Создайте файл `.env` в корневой папке с кодом и запишите туда:
```
SECRET_KEY=ваш секретный ключ
DEBUG=True or False (True для отладки проекта)
```

## Запуск

- Скачайте код.
- Установите зависимости командой:
```
pip install -r requirements.txt
```
- Создайте базу данных SQLite с помощью команды:
```
python manage.py migrate
```
- Запустите сервер разработки командой: 
```
python manage.py runserver
```
## Админ панель

- Создайте суперпользователя с помощью команды:
```
python manage.py createsuperuser
```
Ссылка на панель администратора: `http://127.0.0.1:8000/admin/`. 
В админ панеле вы можете наполнять места(координаты), их описание и фотографии.

## Загрузка новых мест с помощью скрипта

Вы можете использовать специальную команду для подгрузки новых локаций (можно 
добавлять множество ссылок через пробел):
```
python manage.py load_place url_to_json
```
Внутри должен быть json формат вида:
```
{
    title: "Экскурсионная компания «Легенды Москвы»",
    imgs: [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
        ...
    ],
    description_short: "Неважно, живёте ли вы в Москве всю жизнь или впервые оказались в столице, составить ёмкий, познавательный и впечатляющий маршрут по городу — творческая и непростая задача. И её с удовольствием берёт на себя экскурсионная компания «Легенды Москвы»!",
    description_long: "<p>Экскурсия от компании «Легенды Москвы» — простой, удобный и приятный способ познакомиться с городом или освежить свои чувства к нему. Что выберете вы — классическую или необычную экскурсию, пешую прогулку или путешествие по городу на автобусе? Любые варианты можно скомбинировать в уникальный маршрут и создать собственную индивидуальную экскурсионную программу.</p><p>Компания «Легенды Москвы» сотрудничает с аккредитованными экскурсоводами и тщательно следит за качеством экскурсий и сервиса. Автобусные экскурсии проводятся на комфортабельном современном транспорте. Для вашего удобства вы можете заранее забронировать конкретное место в автобусе — это делает посадку организованной и понятной.</p><p>По любым вопросам вы можете круглосуточно обратиться по телефонам горячей линии.</p><p>Подробности узнавайте <a class="external-link" href="https://moscowlegends.ru " target="_blank">на сайте</a>. За обновлениями удобно следить <a class="external-link" href="https://vk.com/legends_of_moscow " target="_blank">«ВКонтакте»</a>, <a class="external-link" href="https://www.facebook.com/legendsofmoscow?ref=bookmarks " target="_blank">в Facebook</a>.</p>",
    coordinates: {
        lng: "37.64912239999976",
        lat: "55.77754550000014",
    },
}
```

Тестовые данные взяты с сайта [KudaGo](https://kudago.com/).
