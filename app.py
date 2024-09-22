# app.py

import streamlit as st
import pandas as pd
from ethereum_scholarship_system import EthereumScholarshipSystem

def main():
    st.title("Ethcash")

    if 'system' not in st.session_state:
        st.session_state.system = EthereumScholarshipSystem()

    system = st.session_state.system

    st.sidebar.header("Actions")
    action = st.sidebar.selectbox("Choose an action", ["View Balances", "Issue Scholarship", "Spend Scholarship", "Transfer Scholarship", "Admin View"])

    if action == "View Balances":
        st.header("Account Balances")
        balances = {name: f"Regular: {account.balance}, Frozen: {account.frozen_balance}" 
                    for name, account in system.accounts.items()}
        st.table(pd.DataFrame(list(balances.items()), columns=["Account", "Balance"]))

    elif action == "Issue Scholarship":
        st.header("Issue Scholarship")
        student = st.selectbox("Select Student", ["Student1", "Student2"])
        amount = st.number_input("Amount", min_value=1, max_value=system.accounts['Admin'].balance)
        if st.button("Issue Scholarship"):
            tx_hash = system.issue_scholarship(student, amount)
            if tx_hash:
                st.success(f"Successfully issued {amount} to {student} as frozen funds. Transaction Hash: {tx_hash}")
            else:
                st.error("Failed to issue scholarship. Insufficient admin funds.")

    elif action == "Spend Scholarship":
        st.header("Spend Scholarship")
        student = st.selectbox("Select Student", ["Student1", "Student2"])
        vendor = st.selectbox("Select Vendor", ["Vendor1", "Vendor2"])
        purpose = st.selectbox("Select Purpose", list(system.educational_purposes) + list(system.disallowed_purposes))
        max_amount = min(system.accounts[student].frozen_balance, system.spending_limits.get(purpose, system.accounts[student].frozen_balance))
        amount = st.number_input("Amount", min_value=1, max_value=max_amount) if max_amount > 0 else 0

        if st.button("Spend Scholarship"):
            tx_hash, proof, message = system.spend_scholarship(student, vendor, amount, purpose)
            if tx_hash:
                st.success(f"Successfully spent {amount} from {student} to {vendor} for {purpose}. Transaction Hash: {tx_hash}")
                st.info(f"Zero-Knowledge Proof: {proof}")
            else:
                st.error(f"Failed to spend scholarship. {message}")

    elif action == "Transfer Scholarship":
        st.header("Transfer Scholarship")
        from_student = st.selectbox("From Student", ["Student1", "Student2"])
        to_student = st.selectbox("To Student", [s for s in ["Student1", "Student2"] if s != from_student])
        max_amount = system.accounts[from_student].frozen_balance
        amount = st.number_input("Amount", min_value=1, max_value=max_amount) if max_amount > 0 else 0

        if st.button("Transfer Scholarship"):
            tx_hash = system.transfer_scholarship(from_student, to_student, amount)
            if tx_hash:
                st.success(f"Successfully transferred {amount} from {from_student} to {to_student}. Transaction Hash: {tx_hash}")
            else:
                st.error("Failed to transfer scholarship. Insufficient frozen funds.")

    elif action == "Admin View":
        st.header("All Transactions")
        transactions = system.get_all_transactions()
        st.table(pd.DataFrame(transactions))

if __name__ == "__main__":
    main()
# app.py

import streamlit as st
import pandas as pd
from ethereum_scholarship_system import EthereumScholarshipSystem

def main():
    st.title("Ethcash")

    if 'system' not in st.session_state:
        st.session_state.system = EthereumScholarshipSystem()

    system = st.session_state.system

    st.sidebar.header("Actions")
    action = st.sidebar.selectbox("Choose an action", ["View Balances", "Issue Scholarship", "Spend Scholarship", "Transfer Scholarship", "Admin View"])

    if action == "View Balances":
        st.header("Account Balances")
        balances = {name: f"Regular: {account.balance}, Frozen: {account.frozen_balance}" 
                    for name, account in system.accounts.items()}
        st.table(pd.DataFrame(list(balances.items()), columns=["Account", "Balance"]))

    elif action == "Issue Scholarship":
        st.header("Issue Scholarship")
        student = st.selectbox("Select Student", ["Student1", "Student2"])
        amount = st.number_input("Amount", min_value=1, max_value=system.accounts['Admin'].balance)
        if st.button("Issue Scholarship"):
            tx_hash = system.issue_scholarship(student, amount)
            if tx_hash:
                st.success(f"Successfully issued {amount} to {student} as frozen funds. Transaction Hash: {tx_hash}")
            else:
                st.error("Failed to issue scholarship. Insufficient admin funds.")

    elif action == "Spend Scholarship":
        st.header("Spend Scholarship")
        student = st.selectbox("Select Student", ["Student1", "Student2"])
        vendor = st.selectbox("Select Vendor", ["Vendor1", "Vendor2"])
        purpose = st.selectbox("Select Purpose", list(system.educational_purposes) + list(system.disallowed_purposes))
        max_amount = min(system.accounts[student].frozen_balance, system.spending_limits.get(purpose, system.accounts[student].frozen_balance))
        amount = st.number_input("Amount", min_value=1, max_value=max_amount) if max_amount > 0 else 0

        if st.button("Spend Scholarship"):
            tx_hash, proof, message = system.spend_scholarship(student, vendor, amount, purpose)
            if tx_hash:
                st.success(f"Successfully spent {amount} from {student} to {vendor} for {purpose}. Transaction Hash: {tx_hash}")
                st.info(f"Zero-Knowledge Proof: {proof}")
            else:
                st.error(f"Failed to spend scholarship. {message}")

    elif action == "Transfer Scholarship":
        st.header("Transfer Scholarship")
        from_student = st.selectbox("From Student", ["Student1", "Student2"])
        to_student = st.selectbox("To Student", [s for s in ["Student1", "Student2"] if s != from_student])
        max_amount = system.accounts[from_student].frozen_balance
        amount = st.number_input("Amount", min_value=1, max_value=max_amount) if max_amount > 0 else 0

        if st.button("Transfer Scholarship"):
            tx_hash = system.transfer_scholarship(from_student, to_student, amount)
            if tx_hash:
                st.success(f"Successfully transferred {amount} from {from_student} to {to_student}. Transaction Hash: {tx_hash}")
            else:
                st.error("Failed to transfer scholarship. Insufficient frozen funds.")

    elif action == "Admin View":
        st.header("All Transactions")
        transactions = system.get_all_transactions()
        st.table(pd.DataFrame(transactions))

if __name__ == "__main__":
    main()
