import pandas as pd
from ecommerce_etl.transform import add_total_amount

def test_total_amount():
    df = pd.DataFrame({
        "quantity": [2, 3],
        "unit_price": [10.0, 5.0]
    })

    df = add_total_amount(df)
    assert df["total_amount"].tolist() == [20.0, 15.0]
