## Дипломный проект. Задание 3: Веб-приложение

### Автотесты для проверки веб-приложения Stellar Burgers



### Структура проекта

- `pages` - пакет, содержащий PageObject
- `tests` - пакет, содержащий тесты, разделенные по классам

### Запуск автотестов

**Установка проекта**

```
git clone https://github.com/a-nefedova/Diplom_2
pip install -r requirements.txt
```

**Запуск автотестов и создание allure-отчёта**

```
pytest tests --alluredir=allure_results
allure serve allure_results 
```
