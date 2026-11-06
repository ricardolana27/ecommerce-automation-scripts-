import os
import json
import requests
import pandas as pd

# ---------------------------------------------------------
# Configuration & API Credentials
# ---------------------------------------------------------
SHOPIFY_STORE_URL = "https://your-store-name.myshopify.com/admin/api/2024-01"
ACCESS_TOKEN = "shpat_xxxxxxxxxxxxxxxxxxxxxxxx"

headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": ACCESS_TOKEN
}

def fetch_shopify_orders():
    """
    Fetches recent orders from the Shopify API and processes
    the payload into a clean Pandas DataFrame.
    """
    endpoint = f"{SHOPIFY_STORE_URL}/orders.json?status=any&limit=50"
    
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        orders_data = response.json().get('orders', [])
        
        processed_orders = []
        for order in orders_data:
            processed_orders.append({
                'Order ID': order.get('id'),
                'Created At': order.get('created_at'),
                'Customer Email': order.get('email'),
                'Total Price': order.get('total_price'),
                'Financial Status': order.get('financial_status'),
                'Fulfillment Status': order.get('fulfillment_status')
            })
            
        df = pd.DataFrame(processed_orders)
        print(f"Successfully processed {len(df)} orders.")
        return df

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Shopify API: {e}")
        return None

if __name__ == "__main__":
    orders_df = fetch_shopify_orders()
    if orders_df is not None:
        # Save output to CSV for automated sync operations
        orders_df.to_csv("shopify_orders_sync.csv", index=False)
        print("Data sync complete. Saved to shopify_orders_sync.csv")
