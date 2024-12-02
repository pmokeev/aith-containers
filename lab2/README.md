# Lab 2

Демо-проект с 3 разными сервисами, которые запускаются через docker-compose

## Структура проекта

```
.
├── docker-compose.yml
├── README.md
├── .env
├── init/
│   ├── Dockerfile
│   └── init.py
├── db/
│   └── Dockerfile
└── app/
    ├── Dockerfile
    ├── requirements.txt
    └── main.py
```

## Сервисы

### Приложение на FastAPI
- Умеет читать текст приветствия из БД
- Использует порт 8000
- API:
  - GET `/` - возвращает приветствие
  - GET `/health` - health check

### PostgreSQL БД
- Использует volume для персистентности данных
- Есть health check

### Инициализатор
- Создает нужные таблицы в БД и закидывает туда текст приветствия
- Зависит от БД

## Окружение
Хранится в .env файле
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

## Вопросы

### Можно ли в docker-compose.yml ограничивать ресурсы?
Да, можно, через deploy -> resources -> limits



### Можно ли запустить лишь отдельный сервис?
Да, можно, если написать его название в команде, к примеру:
```bash
docker-compose up db
```
Правда если этот сервис depends on ещё какой-то, тот тоже будет запущен.


## Использование

```bash
docker-compose up --build
curl http://localhost:8000/
curl http://localhost:8000/health
```
