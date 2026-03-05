from fastapi.routing import APIRouter


router = APIRouter(prefix='/123')

@router.get('/sum/{a}+{b}')
def sum(a:int,b:int):
    return a+b

@router.get('/sum')
def sum2(a:int,b:int):
    return a+b