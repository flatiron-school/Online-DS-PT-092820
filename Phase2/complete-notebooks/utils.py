from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split


def fit_evaluate_model(model, X, y, seed=42, scale=False):
    """
    Performs a train-test split, 
    Evaluates a model, based on training and testing predictions
    In terms of R2, Mean Absolute Error, and Root Mean Squared Error
    --
    Inputs:
     - model - Instantiated sklearn model
     - X - pandas dataframe, containing all independent variables
     - y - pandas series, the target variable
     - seed - integer, for the random_state of the train test split
     - scale - boolean, whether to scale the data with a MinMax Scaler

    Outputs:
     - model - fit sklearn model
     - y_train_preds - predictions for the training set
     - y_test_preds - predictions for the test set
    """
    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, 
                                                    random_state=seed)

    if scale==True:
        scaler = MinMaxScaler()

        scaler.fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)

    model.fit(X_train, y_train)

    y_train_preds = model.predict(X_train)
    y_test_preds = model.predict(X_test)

    print(f"Train R2: {r2_score(y_train, y_train_preds):.3f}")
    print(f"Test R2: {r2_score(y_test, y_test_preds):.3f}")
    print("---")
    print(f"Train MAE: {mean_absolute_error(y_train, y_train_preds):.3f}")
    print(f"Test MAE: {mean_absolute_error(y_test, y_test_preds):.3f}")
    print("---")
    print(f"Train RMSE: {mean_squared_error(y_train, y_train_preds, squared=False):.3f}")
    print(f"Test RMSE: {mean_squared_error(y_test, y_test_preds, squared=False):.3f}")

    return model, y_train_preds, y_test_preds

def evaluate_model(y_train, y_test, y_train_preds, y_test_preds):
    """
    Evaluates a model, based on training and testing predictions
    In terms of R2, Mean Absolute Error, and Root Mean Squared Error
    --
    Inputs:
     - y_train - true target for training set (output of train/test split)
     - y_test - true target for test set
     - y_train_preds - predicted target for training set (output of model.predict)
     - y_test_preds - predicted target for test set
    """
    print(f"Train R2: {r2_score(y_train, y_train_preds):.3f}")
    print(f"Test R2: {r2_score(y_test, y_test_preds):.3f}")
    print("---")
    print(f"Train MAE: {mean_absolute_error(y_train, y_train_preds):.3f}")
    print(f"Test MAE: {mean_absolute_error(y_test, y_test_preds):.3f}")
    print("---")
    print(f"Train RMSE: {mean_squared_error(y_train, y_train_preds, squared=False):.3f}")
    print(f"Test RMSE: {mean_squared_error(y_test, y_test_preds, squared=False):.3f}")
