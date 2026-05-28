"""
Matplotlib Exercises – Company Sales Data
Module 1 – Beginner Deliverable
Generative AI & Data Science Pathway

Data source:
https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ── Load the dataset ─────────────────────────────────────────────────────────
URL = "https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv"
# Load from URL (or fall back to local copy if needed)
try:
    df = pd.read_csv(URL)
except Exception:
    df = pd.read_csv("company_sales_data.csv")

MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# ════════════════════════════════════════════════════════════════════════════
# Exercise 1 – Total Profit (Line Plot)
# ════════════════════════════════════════════════════════════════════════════
fig1, ax1 = plt.subplots(figsize=(10, 5))

ax1.plot(
    MONTHS,
    df["total_profit"],
    color="#2563EB",
    linewidth=2.5,
    marker="o",
    markersize=7,
    markerfacecolor="white",
    markeredgewidth=2,
    label="Total Profit",
)

# Annotate each data point
for i, val in enumerate(df["total_profit"]):
    ax1.annotate(
        f"{val:,}",
        xy=(i, val),
        xytext=(0, 10),
        textcoords="offset points",
        ha="center",
        fontsize=7.5,
        color="#1e3a5f",
    )

ax1.set_title("Total Profit of All Months", fontsize=15, fontweight="bold", pad=15)
ax1.set_xlabel("Month", fontsize=11)
ax1.set_ylabel("Profit (₦)", fontsize=11)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax1.set_xticks(range(12))
ax1.set_xticklabels(MONTHS)
ax1.grid(axis="y", linestyle="--", alpha=0.5)
ax1.legend(fontsize=10)
plt.tight_layout()
plt.savefig("exercise1_total_profit.png", dpi=150)
print("Exercise 1 saved → exercise1_total_profit.png")
plt.show()


# ════════════════════════════════════════════════════════════════════════════
# Exercise 2 – Bathing Soap vs Facewash (Subplot)
# ════════════════════════════════════════════════════════════════════════════
fig2, (ax2, ax3) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
fig2.suptitle("Bathing Soap vs Facewash – Monthly Sales", fontsize=15, fontweight="bold")

# --- Top subplot: Bathing Soap ---
ax2.plot(
    MONTHS,
    df["bathingsoap"],
    color="#DC2626",
    linewidth=2.5,
    marker="s",
    markersize=7,
    markerfacecolor="white",
    markeredgewidth=2,
    label="Bathing Soap",
)
ax2.fill_between(range(12), df["bathingsoap"], alpha=0.12, color="#DC2626")
ax2.set_ylabel("Units Sold", fontsize=10)
ax2.set_title("Bathing Soap", fontsize=12)
ax2.grid(axis="y", linestyle="--", alpha=0.5)
ax2.legend(fontsize=10)
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

# --- Bottom subplot: Facewash ---
ax3.plot(
    MONTHS,
    df["facewash"],
    color="#16A34A",
    linewidth=2.5,
    marker="^",
    markersize=7,
    markerfacecolor="white",
    markeredgewidth=2,
    label="Facewash",
)
ax3.fill_between(range(12), df["facewash"], alpha=0.12, color="#16A34A")
ax3.set_xlabel("Month", fontsize=11)
ax3.set_ylabel("Units Sold", fontsize=10)
ax3.set_title("Facewash", fontsize=12)
ax3.set_xticks(range(12))
ax3.set_xticklabels(MONTHS)
ax3.grid(axis="y", linestyle="--", alpha=0.5)
ax3.legend(fontsize=10)
ax3.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

plt.tight_layout()
plt.savefig("exercise2_subplot.png", dpi=150)
print("Exercise 2 saved → exercise2_subplot.png")
plt.show()
