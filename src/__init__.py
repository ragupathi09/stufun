import pandas as pd

# Define chunk size
chunk_size = 1_000_000  # adjust based on available RAM

# Initialize an empty DataFrame for aggregation
agg_result = pd.DataFrame()

# Read and aggregate in chunks
for chunk in pd.read_csv('your_large_file.csv', chunksize=chunk_size):
    # Example: group by 'category' and sum 'value'
    chunk_agg = chunk.groupby('category')['value'].sum().reset_index()

    # Merge or accumulate
    if agg_result.empty:
        agg_result = chunk_agg
    else:
        agg_result = pd.concat([agg_result, chunk_agg])
        agg_result = agg_result.group




import dask.dataframe as dd

# Read file with Dask (lazy evaluation)
df = dd.read_csv('your_large_file.csv')

# Aggregate
result = df.groupby('category')['value'].sum().compute()

print(result)
