# @version ^0.3.10

DATA: immutable(uint256) # 32 bytes

@external
def __init__(_data: uint256):
    DATA = _data