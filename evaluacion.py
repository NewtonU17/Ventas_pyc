#['tyc', 'gaia', 'hyg', 'hip', 'hd', 'hr', 'gl', 'flam', 'ra','dec',  'mag', 'ci', 'rv', "con"]
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn._loss._loss import CyHuberLoss
import pickle

def preparacion(values):
    #con = np.array(values[13])
    columns = ['año', 'mes', 'dia', 'precio', 'pesos', 'precipitación',
       'TRM', 'IPC campo', 'DISTRIBUIDORA SURTIVEL S.A.S', 'RENDON LUZ AIDE',
       'AGROBOLIVAR SG SAS', 'LA CASA DEL AGRO MCU SAS', 'AGROTIENDA TONE SAS',
       'ZULUAGA VELASQUEZ LUIS EDUARDO', 'COOPERATIVA AGROMULTIACTIVA SAN BAR',
       'CASTAÑEDA SANCHEZ GLORIA PATRICIA', 'VALLEJO TOBON JULIO CESAR',
       'BODEGA CAMPESINA SAS', 'AGROEQUIPOS EL SEMBRADOR SAS ZOMAC',
       'REGIONAGRO SAS', 'ALMACENES AGROSUROESTE S.A.S', 'general',
       'ZULUAGA HOYOS GERARDO DE JESUS', 'RODRIGUEZ GONZALEZ LUIS ALBERTO',
       'AGROPECUARIA LUIS E RENDON B Y CIA', 'CANO DUQUE WILMAR HERNAN',
       'AGROINSUMOS CON LOS MEJORES PRECIOS', 'YEPES BETANCURT RUBEN DARIO',
       'PIEDRAHITA BEDOYA YOAN FELIPE', 'RUA MESA JHON JAIRO',
       'DISTRIBUCIONES MUNDO AGRO ANTIOQUIA', 'ALMACEN AGRICOLA CAMPESINO SAS',
       'ASO GANADEROS DEL ALTIPLANO NORTE D', 'ALMACENES CONSTRUAGRO SAS',
       'RENDON FRANCISCO JAVIER', 'FED COLOMBIANA DE PRODUCTORES DE PA',
       'AGROSANDER DON JORGE S.A.S', 'GIRALDO ARBELAEZ JOSE RAMON',
       'AGROBOLIVAR FLOWERS SAS', 'P. RC NORTE LEJANO', 'P. RC AGRICOLA V.A',
       'P. RC CÓRDOBA', 'RTC VALLE DE ABURRA', 'P. RC AGR.NORTE',
       'RTC ORIENTE A', 'RTC SUR', 'P. RC AGR.ORIEN.A', 'RTC CORDOBA',
       'P. RC AGR.ORIEN B', 'RTC URABA', 'RTC ORIENTE B', 'RTC NORTE',
       'P. RC AGRICOLA B.CAU', 'P. RC URABA', 'P. RC AGR. SUROESTE',
       'P. AGRICOLA ITAGUI', 'P. AGRICOLA STA ROSA', 'AGROQUIMICOS ESTRUCT',
       'FERTILIZANTES ESTRUC', 'CORRECTIVOS ESTRUCTU', 'ALTRIA', 'ECOFERTIL',
       'INTEROC', 'JARDINES SIERRA', 'KIMITEC', 'NUTRIMON', 'PRECISAGRO',
       'PROBELTE', 'STOLLER COLOMBIA', 'SUPERFERTILIZANTES',
       '10-20-30-1-1 BULTO X 50 KGS', '13-26-6 BULTO X 50 KGS',
       '15-15-15 BULTO X 50 KGS', '31-8-8-2-3 (POTREROS) BULTO X 50 KGS',
       'ARPON BOTELLA X 1 LTR', 'BURIL BOL  X 100 GR',
       'CITROEMULSION ENVASE X 1 LTS',
       'FOSFATO DIAMONICO (DAP) BULTO X 50 KGS', 'GRUYA BOTELLA X 1 LTR',
       'IMPERIUS BOTELLA X 1 LTR', 'NOVAPLANT CA-B-ZN X LITRO',
       'PREDOSTAR BOL X 300 GR - GLY', 'PRODUCCION 17-6-18-2 BTO X 50 KG',
       'SUPERPRODUCCION 25-4-24 BTO X 50 KG', 'UREA GRANULADA X 50 KILOS',
       'otro']
    """
    constelations = np.array(['And', 'Ant', 'Aps', 'Aql', 'Aqr', 'Ara', 'Ari', 'Aur', 'Boo', 'CMa',
       'CMi', 'CVn', 'Cae', 'Cam', 'Cap', 'Car', 'Cas', 'Cen', 'Cep', 'Cet',
       'Cha', 'Cir', 'Cnc', 'Col', 'Com', 'CrA', 'CrB', 'Crt', 'Cru', 'Crv',
       'Cyg', 'Del', 'Dor', 'Dra', 'Equ', 'Eri', 'For', 'Gem', 'Gru', 'Her',
       'Hor', 'Hya', 'Hyi', 'Ind', 'LMi', 'Lac', 'Leo', 'Lep', 'Lib', 'Lup',
       'Lyn', 'Lyr', 'Men', 'Mic', 'Mon', 'Mus', 'Nor', 'Oct', 'Oph', 'Ori',
       'Pav', 'Peg', 'Per', 'Phe', 'Pic', 'PsA', 'Psc', 'Pup', 'Pyx', 'Ret',
       'Scl', 'Sco', 'Sct', 'Ser', 'Sex', 'Sge', 'Sgr', 'Tau', 'Tel', 'TrA',
       'Tri', 'Tuc', 'UMa', 'UMi', 'Vel', 'Vir', 'Vol', 'Vul'])
    col = np.where(constelations == con)
    columns = np.concatenate((columns,constelations))
    cons_values = np.array([0 for _ in range(len(constelations))])
   
    cons_values[col] = 1
    values  = np.delete(values,13)
    values = np.concatenate((values,cons_values))
    """
  
    values = [values]
    x_data = pd.DataFrame(columns=columns, data=values)
    return(x_data)
#values = [True,True,False,True,True,False,False,False,1.5,50,2,1.4,10,"Sex"]
#x_data = preparacion(values)

def prediccion(x_data):
    with open("modelo_pyc.pk", 'rb') as f:
        modelo_escogido = pickle.load(f,fix_imports=True)
    dist = modelo_escogido.predict(x_data)
    return(dist)
#print(prediccion(x_data))
