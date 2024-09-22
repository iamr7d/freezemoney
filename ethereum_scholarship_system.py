# ethereum_scholarship_system.py

from ethereum_account import EthereumAccount
from zk_proof import EnhancedZKProof

class EthereumScholarshipSystem:
    def __init__(self):
        self.accounts = {
            'Admin': EthereumAccount('Admin', 1000000),
            'Student1': EthereumAccount('Student1'),
            'Student2': EthereumAccount('Student2'),
            'Vendor1': EthereumAccount('Vendor1'),
            'Vendor2': EthereumAccount('Vendor2')
        }
        self.zkp = EnhancedZKProof()
        self.approved_vendors = {'Vendor1', 'Vendor2'}
        self.educational_purposes = {'Tuition', 'Books', 'School Supplies', 'Accommodation'}
        self.disallowed_purposes = {'Buy Alcohol', 'Buy Cigarette', 'Buy to Watch Non-Educational'}
        self.spending_limits = {'Tuition': 10000, 'Books': 1000, 'School Supplies': 500, 'Accommodation': 5000}

    def issue_scholarship(self, student, amount):
        if self.accounts['Admin'].balance >= amount:
            tx_hash = self.accounts['Admin'].add_transaction(-amount, f"Issue scholarship to {student}", student)
            self.accounts[student].add_transaction(amount, "Receive scholarship", 'Admin', is_frozen=True)
            return tx_hash
        return None

    def spend_scholarship(self, student, vendor, amount, purpose):
        if vendor not in self.approved_vendors:
            return None, None, "Vendor not approved for educational expenses"
        
        if purpose in self.disallowed_purposes:
            return None, None, f"Spending on '{purpose}' is not allowed."

        if purpose not in self.educational_purposes:
            return None, None, "Purpose is not educational"

        if amount > self.spending_limits.get(purpose, 0):
            return None, None, f"Amount exceeds spending limit for {purpose}"

        public = f"{student}{vendor}{amount}{purpose}"
        proof = self.zkp.generate_proof(self.accounts[student].private_key, public)

        if self.zkp.verify_proof(self.accounts[student].public_key, proof, public) and self.accounts[student].frozen_balance >= amount:
            tx_hash_student = self.accounts[student].add_transaction(-amount, f"Spend at {vendor}", vendor, is_frozen=True, purpose=purpose)
            tx_hash_vendor = self.accounts[vendor].add_transaction(amount, f"Receive from {student}", student, purpose=purpose)
            return tx_hash_student, proof, "Transaction successful"
        return None, None, "Insufficient frozen funds or invalid proof"

    def get_all_transactions(self):
        all_transactions = []
        for account in self.accounts.values():
            all_transactions.extend(account.transactions)
        return sorted(all_transactions, key=lambda x: x['timestamp'], reverse=True)

    def transfer_scholarship(self, from_student, to_student, amount):
        if self.accounts[from_student].frozen_balance >= amount:
            tx_hash_from = self.accounts[from_student].add_transaction(-amount, f"Transfer to {to_student}", to_student, is_frozen=True)
            tx_hash_to = self.accounts[to_student].add_transaction(amount, f"Receive from {from_student}", from_student, is_frozen=True)
            return tx_hash_from
        return None

