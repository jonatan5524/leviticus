from abc import ABCMeta, abstractclassmethod
import pyspark.sql.functions as F
from pyspark.sql import SparkSession

class ETL(ABCMeta):

    @abstractclassmethod
    def _extract(self):
        pass

    @abstractclassmethod
    def _transform(self):
        pass

    @abstractclassmethod
    def _load(self):
        pass

    def run(self):
        self._extract()
        self._transform()
        self._load()
