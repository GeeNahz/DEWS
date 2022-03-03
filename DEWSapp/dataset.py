
class PredictDetails:
    def __init__(self, year, drought_index, oceanTemp, climate_direction, SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO, region):
        self.year = year
        self.drought_index = drought_index
        self.ocean_temperature = oceanTemp
        self.climate_direction = climate_direction
        self.SPEI_april = SPEIA
        self.SPEI_may = SPEIM
        self.SPEI_june = SPEIJN
        self.SPEI_july = SPEIJY
        self.SPEI_aug = SPEIAG
        self.SPEI_sept = SPEIS
        self.SPEI_oct = SPEIO
        self.region = region



class SpeiDetails:
    def __init__(self, year, spei_drought_index, region):
        self.year = year
        self.spei_drought_index = spei_drought_index
        self.region = region



class TextDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age
