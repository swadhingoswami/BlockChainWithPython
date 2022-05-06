"""
Author      : Swadhin Goswami
Email       : gsmswadhin@gmail.com
Description :
This script will send funds from one account to another account
"""

from web3 import Web3
ganach_url = 'http://127.0.0.1:7522'
web = Web3(Web3.HTTPProvider(ganach_url))
web.isConnected()

public_key_account_1 = "0x813e641aF9C1b4bFb67C918C241d7cd6f1084A17"
public_key_account_2 = "0x82531878C967C4Ff2cae85805f463DE30B1bE716"

private_key_account_1 = "691a82f2801561d8f9f451ee740e2f6fe1a7ff689dd5b76cedade39d36ac24c2"

## Create Transaction :

# Build txn :
nonce = web.eth.getTransactionCount(public_key_account_1)
txn = {
        'nonce'     : nonce,
        'to'        : public_key_account_2,
        'value'     : web.toWei(1, 'ether'),
        'gas'       : 2000000,
        'gasPrice'  : web.toWei('5', 'gwei')
}

# sign txn
signed_txn = web.eth.account.signTransaction(txn, private_key_account_1)

# send txn and get the txn hash
txn_hash = web.eth.sendRawTransaction(signed_txn.rawTransaction)
print(web.toHex(txn_hash))
