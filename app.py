from typing import Optional

import uvicorn
from fastapi import FastAPI
from omegaconf import OmegaConf, DictConfig

from src.containers.containers import AppContainer
from src.routes.routers import router as app_router
from src.routes import space_image_router

def create_app() -> FastAPI:
    cfg = OmegaConf.load('config/config.yml')
    container = AppContainer()
    container.config.from_dict(cfg)
    container.wire([space_image_router])
    app = FastAPI()
    set_routers(app)
    return app


def set_routers(app: FastAPI):
    app.include_router(app_router, prefix='/space-image', tags=['space-image'])

if __name__ == '__main__':
    app = create_app()
    uvicorn.run(app, port=2444, host='0.0.0.0')
