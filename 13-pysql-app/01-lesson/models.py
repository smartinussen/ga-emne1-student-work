class City:
    def __init__(self, city_id, name):
        self.id = city_id
        self.name = name

    @staticmethod
    def clean_name(value):
        name = value.strip()
        if not 1 <= len(name) <= 35:
            raise ValueError('Use 1 to 35 characters.')
        return name

