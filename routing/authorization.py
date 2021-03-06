from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from database.db import session
from database.models import Dataset, User

router = APIRouter(prefix="/api/v1")


@router.get("/profile/{mail}/", tags=["authorization"], status_code=200)
async def profile(mail: str):
    """
    User profile with list users datasets
    :param mail: user mail
    :return: json dataset list
    """
    user = session.query(User).filter_by(mail=mail).first()
    s = session.query(Dataset).all()
    for x in s:
        print(x.user_pk)
    ds = session.query(Dataset).filter(Dataset.user_pk == user.id).all()
    print(ds)
    all_dataset = []
    for dataset in ds:
        all_dataset.append({
            'id': dataset.id,
            'name': dataset.name,
            'status': dataset.status,
            'data': dataset.data,
            'sell': dataset.sell,
            'price': dataset.price
        })
    data = {
        'datasets': all_dataset
    }
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)


@router.get("/registration/{mail}/", tags=["authorization"], status_code=200)
async def register(mail: str):
    """
    Register new user
    :param mail: user mail
    :return:
    """
    session.add(User(mail=mail))
    session.commit()
    return JSONResponse(status_code=status.HTTP_200_OK)
