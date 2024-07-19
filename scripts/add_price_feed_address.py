# scripts/
from ape import accounts, project

def main():
    account = accounts.load("meta_wallet")

    # Define additional price feed addresses to be added later
    # These can be any trading pair of your choice e.g;
    # ETH-USD, BNB-USD, ARB-USD, etc. Price feed addresses can be found on the following link
    # https://docs.chain.link/data-feeds/price-feeds/addresses?network=arbitrum&page=1#arbitrum-sepolia
    additional_price_feed_addresses = [
        "0x20b1061Acd37302925D9A8c3fD94eb765039dBd5",
        "0x32377717BC9F9bA8Db45A244bCE77e7c0Cc5A775",
        "0x72F48eBe69eB7f5DdA2394C9EA488e621727f8B1",
        "0xD1092a65338d049DB68D7Be6bD89d17a0929945e"
    ]
    # Define the deployed contract address
    consumer_contract_address = "0x24B71B5aA6662640375cf5E2be14EcE208FFcfDd"

    # Load the deployed contract
    contract = project.PriceConsumer.at(consumer_contract_address)

    # Add additional price feed addresses
    for addr in additional_price_feed_addresses:
        contract.addPriceFeedAddress(addr, sender=account)
        print(f"Added price feed address: {addr}")
    
    # Verify that the price feeds were set correctly
    for addr in additional_price_feed_addresses:
        price = contract.get_latest_price(addr)
        print(f"Price feed address: {addr} - Latest price: {price / 1e8}")


if __name__ == "__main__":
    main()
