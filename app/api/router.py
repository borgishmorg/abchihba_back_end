from fastapi import APIRouter
from .get_image import get
from .upload_image import upload

router = APIRouter(
    prefix='',
    tags=['api']
)

router.add_api_route(
    path='/get',
    endpoint=get,
    methods=['GET']
)
router.add_api_route(
    path='/upload',
    endpoint=upload,
    methods=['POST']
)
