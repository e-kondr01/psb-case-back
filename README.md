## Реализованная функциональность
1. Retrieve и Update для информации по проекту
2. Авторизация и разграничение ролей
3. Прохождение викторины с начислением баллов пользователю за правильный ответ
## Особенность проекта в следующем
а в чём??м
## Основной стек технологий
Backend на Python Django Rest Framework, деплой с помощью Docker, Nginx, Gunicorn.
Фронт на React.js
## Демо
Демо доступно по адресу: https://e-kondr01.ru

Реквизиты тестового пользователя: email: worker@test.com, пароль: TESTtest123

Реквизиты тестового руководителя: email: supervisor@test.com, пароль: TESTtest123
## Запуск проекта
Для запуска проекта нужно установить docker и docker-compose,
после чего выполнить скрипт local.sh

Для применения миграций надо выполнить следующую команду:

`docker exec psb_learning_django bash -c "python manage.py migrate"`
## Разработчики
Егор Кондрашов, telegram: @e_kondr01
