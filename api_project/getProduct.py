import requests

def get_products():
    url = "https://api.freeapi.app/api/v1/public/randomproducts"
    response = requests.get(url)
    data = response.json()

    if data.get("success") and "data" in data:
        # Extract top-level info
        # current_page_items = data["data"]["currentPageItems"]
        products = data["data"]["data"]  # List of products

        # Collect first 5 products (or less)
        first_five = products[:5]

        return first_five
    else:
        raise Exception("Failed to fetch product data")

def main():
    try:
        products = get_products()
        # print(f"\nTotal items on current page: {size}")
        print("\n--- Showing First 5 Products ---\n")

        for product in products:
            print(f"Title: {product['title']}")
            print(f"Category: {product['category']}")
            print(f"Price: {product['price']}")
            print(f"Thumbnail: {product['thumbnail']}")
            print("-" * 50)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
