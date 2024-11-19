# Testing Speed Differences between Pandas, Spark and Polars

In this project, we are going to test the speed of Pandas, Spark, Polars using the NYC Yellow Taxi dataset for 2022. The whole year data set has a shape `(39_656_098, 19)` and consist of 12 parquet files, one for each month of the year. We will be performing an aggregate of the data based on 

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jrcas/testing-data-manipulation-tools.git
   cd testing-data-manipulation-tools
    ```
2. Setup a virtual environment and activate it (optional but recommended)

    ```bash
    python -m venv .venv
    source venv/bin/activate  # For Linux/Mac
    activate /.venv/Scripts/Activate.ps1   # For Windows PowerShell
    ```

3. Install dependencies from the `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Downloading the data

For this test we are going to be downloading the NYC yellow taxi data from 2022. Included in this repository is the `download.py` file that will automatically create the `data` folder in the working directory and download 12 parquet files.

While in the environment, run:

```bash
python downloads.py
 ```

## Testing

Once the data is downloaded, you can run the `comparison.ipynb`. It uses the `%%timeit` command on the notebooks we can time how long it takes each framework to read the files, do the aggregations and then save it to parquet.

## Results

After running the test we get the following times:

1. Polars:   `453 ms ± 58.4 ms`
2. Spark:    `513 ms ± 57.7 ms`
3. Pandas:   `6.12 s ± 107 ms`

The bulk of the time of these operations is reading the data into memory while the aggregation is pretty quick. 

The reason for this improvement in performance is that Pandas processes data row by row or chunk by chunk in a single thread. It is limited by the GIL.

Polars uses a columnar format and lazy loading allowing for optimization of queries before calling the data. Polars is written in Rust and uses PyArrow for vectorized computations making it faster.

Spark is optimized for distributed computing for large datasets. It is built to use a master node to delegate tasks to the worker nodes which can be different machines or clusters. This lets it process data in parallel making it a good choice for large datasets.