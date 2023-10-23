# will be able to receive some parameters that will be used for the computations
def main_section(oceanT, itcz10p, nash, litcz10, sumpos10, sumneg10, itczratio, neg10max, pos10max, state):


    # for sahel:
    if state == 'KASTINA' or 'YOBE' or 'BORNO':
        if (oceanT == 'AVERAGE')  and (itcz10p == 'MODERATE SOUTH' or itcz10p == 'EXTREME SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'NORMAL' and nash >= 0.85):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'NORMAL' and nash < 0.85):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'COLD' and itcz10p == 'NORMAL' or itcz10p == 'EXTREME SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME NORTH' and nash >= 0.85):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME NORTH' and nash < 0.85):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM') and (itcz10p == 'EXTREME SOUTH') and (nash >= 0.85) and (litcz10 == 12) and (3 <= sumpos10 < 4):
            drought_index = 'SEVERE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and litcz10 == 12 and sumpos10 >= 4):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and litcz10 != 12):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'WARM' and itcz10p == 'EXTREME SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index


    # for sudan:
    elif state == 'KEBBI' or 'SOKOTO' or 'ZAMFARA' or 'KANO' or 'JIGAWA':
        if (oceanT == 'AVERAGE' and itcz10p == 'MODERATE SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'EXTREME SOUTH' and litcz10 == 12):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'EXTREME SOUTH' and litcz10 != 12):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE') and (itcz10p == 'NORMAL') and (litcz10 != 12):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'NORMAL' and litcz10 == 12 and sumneg10 < 1):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'NORMAL' and litcz10 == 12 and nash < 0.7):
            drought_index = 'SEVERE DROUGHT'
            return drought_index

        elif (oceanT == 'COLD' and itcz10p == 'EXTREME SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'COLD' and itcz10p == 'NORMAL'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'SEVERE SOUTH' and itczratio < 1):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'SEVERE SOUTH' and itczratio > 1):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'NORMAL'):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'MODERATE SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME NORTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and sumneg10 > 5.3 and sumpos10 <4):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and sumneg10 < 5.3 and sumpos10 > 4):
            drought_index = 'SEVERE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash < 0.85 and neg10max > 7):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash <= 0.8 and neg10max < 7):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'WARM' and itcz10p == 'EXTREME SOUTH' and itczratio > 1):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'WARM' and itcz10p == 'EXTREME SOUTH' and itczratio < 1 and litcz10 == 12):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'WARM' and itcz10p == 'EXTREME SOUTH' and itczratio < 1 and litcz10 != 12):
            drought_index = 'MODERATE DROUGHT'
            return drought_index


    # for northern guinea
    elif state == 'PLATEAU' or 'KADUNA' or 'GOMBE' or 'BAUCHI':
        if (oceanT == 'AVERAGE' and itcz10p == 'MODERATE SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'EXTREME SOUTH' and litcz10 == 12):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'EXTREME SOUTH' and litcz10 != 12):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'NORMAL' and nash < 0.85):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'NORMAL' and nash >= 0.85):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'COLD') and (itcz10p == 'NORMAL' or itcz10p == 'EXTREME SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'WARM' and itcz10p == 'EXTREME SOUTH' and nash < 0.85):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME NORTH' and nash >= 0.85):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME NORTH' and nash < 0.85):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'SEVERE SOUTH' and itczratio < 0.7):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'SEVERE SOUTH' and itczratio > 0.7):
            drought_index = 'SEVERE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'NORMAL' and sumneg10 < 0.6):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'NORMAL' and sumneg10 > 0.6 and itczratio < 10):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'NORMAL' and sumneg10 > 0.6 and itczratio > 10):
            drought_index = 'MODERATE DROUGHTC'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'MODERATE SOUTH' and pos10max > 1 and itczratio > 1):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'MODERATE SOUTH' and pos10max < 1 and itczratio < 0):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash < 0.85):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and (0.75 <= nash < 0.85) and sumneg10 < 14):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and (0.75 <= nash <0.85) and sumneg10 > 14):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and litcz10 == 12 and neg10max > 5):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and litcz10 == 12 and neg10max < 3.8):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and litcz10 == 12 and (3.8 < neg10max < 5)):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash > 0.85 and sumneg10 > 13):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and sumneg10 < 13):
            drought_index = 'NO DROUGHT'
            return drought_index


    # for southern guinea
    elif state == 'NASSARAWA' or 'KWARA' or 'NIGER' or 'TARABA' or 'BENUE' or 'FCT' or 'KOGI':
        if (oceanT == 'AVERAGE' and itcz10p == 'MODERATE SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'EXTREME SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'NORMAL' and nash >= 0.85):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'AVERAGE' and itcz10p == 'NORMAL' and nash < 0.85):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif oceanT == 'COLD' and (itcz10p == 'NORMAL' or itcz10p == 'EXTREME SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'NORMAL' and itczratio > 10):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'NORMAL' and itczratio < 10):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'MODERATE SOUTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'SEVERE SOUTH' and itczratio > 1):
            drought_index = 'MILD DROUGHT'

        elif oceanT == 'VERY WARM' and itcz10p == 'SEVERE SOUTH' and itczratio < 1:
            drought_index = 'SEVERE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME NORTH'):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash < 0.3):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash < 0.85 and litcz10 == 3 and neg10max >= 8.5):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash < 0.85 and litcz10 == 3 and neg10max < 8.5 and itczratio > 2):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash < 0.85 and litcz10 == 3 and neg10max < 8.5 and itczratio < 2):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash > 0.85 and litcz10 == 12 and neg10max > 5):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash > 0.85 and litcz10 == 12 and neg10max < 5):
            drought_index = 'MODERATE DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and litcz10 == 2 and neg10max < 3.5 and sumneg10 > 13):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and litcz10 == 2 and neg10max > 3.5):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash >= 0.85 and litcz10 == 1):
            drought_index = 'NO DROUGHT'
            return drought_index

        elif (oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash < 0.6):
            drought_index = 'MILD DROUGHT'
            return drought_index

        elif(oceanT == 'VERY WARM' and itcz10p == 'EXTREME SOUTH' and nash > 0.6):
            drought_index = 'NO DROUGHT'
            return drought_index
