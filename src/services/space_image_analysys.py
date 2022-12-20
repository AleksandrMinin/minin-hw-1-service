from typing import Dict, List

import numpy as np

from src.services.space_image_classifier import SpaceImageClassifier


class SpaceImageAnalytics:

    def __init__(self, space_image_classifier: SpaceImageClassifier):
        self._space_image_classifier = space_image_classifier

    @property
    def image_classes(self):
        return self._space_image_classifier.classes

    def predict(self, image: np.ndarray) -> List[str]:
        """Предсказания класса по спутниковому изображению.

        :param image: входное RGB изображение;
        :return: список классов.
        """

        return self._space_image_classifier.predict(image)

    def predict_proba(self, image: np.ndarray) -> Dict[str, float]:
        """Предсказание вероятностей принадлежности изображения к классам.

        :param image: входное RGB изображение;
        :return: словарь вида `класс`: вероятность.
        """

        return self._space_image_classifier.predict_proba(image)
