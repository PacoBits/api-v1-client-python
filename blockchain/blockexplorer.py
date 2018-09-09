"""This module corresponds to functionality documented
at https://smart.ccore.online/api/ @PacoBits - Poot Modify for free used in smartcash
"""

from os.path import dirname, basename, isfile
import glob
from time import time
from time import sleep
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

import util
import json
import config
from enum import Enum
#from past.builtins import basestring

def log(cadena):
    if config.DEBUG:
        print(cadena)

def logger(cadena):
    #global config.OUTFILE
    config.OUTFILE.write(cadena +"\n")
    print(cadena)


def get_latest_block(api_code=None):
    """Get the latest block on the main chain.
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`LatestBlock` class
    """

    resource = '/api/getblockcount'
    if api_code is not None:
        resource += '?api_code=' + api_code
    response = util.call_api(resource)
    return response


def get_block_hash(block_id, api_code=None):
    """Get a single block based on a block hash.
    :param str block_id: block hash to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Block` class
    """

    resource = '/api/getblockhash?index=' + block_id
    log (resource)
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    return response



def get_block(block_hash, api_code=None):
    """Get a single block based on a block hash.
    :param str block_id: block hash to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Block` class
    """

    resource ='/api/getblock?hash=' + block_hash
    log (resource)
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return Block(json_response)


def get_tx(tx_id, api_code=None):
    """Get a single transaction based on a transaction hash.
    :param str tx_id: transaction hash to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Transaction` class
    """
    log(tx_id)
    resource = '/api/getrawtransaction?txid=' + tx_id
    if api_code is not None:
        resource += '?api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return Transaction(json_response)

def get_address_smartcash(address):
    global resource
    resource=config.BASE_URL
    log (resource)
    return resource



def get_balance(address, filter=None, api_code=None):
    """Get balances for each address provided.
    :param tuple addresses: addresses(xpub or base58) to look up
    :param FilterType filter: the filter for transactions selection (optional)
    :param str api_code: Blockchain.info API code (optional)
    :return: a dictionary of str, :class:`Balance`
    """

    resource = '/ext/getbalance/' + address
    log (resource)
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    return response



class SimpleBlock:
    def __init__(self, b):
        self.height = b['height']
        self.hash = b['hash']
        self.time = b['time']
        self.main_chain = b['main_chain']


class LatestBlock:
    def __init__(self, b):
        self.hash = b['hash']
        self.time = b['time']
        self.block_index = b['block_index']
        self.height = b['height']
        self.tx_indexes = [i for i in b['txIndexes']]


class UnspentOutput:
    def __init__(self, o):
        self.tx_hash = o['tx_hash']
        self.tx_index = o['tx_index']
        self.tx_output_n = o['tx_output_n']
        self.script = o['script']
        self.value = o['value']
        self.value_hex = o['value_hex']
        self.confirmations = o['confirmations']


class Address:
    def __init__(self, a):
        self.hash160 = a['hash160']
        self.address = a['address']
        self.n_tx = a['n_tx']
        self.total_received = a['total_received']
        self.total_sent = a['total_sent']
        self.final_balance = a['final_balance']
        self.transactions = [Transaction(tx) for tx in a['txs']]


# to represent the address summary in multiaddress
class SimpleAddress:
    def __init__(self, a):
        self.address = a['address']
        self.n_tx = a['n_tx']
        self.total_received = a['total_received']
        self.total_sent = a['total_sent']
        self.final_balance = a['final_balance']
        self.change_index = a['change_index']
        self.account_index = a['account_index']


class MultiAddress:
    def __init__(self, a):
        self.n_tx = a['wallet']['n_tx']
        self.n_tx_filtered = a['wallet']['n_tx_filtered']
        self.total_received = a['wallet']['total_received']
        self.total_sent = a['wallet']['total_sent']
        self.final_balance = a['wallet']['final_balance']
        self.addresses = [SimpleAddress(addr) for addr in a['addresses']]
        self.transactions = [Transaction(tx) for tx in a['txs']]


class Xpub:
    def __init__(self, a):
        xpub = a['addresses'][0]
        self.address = xpub['address']
        self.n_tx = xpub['n_tx']
        self.total_received = xpub['total_received']
        self.total_sent = xpub['total_sent']
        self.final_balance = xpub['final_balance']
        self.change_index = xpub['change_index']
        self.account_index = xpub['account_index']
        self.gap_limit = xpub['gap_limit']
        self.transactions = [Transaction(tx) for tx in a['txs']]


class Input:
    def __init__(self, i):
        obj = i.get('TxId')
        if obj is not None:
            # regular TX
        #self.n = obj['n']
        #self.value = i['value']
        #    if 'addr' in obj:
        #        self.address = obj['addr']
            self.TxId = i['TxId']
            self.Address = i['Address']
            self.Amount = i['Amount']

        #    self.script_sig = i['script']
        #    self.sequence = i['sequence']
        #else:
            # coinbase TX
        #    self.script_sig = i['script']
        #    self.sequence = i['sequence']


class Addresses:
    def __init__(self, a):
        #self.Value = o['Value']
        self.Address =a


class Output:
    def __init__(self, o):
        self.Value = o['Value']
        self.Addresses = [Addresses(a) for a in o['ScriptPubKey']['Addresses']]


class Transaction:
    def __init__(self, t):
        self.TxId = t.get('TxId')
        self.BlockTime = t.get('BlockTime')
        self.Time = t['Time']
        self.Confirmations = t['Confirmations']
        self.BlockHash = t['BlockHash']
        self.totalIn=0;
        self.totalOut=0;
        self.inputs = [Input(i) for i in t['VinList']]
        log ("------------------------")

        for i in self.inputs:
            self.totalIn+=i.Amount
        #log(self.totalIn)
        #self.as=Input(i).Amount for i in self.inputs
        self.outputs = [Output(o) for o in t['Vout']]
        for i in self.outputs:
            self.totalOut+=i.Value
        #log(self.totalOut)
        #if self.block_height is None:
        #    self.block_height = -1


class Block:
    def __init__(self, b):
        log ("REpuesta:")
        log (b)
        self.BlockTime = b['BlockTime']
        self.ConfirmationsClient = b['ConfirmationsClient']
        self.TimeFromNowUtc = b['TimeFromNowUtc']
        self.DiffBig = b['DiffBig']
        self.DiffSmall = b['DiffSmall']
        self.Hash = b['Hash']
        self.Confirmations = b['Confirmations']
        self.Size = b['Size']
        self.Height = b['Height']
        self.Version = b['Version']
        self.MerkleRoot = b['MerkleRoot']
        self.Difficulty = b['Difficulty']
        self.ChainWork = b['ChainWork']
        self.transactions=[]
        self.totalIn=0;
        self.totalOut=0;
        self.PreviousBlockHash = b['PreviousBlockHash']

        self.NextBlockHash = b['NextBlockHash']
        self.Bits = b['Bits']
        self.Flags = b['Flags']
        self.Time = b['Time']
        self.Nonce = b['Nonce']
        log(b['Tx'])
        for t in b['Tx']:
            self.transactions.append(get_tx(t))
        for i in self.transactions:
            self.totalIn+=i.totalIn
            self.totalOut+=i.totalOut
            log (i.TxId)
            log (i.totalIn)
            log (i.totalOut)

        #self.transactions =get_tx([Transaction(t) for t in get_tx(b['Tx'])][0])
    #    for tx in self.transactions:
    #        tx.block_height = self.height


class Balance:
    def __init__(self, b):
        self.final_balance = b['final_balance']
        self.n_tx = b['n_tx']
        self.total_received = b['total_received']


class FilterType(Enum):
    All = 4
    ConfirmedOnly = 5
    RemoveUnspendable = 6
