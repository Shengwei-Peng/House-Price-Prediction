from utils import loadData, Train, Test
from catboost import CatBoostRegressor

def main() -> None:

    train_path = "./data/30_Training Dataset_V2"
    test_path = "./data/30_Public Dataset_Public Sumission Template_v2"
    model = CatBoostRegressor(iterations=1e6,
                              depth=10,
                              border_count=512,
                              )

    train_x, train_y, test_x = loadData(train_path, test_path, valid=False)
    model = Train(model, train_x, train_y, valid=False)
    Test(model, test_x, test_path)


if __name__ == '__main__':
    main()
