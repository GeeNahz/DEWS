from .SST import sst_calcs
from .ITCZ10 import itcz10_calcs
from .SPEI import spei_calcs
from .Main import main_section
from .generateData import function_itcz, function_sst

from .extract import ExtractData
# from .generateData import auto_populate

# from .ITCZ5 import ExtractDataITCZ5

def predict(state, year):
    # ===== SST ===== #
    oceanTemp = sst_calcs("jan", 'PARAsst', year)

    # ===== ITCZ10 ===== #
    itcz10p, nash, litcz10, sumpos10, sumneg10, itczratio, neg10max, pos10max = itcz10_calcs("jan", 'PARAitcz10', year)

    drought_index = main_section(oceanTemp, itcz10p, nash, litcz10, sumpos10, sumneg10, itczratio, neg10max, pos10max, state)

    return drought_index, oceanTemp, itcz10p


def spei_predict(lga, year):
    region, synoptic_number = ExtractData('dec', 'DEWS_Stations filledNEW').region_synoptic(lga)

    doc = f'PARAsynoptic{synoptic_number}'
    dataDoc = f'DATAspeiSynoptic{synoptic_number}'
    rvDoc = f'DATArvSynoptic{synoptic_number}'

    # spei_index = spei_calcs(month, dataDoc, doc, year, rvDoc)
    SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO = spei_calcs('dec', dataDoc, doc, year, rvDoc)

    print("SPEIA:", SPEIA)
    print("SPEIO:", SPEIO)

    # return spei_index, region
    return SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO, region
