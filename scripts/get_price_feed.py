from ape import accounts, project,networks

def main():
    contract_address = "0x24B71B5aA6662640375cf5E2be14EcE208FFcfDd"


    # Load the deployed contract
    contract = project.PriceConsumer.at(contract_address)

    # Define the price feed address you want to fetch the price for
    price_feed_address = "0x56a43EB56Da12C0dc1D972ACb089c06a5dEF8e69"

    # Fetch and print the latest price for the specified address
    latest_price = contract.get_latest_price(price_feed_address)
    pair_description = contract.get_symbol(price_feed_address)
    print(f"Price feed for: {pair_description} - Latest price: {latest_price / 1e8}")
       

if __name__ == "__main__":
    main()

