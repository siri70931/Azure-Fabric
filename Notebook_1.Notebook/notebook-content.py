# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# # Sales order data exploration
# Use this notebook to explore sales order data

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/2019.csv")
# df now is a Spark DataFrame containing CSV data from "Files/2019.csv".
display(df.limit(100))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
