DataLakeUtils
    This class instanciates an object to handle read/write operations on an 
    specific bucket on Amazon S3 working as a Data Lake, with folders splitted
    into the following hierarchy, compatible to Apache Hadoop filesystem:
    - schema/
        - table/
            - partition[0]/
                - partition[1]/
                    ...
                        - partition[n]/
                            - object

motor_vehicles/
|-- cars
|   `-- logical_date=2022-10-03
|       `-- account_name=yuca
|           `-- 34e40fce-444e-11ed-8e00-acde48001122.json
|-- accounts_invoices
|   `-- logical_date=2022-10-03
|       `-- account_name=yuca
|           `-- a4eb3018-4458-11ed-b0e9-acde48001122.json
`-- withdraw_conciliations
    `-- logical_date=2022-10-03
        `-- account_name=yuca
            `-- 2c0fea6c-444e-11ed-969f-acde48001122.json

# Data Lake Utility
Package to manipulate data from/into Amazon S3 using partitions compatible with Apache Hadoop filesystem.
At this moment, this package was conceived to handle JSON data only. That being said, it expects a list of dictionaries.
## Features
Convert list of dictionaries...
```python
[
    {"brand": "Ford","model": "Mustang","year": 1965},
    {"brand": "Pontiac","model": "GTO","year": 1964},
    {"brand": "Lamborghini","model": "Miura","year": 1966}
]
```
...to multi-line JSON string
```text
{"brand": "Ford","model": "Mustang","year": 1965}
{"brand": "Pontiac","model": "GTO","year": 1964}
{"brand": "Lamborghini","model": "Miura","year": 1966}
```

Manipulate data on Amazon S3 bucket based on schema, table and partitions
```
motor_vehicles/
`-- cars
    |-- brand=Ford
    |   `-- year=1965
    |       `-- 34e40fce-444e-11ed-8e00-acde48001122.json
    |-- brand=Pontiac
    |   `-- year=1964
    |       `-- a4eb3018-4458-11ed-b0e9-acde48001122.json
    `-- brand=Lamborghini
        `-- year=1966
            `-- 2c0fea6c-444e-11ed-969f-acde48001122.json
```



## How to use
This package does not slice data into partitions defined. You must handle slicing of data to write into partitions desired.
The example below will assume the following file structure:
```
motor_vehicles/
`-- cars
    `-- decade=1960s
        `-- 2c0fea6c-444e-11ed-969f-acde48001122.json
```

```python
from datalake_utils.utils import DataLake
import json

data = [
    {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1965
    },
    {
        "brand": "Pontiac",
        "model": "GTO",
        "year": 1964
    },
    {
        "brand": "Lamborghini",
        "model": "Miura",
        "year": 1966
    }
]

datalake = DataLake(
    bucket_name="vehicles",
    schema="motor_vehicles",
    table="cars",
    partitions=[
        {
            "key": "decade",
            "value": "1960s"
        }
    ],
)

datalake.append_to_s3(data)

retrieved_data = datalake.read_from_s3()
print(json.dumps(retrieved_data, indent=4))

datalake.delete_from_s3()

```