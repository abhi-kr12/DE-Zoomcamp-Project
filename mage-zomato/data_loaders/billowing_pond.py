if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pyarrow as pa
import pyarrow.parquet as pq
import gcsfs

@data_loader
def load_data(*args, **kwargs):

    url = "gs://zomato_bucket_20240321180838/zomato"
    fs = gcsfs.GCSFileSystem()

    files = ["gs://" + path for path in fs.glob(url + "/city_listed_in-*")]
    ds = pq.ParquetDataset(files, filesystem=fs)
    df = ds.read().to_pandas()

    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
