from fastapi.testclient import TestClient
from http import HTTPStatus


def test_genres_list(client: TestClient):
    response = client.get('/space-image/image_classes')
    assert response.status_code == HTTPStatus.OK

    image_classes = response.json()['image_classes']

    assert isinstance(image_classes, list)


def test_predict(client: TestClient, sample_image_bytes: bytes):
    files = {
        'image': sample_image_bytes,
    }
    response = client.post('/space-image/predict', files=files)

    assert response.status_code == HTTPStatus.OK

    predicted_classes = response.json()['image_classes']

    assert isinstance(predicted_classes, list)


def test_predict_proba(client: TestClient, sample_image_bytes: bytes):
    files = {
        'image': sample_image_bytes,
    }
    response = client.post('/space-image/predict_proba', files=files)

    assert response.status_code == HTTPStatus.OK

    classes_prob = response.json()['probabilities_classes']

    for prob in classes_prob.values():
        assert prob <= 1
        assert prob >= 0
