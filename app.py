import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class StockPredictor:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def prepare_data(self):
        self.X = self.data[['Date', 'Open', 'High', 'Low', 'Volume']].values
        self.y = self.data['Close'].values

    def split_data(self):
        tscv = TimeSeriesSplit()
        for train_index, test_index in tscv.split(self.X):
            self.X_train, self.X_test = self.X[train_index], self.X[test_index]
            self.y_train, self.y_test = self.y[train_index], self.y[test_index]

    def train_model(self):
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        y_pred = self.model.predict(self.X_test)
        print('Mean Absolute Error:', metrics.mean_absolute_error(self.y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(self.y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(self.y_test, y_pred)))

    def predict_price(self, date, open_price, high, low, volume):
        predicted_price = self.model.predict([[date, open_price, high, low, volume]])
        print('Predicted closing price:', predicted_price)

if __name__ == "__main__":
    predictor = StockPredictor('historical_stock_data.csv')
    predictor.prepare_data()
    predictor.split_data()
    predictor.train_model()
    predictor.evaluate_model()
    # Replace these parameters with actual values
    predictor.predict_price(date, open_price, high, low, volume)
