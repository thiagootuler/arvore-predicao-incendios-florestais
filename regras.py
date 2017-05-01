# -*- coding: utf-8 -*-
"""
    Identificacao: Alerta de risco de incendio
    Autor: Ronie Jovanhol
           Thiago Tuler
    Utilidades: Dado os preditores de entrada, Esse algoritmo fornece um
                percentual de risco de incendio por meio da navegação na 
                arvore CART.
"""
# Make a prediction with a decision tree
def predict(node, row):
	if row[node['index']] <= node['value']:
		if isinstance(node['left'], dict):
			return predict(node['left'], row)
		else:
			return node['left']
	else:
		if isinstance(node['right'], dict):
			return predict(node['right'], row)
		else:
			return node['right']

if __name__ == '__main__':
    dataset = [
        #['dens_demo', 'renda', 'SLOPE', 'prec', 'VCF', 'uso_terra', 'DEM', 'temp']
        [3.63463, 556.09497, 0, 1034.39551, 0, 8, 0, 0, 0.0835317],
        [3.63463, 556.09497, 0, 1090.74597, 0, 8, 0, 0, 0.330305],
        [3.63463, 556.09497, 0, 1090.74598, 0, 8, 0, 0, 0.18456],
        [3.63463, 841.71002, 0, 1109.07446, 0, 8, 0, 0, 0.110923],
        [3.63463, 864.86499, 0, 1109.07446, 0, 8, 0, 0, 0.434419],
        [3.63463, 864.865, 0, 1109.07446, 0, 8, 0, 0, 0.175612],
        [3.26368, 0, 0, 1109.07447, 54.5, 8, 0, 0, 0.109868],
        [3.26368, 0, 0, 1109.07447, 54.6, 8, 44.50000, 24.79185, 0.0168376],
        [3.26368, 0, 0, 1109.07447, 54.6, 8, 44.50000, 24.79186, 0.131192],
        [3.26368, 0, 0, 1109.07447, 54.6, 8, 44.50001, 0, 0.0499697],
        [3.26369, 0, 0, 1109.07447, 0, 8, 0, 0, 0.139411],
        [3.26369, 859.72498, 0, 1350.50757, 0, 9, 0, 24.75305, 0.0372407],
        [3.26369, 859.72498, 0, 1350.50757, 0, 9, 0, 24.75306, 0.150805],
        [3.26369, 859.72499, 0, 1350.50757, 0, 9, 0, 0, 0.250526],
        [3.26369, 684.70502, 0, 1350.50758, 0, 9, 0, 24.68275, 0.281141],
        [3.26369, 684.70503, 0, 1350.50758, 0, 9, 0, 24.68275, 0.748276],
        [2.35704, 859.72499, 0, 1350.50758, 0, 9, 0, 24.68275, 0.0606344],
        [2.35705, 859.72499, 0, 1350.50758, 0, 9, 0, 24.68275, 0.52072],
        [2.35704, 684.70503, 0, 1350.50758, 0, 9, 0, 24.71705, 0.0901171],
        [2.35704, 684.70503, 0, 1350.50758, 0, 9, 0, 24.71706, 0.338749],
        [2.50642, 684.70503, 0, 1350.50758, 0, 9, 0, 24.68276, 0.239003],
        [2.50643, 684.70503, 0, 1350.50758, 0, 9, 0, 24.68276, 0.571113],
        [3.63464, 0, 0, 1169.50452, 0, 0, 55.50000, 25.03165, 0.185039],
        [3.63464, 0, 0, 1169.50452, 0, 0, 55.50000, 25.03166, 0.0699455],
        [3.63464, 736.80499, 0, 1169.50453, 0, 6, 55.50000, 25.03165, 0.0639006],
        [3.63464, 736.80499, 0, 1371.60449, 0, 7, 55.50000, 25.03165, 0.125505],
        [24.23654, 736.80499, 0, 1371.6045, 0, 7, 55.50000, 25.03165, 0.0750805],
        [24.23655, 736.80499, 0, 1371.6045, 0, 7, 55.50000, 25.03165, 0.586747],
        [3.63464, 736.805, 0, 1169.50453, 0, 0, 55.50000, 25.03165, 0.0473021],
        [6.08065, 506.88501, 0, 1169.50453, 0, 0, 55.50001, 0, 0.0315917],
        [4.63185, 506.88502, 0, 1169.50453, 0, 0, 55.50001, 0, 0.0978987],
        [4.63186, 506.88502, 0, 1169.50453, 0, 0, 55.50001, 0, 0.202195],
        [5.8944, 624.57502, 0, 1169.50453, 0, 0, 55.50001, 0, 0.0575384],
        [5.89441, 624.57502, 0, 1169.50453, 0, 0, 55.50001, 0, 0.175359],
        [6.08066, 624.57502, 5.29967, 1130.84399, 0, 0, 55.50001, 0, 0.0818293],
        [6.08066, 624.57502, 5.29968, 1130.84399, 0, 0, 55.50001, 0, 0.0408473],
        [6.08066, 624.57502, 0, 1130.84400, 0, 0, 55.50001, 0, 0.0214471]
    ]

    tree = {
        'index': 0, 
        'right': {
            'index': 6, 
            'right': {
                'index': 0, 
                'right': {
                    'index': 3, 
                    'right': 0.0214471, # terminal node 37
                    'value': 1130.84399, 
                    'left': {
                        'index': 2, 
                        'right': 0.0408473, # terminal node 36
                        'value': 5.29967, 
                        'left': 0.0818293 # terminal node 35
                    }
                }, 
                'value': 6.08065, 
                'left': {
                    'index': 1, 
                    'right': {
                        'index': 0, 
                        'right': 0.175359, # terminal node 34
                        'value': 5.89440, 
                        'left': 0.0575384 # terminal node 33
                    }, 
                    'value': 624.57501, 
                    'left': {
                        'index': 1, 
                        'right': {
                            'index': 0, 
                            'right': 0.202195, # terminal node 32
                            'value': 4.63185, # CONFERIR AQUI <<<<========================================================
                            'left': 0.0978987 # terminal node 31
                        }, 
                        'value': 506.88501, 
                        'left': 0.0315917 # terminal node 30
                    }
                }
            }, 
            'value': 55.50000, 
            'left': {
                'index': 3, 
                'right': {
                    'index': 1, 
                    'right': 0.0473021, # terminal node 29
                    'value': 736.80499, 
                    'left': {
                        'index': 5, 
                        'right': {
                            'index': 3, 
                            'right': {
                                'index': 0, 
                                'right': 0.586747, # terminal node 28
                                'value': 24.23654, 
                                'left': 0.0750805 # terminal node 27
                            }, 
                            'value': 1371.60449, 
                            'left': 0.125505 # terminal node 26
                        }, 
                        'value': 6, 
                        'left': 0.0639006 # terminal node 25
                    }
                }, 
                'value': 1169.50452, 
                'left': {
                    'index': 7, 
                    'right': 0.0699455, # terminal node 24
                    'value': 25.03165, 
                    'left': 0.185039 # terminal node 23
                }
            }
        }, 
        'value': 3.63463, 
        'left': {
            'index': 5, 
            'right': {
                'index': 3, 
                'right': {
                    'index': 7, 
                    'right': {
                        'index': 0, 
                        'right': {
                            'index': 0, 
                            'right': 0.571113, # terminal node 22
                            'value': 2.50642, 
                            'left': 0.239003 # terminal node 21
                        }, 
                        'value': 2.35704, 
                        'left': {
                            'index': 7, 
                            'right': 0.338749, # terminal node 20
                            'value': 24.71705, 
                            'left': 0.0901171 # terminal node 19
                        }
                    }, 
                    'value': 24.68275, 
                    'left': {
                        'index': 1, 
                        'right': {
                            'index': 0, 
                            'right': 0.52072, # terminal node 18
                            'value': 2.35704, 
                            'left': 0.0606344 # terminal node 17
                        }, 
                        'value': 859.72498, 
                        'left': {
                            'index': 1, 
                            'right': 0.748276, # terminal node 16
                            'value': 684.70502, 
                            'left': 0.281141 # terminal node 15
                        }
                    }
                }, 
                'value': 1350.50757, 
                'left': {
                    'index': 1, 
                    'right': 0.250526, # terminal node 14
                    'value': 859.72498, 
                    'left': {
                        'index': 7, 
                        'right': 0.150805, # terminal node 13
                        'value': 24.75305, 
                        'left': 0.0372407 # terminal node 12
                    }
                }
            }, 
            'value': 8, 
            'left': {
                'index': 3, 
                'right': {
                    'index': 0,
                    'right': 0.139411, # terminal node 11
                    'value': 3.26368, 
                    'left': {
                        'index': 4,
                        'right': {
                            'index': 6,
                            'right': 0.0499697, # terminal node 10
                            'value': 44.50000, 
                            'left': {
                                'index': 7,
                                'right': 0.131192, # terminal node 09
                                'value': 24.79185, 
                                'left': 0.0168376 # terminal node 08
                            }
                        },
                        'value': 54.5, 
                        'left': 0.109868 # terminal node 07
                    }
                }, 
                'value': 1109.07446, 
                'left': {
                    'index': 1, 
                    'right': {
                        'index': 1, 
                        'right': {
                            'index': 1, 
                            'right': 0.175612, # terminal node 06
                            'value': 864.86499, 
                            'left': 0.434419 # terminal node 05
                        }, 
                        'value': 841.71002, 
                        'left': 0.110923 # terminal node 04
                    }, 
                    'value': 556.09497, 
                    'left': {
                        'index': 3, 
                        'right': {
                            'index': 3, 
                            'right': 0.18456, # terminal node 03
                            'value': 1090.74597, 
                            'left': 0.330305 # terminal node 02
                        }, 
                        'value': 1034.39551, 
                        'left': 0.0835317 # terminal node 01
                    }
                }
            }
        }
    }
    for index, row in enumerate(dataset):
        prediction = predict(tree, row)
        #if row[-1] != prediction:
        #	print('Rule=%d - Expected=%f, Got=%f' % (index+1, row[-1], prediction))
        print('Rule=%d - Expected=%f, Got=%f' % (index+1, row[-1], prediction))
    '''
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
        print '5 - SOLO EXPOSTO'
        print '6 - PASTAGEM'
        print '7 - SILVICULTURA'
        print '8 - MANGUEZAIS'
        print '9 - ÁREAS ALAGADAS'
        print '10 - RESTINGA'
        uso_terra = int(raw_input('> '))
        print 'Informa o DEM: '
        DEM = float(raw_input('> '))
        print 'Informa a Temperatura: '
        temp = float(raw_input('> '))
        if not dens_demo or not renda or not SLOPE or not prec or not VCF or not uso_terra or not DEM or not temp:
            break
        '''
