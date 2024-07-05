# FriendAlertAnalytics

## How to Run

### Необходимые для запуска библиотеки:

- FastAPI 
```bash
pip install fastapi
```

- Uvicorn
```bash
pip install uvicorn[standard]
```

### Запуск API

Для запуска API достаточно выполнить команду:
```bash
fastapi dev src/web/controller/demo_controller.py
```
API будет доступен по адресу
```
 http://localhost:8000 
```

### Возможные траблы

- Если одновременно запустить один контроллер несколько раз, то запросы не будут обрабатываться вовсе
- Если закрыть терминал, в котором запущен API, то демон не прекратит работу. В таком случае нужно убивать процесс
