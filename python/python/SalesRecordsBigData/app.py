from pyspark.sql import SparkSession

# SparkSession oluştur
spark = SparkSession.builder \
    .appName("SalesRecordsBigData") \
    .getOrCreate()

# CSV dosyasını oku
df = spark.read.csv("sales_data_sample.csv", header=True, inferSchema=True)

# Veri yapısını göster
print("Veri Yapısı (Şema):")
df.printSchema()

# İlk 5 satırı göster
print("İlk 5 Satır:")
df.show(5)
