from .extract import ExtractData
from .generateData import function_spei

# import time

def spei_calcs(month, dataDoc, doc, year, rvDoc):


    mean_Jan_c = ExtractData('jan', doc, value='mean')
    mean_Jan = mean_Jan_c.value_extract()

    mean_Dec_c = ExtractData('dec', doc, value='mean')
    mean_Dec = mean_Dec_c.value_extract()

    b_Dec_c = ExtractData('jan', doc, 'b')
    b_Dec = b_Dec_c.value_extract()

    SPEID_C = ExtractData('dec', dataDoc, yr=year-1)
    SPEID = SPEID_C.yr_extract()

    rv_Jan_c = ExtractData('jan', rvDoc, yr=year)
    rv_Jan = rv_Jan_c.yr_extract()

    s_Jan_c = ExtractData('jan', doc, value='s')
    s_Jan = s_Jan_c.value_extract()

    r_Dec_c = ExtractData('jan', doc, value='r')
    r_Dec = r_Dec_c.value_extract()

    SPEIJ = mean_Jan+b_Dec*(SPEID-mean_Dec)+rv_Jan*s_Jan*((1-(r_Dec)**2)**0.5)

    SPEIJ = round(SPEIJ, 2)

    ExtractData('jan', dataDoc, yr=year).save_value(SPEIJ)

    SPEIF = ExtractData('feb', dataDoc, yr=year).yr_extract()

    if SPEIF is not None:
        pass
    else:
        function_spei(dataDoc, doc, rvDoc, year=year)
        SPEIF = ExtractData('feb', dataDoc, yr=year).yr_extract()
    
    # at this point all the other month's data must have been generated
    SPEIM = ExtractData('march', dataDoc, yr=year).yr_extract()
    SPEIA = ExtractData('april', dataDoc, yr=year).yr_extract()
    SPEIMY = ExtractData('may', dataDoc, yr=year).yr_extract()
    SPEIJN = ExtractData('june', dataDoc, yr=year).yr_extract()
    SPEIJY = ExtractData('july', dataDoc, yr=year).yr_extract()
    SPEIAG = ExtractData('aug', dataDoc, yr=year).yr_extract()
    SPEIS = ExtractData('sept', dataDoc, yr=year).yr_extract()
    SPEIO = ExtractData('oct', dataDoc, yr=year).yr_extract()
    SPEIN = ExtractData('nov', dataDoc, yr=year).yr_extract()
    SPEIDE = ExtractData('dec', dataDoc, yr=year).yr_extract()

    # === prediction === #

    list = [SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO]

    # spei_index = ''

    for i, spei in enumerate(list):
        if spei > -0.5:
          list[i] = 'no drought'
        elif -0.5 >= spei > -1:
          list[i] = 'mild drought'
        elif -1 >= spei > -1.5:
          list[i] = 'moderate drought'
        elif -1.5 >= spei > -2:
          list[i] = 'severe drought'
        elif spei < -2:
          list[i] = 'extreme drought'
        else:
          list[i] = 'invalid parameter'

    return list[0], list[1], list[2], list[3], list[4], list[5], list[6]
