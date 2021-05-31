from pathlib import Path


class LastReadStore:
    def __init__(self, store_location):
        self.store_location = Path(store_location)
        self.store_location.parent.mkdir(exist_ok=True, parents=True)
        self.store_location.touch(exist_ok=True)

    def set_last_read(self, last_read_id):
        self.store_location.write_text(last_read_id)

    def get_last_read(self):
        store_content = self.store_location.read_text().rstrip()
        if store_content:
            return store_content
        else:
            return None
