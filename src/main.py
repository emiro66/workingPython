from fastapi import FastAPI
import uvicorn


from ino import router

BASE_ROUTE_PATH = "/api/v1"

app = FastAPI(
    openapi_url=f"{BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{BASE_ROUTE_PATH}/docs",
)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )
