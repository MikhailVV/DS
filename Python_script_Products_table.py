import pandas as pd
products_short = dataset.loc[:,['ID', 'Product Code', 'Product Name', 'Description','Standard Cost', 'List Price']] 
products_short['Description'] = products_short ['Product Code'] + ' - ' +  products_short ['Product Name']




