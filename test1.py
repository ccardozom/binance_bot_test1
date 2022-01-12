import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = "XRc8GQqmJaoQw2wNd3DGOARTvo4uq5x5LQiAqkfYde41MUUBcJxQEkmffCWtXvUX"
secret = "m9KEdobo7HTcp5HGiJWOMWJUfLo5TuyrOxGvQxlybKZYQ8RMHXmxK3LADIYkynCO"

spot_client = Client(key, secret)
logging.info(spot_client.account_status())
logging.info(spot_client.coin_info())