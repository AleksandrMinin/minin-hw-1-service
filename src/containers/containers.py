from dependency_injector import containers, providers

from src.services.space_image_analysys import SpaceImageAnalytics
from src.services.space_image_classifier import SpaceImageClassifier


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    space_image_classifier = providers.Factory(
        SpaceImageClassifier,
        config=config.services.space_image_classifier,
    )

    space_image_analytics = providers.Singleton(
        SpaceImageAnalytics,
        space_image_classifier=space_image_classifier,
    )
