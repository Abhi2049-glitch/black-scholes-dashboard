import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# ==========================================
# 1. The Logic (Black-Scholes Class)
# ==========================================
class BlackScholes:
    def __init__(self, S, K, T, r, sigma):
        self.S = S        # Underlying Price
        self.K = K        # Strike Price
        self.T = T        # Time to Expiry (years)
        self.r = r        # Risk-Free Rate
        self.sigma = sigma # Volatility

    def _calculate_d1_d2(self):
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return d1, d2

    def price(self, option_type='call'):
        d1, d2 = self._calculate_d1_d2()
        if option_type == 'call':
            return self.S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        else:
            return self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)

# ==========================================
# 2. The Dashboard (Streamlit UI)
# ==========================================
st.set_page_config(page_title="Black-Scholes Option Pricer", layout="wide")

st.title("⚡ Interactive Black-Scholes Simulator")
st.markdown("Play with the sliders to see how option prices react to volatility and time.")

# --- Sidebar Inputs ---
st.sidebar.header("Market Parameters")
current_price = st.sidebar.slider("Current Asset Price ($)", 50, 200, 100)
strike_price  = st.sidebar.slider("Strike Price ($)", 50, 200, 100)
time_to_expiry = st.sidebar.slider("Years to Expiry", 0.01, 2.0, 1.0)
volatility    = st.sidebar.slider("Volatility (Sigma)", 0.01, 1.0, 0.2)
interest_rate = st.sidebar.number_input("Risk-Free Interest Rate", 0.0, 0.2, 0.05)

# --- Calculations ---
model = BlackScholes(current_price, strike_price, time_to_expiry, interest_rate, volatility)
call_price = model.price('call')
put_price = model.price('put')

# --- Display Prices ---
col1, col2 = st.columns(2)
with col1:
    st.metric(label="CALL Option Price", value=f"${call_price:.2f}")
with col2:
    st.metric(label="PUT Option Price", value=f"${put_price:.2f}")

# --- Heatmap Visualization ---
st.subheader(f"Call Price Heatmap (Strike: ${strike_price})")

# Generate Heatmap Data
# We create a matrix of prices based on a range of Spot Prices and Volatilities
spot_range = np.linspace(current_price * 0.5, current_price * 1.5, 10)
vol_range = np.linspace(volatility * 0.5, volatility * 1.5, 10)

prices = np.zeros((len(vol_range), len(spot_range)))

for i, vol in enumerate(vol_range):
    for j, spot in enumerate(spot_range):
        bs_temp = BlackScholes(spot, strike_price, time_to_expiry, interest_rate, vol)
        prices[i, j] = bs_temp.price('call')

# Plotting the Heatmap
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(prices, 
            xticklabels=np.round(spot_range, 1), 
            yticklabels=np.round(vol_range, 2), 
            annot=True, 
            fmt=".1f", 
            cmap="viridis", 
            ax=ax)
ax.set_xlabel("Spot Price")
ax.set_ylabel("Volatility")
ax.invert_yaxis() # Standard convention: Low vol at bottom
st.pyplot(fig)