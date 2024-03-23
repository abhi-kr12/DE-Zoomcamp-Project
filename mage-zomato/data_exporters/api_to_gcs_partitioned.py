import pyarrow
import pyarrow.parquet as pq
import os
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "my_creds.json"

bucket_name="zomato_bucket_20240321180838"
object_key="zomato-zoomcamp"

table_name = 'zomato'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    table = pyarrow.Table.from_pandas(data)
    
    gcs = pyarrow.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols = ['city_listed_in'],
        filesystem=gcs
    )

