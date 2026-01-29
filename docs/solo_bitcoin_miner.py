# phi_solo_bitcoin_miner.py

import requests
import hashlib
import time
import json
import os
from base64 import b64encode

# === CONFIGURATION ===
RPC_USER = 'your_rpc_username'
RPC_PASSWORD = 'your_rpc_password'
BITCOIN_ADDRESS = '3AFuj5hsuCrFBcEsavmCZZJGFYsaoXaRkm'
RPC_URL = 'http://127.0.0.1:8332/'  # Default local Bitcoin Core node
HEADERS = {'content-type': 'application/json'}

# === HELPER FUNCTIONS ===
def rpc_call(method, params=[]):
    payload = json.dumps({"method": method, "params": params, "id": 0})
    auth = b64encode(f"{RPC_USER}:{RPC_PASSWORD}".encode()).decode()
    headers = HEADERS.copy()
    headers['Authorization'] = f'Basic {auth}'
    response = requests.post(RPC_URL, headers=headers, data=payload)
    if response.status_code != 200:
        print(f"RPC Error {response.status_code}: {response.text}")
        return None
    return response.json()['result']

def sha256d(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def mine_block(template):
    version = template['version']
    previousblockhash = bytes.fromhex(template['previousblockhash'])[::-1]
    merkle_root = bytes.fromhex(template['coinbaseaux']['flags'])[::-1]
    curtime = template['curtime']
    bits = int(template['bits'], 16)
    target = (bits & 0xffffff) * 2**(8*(bits >> 24 - 3))

    # Build coinbase transaction
    coinbase_tx = create_coinbase_tx(template)
    coinbase_txid = sha256d(bytes.fromhex(coinbase_tx)).hex()

    # Simplified Merkle Root (only coinbase)
    merkle_root = bytes.fromhex(coinbase_txid)[::-1]

    print(f"[*] Mining new block at time {curtime}... Target: {hex(target)}")

    for nonce in range(0, 0xFFFFFFFF):
        header = (
            version.to_bytes(4, 'little') +
            previousblockhash +
            merkle_root +
            curtime.to_bytes(4, 'little') +
            int(template['bits'], 16).to_bytes(4, 'little') +
            nonce.to_bytes(4, 'little')
        )

        hash_result = sha256d(header)
        hash_int = int.from_bytes(hash_result[::-1], byteorder='big')

        if hash_int < target:
            print(f"\n[!] Block Found! Nonce: {nonce}")
            print(f"[!] Hash: {hash_result[::-1].hex()}")
            submit_block(header.hex(), template)
            return

        if nonce % 1000000 == 0:
            print(f"Checked {nonce} nonces...")

def create_coinbase_tx(template):
    # This is a minimal coinbase TX for mining
    coinbase_script = b'phi_miner_script' + os.urandom(10)
    tx = (
        b'01000000' +  # Version
        b'01' +        # 1 input
        b'00' * 32 +   # Prev txid
        b'ffffffff' +  # Prev vout
        bytes([len(coinbase_script)]).hex().encode() +
        coinbase_script.hex().encode() +
        b'ffffffff' +  # Sequence
        b'01' +        # 1 output
        (template['coinbasevalue']).to_bytes(8, 'little').hex().encode() +
        b'19' +        # Length of standard scriptPubKey
        b'76a914' +
        bytes.fromhex(hashlib.new('ripemd160', hashlib.sha256(bytes.fromhex(BITCOIN_ADDRESS)).digest()).hexdigest()).hex().encode() +
        b'88ac' +
        b'00000000'    # Locktime
    )
    return tx.decode()

def submit_block(header_hex, template):
    block = header_hex + template['coinbaseaux']['flags'] + ''.join(template['transactions'])
    result = rpc_call('submitblock', [block])
    if result is None:
        print("[+] Block submitted successfully!")
    else:
        print(f"[!] Block submission failed: {result}")

# === MAIN LOOP ===
if __name__ == "__main__":
    while True:
        block_template = rpc_call('getblocktemplate', [{"rules": ["segwit"]}])
        if block_template:
            mine_block(block_template)
        else:
            print("[-] Failed to get block template. Retrying in 10s...")
            time.sleep(10)
