# Имплементация проекта
В данной директории лежат подпроекты для backend и frontend частей habrolinker. Разложены они так, чтобы их можно было относительно удобным способом запустить через Docker.
## Быстрый старт через Docker
1) Установите [Docker](https://docs.docker.com/desktop/) для вашей платформы. Для Windows рекомендуется использовать [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)
2) Из данной директории запустите 
```
docker compose up -d --build
```
или, если вы уже хоть раз собирали контейнеры
```
docker compose up -d
```
## Структура проекта
1) **backend** - директория для backend API сервера на [FastAPI](https://fastapi.tiangolo.com/)
2) **frontend** - директория для frontend web-приложения на [React](https://react.dev/)
2) **database** - директория для хранения файлов необходимых для развертывания правильной базы данных [PostreSQL](https://www.postgresql.org/)
3) **docker-compose.yml** - YAML файл для "удобного" развертывания контейнеров
## Список контейнеров
1) **habrolink_back** - контейнер для backend API сервера на [FastAPI](https://fastapi.tiangolo.com/)
2) **habrolink_front** - контейнер для frontend web-приложения на [React](https://react.dev/)
2) **habrolink_db** - контейнер с развернутой базой данных [PostreSQL](https://www.postgresql.org/)
