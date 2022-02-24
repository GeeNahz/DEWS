
class PredictDetails:
    def __init__(self, year, drought_index, oceanTemp, climate_direction):
        self.year = year
        self.drought_index = drought_index
        self.ocean_temperature = oceanTemp
        self.climate_direction = climate_direction



class SpeiDetails:
    def __init__(self, year, spei_drought_index, region):
        self.year = year
        self.spei_drought_index = spei_drought_index
        self.region = region



class TextDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age
