#This approach uses pandas which is a little faster than the basic approach but consumes memory storage.
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return result_df[['product_id']]