# 🛒 Automação de Inventário e Encomendas (Shopify)

Pipeline automatizado em Python desenvolvido para eliminar o tratamento manual de folhas de cálculo em lojas online Shopify. O script extrai dados de produtos e níveis de stock em tempo real através da API REST da Shopify, limpa os ficheiros JSON brutos e exporta relatórios operacionais em CSV prontos a utilizar.

## 🎯 Problema de Negócio & Solução
* **O Problema:** Gestores de e-commerce perdem horas a exportar, filtrar e formatar manualmente folhas de cálculo para identificar produtos com stock baixo ou atualizar encomendas.
* **A Solução:** Um script leve em Python que automatiza toda a extração, limpeza e formatação dos dados em segundos, reduzindo falhas humanas e poupando horas semanais de trabalho operacional.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Bibliotecas:** `requests` (chamadas à API), `pandas` (manipulação e limpeza de dados), `python-dotenv` (gestão segura de credenciais)
* **Integração:** Shopify Admin REST API
* **Automação:** Preparado para execução agendada na cloud (GitHub Actions / Cron jobs)

## ⚙️ Funcionalidades Principais
* **Extração Automatizada:** Ligação segura à API da Shopify para recolher produtos ativos e níveis atuais de stock.
* **Tratamento de Dados (ETL):** Transformação de respostas JSON complexas em DataFrames estruturados com Pandas, com tratamento de campos vazios para evitar falhas de execução.
* **Alerta de Stock Baixo:** Filtragem automática de artigos abaixo do limite definido e exportação de um relatório limpo em `.csv`.

## 🚀 Como Executar Localmente

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com
   cd ecommerce-automation-scripts-
   ```

2. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar as variáveis de ambiente:**
   Renomeie o ficheiro `.env.example` para `.env` e adicione as credenciais da sua loja Shopify:
   ```env
   SHOPIFY_STORE_URL=https://myshopify.com
   SHOPIFY_ACCESS_TOKEN=seu_token_de_acesso_admin
   ```

4. **Executar o script:**
   ```bash
   python main.py
   ```

---
**Desenvolvido por Ricardo Lana** | [LinkedIn](https://www.linkedin.com/in/ricardo-lana/) • [E-mail](mailto:ricardosimass99@gmail.com)
