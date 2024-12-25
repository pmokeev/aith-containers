# Задание: Развернуть свой собственный сервис в Kubernetes
### building Custom Images 


```bash

docker build -t llm-init ./init/

docker build -t llm-app ./llm_app/
```
![doc-1](image/doc-1.png)

### Tакже для Language-Model 
```bash

docker build -t llm-app ./llm_app/
```
![doc-2](image/doc-2.png)

### Images for the models 

```bash
# Image
cd init
docker build -t llm-init .

# Image
cd ../llm_app
docker build -t llm-app .
```
![doc-3](image/doc-11.png)

### запускаем minikube
```bash
minikube start
```
![doc-4](image/doc-3.png)
![doc-5](image/doc-4.png)


### Container   Результаты

![doc-6](image/doc-12.png)

##  создаем namespace
```bash
kubectl create namespace llm-app

```
## Applying all the manifestations to the namespace

```bash
kubectl apply -f secrets.yaml -n llm-app


kubectl apply -f volume.yaml -n llm-app


kubectl apply -f db_deploy.yaml -n llm-app


kubectl apply -f db_service.yaml -n llm-app


kubectl apply -f app_deploy.yaml -n llm-app


kubectl apply -f app_service.yaml -n llm-app


minikube service llm-app -n llm-app
```
## Проверяем If all pods are working 
```bash

$ kubectl get pods -n llm-app
```
![doc-7](image/doc-7.png)
## ALL ports should be infinity 
```bash
 ports:
        - containerPort: 1337
        command: ["sleep", "infinity"] 
```
![doc-8](image/doc-8.png)
