from io import BytesIO
from fastapi import Depends, HTTPException, status, Query
from fastapi.responses import StreamingResponse
from ..models import ImageDB
from ..db import session_scope, Session


async def get(
    id: int = Query(...),
    db: Session = Depends(session_scope)
) -> StreamingResponse:
    image_db = db.query(ImageDB).filter(ImageDB.id == id).first()

    if not image_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Image not found'
        )

    return StreamingResponse(
        content=BytesIO(image_db.data),
        headers={
            'Content-Disposition': f'attachment; filename="{id}.jpg"'
        }
    )
