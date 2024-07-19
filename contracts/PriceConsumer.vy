# SPDX-License-Identifier: MIT
#pragma version ^0.3.10

import contracts.interfaces.AggregatorV3Interface as AggregatorV3Interface

price_feeds: public(HashMap[address, AggregatorV3Interface])
owner: public(address)

@external
def __init__(_initial_price_feed_address: address):
    """
    @dev Initializes the contract with an array of price feed addresses.
    """
    self.owner = msg.sender
    self.price_feeds[_initial_price_feed_address] = AggregatorV3Interface(_initial_price_feed_address)

@external
@view
def get_latest_price(_address: address) -> int256:
    a: uint80 = 0
    price: int256 = 0
    b: uint256 = 0
    c: uint256 = 0
    d: uint80 = 0
    (a, price, b, c, d) = self.price_feeds[_address].latestRoundData()
    return price

@external
def addPriceFeedAddress(_address: address):
    """
    @dev Adds a new price feed address to the price_feeds mapping.
    """
    assert msg.sender == self.owner, "Only the owner can set new price feeds"
    self.price_feeds[_address] = AggregatorV3Interface(_address)

@external
@view
def get_symbol(_address: address) -> String[1000]:
    """
    @dev Returns the symbol pair for a given price feed address.
    """
    return self.price_feeds[_address].description()