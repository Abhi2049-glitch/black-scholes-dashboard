# black-scholes-dashboard
This is my first quant project.
⚡ Interactive Black-Scholes Option Pricing DashboardA real-time financial dashboard that calculates European Option Prices using the Black-Scholes-Merton (BSM) model. It allows users to visualize how different market parameters (like volatility and time decay) impact option values.🌟 FeaturesReal-Time Calculations: Instantly computes Call and Put premiums.Dynamic Visualizations: Includes an interactive Heatmap to visualize the relationship between Spot Price and Volatility.User-Friendly Interface: Built with Streamlit for easy parameter adjustments via sliders.📂 Project Structureblack-scholes-dashboard/
├── app.py                # The main application code (Streamlit + Math logic)
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
🚀 Quick Start1. Clone the Repositorygit clone [https://github.com/YOUR_USERNAME_HERE/black-scholes-dashboard.git](https://github.com/YOUR_USERNAME_HERE/black-scholes-dashboard.git)
cd black-scholes-dashboard
2. Install Dependenciespip install -r requirements.txt
3. Run the Appstreamlit run app.py
The application will open automatically in your browser at http://localhost:8501.🧮 The Math Behind the ModelThis project implements the closed-form solution for pricing European options:$$C = S N(d_1) - K e^{-rT} N(d_2)$$Where:$S$ = Current Stock Price$K$ = Strike Price$r$ = Risk-free Interest Rate$T$ = Time to Maturity (Years)$\sigma$ = Volatility (Standard Deviation)
