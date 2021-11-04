import uvicorn
from app import settings

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='0.0.0.0',
        port=settings.PORT,
        reload=settings.ENABLE_AUTORELOAD
    )
