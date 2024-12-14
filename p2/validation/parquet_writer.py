import pyarrow as pa
import pyarrow.parquet as pq

class SignalStore:
    def save_batch(self, df: pd.DataFrame, path: str):
        table = pa.Table.from_pandas(df)
        pq.write_table(table, path, compression='snappy')