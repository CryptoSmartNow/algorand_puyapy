from puyapy import ARC4Contract, Bytes, LocalState, Txn, UInt64, arc4, itxn

from smart_contracts.program.ChildApprovalHex import (
    BITSAVE_CHILD_WORLD_APPROVAL_HEX,
    BITSAVE_CHILD_WORLD_CLEAR,
)


class Bitsave(ARC4Contract):
    def __init__(Self) -> None:
        Self.users_app_id = LocalState(UInt64)

    @arc4.abimethod()
    def hello(self, name: arc4.String) -> arc4.String:
        return "Hello, " + name

    def optin(self) -> UInt64:
        """
        Optin now concerns with deploying and saving child contract for user
        1. Creates child contract for new user
        2. Saves user child contract id
        :return:
        uint64 childContractId
        """
        # confirm user not opt in already
        curr_child_id, exists = self.users_app_id.maybe(Txn.sender)
        assert not exists, "User has been opted in"
        # deploy child contract
        self.users_app_id[Txn.sender] = (
            itxn.ApplicationCall(
                approval_program=Bytes.from_hex(BITSAVE_CHILD_WORLD_APPROVAL_HEX),
                clear_state_program=BITSAVE_CHILD_WORLD_CLEAR,
            )
            .submit()
            .created_app.application_id
        )
        return self.users_app_id[Txn.sender]

    @arc4.abimethod()
    def create_savings(self) -> arc4.Bool:
        return arc4.Bool(value=False)

    @arc4.abimethod()
    def increment_savings(self) -> arc4.UInt256:
        return arc4.UInt256(0)

    @arc4.abimethod()
    def withdraw_savings(self) -> arc4.Bool:
        return arc4.Bool(value=False)
