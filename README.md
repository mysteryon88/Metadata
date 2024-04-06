# Metadata

## Solidity Metadata

### Simple smart-contract

#### First

```sh
$ solc --bin EmptyContract.sol

======= contract.sol:EmptyContract =======
Binary:
6080604052603e80600f5f395ff3fe60806040525f80fdfea264697066735822122049842f421961b60b907894fd44a02ebfce0353d5039299ccf1256a91f50e872c64736f6c63430008190033

$ solc --bin --no-cbor-metadata EmptyContract.sol

======= contract.sol:EmptyContract =======
Binary:
6080604052600880600f5f395ff3fe60806040525f80fd

$ solc --bin-runtime --no-cbor-metadata EmptyContract.sol

======= EmptyContract.sol:EmptyContract =======
Binary of the runtime part:
60806040525f80fd
```

#### Second

```sh
$ solc --bin Empty.sol

======= Empty.sol:Empty =======
Binary:
6080604052603e80600f5f395ff3fe60806040525f80fdfea264697066735822122036298a5831c451ef78fc876835cd1b05e71fa0df134dbe6dbbcb91bca429478c64736f6c63430008190033

$ solc --bin --no-cbor-metadata Empty.sol

======= Empty.sol:Empty =======
Binary:
6080604052600880600f5f395ff3fe60806040525f80fd

$ solc --bin-runtime --no-cbor-metadata Empty.sol

======= Empty.sol:Empty =======
Binary of the runtime part:
60806040525f80fd
```

### Deep dive into metadata

```sh
fe      # INVALID
# metadata
a2646970667358221220c9575193f43c762b622f818e18eb8e9467653ba74e171cc817b4db02503f444b64736f6c6343000819
0033    # 0x33 = 51 len(metadata)
```

```sh
# 1
6080604052603e80600f5f395ff3fe  # init
60806040525f80fd                # runtime
fe                              # INVALID
# cbor
a2                              # map (0x00..0x17 pairs of data items follow) (len 2)
64                              # UTF-8 string (0x00..0x17 bytes follow) (len 4)
69706673                        # 'ipfs'
58                              # byte string (one-byte uint8_t for n, and then n bytes follow)
22                              # len 0x22 = 34
# hash base58
122049842f421961b60b907894fd44a02ebfce0353d5039299ccf1256a91f50e872c
64                              # UTF-8 string (0x00..0x17 bytes follow) (len 4)
736f6c63                        # 'solc'
43                              # byte string (0x00..0x17 bytes follow) (len 3)
000819                          # 0.8.25
0033                            # len 0x33 = 51

# 2
6080604052603e80600f5f395ff3fe  # init
60806040525f80fd                # runtime
fe                              # INVALID
# cbor
a2                              # map (0x00..0x17 pairs of data items follow) (len 2)
64                              # UTF-8 string (0x00..0x17 bytes follow) (len 4)
69706673                        # 'ipfs'
58                              # byte string (one-byte uint8_t for n, and then n bytes follow)
22                              # len 0x22 = 34
# hash base58
122036298a5831c451ef78fc876835cd1b05e71fa0df134dbe6dbbcb91bca429478c
64                              # UTF-8 string (0x00..0x17 bytes follow) (len 4)
736f6c63                        # 'solc'
43                              # byte string (0x00..0x17 bytes follow) (len 3)
000819                          # 0.8.25
0033                            # len 0x33 = 51
```

#### IPFS

```sh
$ mkdir out

$ solc --bin --metadata EmptyContract.sol --output-dir out
$ solc --bin --metadata Empty.sol --output-dir out

$ ipfs add -qr --only-hash out/EmptyContract_meta.json
QmTHdNmp7Ky32nVCfcwLDsvacq27vzFdTMUFgCX55yQCTd

$ ipfs add -qr --only-hash out/Empty_meta.json
QmRz5TrMgPNiWiWNxiccrqy2QQNamGSFzzJTCYzUn6LZZd
```

```sh
# You can use a python script
$ python3 scripts/ipfsHash.py
QmTHdNmp7Ky32nVCfcwLDsvacq27vzFdTMUFgCX55yQCTd
QmRz5TrMgPNiWiWNxiccrqy2QQNamGSFzzJTCYzUn6LZZd
```

```sh
# This hash is in the '_meta.json' files
$ ipfs add -qr --only-hash Empty.sol
QmSrpmAQC3kWnT9T6bQuM8AKDF5djsYb974hYK6ScEE8xo

$ ipfs add -qr --only-hash EmptyContract.sol
QmSpybP5G8xH61EyQUExnDGFE53Sj1Z8cfnvn4AvuPcgVk
```

#### 0.8.26-nightly.2024.4.4+commit.3d7b3d94

```sh
6080604052606380600f5f395ff3fe60806040525f80fdfea2646970667358221220819347f85535ded427d5ebe4df3b3323450dc70b2b5db43691c2288c9574961864736f6c637827302e382e32362d6e696768746c792e323032342e342e342b636f6d6d69742e33643762336439340058

6080604052606380600f5f395ff3fe  # init
60806040525f80fd                # runtime
fe                              # INVALID
# cbor
a2                              # map (0x00..0x17 pairs of data items follow) (len 2)
64                              # UTF-8 string (0x00..0x17 bytes follow) (len 4)
69706673                        # 'ipfs'
58                              # byte string (one-byte uint8_t for n, and then n bytes follow)
22                              # len 0x22 = 34
1220819347f85535ded427d5ebe4df3b3323450dc70b2b5db43691c2288c95749618
64                              # UTF-8 string (0x00..0x17 bytes follow) (len 4)
736f6c63                        # 'solc'
78                              # UTF-8 string (one-byte uint8_t for n, and then n bytes follow)
27                              # len 0x27 = 39
302e382e32362d6e696768746c792e323032342e342e342b636f6d6d69742e3364376233643934
0058                            # len 0x58 = 88
```

#### 0.5.17+commit.d19bba13

```solidity
//SPDX-License-Identifier: MIT
pragma solidity <=0.8.26;

contract EmptyContract {}
```

```sh

6080604052348015600f57600080fd5b50603e80601d6000396000f3fe6080604052600080fdfea265627a7a72315820aab07412a6c36f5b09466d3f973ff1bd9d8c544731b390842691474ae0a5755c64736f6c63430005110032

# cbor
a2          # map (0x00..0x17 pairs of data items follow) (len 2)
65          # UTF-8 string (0x00..0x17 bytes follow) (len 5)
627a7a7231  # 'bzzr1'
58          # byte string (one-byte uint8_t for n, and then n bytes follow)
20          # len 0x20 = 32
aab07412a6c36f5b09466d3f973ff1bd9d8c544731b390842691474ae0a5755c
64          # UTF-8 string (0x00..0x17 bytes follow) (len 4)
736f6c63    # 'solc'
43          # byte string (0x00..0x17 bytes follow) (len 3)
000511      # 0.5.17
0032        # len 0x32 = 50
```

#### 0.6.0+commit.26b70077

```sh
6080604052348015600f57600080fd5b50603f80601d6000396000f3fe6080604052600080fdfea264697066735822122035aa157219ccfa42717edbdc218f5f1c466ab6b0705840b2f4ec293f2a898b6364736f6c63430006000033

# cbor
a2          # map (0x00..0x17 pairs of data items follow) (len 2)
64          # UTF-8 string (0x00..0x17 bytes follow) (len 4)
69706673    # 'ipfs'
58          # byte string (one-byte uint8_t for n, and then n bytes follow)
22          # len 0x22 = 34
122035aa157219ccfa42717edbdc218f5f1c466ab6b0705840b2f4ec293f2a898b63
64          # UTF-8 string (0x00..0x17 bytes follow) (len 4)
736f6c63    # 'solc'
43          # byte string (0x00..0x17 bytes follow) (len 3)
000600      # 0.6.0
0033        # len 0x32 = 50
```

### JSON-input-output interface

#### bzzr1

```js
{
  ...
  "metadata": {
    // The CBOR metadata is appended at the end of the bytecode by default.
    // Setting this to false omits the metadata from the runtime and deploy time code.
    "appendCBOR": true,
    // Use only literal content and not URLs (false by default)
    "useLiteralContent": true,
    // Use the given hash method for the metadata hash that is appended to the bytecode.
    // The metadata hash can be removed from the bytecode via option "none".
    // The other options are "ipfs" and "bzzr1".
    // If the option is omitted, "ipfs" is used by default.
    "bytecodeHash": "ipfs"
  }
}
```

```sh
$ solc --standard-json compile.json

6080604052603d80600f5f395ff3fe60806040525f80fdfea265627a7a723158206cc665b253324ab3a06673604b1ed10373ba4f0c0d668e79947a82acc29a20ee64736f6c63430008190032

6080604052603d80600f5f395ff3fe  # init
60806040525f80fd                # runtime
fe                              # INVALID
# cbor
a2                              # map (0x00..0x17 pairs of data items follow) (len 2)
65                              # UTF-8 string (0x00..0x17 bytes follow) (len 5)
627a7a7231                      # 'bzzr1'
58                              # byte string (one-byte uint8_t for n, and then n bytes follow)
20                              # len 0x20 = 32
6cc665b253324ab3a06673604b1ed10373ba4f0c0d668e79947a82acc29a20ee
64                              # UTF-8 string (0x00..0x17 bytes follow) (len 4)
736f6c63                        # 'solc'
43                              # byte string (0x00..0x17 bytes follow) (len 3)
000819                          # 0.8.25
0032                            # len 0x32 = 50
```

## Vyper Metadata

### Compile

```sh
$ vyper -f bytecode contract.vy
$ vyper --no-bytecode-metadata  contract.vy
$ vyper -f bytecode_runtime contract.vy
```

### Deep dive into vyper metadata

#### Metadata now (0.3.10)

```sh
CBOR-encoded list:
  runtime code length
  [<length of data section> for data section in runtime data sections]
  immutable section length
  {"vyper": (major, minor, patch)}
length of CBOR-encoded list + 2, encoded as two big-endian bytes.
```

#### 0.3.10+commit.9136169

```sh
$ vyper -f bytecode HelloWorld.vy

0x600b6040527f48656c6c6f20576f726c64000000000000000000000000000000000000000000606052604080515f556020810151600155506100836100476000396100836000f35f3560e01c63cfae3217811861007b573461007f576020806040528060400160205f54015f81601f0160051c6005811161007f57801561004f57905b80548160051b85015260010181811861003b575b5050508051806020830101601f825f03163682375050601f19601f825160200101169050810190506040f35b5f5ffd5b5f80fd8418838000a16576797065728300030a0012

$ vyper --no-bytecode-metadata  HelloWorld.vy

0x600b6040527f48656c6c6f20576f726c64000000000000000000000000000000000000000000606052604080515f556020810151600155506100836100476000396100836000f35f3560e01c63cfae3217811861007b573461007f576020806040528060400160205f54015f81601f0160051c6005811161007f57801561004f57905b80548160051b85015260010181811861003b575b5050508051806020830101601f825f03163682375050601f19601f825160200101169050810190506040f35b5f5ffd5b5f80fd

$ vyper -f bytecode_runtime HelloWorld.vy

0x5f3560e01c63cfae3217811861007b573461007f576020806040528060400160205f54015f81601f0160051c6005811161007f57801561004f57905b80548160051b85015260010181811861003b575b5050508051806020830101601f825f03163682375050601f19601f825160200101169050810190506040f35b5f5ffd5b5f80fd

# metadata

84          # array (0x00..0x17 data items follow) (len 4)
18          # unsigned integer (one-byte uint8_t follows)
83          # 131 len runtime code
80          # array (0x00..0x17 data items follow) (len 0)
00          # unsigned integer 0x00..0x17 (0)
a1          # map (0x00..0x17 pairs of data items follow) (len 1)
65          # UTF-8 string (0x00..0x17 bytes follow) (len 5)
7679706572  # 'vyper'
83          # array (0x00..0x17 data items follow) (len 3)
00030a      # 0.3.10
0012        # len 0x12 = 18

$ python3 scripts/vyperCBOR.py

{'runtime_size': 131, 'data_sizes': [], 'immutable_size': 0, 'compiler': {'vyper': [0, 3, 10]}}
```

##### immutable.vy

```sh
$ vyper immutable.vy

0x604051503461002457602061003d5f395f51604052610003610028603d39610023603df35b5f80fd5f5ffd8403801820a16576797065728300030a0012

$ vyper -f bytecode_runtime immutable.vy
0x5f5ffd

84          # array (0x00..0x17 data items follow) (len 4)
03          # unsigned integer 0x00..0x17 (0..23) (len runtime code = 3)
80          # array (0x00..0x17 data items follow) (len 0)
18          # unsigned integer (one-byte uint8_t follows)
20          # 0x20 = 32 'immutable_size'
a1          # map (0x00..0x17 pairs of data items follow) (len 1)
65          # UTF-8 string (0x00..0x17 bytes follow) (len 5)
7679706572  # 'vyper'
83          # array (0x00..0x17 data items follow) (len 3)
00030a      # 0.3.10
0012        # len 0x12 = 18

$ python3 scripts/vyperCBOR.py
{'runtime_size': 3, 'data_sizes': [], 'immutable_size': 32, 'compiler': {'vyper': [0, 3, 10]}}

```

#### 0.3.7+commit.6020b8b

```sh
$ vyper -f bytecode HelloWorld.vy

0x600b6040527f48656c6c6f20576f726c6400000000000000000000000000000000000000000060605260408051806000556020820180516001555050506100b661004c6000396100b66000f36003361161000c5761009e565b60003560e01c346100a45763cfae3217811861009c57600436106100a4576020806040528060400160005480825260208201600082601f0160051c600481116100a457801561006e57905b80600101548160051b840152600101818118610057575b505050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506040f35b505b60006000fd5b600080fda165767970657283000307000b

$ vyper --no-bytecode-metadata HelloWorld.vy

0x600b6040527f48656c6c6f20576f726c6400000000000000000000000000000000000000000060605260408051806000556020820180516001555050506100a961004c6000396100a96000f36003361161000c5761009e565b60003560e01c346100a45763cfae3217811861009c57600436106100a4576020806040528060400160005480825260208201600082601f0160051c600481116100a457801561006e57905b80600101548160051b840152600101818118610057575b505050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506040f35b505b60006000fd5b600080fd

$ vyper -f bytecode_runtime HelloWorld.vy

0x5f3560e01c63cfae3217811861007b573461007f576020806040528060400160205f54015f81601f0160051c6005811161007f57801561004f57905b80548160051b85015260010181811861003b575b5050508051806020830101601f825f03163682375050601f19601f825160200101169050810190506040f35b5f5ffd5b5f80fd

# metadata

a1          # map (0x00..0x17 pairs of data items follow) (len 1)
65          # UTF-8 string (0x00..0x17 bytes follow) (len 5)
7679706572  # 'vyper'
83          # array (0x00..0x17 data items follow) (len 3)
000307      # 0.3.7
000b        # len 0x0b = 11
```

## References

- [Contract Metadata](https://docs.soliditylang.org/en/latest/metadata.html)
- [RFC 8949 CBOR](https://www.rfc-editor.org/rfc/rfc8949.html#jumptable)
- [Properly parse contract creation bytecode metadata hash using cbor module in npm](https://ethereum.stackexchange.com/questions/111909/properly-parse-contract-creation-bytecode-metadata-hash-using-cbor-module-in-npm)
- [feat: add runtime code layout to initcode](https://github.com/vyperlang/vyper/pull/3584)
- [Installing Vyper](https://docs.vyperlang.org/en/latest/installing-vyper.html)
