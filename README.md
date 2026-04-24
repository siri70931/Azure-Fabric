# Azure-Fabric

Microsoft Fabric end-to-end project containing multiple Fabric artifacts such as Dataflows, Pipelines, Lakehouse, Warehouse, Eventstream, Eventhouse, Notebooks, Dashboards, and Reflex.

### Project Objective:

Build a complete data platform in Microsoft Fabric to ingest, process, analyze, and visualize stock market data using both batch and real-time pipelines.

---

# Artifact Descriptions

| Item Name                             | Type          | Description                                                                                                  |
| ------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------ |
| **Dataflow_1.Dataflow**               | Dataflow      | Used for no-code ETL transformations such as cleaning stock/sales/raw files before loading into Lakehouse.   |
| **Delta Tables.Notebook**             | Notebook      | PySpark notebook to create and manage Delta Tables in Fabric Lakehouse. Used for ACID storage and analytics. |
| **Eventhouse_Stock.Eventhouse**       | Eventhouse    | Real-time analytics database to store streaming stock tick data using KQL.                                   |
| **Ingest_Sales_Data.CopyJob**         | Copy Job      | Batch ingestion pipeline to copy sales/stock CSV or SQL data into Lakehouse/Warehouse.                       |
| **KustoQueryWorkbench_1.KQLQueryset** | KQL Queryset  | Used to run KQL queries against Eventhouse for stock trend analysis.                                         |
| **Load_Data.DataPipeline**            | Data Pipeline | Orchestration pipeline to automate ingestion, transformation, and loading processes.                         |
| **Model_Warehouse.Warehouse**         | Warehouse     | SQL-based enterprise data warehouse for reporting and structured analytics.                                  |
| **Monitoring_sample**                 | Monitoring    | Used to monitor pipeline runs, refresh history, job success/failure logs.                                    |
| **Notebook_1.Notebook**               | Notebook      | PySpark notebook for transformations, feature engineering, aggregations.                                     |
| **RTISample.Eventhouse**              | Eventhouse    | Real-Time Intelligence sample database.                                                                      |
| **RTISample.Eventstream**             | Eventstream   | Captures real-time streaming data from APIs/devices/stock feeds.                                             |
| **RTISample.KQLDashboard**            | Dashboard     | Dashboard built using KQL visuals for live monitoring.                                                       |
| **RTISample.KQLQueryset**             | Queryset      | KQL queries for stream analysis.                                                                             |
| **RTISample.Reflex**                  | Reflex        | Trigger-based automation (send alerts when stock price crosses threshold).                                   |
| **RTISample.Report**                  | Report        | Power BI report for stock KPIs and trends.                                                                   |
| **Shipping Activator.Reflex**         | Reflex        | Event-based notifications/workflows.                                                                         |
| **Sireesha_Lakehouse.Lakehouse**      | Lakehouse     | Central data lake storing raw, silver, and curated stock/sales data.                                         |
| **Stock Dashboard.KQLDashboard**      | Dashboard     | Live stock market dashboard using Eventhouse data.                                                           |
| **stock_data.Eventstream**            | Eventstream   | Streams live stock prices into Eventhouse/Lakehouse.                                                         |                                     |

# Complete Project Architecture

```text
Stock API / CSV / SQL Data
        ↓
Eventstream + Copy Job
        ↓
Lakehouse (Raw Data)
        ↓
Notebook / Dataflow Transformation
        ↓
Delta Tables
        ↓
Warehouse / Eventhouse
        ↓
Power BI Dashboard / KQL Dashboard
        ↓
Reflex Alerts
```

---

* Built end-to-end stock analytics solution using Microsoft Fabric.
* Ingested batch and streaming data using Copy Jobs and Eventstream.
* Developed PySpark notebooks for transformations and Delta tables.
* Created Lakehouse and Warehouse models.
* Built real-time KQL dashboards and Power BI reports.
* Implemented Reflex alerts for threshold-based notifications.
