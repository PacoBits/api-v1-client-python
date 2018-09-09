
from os.path import dirname, basename, isfile
import glob
from time import time
from time import sleep
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

import util
import json
import blockexplorer
import config
from enum import Enum
#from past.builtins import basestring

sleep(1)

if config.OUTFILE is None:
    config.OUTFILE = open('Explorersmartcash.log', 'w')

tiempo_inicial = time()
BloqueInicio=blockexplorer.get_block(blockexplorer.get_block_hash(str(config.BLOQUEINICIO)))
tiempo_final = time()
BloqueSiguiente=BloqueInicio
blockexplorer.logger("************** DESDE:" + str(BloqueSiguiente.BlockTime ))
while (BloqueSiguiente.Height<(config.HASTABLOQUE)):
    blockexplorer.logger("------------ " + BloqueSiguiente.BlockTime + "------------ " + str(BloqueSiguiente.Height) +"------------ TX:" +str(len(BloqueSiguiente.transactions))  + "------------ " + str(tiempo_final - tiempo_inicial) +" s"  +"------------ BalanceOut:" +str((BloqueSiguiente.totalOut)))
    if (BloqueSiguiente.totalOut>config.VALORMAX) or (BloqueSiguiente.totalIn>config.VALORMAX):
        blockexplorer.logger("*******************************************************************************************************************************************")
        blockexplorer.logger("THISSSSSS")
        blockexplorer.logger("Total IN:" +str(BloqueSiguiente.totalIn))
        blockexplorer.logger("Total OUT:" +str(BloqueSiguiente.totalOut))
        blockexplorer.logger("*******************************************************************************************************************************************")
    tiempo_inicial = time()
    try:
        if BloqueSiguiente.NextBlockHash is not None:
            BloqueSiguiente=blockexplorer.get_block(BloqueSiguiente.NextBlockHash)
        else:
            BloqueSiguiente=blockexplorer.get_block(blockexplorer.get_block_hash(str(BloqueSiguiente.Height+1)))
        #BloqueSiguiente=get_block(get_block_hash(str(BloqueSiguiente.Height+1)))
    except:
        print ("+++++++++++++Fallo al leer el bloque esperamos XX segundos y reintentamos+++++++++++")
        sleep(config.TIMEWAITTORETRY)
        #BloqueSiguiente=get_block(BloqueSiguiente.NextBlockHash)
        BloqueSiguiente=blockexplorer.get_block(blockexplorer.get_block_hash(str(BloqueSiguiente.Height+1)))

    tiempo_final = time()

blockexplorer.logger("************** HASTA:" + str(BloqueSiguiente.BlockTime ))
#log (s.Hash)
#s=get_tx('97181c72a1ed04f7e23669a4abe8ea18a44be8139f8a6a436d261da86559b6a8')
outfile.close()
