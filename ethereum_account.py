# ethereum_account.py

import hashlib
from datetime import datetime
from zk_proof import EnhancedZKProof

class EthereumAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.frozen_balance = 0
        self.nonce = 0
        self.transactions = []
        self.private_key, self.public_key = EnhancedZKProof.generate_keys()

    def add_transaction(self, amount, description, to_address, is_frozen=False, purpose=None):
        if is_frozen:
            self.frozen_balance += amount
        else:
            self.balance += amount
        self.nonce += 1
        tx_hash = hashlib.sha256(f"{self.nonce}{amount}{to_address}".encode()).hexdigest()
        self.transactions.append({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount,
            'description': description,
            'balance': self.balance,
            'frozen_balance': self.frozen_balance,
            'tx_hash': tx_hash,
            'purpose': purpose
        })
        return tx_hash

