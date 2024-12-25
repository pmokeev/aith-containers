



### Билд кастомных образов

```bash
# init-контейнер
docker build -t llm-init ./init/

# контейнер приложения
docker build -t llm-app ./llm_app/
```

### Оркестрация

```bash
# билдим образы init-контейнера
cd init
docker build -t llm-init .

# билдим образы init-контейнера
cd ../llm_app
docker build -t llm-app .

# возвращаемся в корень
cd ..

# запускает minikube
minikube start

# загружаем в него образы 
minikube image load llm-init
minikube image load llm-app

# создаем namespace
kubectl create namespace llm-app

# создаем секрет с переменными среды
kubectl apply -f secrets.yaml -n llm-app

# volume для базы данных
kubectl apply -f volume.yaml -n llm-app

# запуск базы данных
kubectl apply -f db_deploy.yaml -n llm-app

# настройка сервиса БД
kubectl apply -f db_service.yaml -n llm-app

# запуск приложения
kubectl apply -f app_deploy.yaml -n llm-app

# настройка сервиса приложения
kubectl apply -f app_service.yaml -n llm-app

# запуск сервера
minikube service llm-app -n llm-app
```
