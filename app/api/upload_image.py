from PIL import Image, UnidentifiedImageError
from sqlalchemy.exc import DataError
from fastapi import File, UploadFile, Depends, HTTPException, status
from ..models import ImageDB
from ..db import session_scope, Session


async def upload(
    file: UploadFile = File(...),
    db: Session = Depends(session_scope)
) -> int:
    image_bytes = await file.read()
    try:
        _ = Image.open(file.file, formats=['jpeg'])
    except UnidentifiedImageError:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail='File must be a valid JPEG image'
        )

    try:
        image_db = ImageDB(data=image_bytes)
        db.add(image_db)
        db.commit()
    except DataError as data_error:
        if data_error.code == 1406:
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail='File must be less then 16 Mb'
            )
        raise data_error

    return image_db.id
