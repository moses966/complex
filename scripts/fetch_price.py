from ape import accounts, project, networks
import sys

def main(price_feed_address):
    contract_address = "0x24B71B5aA6662640375cf5E2be14EcE208FFcfDd"

    # Load the deployed contract
    contract = project.PriceConsumer.at(contract_address)

    # Fetch and print the latest price for the specified address
    latest_price = contract.get_latest_price(price_feed_address)
    pair_description = contract.get_symbol(price_feed_address)
    print(f"Price feed for: {pair_description} - Latest price: {latest_price / 1e8}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_price_feed.py <price_feed_address>")
        sys.exit(1)

    price_feed_address = sys.argv[1]
    main(price_feed_address)
