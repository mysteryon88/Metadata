import base58 

def hash(hex_ipfs_hash):
    bytes_str = bytes.fromhex(hex_ipfs_hash) 
    print(base58.b58encode(bytes_str).decode("utf-8"))

hex_ipfs_hash = "122049842f421961b60b907894fd44a02ebfce0353d5039299ccf1256a91f50e872c"
hash(hex_ipfs_hash)

hex_ipfs_hash = "122036298a5831c451ef78fc876835cd1b05e71fa0df134dbe6dbbcb91bca429478c"
hash(hex_ipfs_hash)