import random
from copy import deepcopy

import cv2
import numpy as np

from src.containers.containers import AppContainer


class FakeImageClassifier:

    def predict(self, image):
        return []

    def predict_proba(self, image):
        return dict(value=0.2)


def test_predicts_not_fail(app_container: AppContainer, sample_image_np: np.ndarray):
    with app_container.reset_singletons():
        with app_container.space_image_classifier.override(FakeImageClassifier()):
            space_image_analytics = app_container.space_image_analytics()
            space_image_analytics.predict(sample_image_np)
            space_image_analytics.predict_proba(sample_image_np)


def test_prob_less_or_equal_to_one(app_container: AppContainer, sample_image_np: np.ndarray):
    with app_container.reset_singletons():
        with app_container.space_image_classifier.override(FakeImageClassifier()):
            space_image_analytics = app_container.space_image_analytics()
            classes_prob = space_image_analytics.predict_proba(sample_image_np)
            for prob in classes_prob.values():
                assert prob <= 1
                assert prob >= 0


def test_predict_dont_mutate_initial_image(app_container: AppContainer, sample_image_np: np.ndarray):
    with app_container.reset_singletons():
        with app_container.space_image_classifier.override(FakeImageClassifier()):
            initial_image = deepcopy(sample_image_np)
            space_image_analytics = app_container.space_image_analytics()
            space_image_analytics.predict(sample_image_np)

            assert np.allclose(initial_image, sample_image_np)
