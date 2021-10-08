from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from database.db import session
from database.models import Dataset, User

router = APIRouter(prefix="/api/v1")


@router.get("/profile/{user_id}", status_code=200)
async def profile(user_id: str):
    ds = session.query(Dataset).filter_by(user_id=int(user_id))
    all_dataset = []
    for dataset in ds:
        all_dataset.append({
            'name': dataset.name,
            'url': dataset.url,
            'sell': dataset.sell,
            'price': dataset.price
        })
    data = {
        'datasets': all_dataset
    }
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)


@router.get("/registration/{mail}", status_code=200)
async def register(mail: str):
    session.add(User(mail=mail))
    session.commit()
    return JSONResponse(status_code=status.HTTP_200_OK)