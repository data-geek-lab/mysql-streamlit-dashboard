import random

def generate_insight(df):
    if df.empty:
        return "No data available to analyze."

    top_product = df.groupby("product")["total_sales"].sum().idxmax()
    total = df["total_sales"].sum()
    avg_order = df["total_sales"].mean()

    options = [
        f"💰 Total sales in this dataset: **${total:,.2f}**",
        f"🔥 Best-selling product: **{top_product}**",
        f"📦 Average order value: **${avg_order:,.2f}**",
        f"💡 Try focusing your marketing on **{top_product}**, it's performing best!"
    ]
    return random.choice(options)
