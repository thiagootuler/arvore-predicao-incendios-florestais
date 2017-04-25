# -*- coding: utf-8 -*-
"""
    Identificacao: Alerta de risco de incendio
    Autor: Ronie Jovanhol
           Thiago Tuler
    Utilidades: Dado os preditores de entrada, Esse algoritmo fornece um
                percentual de risco de incendio por meio de um conjunto 
                de regras gerados por uma arvore de decisao.
"""
import os

from xlrd import open_workbook
from xlwt import easyxf
from xlutils.copy import copy as copy_workbook

class AlertaIncendio (object):
    #Inicia a variavel relativa ao caminho dos arquivos utilizados
    def __init__(self):
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    #Converte o nome da classe de uso da terra para um coeficiente numérico
    def classificar(self, uso_terra):
        if uso_terra == "Agricultura":
            return 1
        elif uso_terra == "Areas urbanas":
            return 2
        elif uso_terra == "Curso d'agua":
            return 3
        elif uso_terra == "Floresta natural":
            return 4
        elif uso_terra =="Manguezais":
            return 5
        elif uso_terra == "Pastagem":
            return 6
        elif uso_terra == "Silvicultura":
            return 7
        elif uso_terra == "Solo Exposto":
            return 8
        elif uso_terra == "Areas alagadas":
            return 9
        elif uso_terra == "Restinga":
            return 10
    
    #Caminha pela arvore de decisão para localizar o melhor coeficiente de incendio para tais preditores
    def avaliar(self, dens_demo, renda, SLOPE, prec, VCF, uso_terra, DEM, temp):
        #Claee
        uso = AlertaIncendio().classificar(uso_terra)
        #Regra para o nó terminal 1
        if dens_demo <= 3.63463 and uso <= 8 and prec <= 1034.39551 and renda <= 556.09497:
            return 0.0835317
        #Regra para o nó terminal 2
        if dens_demo <= 3.63463 and uso <= 8 and prec > 1034.39551 and prec <= 1090.74597 and renda <= 556.09497:
            return 0.330305
        #Regra para o nó terminal 3
        if dens_demo <= 3.63463 and uso <= 8 and prec > 1090.74597 and prec <= 1109.07446 and renda <= 556.09497:
            return 0.18456
        #Regra para o nó terminal 4
        if dens_demo <= 3.63463 and uso <= 8 and prec <= 1109.07446 and renda > 556.09497 and renda <= 841.71002:
            return 0.110923
        #Regra para o nó terminal 5
        if dens_demo <= 3.63463 and uso <= 8 and prec <= 1109.07446 and renda > 841.71002 and renda <= 864.86499:
            return 0.434419
        #Regra para o nó terminal 6
        if dens_demo <= 3.63463 and uso <= 8 and prec <= 1109.07446 and renda > 864.86499:
            return 0.175612
        #Regra para o nó terminal 7
        if dens_demo <= 3.26368 and uso <= 8 and prec > 1109.07446 and VCF <= 54.5:
            return 0.109868
        #Regra para o nó terminal 8
        if dens_demo <= 3.26368 and uso <= 8 and prec > 1109.07446 and VCF > 54.5 and DEM <= 44.50000 and temp <= 24.79185:
            return 0.0168376
        #Regra para o nó terminal 9
        if dens_demo <= 3.26368 and uso <= 8 and prec > 1109.07446 and VCF > 54.5 and DEM <= 44.50000 and temp > 24.79185:
            return 0.131192
        #Regra para o nó terminal 10
        if dens_demo <= 3.26368 and uso <= 8 and prec > 1109.07446 and VCF > 54.5 and DEM > 44.50000:
            return 0.0499697
        #Regra para o nó terminal 11
        if dens_demo > 3.26368 and dens_demo <= 3.63463 and uso <= 8 and prec > 1109.07446:
            return 0.139411
        #Regra para o nó terminal 12
        if dens_demo <= 3.63463 and uso > 8 and prec <= 1350.50757 and renda <= 859.72498 and temp <= 24.75305:
            return 0.0372407
        #Regra para o nó terminal 13
        if dens_demo <= 3.63463 and uso > 8 and prec <= 1350.50757 and renda <= 859.72498 and temp > 24.75305:
            return 0.150805
        #Regra para o nó terminal 14
        if dens_demo <= 3.63463 and uso > 8 and prec <= 1350.50757 and renda > 859.72498:
            return 0.250526
        #Regra para o nó terminal 15
        if dens_demo <= 3.63463 and uso > 8 and prec > 1350.50757 and renda <= 684.70502 and temp <= 24.68275:
            return 0.281141
        #Regra para o nó terminal 16
        if dens_demo <= 3.63463 and uso > 8 and prec > 1350.50757 and renda > 684.70502 and renda <= 854.57001 and temp <= 24.68275:
            return 0.748276
        #Regra para o nó terminal 17
        if dens_demo <= 2.35704 and uso > 8 and prec > 1350.50757 and renda > 854.57001 and temp <= 24.68275:
            return 0.0606344
        #Regra para o nó terminal 18
        if dens_demo > 2.35704 and dens_demo <= 3.63463 and uso > 8 and prec > 1350.50757 and renda > 854.57001 and temp <= 24.68275:
            return 0.52072
        #Regra para o nó terminal 19
        if dens_demo <= 2.35704 and uso > 8 and prec > 1350.50757 and temp > 24.68275 and temp <= 24.71705:
            return 0.0901171
        #Regra para o nó terminal 20
        if dens_demo <= 2.35704 and uso > 8 and prec > 1350.50757 and temp > 24.71705:
            return 0.338749
        #Regra para o nó terminal 21
        if dens_demo > 2.35704 and dens_demo <= 2.50642 and uso > 8 and prec > 1350.50757 and temp > 24.68275:
            return 0.239003
        #Regra para o nó terminal 22
        if dens_demo > 2.50642 and dens_demo <= 3.63463 and uso > 8 and prec > 1350.50757 and temp > 24.68275:
            return 0.571113
        #Regra para o nó terminal 23
        if dens_demo > 3.63463 and prec <= 1169.50452 and temp <= 25.03165 and DEM <= 55.50000:
            return 0.185039
        #Regra para o nó terminal 24
        if dens_demo > 3.63463 and prec <= 1169.50452 and temp > 25.03165 and DEM <= 55.50000:
            return 0.0699455
        #Regra para o nó terminal 25
        if dens_demo > 3.63463 and (uso <= 4 or uso == 6 or uso == 8) and prec > 1169.50452 and renda <= 736.80499 and DEM <= 55.50000:
            return 0.0639006
        #Regra para o nó terminal 26
        if dens_demo > 3.63463 and (uso == 5 or uso == 7 or uso > 8) and prec > 1169.50452 and prec <= 1371.60449 and renda <= 736.80499 and DEM <= 55.50000:
            return 0.125505
        #Regra para o nó terminal 27
        if dens_demo > 3.63463 and dens_demo <= 24.23654 and (uso == 5 or uso == 7 or uso > 8) and prec > 1371.60449 and renda <= 736.80499 and DEM <= 55.50000:
            return 0.0750805
        #Regra para o nó terminal 28
        if dens_demo > 24.23654 and (uso == 5 or uso == 7 or uso > 8) and prec > 1371.60449 and renda <= 736.80499 and DEM <= 55.50000:
            return 0.586747
        #Regra para o nó terminal 29
        if dens_demo > 3.63463 and prec > 1169.50452 and renda > 736.80499 and DEM <= 55.50000:
            return 0.0473021
        #Regra para o nó terminal 30
        if dens_demo > 3.63463 and dens_demo <= 6.08065 and renda <= 506.88501 and DEM > 55.50000:
            return 0.0315917
        #Regra para o nó terminal 31
        if dens_demo > 3.63463 and dens_demo <= 4.63185 and renda > 506.88501 and renda <= 624.57501 and DEM > 55.50000:
            return 0.0978987
        #Regra para o nó terminal 32
        if dens_demo > 4.63185 and dens_demo <= 6.08065 and renda > 506.88501 and renda <= 624.57501 and DEM > 55.50000:
            return 0.202195
        #Regra para o nó terminal 33
        if dens_demo > 3.63463 and dens_demo <= 5.89440 and renda > 624.57501 and DEM > 55.50000:
            return 0.0575384
        #Regra para o nó terminal 34
        if dens_demo > 5.89440 and dens_demo <= 6.08065 and renda > 624.57501 and DEM > 55.50000:
            return 0.175359
        #Regra para o nó terminal 35
        if dens_demo > 6.08065 and prec <= 1130.84399 and DEM > 55.50000 and SLOPE <= 5.29967:
            return 0.0818293
        #Regra para o nó terminal 36
        if dens_demo > 6.08065 and prec <= 1130.84399 and DEM > 55.50000 and SLOPE > 5.29967:
            return 0.0408473
        #Regra para o nó terminal 37
        if dens_demo > 6.08065 and prec > 1130.84399 and DEM > 55.50000:
            return 0.0214471
    
    #Compara o resultado esperedo com o obtido através do calculo do erro relativo
    def comparar(self, result_esp, result_obt):
        diferenca = (result_esp-result_obt)/result_obt
        if diferenca < -0.2:
            style = easyxf('font: name Calibri, height 220; pattern: pattern solid, fore_colour blue;')
        elif diferenca > +0.2:
            style = easyxf('font: name Calibri, height 220; pattern: pattern solid, fore_colour red;')
        else:
            style = easyxf('font: name Calibri, height 220;')
        return diferenca, style
    
    #Utiliza os dados da tabela pra localizar o coeficiente de incêndio
    def processar(self):
        print "Abrindo o arquivo..."
        readbook = open_workbook(os.path.join(self.__location__, 'dados.xls'), formatting_info=True, on_demand=True)
        workbook = copy_workbook(readbook)
        print "Lendo a planilha..."
        readsheet = readbook.sheet_by_index(0)
        worksheet = workbook.get_sheet(0)
        for row_num in range(readsheet.nrows):
            if row_num != 0:
                row = readsheet.row_values(row_num)
                percentual = AlertaIncendio().avaliar(float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), row[7], float(row[8]), float(row[9]))
                diferenca, style = AlertaIncendio().comparar(float(row[10]), percentual)
                worksheet.write(row_num, 11, percentual, style)
                worksheet.write(row_num, 12, diferenca*100, easyxf(num_format_str='0.00'))
                print 'Calculando {0} de {1}\r'.format(row_num+1, readsheet.nrows),
            else:
                worksheet.write(row_num, 12, u"ERRO RELATIVO", easyxf('font: name Calibri, height 220;'))
        workbook.save(os.path.join(self.__location__, 'dados.xls'))

if __name__ == '__main__':
    AlertaIncendio().processar()
