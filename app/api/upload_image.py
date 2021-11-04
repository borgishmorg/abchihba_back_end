from typing import Iterable, Optional
import numpy as np
from sqlalchemy.exc import DataError
from PIL import Image, UnidentifiedImageError
from fastapi import File, UploadFile, Depends, HTTPException, status
from app.settings import settings
from ..models import ImageDB
from ..db import session_scope, Session


async def upload(
    file: UploadFile = File(...),
    db: Session = Depends(session_scope)
) -> int:
    image_bytes = await file.read()
    try:
        image = Image.open(file.file, formats=['jpeg'])
    except UnidentifiedImageError:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail='File must be a valid JPEG image'
        )

    image_ratio = image.height / image.width
    image_hash = hash(image)

    image_db = find_image(db, image_ratio, image_hash)

    # Можно добавить проверку на полное совпадение, при совпавших кэшах, чтобы избедать коллизий (но это замедлит работуж и, видимо, это не требуется в задании)
    if image_db:
        if image.height * image.width > image_db.height * image_db.width:
            image_db.data = image_bytes
            image_db.width = image.width
            image_db.height = image.height
            image_db.ratio = image_ratio
            image_db.hash = image_hash
    else:
        image_db = ImageDB(
            data=image_bytes,
            width=image.width,
            height=image.height,
            ratio=image_ratio,
            hash=image_hash
        )

    save_image(db, image_db)

    return image_db.id


def find_image(db: Session, ratio: float, hash: bytes) -> Optional[ImageDB]:
    return (
        db
        .query(ImageDB)
        .filter(ImageDB.hash == hash)
        .filter(ImageDB.ratio <= ratio + settings.RATIO_EPS)
        .filter(ImageDB.ratio >= ratio - settings.RATIO_EPS)
        .first()
    )


def save_image(db: Session, image_db: ImageDB):
    try:
        db.add(image_db)
        db.commit()
    except DataError as data_error:
        if data_error.code == 1406:
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail='File must be less then 16 Mb'
            )
        raise data_error


def hash(image: Image.Image) -> bytes:  # 27 bytes
    image = image.resize((8, 8), Image.ANTIALIAS)
    pixels = np.asarray(image)

    hash_bytes = list()

    for color_channel in range(3):
        channel: np.ndarray = pixels[..., color_channel]

        mean = int(channel.mean())

        hash_bytes.append(mean)  # 1 byte

        diff = channel > mean
        hash_bytes += map(bool_array_to_int, diff)  # 8 bytes

    return bytes(hash_bytes)


def bool_array_to_int(array: Iterable[bool]) -> int:
    result = 0

    for b in array:
        result = result * 2 + b

    return result
