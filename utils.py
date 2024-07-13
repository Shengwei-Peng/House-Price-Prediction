import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def loadData(
        train_path: str,
        test_path: str,
        valid: bool = True
        ) -> pd.DataFrame:

    train = pd.read_csv(f"{train_path}/training_data_processed.csv")
    test = pd.read_csv(f"{test_path}/public_dataset_processed.csv")

    train_y = train["單價"]
    train_x = train.drop(["單價", "ID"], axis=1)
    test_x = test.drop(["ID"], axis=1)

    train_len = len(train_x)
    all_x = pd.concat([train_x, test_x], axis=0)

    encoder = LabelEncoder()
    for i in all_x:
        if all_x[i].dtypes == "object":
            all_x[i] = encoder.fit_transform(all_x[i])

    train_x = all_x[:train_len]
    test_x = all_x[train_len:]

    if valid:
        train_x, valid_x, train_y, valid_y = train_test_split(
            train_x,
            train_y,
            train_size=0.8,
            random_state=0,
            )
        return train_x, train_y, valid_x, valid_y, test_x
    else:
        return train_x, train_y, test_x

def Train(
        model: BaseEstimator,
        train_x: pd.DataFrame,
        train_y: pd.DataFrame,
        valid_x: pd.DataFrame = None,
        valid_y: pd.DataFrame = None,
        valid: bool = True,
        ) -> BaseEstimator:

    model.fit(train_x, train_y)
    if valid:
        score = model.score(valid_x, valid_y)
        valid_pred = model.predict(valid_x)
        mape = mean_absolute_percentage_error(valid_y, valid_pred)
        print(f"Score: {score:.2%}\nMAPE: {mape:.2%}\n")

    return model

def Test(
        model: BaseEstimator,
        test_x: pd.DataFrame,
        test_path: str
        ) -> None:

    test_y = model.predict(test_x)
    df = pd.read_csv(f"{test_path}/public_submission_template.csv")
    df["predicted_price"] = test_y
    df.to_csv(f"{test_path}/submission.csv", index=False)
