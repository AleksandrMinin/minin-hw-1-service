from copy import deepcopy
import numpy as np
from src.containers.containers import AppContainer


def test_predicts_not_fail(app_container: AppContainer, sample_image_np: np.ndarray):
    space_image_classifier = app_container.space_image_classifier()
    space_image_classifier.predict(sample_image_np)
    space_image_classifier.predict_proba(sample_image_np)


def test_prob_less_or_equal_to_one(app_container: AppContainer, sample_image_np: np.ndarray):
    space_image_classifier = app_container.space_image_classifier()
    classes_prob = space_image_classifier.predict_proba(sample_image_np)
    for prob in classes_prob.values():
        assert prob <= 1
        assert prob >= 0


def test_predict_dont_mutate_initial_image(app_container: AppContainer, sample_image_np: np.ndarray):
    initial_image = deepcopy(sample_image_np)
    space_image_classifier = app_container.space_image_classifier()
    space_image_classifier.predict(sample_image_np)

    assert np.allclose(initial_image, sample_image_np)
