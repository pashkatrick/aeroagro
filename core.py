
from decouple import config


class base(object):

    def exc_handler(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f'error in method {func.__name__}: {e}')
                return False
        return wrapper

    def update_handler(upd_data):
        return {k: v for k, v in upd_data.items() if v is not None}

    def logger(func):
        return func


class CoreController():

    @base.exc_handler
    def add_field(self, geo_json_obj: dict):
        pass

    @base.exc_handler
    def get_field(self, id: int):
        pass

    @base.exc_handler
    def delete_field(self, id: int):
        pass

    @base.exc_handler
    def get_ndvi(self, field_id: int):
        pass

    @base.exc_handler
    def get_image(self, field_id: int):
        pass

    @base.exc_handler
    def get_image_and_ndvi(self, field_id: int):
        pass
