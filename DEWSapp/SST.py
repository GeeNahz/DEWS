from .extract import ExtractData
from .generateData import function_sst


def sst_calcs(month, doc, year):

    mean_Jan_c = ExtractData(month, doc, value='mean')
    mean_Jan = mean_Jan_c.value_extract()

    mean_Dec_c = ExtractData('dec', doc, value='mean')
    mean_Dec = mean_Dec_c.value_extract()

    b_Dec_c = ExtractData('dec', doc, 'b')
    b_Dec = b_Dec_c.value_extract()

    SSTD_c = ExtractData('dec', 'DATAsst', yr=year-1)
    SSTD = SSTD_c.yr_extract()

    rv_Jan_c = ExtractData(month, 'DATArvSST-1', yr=year)
    rv_Jan = rv_Jan_c.yr_extract()
    # rv_Jan = 1.150832691
    # ====== NOTE: set a value for rv before attempting to predict

    s_Jan_c = ExtractData(month, doc, value='s')
    s_Jan = s_Jan_c.value_extract()

    r_Dec_c = ExtractData('dec', doc, value='r')
    r_Dec = r_Dec_c.value_extract()

    SSTJ = mean_Jan+b_Dec*(SSTD-mean_Dec)+rv_Jan*s_Jan*((1-(r_Dec)**2)**0.5)

    SSTD = SSTD
    SSTJ = round(SSTJ, 2)

    ExtractData('jan', 'DATAsst', yr=year).save_value(SSTJ)

    SSTF = ExtractData('feb', 'DATAsst', yr=year).yr_extract()
    if SSTF == None:
        function_sst(year=year)
        SSTF = ExtractData('feb', 'DATAsst', yr=year).yr_extract()
    else:
        pass


    # ===== SST temperature section ===== #
    """Data: SST"""
    MSSTD = 28.1
    MSSTJ = 28.1
    MSSTF = 28.4
    MSSTDJF = 28.2

    AVSST = (SSTD + SSTJ + SSTF)/3

    if (AVSST - MSSTDJF) < -0.4:
        oceanT = 'Very Cold'
    elif -0.4 <= (AVSST - MSSTDJF) < -0.2:
        oceanT = 'Cold'
    elif -0.2 <= (AVSST - MSSTDJF) < 0.2:
        oceanT = 'Average'
    elif 0.2 <= (AVSST - MSSTDJF) < 0.4:
        oceanT = 'Warm'
    elif (AVSST - MSSTDJF) > 0.4:
        oceanT = 'Very Warm'

    # print("Sea Surface Temperature: ", SSTJ)
    # print("Ocean Temperature: ", oceanT)

    return oceanT.upper()
