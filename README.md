## Local deploy
./local.sh

## Production deploy
./deploy.sh

Добавить в Github HOST, USERNAME и PASSWORD для CI/CD.

SSL:

https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71

Прописать следующие команды:

`sudo chown -R 777:777 ./logs/gunicorn`

`sudo chown -R 777:777 ./psb_learning/media`

Т. к. это mounted папки, в которые хотят писать приложения внутри докера. Но они работают не от root, а от пользователя 777:777.

## Линтеры

Встроены в vscode, с помощью файла .vscode/settings.

Через коммандную строку:

`pylint psb_learning`

`isort psb_learning`

`pycodestyle psb_learning`

## Тестирование

`docker exec django bash -c "python manage.py test --settings config.settings.test --parallel --keepdb"`

Test coverage: 

`docker exec django bash -c "coverage run manage.py test --settings config.settings.test --keepdb && coverage html"`

смотрим htmlcov/index.html


## Postgres DB Backup:
https://cookiecutter-django.readthedocs.io/en/latest/docker-postgres-backups.html

