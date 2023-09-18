import dill

class SerializationUtil:
    def load(self, file):
        try:
            with open(file, 'rb') as f:
                return dill.load(f)
        except FileNotFoundError:
            return None
        except Exception as e:
            raise e

    def dump(self, item, filetodumpinto):
        try:
            with open(filetodumpinto, 'wb') as f:
                dill.dump(item, f)
        except Exception as e:
            raise e
