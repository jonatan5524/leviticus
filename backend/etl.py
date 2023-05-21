import arrow
from abc import ABC, abstractmethod
import pyspark.sql.functions as F
from pyspark.sql import SparkSession

class ETL(ABC):
    def __init__(self, start_date, end_date=arrow.get(arrow.get().format('YYYY-MM-DD')).shift(hours=1)):
        self._start_date = arrow.get(start_date)
        self._end_date = arrow.get(end_date)

    @abstractmethod
    def _extract(self):
        pass

    @abstractmethod
    def _transform(self):
        pass

    @abstractmethod
    def _load(self):
        pass

    def _run(self):
        self._extract()
        self._transform()
        self._load()
