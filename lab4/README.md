# Задание: Развернуть свой собственный сервис в Kubernetes
### Билд кастомных образов

```bash
# init-контейнер
docker build -t llm-init ./init/

# контейнер приложения
docker build -t llm-app ./llm_app/
```
