# BlockChainWithPython
Create a Blockchain App using Python (Solidity, Ethereum, Web 3.0) :::

------------------------------------------------------------------------------
Create a Simple Blockchain App using Python (Solidity, Ethereum, Web 3.0) :::
------------------------------------------------------------------------------

Enviroment setting and requited software and tools.
1) Metamask :
    Download Link : https://metamask.io/
    In Metamask, use the following settings for the Custom RPC:
    New RPC URL http://172.29.64.1:7545 [ ganach_url ]
    Chain ID 1337
  
2) Ganache :
    Personal Ethereum blockchain which you can use to run tests.
    Download Link : https://trufflesuite.com/ganache/

------------------------------------------------------------------------------
PYTHON SETUP [ Web3 ] :
------------------------------------------------------------------------------
web3 requires python 3.5 or above. Its good to work in a virtual environment. 
Try the following:

## Install web3 in python virtual environment :
python3 -m venv venv
. venv/bin/activate
pip install web3


## A SIMPLE PYTHON SCRIPT TO SEND FUND FROM ACCOUNT_1 TO ACCOUNT_2

from web3 import Web3

ganach_url = 'http://127.0.0.1:7522'
web = Web3(Web3.HTTPProvider(ganach_url))
web.isConnected()
web.eth.blockNumber
balance = web.eth.getBalance("0x813e641aF9C1b4bFb67C918C241d7cd6f1084A17")
print(balance)
web.fromWei(balance, 'ether')

public_key_account_1 = "0x813e641aF9C1b4bFb67C918C241d7cd6f1084A17" # Took this key from MetaMask account1
public_key_account_2 = "0x82531878C967C4Ff2cae85805f463DE30B1bE716" # Took this key from MetaMask account2

private_key_account_1 = "691a82f2801561d8f9f451ee740e2f6fe1a7ff689dd5b76cedade39d36ac24c2" # Took this private key address from ganach 
                                                                                           # which is mapped with MetaMask account1

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
