from brownie import Lottery, accounts, network, config
from web3 import Web3


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    # This is a hard coded value just for a quick check of the math
    assert lottery.getEntranceFee() > Web3.toWei(0.040, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.045, "ether")