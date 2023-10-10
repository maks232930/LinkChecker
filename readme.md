# LinkChecker - Веб-приложение для проверки веб-ссылок

LinkChecker - это приложение, построенное с использованием Django и других современных технологий, которое предназначено для управления списком веб-ссылок и автоматической проверки их доступности на основе условий, заданных пользователем. Приложение позволяет пользователям добавлять ссылки, определять условия проверки, просматривать результаты проверки и управлять периодической проверкой.

## Технологический стек

LinkChecker использует следующий технологический стек:

- Docker: для контейнеризации приложения и его зависимостей.
- Django: веб-фреймворк для разработки приложений.
- PostgreSQL: реляционная база данных для хранения информации о ссылках и результатах проверки.
- Celery: фреймворк для обработки асинхронных задач, таких как периодическая проверка ссылок.
- Redis: для хранения очередей задач Celery.
- djangorestframework: фреймворк для разработки RESTful API.
- rest_framework_swagger: для автоматической генерации интерфейса Swagger на основе API приложения.

## Функциональность приложения

### Управление ссылками

- Пользователи могут добавлять новые ссылки в базу данных, указывая имя, URL и условия проверки.
- Условия проверки могут включать: правильный JSON-ответ, наличие определенного текста в ответе, успешный HTTP-статус код 200.
- Пользователи могут редактировать имя, URL и условия проверки для существующих ссылок.
- Пользователи могут включать или выключать периодическую проверку для каждой ссылки.

### Периодическая проверка ссылок

- Приложение автоматически выполняет периодическую проверку добавленных ссылок каждые 3 минуты. 
- Время можно изменить.
- Результаты проверки сохраняются в базе данных, включая дату и время последней проверки и результат (пройдено или не пройдено).

### Интерфейс взаимодействия

- Пользователи могут взаимодействовать с приложением через административный интерфейс Django для просмотра и управления ссылками.
- Также предоставляется интерфейс API, представленный в Swagger UI, созданный на основе API приложения с использованием Django REST framework (DRF).

## Установка и запуск

Для запуска LinkChecker в среде Docker выполните следующие шаги:

1. Убедитесь, что Docker и Docker Compose установлены на вашем компьютере.

2. Клонируйте репозиторий LinkChecker:

   ```bash
   https://github.com/maks232930/LinkChecker.git
   cd link-checker
    ```
3. Запустите контейнер:
    ```bash
    sudo docker-compose up --build
   ```
4. Создайте суперпользователя:
    ```bash
    sudo docker-compose exec web python manage.py createsuperuser
   ```
5. Создайте "Периодическую задачу":
    ```
   Напишите название;
   Задача (зарегистрированные): выберите link_manager.main_task;
   Создайте расписание в разделе Schedule
   ```
6. Можно добавлять ссылки.