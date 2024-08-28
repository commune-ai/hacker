
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np

class Predictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.le = LabelEncoder()

    def predict(self, data):
        # Prepare the data
        X = data[['exchange', 'volume']]
        y = data['price']

        X['exchange'] = self.le.fit_transform(X['exchange'])

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Make predictions
        predictions = self.model.predict(X_test)

        # Prepare the results
        results = []
        for i, prediction in enumerate(predictions):
            results.append({
                'symbol': data.iloc[X_test.index[i]]['symbol'],
                'predicted_price': prediction,
                'actual_price': y_test.iloc[i]
            })

        return results

