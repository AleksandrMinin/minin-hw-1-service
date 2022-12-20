# kaggle-planet-service

Разработка сервиса для мультилейбл классификации спутниковых изображений Амазонки.


### Ссылка на сервис
> http://91.206.15.25:9830

### Описание API, примеры запросов

##### 1. Список всех классов, которые предсказывает модель.

###### Request
```http request
GET /space-image/image_classes
```
###### Responses

```http responses
200 OK
```

```json5
{
  "image_classes": [
    "string"
  ]
}
```

```json5
{
  "image_classes": [
    "agriculture",
    "artisinal_mine",
    "bare_ground",
    "blooming",
    "blow_down",
    "clear",
    "cloudy",
    "conventional_mine",
    "cultivation",
    "habitation",
    "haze",
    "partly_cloudy",
    "primary",
    "road",
    "selective_logging",
    "slash_burn",
    "water"
  ]
}
```

##### 2. Предсказание классов для изображения.

###### Request
```http request
POST /space-image/predict

image *
string($binary)
```
###### Responses

```http responses
200 OK
```

```json5
{
  "image_classes": [
    "string"
  ]
}
```

```json5
{
  "image_classes": [
    "clear",
    "primary"
  ]
}
```

##### 3. Получение вероятности для каждого класса по изображению.

###### Request
```http request
POST /space-image/predict_proba

image *
string($binary)
```

###### Responses

```http responses
200 OK
```

```json5
{
  "probabilities_classes": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  }
}
```

```json5
{
  "probabilities_classes": {
    "primary": 0.9930514097213745,
    "clear": 0.7574966549873352,
    "agriculture": 0.1604226976633072,
    "water": 0.08843692392110825,
    "partly_cloudy": 0.07391438633203506,
    "road": 0.07324405014514923,
    "cultivation": 0.03318564593791962,
    "habitation": 0.018299104645848274,
    "haze": 0.011250956915318966,
    "bare_ground": 0.005441127810627222,
    "selective_logging": 0.002786999801173806,
    "blooming": 0.0026602395810186863,
    "cloudy": 0.0026372643187642097,
    "slash_burn": 0.0024998399894684553,
    "artisinal_mine": 0.0017721290932968259,
    "blow_down": 0.0016868725651875138,
    "conventional_mine": 0.0015352433547377586
  }
}
```

##### 4. Проверка работы сервиса.

###### Request
```http request
GET /space-image/health_check

```
###### Responses

```http responses
200 OK
```

```json5
"string"
```

```json5
"OK"
```

### Разворачивание сервиса
#### Локально
1. Создание и активация окружения
    ```
    python3 -m venv /path/to/new/virtual/environment
    ```
    ```
    source /path/to/new/virtual/environment/bin/activate
    ```
2. Установка пакетов

    В активированном окружении:
    ```
    make install 
    ```
3. Обновление весов модели(требуется, чтобы был ssh-ключ ~/.ssh/id_rsa для входа на aleksandrminin@91.206.15.25):
    ```
    make download_weights
    ```
4. Запуск сервиса:
    ```
    python3 -m uvicorn app:create_app --host='0.0.0.0' --port=9930
    ```

#### Через Docker
1. Создание и активация окружения
    ```
    python3 -m venv /path/to/new/virtual/environment
    ```
    ```
    source /path/to/new/virtual/environment/bin/activate
    ```
2. Установка пакетов

    В активированном окружении:
    ```
    pip install --upgrade pip
    pip install dvc[ssh]==2.34.2
    ```
3. Обновление весов модели(требуется, чтобы был ssh-ключ ~/.ssh/id_rsa для входа на aleksandrminin@91.206.15.25):
    ```
    make download_weights
    ```
4. Создание Image:
    ```
    docker build -t  $(DOCKER_IMAGE):$(DOCKER_TAG) .
    ```
5. В списке Images находим нужный ImageID:
    ```
    docker images
    ```
6. Запуск Container:
    ```
    docker run -d --name space_image_service -p 9830:9930 ImageID
    ```


### Запуск тестов
1. Unit tests:
    ```
    make run_unit_tests
    ```
2. Integration tests:
    ```
    make run_integration_tests
    ```
3. Lint:
    ```
    make lint
    ```

