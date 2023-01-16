# Порядок запуска API Проекта YaMDb в Docker контейнерах
### Краткое описание YaMDb
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся. Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка».
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.
Ресурсы API YaMDb:
- Ресурс auth: аутентификация.
- Ресурс users: пользователи.
- Ресурс titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- Ресурс categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс reviews: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс comments: комментарии к отзывам. Комментарий привязан к определённому отзыву.

### Шаблон наполнения env-файла
В директории `infra` создать файл `.env`.
Шаблон заполнения файла `.env`:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```
### Описание команд для запуска приложения в контейнерах
Клонировать репозиторий и перейти в него в командной строке.  
Из директории `infra` cобрать и запустить контейнеры:
```sh
docker-compose up -d --build 
```
В контейнере web выполнить миграции и собрать статику:
```sh
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input 
```
### Описание команды для заполнения базы данными
Для заполнения базы данных тестовыми данными, находясь в директории `infra`, выполнить команду:
```sh
docker-compose exec web python manage.py loaddata fixtures.json
```
Приложение будет доступно по адресу http://localhost/.  
Создать суперпользователя:
```sh
docker-compose exec web python manage.py createsuperuser
```
Используя учетную запись суперпользователя зайти в админ-панель http://localhost/admin.  
По адресу http://localhost/redoc/ находится подробная документация с описаниями доступных эндпоинтов.

Образ `api_yamdb` проекта доступен в репозитории DockerHub
```sh
docker pull ferumv/api_yamdb:v1.01.2023
```
### Использованные технологии
ля разработкиw Django-приложений YaMDb и API YaMDb использовались:
- Python 3.7.9
- Django 2.2.16
- Djangorestframework 3.12.4
- Djangorestframework-simplejwt 4.7.2
- Djangj-filter 2.4.0  

Для взаимодействия Django-приложений и web-сервера Nginx использовался WSGI-сервер Gunicorn:
- Gunicorn 20.0.4  

Драйвер для работы с PostgreSQL:
- Psycopg2-binary 2.8.6

### Автор
Мария Феруленкова