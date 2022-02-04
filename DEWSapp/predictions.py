from .SST import sst_calcs
from .ITCZ10 import itcz10_calcs
from .Main import main_section
from .generateData import function_itcz, function_sst

# from .extract import ExtractData
# from .generateData import auto_populate

# from .ITCZ5 import ExtractDataITCZ5

def predict(month, year):

    # auto_populate('DATAitcz10', 'jan', 1988)
    # function_sst(2021)
    # function_itcz(2021)

    # ===== SST ===== #
    oceanTemp = sst_calcs(month, 'PARAsst', year)

    # ===== ITCZ5 ===== #

    # ===== ITCZ10 ===== #

    """what to do next:
    before doing the calculations, check whether the required data for the selected year is available. If it isn't, which is most cases this will be the case, try to automatically generate for data for the previous years up till that selected year. Save this to the excel sheet for future purposes.

    Then if it has already been generated, i.e. it is available, then it should just be fetched and used as is.

    Work on the DATArvitcz10 sheet, those dates are all messed up. Organize it so that the year is on the x-axis and the month is on the y-axis. That should make working with it a whole lot easier.

    Look for this section in ITCZ10 module and do what it says
    """


    itcz10p, nash, litcz10, sumpos10, sumneg10, itczratio, neg10max, pos10max = itcz10_calcs(month, 'PARAitcz10', year)

    drought_index = main_section(oceanTemp, itcz10p, nash, litcz10, sumpos10, sumneg10, itczratio, neg10max, pos10max)

    print(drought_index)

    # return drought_index
