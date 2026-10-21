---
name: enterprise-data-and-sql
description: Enterprise data engineering standard: SQL performance tuning, automated data cleaning, dbt/Dataform transformation pipelines, and schema mapping.
---

# Enterprise Data, SQL & Cloud Analytics

A comprehensive data engineering standard consolidating best practices for SQL performance, cloud data warehouses (BigQuery, PostgreSQL), and ETL/ELT pipelines.

## 1. High-Performance SQL Optimization
- **Prune Early**: Filter rows with `WHERE` and select only necessary columns before performing joins. Avoid `SELECT *`.
- **Partitioning & Clustering**: Always leverage partition and cluster keys to prevent expensive full-table scans.
- **Join Hygiene**: Join smaller dimension tables against larger fact tables; avoid cartesian cross-joins.
- **Window Functions**: Prefer window functions (`ROW_NUMBER()`, `DENSE_RANK()`) over self-joins.

## 2. Data Pipelines & ELT (dbt / Dataform)
- **Modular Data Modeling**:
  - `stg_` (Staging): Clean raw ingested data with uniform naming and types.
  - `int_` (Intermediate): Business logic aggregations and joins.
  - `fct_` / `dim_` (Marts): Curated fact and dimension tables for analytics.
- **Data Quality & Testing**: Enforce `not_null`, `unique`, and referential integrity tests on all primary keys.

## 3. Schema Mapping & Migration Manifesto
Before migrating data across schemas:
1. Document source-to-target field mappings with explicit type casting.
2. Define transformation logic for null, missing, or malformed records.
3. Validate row counts and checksums post-migration.
