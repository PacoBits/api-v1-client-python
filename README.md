# Blockchain API library (Python, v1)

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

### Connection timeouts

It is possible to set arbitrary connection timeouts.

```python
from blockchain import util
util.TIMEOUT = 5 #time out after 5 seconds
```


