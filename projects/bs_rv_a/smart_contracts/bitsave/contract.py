from puyapy import ARC4Contract, UInt64, arc4, subroutine


class Bitsave(ARC4Contract):
    @arc4.abimethod()
    def hello(self, name: arc4.String) -> arc4.String:
        return "Hello, " + name

    @arc4.abimethod()
    def optin(self) -> UInt64:
        """
        Optin now concerns with deploying and saving child contract for user
        1. Creates child contract for new user
        2. Saves user child contract id
        :return:
        uint64 childContractId
        """
        child_contract_id = mask_create_child_contract()
        return child_contract_id



@subroutine
def mask_create_child_contract() -> UInt64:
    """
    Functionality to deploy a child contract
    :return: uint64 childContractId
    """
    # todo: write out functionality
    return UInt64(22)
