import pandas as pd

mtcars_short = dataset.loc[:, ['model','mpg', 'hp', 'wt']]

# 1 mpg = 0.43 kpl
mtcars_short ['kpl'] = mtcars_short ['mpg'] * 0.43

# Metric tons
mtcars_short ['wt'] = mtcars_short ['wt'] * 0.454
