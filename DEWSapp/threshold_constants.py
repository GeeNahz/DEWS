# threshold constants

def thresholds(value: int | float):
    if value >= 2.0:
        return 'EXTREMELY WET (EW)'
    elif (1.50 <= value) and (value <= 1.99):
        return 'VERY WET (VW)'
    elif (1.00 <= value) and (value <= 1.49):
        return 'MODERATELY WET (MW)'
    elif (-0.99 <= value) and (value <= 0.99):
        return 'NEAR NORMAL (NN)'
    elif (-1.00 <= value) and (value <= -1.49):
        return 'MODERATELY DRY (MD)'
    elif (-1.50 <= value) and (value <= -1.99):
        return 'SEVERELY DRY (SD)'
    elif (value <= -2.00):
        return 'EXTREMELY DRY (ED)'
