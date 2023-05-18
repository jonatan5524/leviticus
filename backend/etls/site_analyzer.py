import pyspark.sql.functions as F
from pyspark.sql import Window
from pyspark.sql import SparkSession


class siteAnalyzer:
    def _extract(self):
        self._connections = SparkSession.builder.getOrCreate().read.csv(
            r"oci://bucket-20230517-1923@idydrpfy5bgb/*/*/*[.]data[.]gz", sep="\t"
        )

    def _transform(self):
        self._connections.show(30, False)
        exit(1)

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

        self._res = (
            self._connections.filter(F.col("score") > 0.5).select("destIp").distinct()
        )

        self._res = self._res.select(
            F.col("DestIp").alias("site"), F.lit("Gambling").alias("category")
        )

    def _load(self):
        self._res.write.format("oracle").option(
            "adbId",
            "ocid1.autonomousdatabase.oc1.iad.anuwcljri5rgbiaanm4gtavqnr37v4l5kkjzgxyii2iqbsfkpumj7c625qca",
        ).option("dbtable", "categories").option("user", "Team").option(
            "password", "P@ssw0rd123?"
        ).save()


def main():
    sa = siteAnalyzer()

    sa._extract()
    sa._transform()
    sa._load()


main()
