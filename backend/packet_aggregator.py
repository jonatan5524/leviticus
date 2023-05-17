from etl import ETL

import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType


class packetAggregator(ETL):

    def _extract(self):
        # Create a spark session
        spark = SparkSession.builder.appName('Empty_Dataframe').getOrCreate()
        
        # Create an empty RDD with empty schema
        self._data = spark.createDataFrame(data = [], schema = StructType([]))


    def _transform(self):
        self._data.show(20, False)

    def _load(self):
        pass
