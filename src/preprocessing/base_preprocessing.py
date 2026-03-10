import pandas as pd
class BasePreprocess: 
    def __init__(self, var_to_process, target):
        self.raw_predictors_vars = pd.read_excel(var_to_process)
        self.raw_predictors_vars = (self.raw_predictors_vars
                       .query("posible_predictora == 'si'")
                        .variable
                        .tolist())
        self.target_var = target

    def fit(self, data):
        df = pd.read_csv(data)
        self.train_X_data = df[self.raw_predictors_vars]
        self.train_Y_data = df[self.target_var]