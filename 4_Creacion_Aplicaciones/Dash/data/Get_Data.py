'''
    Metodo para importar datos de la energia eléctrica.

    Fuente: https://pypi.org/project/OMIEData/

    Nota: Dado que recoger los datos de la web lleva un tiempo excesivo, se ha
            guardado cada uno de los DataFrame para trabajar posteriormente con
            ellos.
'''

import datetime as dt

# Precios y demanda horaria de la electricidad
from OMIEData.DataImport.omie_marginalprice_importer import OMIEMarginalPriceFileImporter

dateInit = dt.datetime(2020,1,1)
dateFin = dt.datetime(2022,3,30)

df = OMIEMarginalPriceFileImporter(date_ini=dateInit,
                                   date_end=dateFin).read_to_dataframe(verbose=True)
df.sort_values(by='DATE', axis=0, inplace=True)
df.to_csv('MarginalPrice.csv',index = False)

# Importar datos de la oferta y demanda de la electricidad
from OMIEData.DataImport.omie_supply_demand_curve_importer import OMIESupplyDemandCurvesImporter

dateInit = dt.datetime(2020,1,1)
dateFin = dt.datetime(2022,3,30)
hour=1

df = OMIESupplyDemandCurvesImporter(date_ini=dateInit,
                                    date_end=dateFin,
                                    hour=hour).read_to_dataframe(verbose=True)
df.sort_values(by=['DATE', 'HOUR'], axis=0, inplace=True)
df.to_csv('Oferta-Demanda.csv',index = False)

# Mercado diario de subasta y cierre por tecnologia
from OMIEData.Enums.all_enums import SystemType
from OMIEData.DataImport.omie_energy_by_technology_importer import OMIEEnergyByTechnologyImporter

dateIni = dt.datetime(2022, 1, 1)
dateEnd = dt.datetime(2022, 3, 30)
system_type = SystemType.SPAIN

df = OMIEEnergyByTechnologyImporter(date_ini=dateIni,
                                    date_end=dateEnd,
                                    system_type=system_type).read_to_dataframe(verbose=True)
df.sort_values(by=['DATE', 'HOUR'], axis=0, inplace=True)
df.to_csv('Subasta y cierres por tecnologia.csv',index = False)