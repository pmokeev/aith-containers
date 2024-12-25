# Используем актуальную версию базового образа
FROM python:3.11.5-alpine


# устанавливаем только нужные файлы
COPY start.py /app/start.py
COPY DAO.py /app/DAO.py
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости с указанием версии
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

# Запускаем без root прав
USER nobody
CMD ["python3", "./start.py"]