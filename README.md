﻿# Stock-Agent
The Stock Agent is a multi-agent system built using Python and Streamlit to interact with financial stock data. The system includes various agents designed for specific tasks related to stock data handling:

StockFetcherAgent: This agent is responsible for fetching stock data based on a given stock symbol (such as AAPL for Apple) and a specified time period (such as 1 day, 1 month, or 1 year). It uses the yfinance library to retrieve historical stock data and outputs it in a structured format.

StockAnalyzerAgent: This agent analyzes the stock data retrieved by the StockFetcherAgent. It calculates basic statistics such as the average closing price, the highest closing price, and the lowest closing price within the specified time period, providing a quick insight into the stock's performance.

StockVisualizerAgent: This agent visualizes the stock data by creating a line chart of the stock's closing price over time. It helps the user easily spot trends or fluctuations in the stock price visually, enhancing the user's understanding of the stock's movements.

The Multi-Agent System coordinates these three agents. Upon user interaction via the Streamlit interface, the system fetches the stock data, analyzes it, and then visualizes it for the user, making it a powerful tool for quick stock analysis and visualization.

Streamlit UI
Input Fields: Users can input a stock symbol (like "AAPL" for Apple) and select a time period for analysis.
Fetch, Analyze, and Visualize Button: Upon clicking this button, the system fetches the stock data, performs analysis, and generates a plot.
Outputs: The analysis results, including average, max, and min prices, along with a graphical chart showing the stock's closing prices, are displayed within the Streamlit interface.
This tool provides users with a user-friendly platform to quickly fetch, analyze, and visualize stock performance.
