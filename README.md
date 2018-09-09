# Blockchain API library (Python, v1) - SmartCash

Initial adapt from Blockexplorer Bitcoin Blockchain to Smartcash Blockchain

### Getting started

You can execute example.py. Config values in config.py if you want

The module consists of the following sub-modules:

* `blockexplorer` ([docs](docs/blockexplorer.md)) ([api/blockchain_api][api1])
* `createwallet` ([docs](docs/createwallet.md)) ([api/create_wallet][api2]) # Not adapted
* `exchangerates` ([docs](docs/exchangerates.md)) ([api/exchange\_rates\_api][api3]) Not adapted
* `pushtx` ([docs](docs/pushtx.md)) ([pushtx][api7]) Not adapted
* `v2.receive` ([docs](docs/receive.md)) ([api/api_receive][api4]) Not adapted
* `statistics` ([docs](docs/statistics.md)) ([api/charts_api][api5]) Not adapted
* `wallet` ([docs](docs/wallet.md)) ([api/blockchain\_wallet\_api][api6]) Not adapted

### Error handling

All functions may raise exceptions caused by incorrectly passed parameters or other problems. If a call is rejected server-side, the `APIException` exception will be raised.

### Config values
DEBUG = True 'if you want see all procesing
TIMEWAITTORETRY=30 'time to retry case server doesnot response
BLOQUEINICIO=438286 'Block where start to search
HASTABLOQUE=BLOQUEINICIO+50000 '#Until blocks
VALORMAX=8000000 'Mark all blocks which amount is upper to VALORMAX
BASE_URL = "https://smart.ccore.online" 'explorer
TIMEOUT_URL = 100 ' timeout http request
TIME_SLEEP_REQUEST=1 'Time to sleep case server ban for ddos



