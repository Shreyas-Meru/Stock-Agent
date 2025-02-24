import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Tool to fetch stock data
class StockTool:
    def __init__(self):
        pass
    
    def fetch_stock_data(self, symbol: str, period: str = '1d'):
        """
        Fetch stock data for the given symbol and period.
        """
        stock = yf.Ticker(symbol)
        data = stock.history(period=period)
        return data

    def plot_stock_data(self, data):
        """
        Plot stock data with closing price.
        """
        data['Close'].plot(title="Stock Closing Price Over Time")
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.grid(True)
        st.pyplot(plt)  # Display the plot in the Streamlit UI

# Agent 1: StockFetcherAgent - Fetches stock data
class StockFetcherAgent:
    def __init__(self, tool):
        self.tool = tool
    
    def fetch_data(self, symbol: str, period: str = '1y'):
        """
        Fetch stock data for a specific symbol.
        """
        st.write(f"Fetching data for {symbol}...")
        data = self.tool.fetch_stock_data(symbol, period)
        return data

# Agent 2: StockAnalyzerAgent - Analyzes stock data
class StockAnalyzerAgent:
    def __init__(self):
        pass
    
    def analyze_data(self, data):
        """
        Analyze stock data and return statistics like average, max, min.
        """
        avg_price = np.mean(data['Close'])
        max_price = np.max(data['Close'])
        min_price = np.min(data['Close'])
        return {"average": avg_price, "max": max_price, "min": min_price}

# Agent 3: StockVisualizerAgent - Visualizes stock data
class StockVisualizerAgent:
    def __init__(self, tool):
        self.tool = tool
    
    def visualize_data(self, data):
        """
        Visualize the stock data using a line chart.
        """
        st.write("Visualizing stock data...")
        self.tool.plot_stock_data(data)

# Multi-Agent System that coordinates the agents
class MultiAgentSystem:
    def __init__(self):
        self.tool = StockTool()
        self.fetcher = StockFetcherAgent(self.tool)
        self.analyzer = StockAnalyzerAgent()
        self.visualizer = StockVisualizerAgent(self.tool)
    
    def execute_task(self, symbol: str, period: str = '1y'):
        """
        Execute the multi-agent task: Fetch, Analyze, Visualize.
        """
        # Agent 1: Fetch stock data
        data = self.fetcher.fetch_data(symbol, period)
        
        if data.empty:
            st.write(f"No data available for {symbol}.")
            return
        
        # Agent 2: Analyze stock data
        analysis_result = self.analyzer.analyze_data(data)
        st.write(f"Stock Analysis for {symbol}:")
        st.write(f"Average Price: {analysis_result['average']}")
        st.write(f"Maximum Price: {analysis_result['max']}")
        st.write(f"Minimum Price: {analysis_result['min']}")
        
        # Agent 3: Visualize stock data
        self.visualizer.visualize_data(data)

# Streamlit UI for interacting with the multi-agent system
def main():
    st.title('Stock Data Fetcher, Analyzer, and Visualizer')

    # User input fields
    symbol = st.text_input('Enter Stock Symbol (e.g., AAPL, MSFT):', 'AAPL')
    period = st.selectbox('Select Time Period:', ['1d', '1mo', '1y', '5y'])

    # Initialize the multi-agent system
    multi_agent_system = MultiAgentSystem()

    # Execute the task when the button is clicked
    if st.button('Fetch, Analyze, and Visualize'):
        multi_agent_system.execute_task(symbol, period)

if __name__ == '__main__':
    main()
