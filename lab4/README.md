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
minikube start.
```
![doc-4](image/doc-3.png)
![doc-5](image/doc-4.png)
