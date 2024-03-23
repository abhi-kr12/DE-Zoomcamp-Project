if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data.columns = ['url','address','name','online_order','book_table','rate','votes','phone','location',
    'restaurant_type','dish_liked','cuisines','approx_cost','reviews_list','menu_item','type_listed_in','city_listed_in']
    data['city_listed_in'] = data['city_listed_in'].str.replace(' ','_')
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
