# Ethcash: Ethereum-based Scholarship System

## Overview

Ethcash is an Ethereum-based scholarship management system designed to facilitate the issuance and spending of scholarships using zero-knowledge proofs (ZKP). This application ensures secure transactions while maintaining privacy and integrity.

## Features

- **Scholarship Issuance**: Admin can issue scholarships to students.
- **Spending Control**: Students can spend their scholarships only on approved vendors and for educational purposes.
- **Zero-Knowledge Proofs**: Transactions use ZKPs to enhance privacy and security.
- **Transaction Tracking**: View all account transactions in real-time.

## Architecture

The project is structured into multiple modules for clarity:

- `zk_proof.py`: Contains the `EnhancedZKProof` class for generating and verifying zero-knowledge proofs.
- `ethereum_account.py`: Contains the `EthereumAccount` class to manage accounts and transactions.
- `ethereum_scholarship_system.py`: Contains the `EthereumScholarshipSystem` class that manages the scholarship logic.
- `app.py`: The main Streamlit application that provides the user interface.

## Installation

To run this project, ensure you have Python installed on your machine. Then, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
