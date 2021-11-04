from io import BytesIO
from PIL import Image
from fastapi import Depends, HTTPException, status, Query
from fastapi.responses import StreamingResponse
from ..models import ImageDB
from ..db import session_scope, Session


async def get(
    id: int = Query(...),
    scale: float = Query(1., gt=0.),
    db: Session = Depends(session_scope)
) -> StreamingResponse:
    image_db = db.query(ImageDB).filter(ImageDB.id == id).first()

    if not image_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Image not found'
        )

    image = Image.open(BytesIO(image_db.data), formats=['JPEG'])

    if scale != 1.:
        new_width = max(int(image.width * scale), 1)
        new_height = max(int(image.height * scale), 1)

        image = image.resize((new_width, new_height))

    return StreamingResponse(
        content=image_io(image),
        headers={
            'Content-Disposition': f'attachment; filename="{id}.jpg"'
        }
    )


def image_io(image: Image.Image) -> BytesIO:
    image_io = BytesIO()
    image.save(image_io, format='JPEG')
    image_io.seek(0)
    return image_io
