# scripts/
from ape import accounts, project

def main():
    account = accounts.load("meta_wallet")
    aggregator_address ="0x56a43EB56Da12C0dc1D972ACb089c06a5dEF8e69" # BTC-USD price feed address
    contract = account.deploy(project.PriceConsumer, aggregator_address)
    print(f"Contract deployed at: {contract.address}")


if __name__ == "__main__":
    main()
