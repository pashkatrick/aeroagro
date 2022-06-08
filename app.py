from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI
from core import CoreController


# TODO:

# 1. Добавить и удалить сельхоз поле в формате GeoJSON - last one
# 2. Получение снимка поля по API поставщиков космических снимков - first one
# 3. Расчёт NDVI для сельхоз поля
# 4. Получить изображение поля с NDVI

# после

# - ссылку на GitHub репозиторий
# - задеплоенный backend на AWS / other
# - файл коллекции Postman.

app = FastAPI()
app.add_middleware(CORSMiddleware)
core = CoreController()


@app.get('/', tags=['index'])
def index():
    return dict(data='Welcome to Aerospace Agro')


@app.post('/field/add')
def add_field():
    # pass geoJSON example
    # return field_id
    core.add_field()


@app.get('/{field_id}/ndvi')
def get_ndvi(field_id: int):
    core.get_ndvi(field_id)


@app.get('/{field_id}/image')
def get_image(field_id: int):
    core.get_image(field_id)


@app.get('/{field_id}/full')
def get_image_and_ndvi(field_id: int):
    core.get_image_and_ndvi(field_id)


@app.delete('/field/{field_id}/delete')
def delete_field(field_id: int):
    core.delete_field(field_id)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
