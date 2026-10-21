---
name: data
description: Enterprise data engineering: SQL performance tuning, automated data cleaning, dbt/Dataform pipelines, and schema mapping. Use on 'data', 'sql', 'bigquery', 'dbt', 'database', 'pipeline', or German: 'daten', 'datenbank', 'abfrage', 'datenbereinigung', 'schema-mapping'.
---

# Data: SQL, Pipelines & Cloud Analytics

An enterprise standard for high-performance SQL, data transformations (dbt/Dataform), and robust schema mapping.

## Trigger-Keywords / Aufruf

- **English:** `data`, `sql`, `bigquery`, `dbt`, `dataform`, `pipeline`, `schema`
- **Deutsch:** `daten`, `datenbank`, `abfrage`, `datenbereinigung`, `schema-mapping`, `analytik`

---

## 1. High-Performance SQL Optimization

- **Prune Early:** Filter rows with `WHERE` and select only necessary columns before joins. Never use `SELECT *`.
- **Partitioning & Clustering:** Always filter by partition/cluster keys to prevent expensive full-table scans.
- **Join Hygiene:** Join smaller dimension tables against larger fact tables; avoid cartesian cross-joins.
- **Window Functions:** Use window functions (`ROW_NUMBER()`, `DENSE_RANK()`) over costly self-joins.

---

## 2. Modular Data Pipelines (dbt / Dataform)

- `stg_` (Staging): Clean raw ingested data with uniform column types and names.
- `int_` (Intermediate): Business logic aggregations and joins.
- `fct_` / `dim_` (Marts): Curated fact and dimension tables ready for reporting.
- Enforce `not_null`, `unique`, and referential integrity tests on all primary keys.

---

## 3. Schema Mapping & Migration Manifesto

Before migrating datasets:

1. Document source-to-target field mappings with explicit type casting.
2. Define transformation logic for null, missing, or malformed records.
3. Validate row counts and checksums post-migration.
