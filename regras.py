# -*- coding: utf-8 -*-
"""
    Identificacao: Alerta de risco de incendio
    Autor: Ronie Jovanhol
    Utilidades: Dado os preditores de entrada, Esse algoritmo fornece um
                percentual de risco de incendio por meio de um conjunto 
                de regras gerados por uma arvore de decisao.
"""
if __name__ == '__main__':
    while True:
        print 'Informa a Densidade Demografica: '
        dens_demo = float(raw_input('> '))
        print 'Informa a Renda: '
        renda = float(raw_input('> '))
        print 'Informa o SLOPE: '
        SLOPE = float(raw_input('> '))
        print 'Informa a Precipitacao: '
        prec = float(raw_input('> '))
        print 'Informa o VCF: '
        VCF = float(raw_input('> '))
        print 'Escolha um Uso da Terra:'
        print '1 - AGRICULTURA'
        print '2 - ÁREAS URBANAS'
        print '3 - CURSO D’ÁGUA'
        print '4 - FLORESTA NATURAL'
        print '5 - MANGUEZAIS'
        print '6 - PASTAGEM'
        print '7 - SILVICULTURA'
        print '8 - SOLO EXPOSTO'
        print '9 - ÁREAS ALAGADAS'
        print '10 - RESTINGA'
        uso_terra = int(raw_input('> '))
        print 'Informa o DEM: '
        DEM = float(raw_input('> '))
        print 'Informa a Temperatura: '
        temp = float(raw_input('> '))
        if not dens_demo or not renda or not SLOPE or not prec or not VCF or not uso_terra or not DEM or not temp:
            break
        #Rules for terminal node 1
        if dens_demo <= 3.63463 and uso_terra <= 8 and prec <= 1034.39551 and renda <= 556.09497:
            print "terminalNode = -1 \nmean = 0.0835317"
        #Rules for terminal node 2
        if dens_demo <= 3.63463 and uso_terra <= 8 and prec > 1034.39551 and prec <= 1090.74597 and renda <= 556.09497:
            print "terminalNode = -2 \nmean = 0.330305"
        #Rules for terminal node 3
        if dens_demo <= 3.63463 and uso_terra <= 8 and prec > 1090.74597 and prec <= 1109.07446 and renda <= 556.09497:
            print "terminalNode = -3 \nmean = 0.18456"
        #Rules for terminal node 4
        if dens_demo <= 3.63463 and uso_terra <= 8 and prec <= 1109.07446 and renda > 556.09497 and renda <= 841.71002:
            print "terminalNode = -4 \nmean = 0.110923"
        #Rules for terminal node 5
        if dens_demo <= 3.63463 and uso_terra <= 8 and prec <= 1109.07446 and renda > 841.71002 and renda <= 864.86499:
            print "terminalNode = -5 \nmean = 0.434419"
        #Rules for terminal node 6
        if dens_demo <= 3.63463 and uso_terra <= 8 and prec <= 1109.07446 and renda > 864.86499:
            print "terminalNode = -6 \nmean = 0.175612"
        #Rules for terminal node 7
        if dens_demo <= 3.26368 and uso_terra <= 8 and prec > 1109.07446 and VCF <= 54.5:
            print "terminalNode = -7 \nmean = 0.109868"
        #Rules for terminal node 8
        if dens_demo <= 3.26368 and uso_terra <= 8 and prec > 1109.07446 and VCF > 54.5 and DEM <= 44.50000 and temp <= 24.79185:
            print "terminalNode = -8 \n mean = 0.0168376"
        #Rules for terminal node 9
        if dens_demo <= 3.26368 and uso_terra <= 8 and prec > 1109.07446 and VCF > 54.5 and DEM <= 44.50000 and temp > 24.79185:
            print "terminalNode = -9 \nmean = 0.131192"
        #Rules for terminal node 10
        if dens_demo <= 3.26368 and uso_terra <= 8 and prec > 1109.07446 and VCF > 54.5 and DEM > 44.50000:
            print "terminalNode = -10 \nmean = 0.0499697"
        #Rules for terminal node 11
        if dens_demo > 3.26368 and dens_demo <= 3.63463 and uso_terra <= 8 and prec > 1109.07446:
            print "terminalNode = -11 \nmean = 0.139411"
        #Rules for terminal node 12
        if dens_demo <= 3.63463 and uso_terra > 8 and prec <= 1350.50757 and renda <= 859.72498 and temp <= 24.75305:
            print "terminalNode = -12 \nmean = 0.0372407"
        #Rules for terminal node 13
        if dens_demo <= 3.63463 and uso_terra > 8 and prec <= 1350.50757 and renda <= 859.72498 and temp > 24.75305:
            print "terminalNode = -13 \nmean = 0.150805"
        #Rules for terminal node 14
        if dens_demo <= 3.63463 and uso_terra > 8 and prec <= 1350.50757 and renda > 859.72498:
            print "terminalNode = -14 \nmean = 0.250526"
        #Rules for terminal node 15
        if dens_demo <= 3.63463 and uso_terra > 8 and prec > 1350.50757 and renda <= 684.70502 and temp <= 24.68275:
            print "terminalNode = -15 \nmean = 0.281141"
        #Rules for terminal node 16
        if dens_demo <= 3.63463 and uso_terra > 8 and prec > 1350.50757 and renda > 684.70502 and renda <= 854.57001 and temp <= 24.68275:
            print "terminalNode = -16 \nmean = 0.748276"
        #Rules for terminal node 17
        if dens_demo <= 2.35704 and uso_terra > 8 and prec > 1350.50757 and renda > 854.57001 and temp <= 24.68275:
            print "terminalNode = -17 \nmean = 0.0606344"
        #Rules for terminal node 18
        if dens_demo > 2.35704 and dens_demo <= 3.63463 and uso_terra > 8 and prec > 1350.50757 and renda > 854.57001 and temp <= 24.68275:
            print "terminalNode = -18 \nmean = 0.52072"
        #Rules for terminal node 19
        if dens_demo <= 2.35704 and uso_terra > 8 and prec > 1350.50757 and temp > 24.68275 and temp <= 24.71705:
            print "terminalNode = -19 \nmean = 0.0901171"
        #Rules for terminal node 20
        if dens_demo <= 2.35704 and uso_terra > 8 and prec > 1350.50757 and temp > 24.71705:
            print "terminalNode = -20 \nmean = 0.338749"
        #Rules for terminal node 21
        if dens_demo > 2.35704 and dens_demo <= 2.50642 and uso_terra > 8 and prec > 1350.50757 and temp > 24.68275:
            print "terminalNode = -21 \nmean = 0.239003"
        #Rules for terminal node 22
        if dens_demo > 2.50642 and dens_demo <= 3.63463 and uso_terra > 8 and prec > 1350.50757 and temp > 24.68275:
            print "terminalNode = -22 \nmean = 0.571113"
        #Rules for terminal node 23
        if dens_demo > 3.63463 and prec <= 1169.50452 and temp <= 25.03165 and DEM <= 55.50000:
            print "terminalNode = -23 \nmean = 0.185039"
        #Rules for terminal node 24
        if dens_demo > 3.63463 and prec <= 1169.50452 and temp > 25.03165 and DEM <= 55.50000:
            print "terminalNode = -24 \nmean = 0.0699455"
        #Rules for terminal node 25
        if dens_demo > 3.63463 and (uso_terra <= 4 or uso_terra == 6 or uso_terra == 8) and prec > 1169.50452 and renda <= 736.80499 and DEM <= 55.50000:
            print "terminalNode = -25 \nmean = 0.0639006"
        #Rules for terminal node 26
        if dens_demo > 3.63463 and (uso_terra == 5 or uso_terra == 7 or uso_terra > 8) and prec > 1169.50452 and prec <= 1371.60449 and renda <= 736.80499 and DEM <= 55.50000:
            print "terminalNode = -26 \nmean = 0.125505"
        #Rules for terminal node 27
        if dens_demo > 3.63463 and dens_demo <= 24.23654 and (uso_terra == 5 or uso_terra == 7 or uso_terra > 8) and prec > 1371.60449 and renda <= 736.80499 and DEM <= 55.50000:
            print "terminalNode = -27 \nmean = 0.0750805"
        #Rules for terminal node 28
        if dens_demo > 24.23654 and (uso_terra == 5 or uso_terra == 7 or uso_terra > 8) and prec > 1371.60449 and renda <= 736.80499 and DEM <= 55.50000:
            print "terminalNode = -28 \nmean = 0.586747"
        #Rules for terminal node 29
        if dens_demo > 3.63463 and prec > 1169.50452 and renda > 736.80499 and DEM <= 55.50000:
            print "terminalNode = -29 \nmean = 0.0473021"
        #Rules for terminal node 30
        if dens_demo > 3.63463 and dens_demo <= 6.08065 and renda <= 506.88501 and DEM > 55.50000:
            print "terminalNode = -30 \nmean = 0.0315917"
        #Rules for terminal node 31
        if dens_demo > 3.63463 and dens_demo <= 4.63185 and renda > 506.88501 and renda <= 624.57501 and DEM > 55.50000:
            print "terminalNode = -31 \nmean = 0.0978987"
        #Rules for terminal node 32
        if dens_demo > 4.63185 and dens_demo <= 6.08065 and renda > 506.88501 and renda <= 624.57501 and DEM > 55.50000:
            print "terminalNode = -32 \nmean = 0.202195"
        #Rules for terminal node 33
        if dens_demo > 3.63463 and dens_demo <= 5.89440 and renda > 624.57501 and DEM > 55.50000:
            print "terminalNode = -33 \nmean = 0.0575384"
        #Rules for terminal node 34
        if dens_demo > 5.89440 and dens_demo <= 6.08065 and renda > 624.57501 and DEM > 55.50000:
            print "terminalNode = -34 \nmean = 0.175359"
        #Rules for terminal node 35
        if dens_demo > 6.08065 and prec <= 1130.84399 and DEM > 55.50000 and SLOPE <= 5.29967:
            print "terminalNode = -35 \nmean = 0.0818293"
        #Rules for terminal node 36
        if dens_demo > 6.08065 and prec <= 1130.84399 and DEM > 55.50000 and SLOPE > 5.29967:
            print "terminalNode = -36 \nmean = 0.0408473"
        #Rules for terminal node 37
        if dens_demo > 6.08065 and prec > 1130.84399 and DEM > 55.50000:
            print "terminalNode = -37 \nmean = 0.0214471"
