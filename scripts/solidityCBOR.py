import cbor2
import base58

bytecode = "6080604052348015600f57600080fd5b50603e80601d6000396000f3fe6080604052600080fdfea265627a7a72315820aab07412a6c36f5b09466d3f973ff1bd9d8c544731b390842691474ae0a5755c64736f6c63430005110032"

key_mappings = {
    'ipfs': 'ipfs',
    'bzzr1': 'bzzr1',
    'bzzr0': 'bzzr0',
    'solc': 'solc'
}

result = {}

code = bytes.fromhex(bytecode)
offset = int.from_bytes(code[-2:], 'big') + 2
metadata = cbor2.loads(code[-offset:])

for key, new_key in key_mappings.items():
    if key in metadata:
        if isinstance(metadata[key], bytes):
            if key == 'solc':
                result[new_key] = '.'.join(str(byte) for byte in metadata['solc'])
                continue
            if key == 'bzzr1' or key == 'bzzr0':
                result[new_key] = metadata[key].hex()
                continue
            # if ipfs
            result[new_key] = base58.b58encode(metadata[key]).decode('utf-8')           
        else: 
            result[new_key] = metadata[key]

if 'experimental' in metadata:
    result['experimental'] = metadata['experimental']

print(result)