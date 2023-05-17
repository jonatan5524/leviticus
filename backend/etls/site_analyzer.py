import pyspark.sql.functions as F
from pyspark.sql import Window
from pyspark.sql import SparkSession


class siteAnalyzer:
    def _extract(self):
        self._connections = SparkSession.builder.getOrCreate().read.parquet(
            "oci://bucket-20230517-1923@idydrpfy5bgb/connections.parquet"
        )

    def _transform(self):
        self._connections = self._connections.withColumn(
            "tf-normalized",
            F.size(
                F.collect_set("sourceIp").over(
                    Window.partitionBy(
                        F.col("sourceIp").isin(["10.0.1.3", "10.0.1.6"]), "destIp"
                    )
                )
            )
            / F.size(
                F.collect_set("sourceIp").over(
                    Window.partitionBy(
                        F.col("sourceIp").isin(["10.0.1.3", "10.0.1.6"]),
                    )
                ),
            ),
        )

        self._connections = self._connections.withColumn(
            "df-normalized",
            F.size(F.collect_set("sourceIp").over(Window.partitionBy("destIp")))
            / F.size(F.collect_set("sourceIp").over(Window.partitionBy())),
        )

        self._connections = self._connections.withColumn(
            "score", F.sqrt((1 - F.col("df-normalized")) * F.col("tf-normalized"))
        )

        self._res = self._connections.groupby(
            (F.col("score") * 100).cast("integer")
        ).count()

        self._connections.show(20, False)
        self._res.show(100, False)

    def _load(self):
        pass


def main():
    sa = siteAnalyzer()

    sa._extract()
    sa._transform()
    sa._load()


main()
