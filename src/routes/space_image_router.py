import cv2
import numpy as np
from typing import Dict, List
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, File, HTTPException

from src.containers.containers import AppContainer
from src.routes.routers import router
from src.services.space_image_analysys import SpaceImageAnalytics

from pydantic import BaseModel


class ItemOutClasses(BaseModel):
    image_classes: List[str]


class ItemOutPredictProba(BaseModel):
    probabilities_classes: Dict[str, float]


@router.get('/image_classes', response_model=ItemOutClasses)
@inject
def image_classes_list(service: SpaceImageAnalytics = Depends(Provide[AppContainer.space_image_analytics])):
    return ItemOutClasses(**{'image_classes': service.image_classes})


@router.post('/predict', response_model=ItemOutClasses)
@inject
def predict(
    image: bytes = File(),
    service: SpaceImageAnalytics = Depends(Provide[AppContainer.space_image_analytics]),
):
    try:
        img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)

    except Exception:
        raise HTTPException(400, detail="Invalid document type")

    image_classes = service.predict(img)

    return ItemOutClasses(**{'image_classes': image_classes})


@router.post('/predict_proba', response_model=ItemOutPredictProba)
@inject
def predict_proba(
    image: bytes = File(),
    service: SpaceImageAnalytics = Depends(Provide[AppContainer.space_image_analytics]),
):
    try:
        img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)

    except Exception:
        raise HTTPException(400, detail="Invalid document type")

    prob_classes = service.predict_proba(img)

    return ItemOutPredictProba(**{'probabilities_classes': prob_classes})


@router.get('/health_check')
def health_check():
    return 'OK'
