import math


def brokerage(bp, sp, qty, typ):

        brokerage_factor = {'intra' : 1, 'delivery' : 0, 'futures' : 1, 'options' : 0}
        brokerage_const = {'intra' : 0, 'delivery' : 0, 'futures' : 0, 'options' : 40}
        
        stt_factor = {'intra' : 0.00025, 'delivery' : 0.001, 'futures' : 0.0001, 'options' : 0.0005}

        exc_factor = {'intra' :  0.0000345, 'delivery' : 0.0000345, 'futures' : 0.00002, 'options' : 0.00053}

        stamp_factor = {'intra' :  0.00003, 'delivery' : 0.00015, 'futures' : 0.00002, 'options' : 0.00003}



        brokerage = round(min((bp * qty * 0.0003),20) + min((sp * qty * 0.0003),20) , 2) * brokerage_factor[typ] + brokerage_const[typ]

        turnover = round((bp + sp)*qty, 2)

        stt_total = int(round(((typ == 'delivery') * bp + sp) * qty * stt_factor[typ], 2))

        exc_trans_charge = round(exc_factor[typ] * turnover, 2) 

        cc = 15.93 if typ == 'delivery' else 0

        stax = round(0.18 * (brokerage + exc_trans_charge), 2)

        sebi_charges = round(turnover*0.000001, 2)

        sebi_charges = round(sebi_charges + (sebi_charges * 0.18), 2)

        stamp_charges = int(round((bp*qty)*stamp_factor[typ],0))

        total_tax = round(brokerage + stt_total + exc_trans_charge + cc + stax + sebi_charges + stamp_charges, 2)

        breakeven = round(total_tax / qty, 2) if not math.isnan(total_tax / qty) else 0

        net_profit = round(((sp - bp) * qty) - total_tax, 2)

        print("Turnover:", turnover)
        print("Brokerage:", brokerage)
        print("STT:", stt_total)
        print("Exc Trans Charge:", exc_trans_charge)
        print('DP:' if typ == 'delivery' else 'CC:', cc)
        print("ST:", stax)
        print("SEBI Charges:", sebi_charges)
        print("Stamp Duty:", stamp_charges)
        print("Total Tax:", total_tax)
        print("Breakeven:", breakeven)
        print("Net Profit:", net_profit)


print(brokerage(100,110,400, 'intra'))
print(brokerage(100,110,400, 'delivery'))
print(brokerage(100,110,400, 'futures'))
print(brokerage(100,110,400, 'options'))
