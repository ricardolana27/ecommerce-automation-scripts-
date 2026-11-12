# 🛒 Shopify Inventory & Order Automation

An automated Python pipeline designed to eliminate manual spreadsheet handling for Shopify store owners. This script fetches real-time product and inventory data via the Shopify REST API, cleans raw JSON payloads, and exports ready-to-use operational CSV reports.

## 🎯 Business Problem & Solution
* **The Bottleneck:** Store managers often spend hours manually exporting, filtering, and formatting inventory spreadsheets to identify low-stock items.
* **The Solution:** A lightweight Python script that automates data extraction and formatting in seconds, reducing human error and saving operational hours.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Libraries:** `requests` (API calls), `pandas` (Data manipulation & cleaning), `python-dotenv` (Security/Credentials)
* **Integration:** Shopify Admin REST API
* **Deployment:** Ready for scheduled cloud execution (GitHub Actions / Cron jobs)

## ⚙️ Key Features
* **Automated Extraction:** Connects securely to the Shopify API to pull active products and current stock levels.
* **Data Transformation:** Flattens nested JSON responses into structured Pandas DataFrames.
* **Low-Stock Flagging:** Automatically filters items below a defined threshold and exports a clean `.csv` report.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd your-repo-name
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Rename `.env.example` to `.env` and add your Shopify credentials:
   ```env
   SHOPIFY_STORE_URL=://myshopify.com
   SHOPIFY_ACCESS_TOKEN=your_admin_api_token
   ```

4. **Execute the script:**
   ```bash
   python main.py
   ```

## 📊 Output Example
*(Dica: Cole aqui um print ou GIF mostrando o terminal rodando e a tabela CSV gerada)*

---
**Developed by Ricardo Lana** | [LinkedIn](https://www.linkedin.com/in/ricardo-lana/) • [Email](mailto:ricardosimass99@gmail.com)
