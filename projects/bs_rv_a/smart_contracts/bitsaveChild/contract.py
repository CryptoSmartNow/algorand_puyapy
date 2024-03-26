import typing

from puyapy import (
    ARC4Contract, 
    Asset, 
    Bytes, 
    Global, 
    UInt64, 
    arc4, 
    itxn, 
    subroutine,
)


Names: typing.TypeAlias = arc4.DynamicArray


class Bitsavechild(ARC4Contract):
    def __init__(Self) -> None:
        """
        Initiates the states of the child contract
        """

    @arc4.abimethod()
    def hello(self, name: arc4.String) -> arc4.String:
        return "Hello, " + name

    def opt_contract_to_token(self, token: Asset) -> Bytes:
        asset_opt_txn = itxn.AssetTransfer(
            asset_amount=UInt64(0),
            xfer_asset=token.asset_id,
            asset_receiver=Global.current_application_address
        ).submit()
        return asset_opt_txn.txn_id


@subroutine
def calc_interest(principal: UInt64, percentage: UInt64) -> UInt64:
    return principal * percentage // UInt64(100)
