import pandas as pd
from utils.transform import transform_data

def test_transform_logic():
    sample_data = {
        'Title': ['Cool Shirt', 'dos-image.jpeg'],
        'Price': ['$10.00', 'invalid.png'],
        'Rating': ['4.5 / 5', '4.8'],
        'Colors': ['3 Colors', '1 Color'],
        'Size': ['Size: L', 'Size: M'],
        'Gender': ['Gender: Men', 'Gender: Women']
    }
    df = pd.DataFrame(sample_data)
    result = transform_data(df)
    
    assert len(result) == 1
    assert result['Price'].iloc[0] == 160000.0
    assert result['Size'].iloc[0] == 'L'
    assert result['Colors'].iloc[0] == 3