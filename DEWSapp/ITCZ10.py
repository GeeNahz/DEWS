from .extract import ExtractData
from .generateData import function_itcz

def itcz10_calcs(month, doc, year):


    mean_Jan_c = ExtractData(month, doc, value='mean')
    mean_Jan = mean_Jan_c.value_extract()

    mean_Dec_c = ExtractData('dec', doc, value='mean')
    mean_Dec = mean_Dec_c.value_extract()

    b_Dec_c = ExtractData(month, doc, 'b')
    b_Dec = b_Dec_c.value_extract()

    ITCZ10D_C = ExtractData('dec', 'DATAitcz10', yr=year-1)
    ITCZ10D = ITCZ10D_C.yr_extract()

    rv_Jan_c = ExtractData(month, 'DATArvITCZ10-1', yr=year)
    rv_Jan = rv_Jan_c.yr_extract()

    # rv_Jan = 1.150832691
    # ====== NOTE: set a value for rv before attempting to predict

    s_Jan_c = ExtractData(month, doc, value='s')
    s_Jan = s_Jan_c.value_extract()

    r_Dec_c = ExtractData(month, doc, value='r')
    r_Dec = r_Dec_c.value_extract()

    ITCZ10J = mean_Jan+b_Dec*(ITCZ10D-mean_Dec)+rv_Jan*s_Jan*((1-(r_Dec)**2)**0.5)



    """What to do next:
    Calculate the values for ITCZ for the months of January down to December of the year to be predicted.

    Do this and fill them up in the excel sheet to be saved and used for the next year.

    Try to do this by creating another function within this one. Within this function, create a loop that will run throughout the months, making sure it doesn't exceed December. So while this is true, it should calculate the ITCZ values for the required year and only return the value for January down to April since those are the only ones to be actively used for the prediction.

    All the while this should be saving the values at corresponding fields.
    """

    ITCZ10D = ITCZ10D
    ITCZ10J = round(ITCZ10J, 2)
    ExtractData('jan', 'DATAitcz10', yr=year).save_value(ITCZ10J)

    ITCZ10F = ExtractData('feb', 'DATAitcz10', yr=year).yr_extract()

    if ITCZ10F == None:
        function_itcz(year=year)
        ITCZ10F = ExtractData('feb', 'DATAitcz10', yr=year).yr_extract()
        print('feb:',ITCZ10F)
    else:
        pass

    ITCZ10M = ExtractData('march', 'DATAitcz10', yr=year).yr_extract()
    ITCZ10A = ExtractData('april', 'DATAitcz10', yr=year).yr_extract()

    # ===== ITCS10 determinants section ===== #
    """Data: ITCZ10"""
    MITCZ10D = 5.8
    MITCZ10J = 6.1
    MITCZ10F = 4.8
    MITCZ10M = 7.2
    MITCZ10A = 10.8

    ITCZ10DEM = 21.6

    MMITCZ10 = 4.8

    AVITCZ10 = 6.9

    MINITCZ10 = min(ITCZ10D, ITCZ10J, ITCZ10F, ITCZ10M, ITCZ10A)

    # Which month does minimum itcz10 occurs:
    if ITCZ10D == MINITCZ10:
        LITCZ10 = 12
    if ITCZ10J == MINITCZ10:
        LITCZ10 = 1
    if ITCZ10F == MINITCZ10:
        LITCZ10 = 2
    if ITCZ10M == MINITCZ10:
        LITCZ10 = 3
    if ITCZ10A == MINITCZ10:
        LITCZ10 = 4

    # Which direction is the climate:
    if MINITCZ10 - MMITCZ10 < -1.5:
        ITCZ10P = 'EXTREME SOUTH'
    elif -1.5 <= MINITCZ10 - MMITCZ10 < -1.0:
        ITCZ10P = "SEVERE SOUTH"
    elif -1.0 <= MINITCZ10 - MMITCZ10 < -0.5:
        ITCZ10P = 'MODERATE SOUTH'
    elif -0.5 <= MINITCZ10 - MMITCZ10 < 0.5:
        ITCZ10P = 'NORMAL'
    elif 0.5 <= MINITCZ10 - MMITCZ10 < 1.0:
        ITCZ10P = 'MODERATE NORTH'
    elif 1.0 <= MINITCZ10 - MMITCZ10 < 1.5:
        ITCZ10P = 'SEVERE NORTH'
    elif MINITCZ10 - MMITCZ10 > 1.5:
        ITCZ10P = 'EXTREME NORTH'

    """
    Compute NASH and deviations of itcz10 to one decimal place:  NASH, NEG10MAX, POS10MAX, SUMPOS10, SUMNEG10, ITCZRATIO
    """

    NASH = 1-((ITCZ10D-MITCZ10D)**2+(ITCZ10J-MITCZ10J)**2+(ITCZ10F-MITCZ10F)**2+(ITCZ10M-MITCZ10M)**2+(ITCZ10A-MITCZ10A)**2)/(ITCZ10DEM)**2

    NEG10D = 0
    NEG10J = 0
    NEG10F = 0
    NEG10M = 0
    NEG10A = 0

    POS10D = 0
    POS10J = 0
    POS10F = 0
    POS10M = 0
    POS10A = 0

    if ITCZ10D < MITCZ10D:
        NEG10D = MITCZ10D-ITCZ10D
    else:
        POS10D = ITCZ10D-MITCZ10D

    if ITCZ10J < MITCZ10J:
        NEG10J = MITCZ10J - ITCZ10J
    else:
        POS10J = ITCZ10J - MITCZ10J

    if ITCZ10F < MITCZ10F:
        NEG10F = MITCZ10F - ITCZ10F
    else:
        POS10F = ITCZ10F - MITCZ10F

    if ITCZ10M < MITCZ10M:
        NEG10M = MITCZ10M - ITCZ10M
    else:
        POS10M = ITCZ10M - MITCZ10M

    if ITCZ10A < MITCZ10A:
        NEG10A = MITCZ10A - ITCZ10A
    else:
        POS10A = ITCZ10A - MITCZ10A

    NEG10MAX = max(NEG10D, NEG10J, NEG10F, NEG10M, NEG10A)
    POS10MAX = max(POS10D, POS10J, POS10F, POS10M, POS10A)

    SUMNEG10 = NEG10D + NEG10J + NEG10F + NEG10M + NEG10A

    SUMPOS10 = POS10D + POS10J + POS10F + POS10M + POS10A

    ITCZRATIO = SUMPOS10 / SUMNEG10

    # print('ITCZRATIO: ', ITCZRATIO)
    # print('ITCZ10P: ', ITCZ10P)

    return ITCZ10P, NASH, LITCZ10, SUMPOS10, SUMNEG10, ITCZRATIO, NEG10MAX, POS10MAX
