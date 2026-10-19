---
id: "3b241426-eb50-8103-88f3-c42030d188de"
title: "Generate Data Loading Scripts"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate Data Loading Scripts

**Category:** Coding

## Description

Create a scalable data pipeline with this AI prompt, focusing on memory efficiency and real-world data challenges.

## What This Prompt Does

● Develops a comprehensive, production-ready data loading script in Python.
● Focuses on memory efficiency and scalability for handling large datasets.
● Implements robust error handling and logging for real-world data challenges.

## Prompt

```text
Adopt the role of an expert data engineer and Python developer who specializes in scalable data pipeline architecture, following the proven methodologies from Wes McKinney's "Python for Data Analysis." Your primary objective is to generate a comprehensive, production-ready data loading script that prioritizes memory efficiency, handles real-world data challenges, and scales beyond toy datasets in a complete Python script format. You understand that modern data ingestion requires sophisticated approaches including chunking for large files, explicit type specification for memory optimization, lazy loading strategies, graceful handling of encoding issues and missing values, automatic file type detection, robust error handling for corrupt data, and real-time progress feedback. Design the script to be modular, maintainable, and capable of handling multiple data formats while providing detailed logging and performance metrics. Take a deep breath and work on this problem step-by-step.

Begin by analyzing the user's data specifications to determine optimal loading strategies. Implement automatic file type detection using file extensions and content sniffing. Create memory-efficient loading functions using pandas chunking, appropriate dtypes, and lazy evaluation where possible. Build comprehensive error handling for common issues like encoding problems, malformed data, and missing files. Include progress bars and logging for large file processing. Optimize memory usage through strategic column selection, data type optimization, and garbage collection. Provide data quality checks and summary statistics upon successful loading.

#INFORMATION ABOUT ME:
My data format(s): [INSERT YOUR DATA FORMATS - e.g., CSV, JSON, Parquet, Excel]
My approximate data size: [INSERT DATA SIZE - e.g., 100MB, 5GB, 50GB]
My data location: [INSERT DATA LOCATION - e.g., local files, S3, database, URLs]
My available memory: [INSERT AVAILABLE RAM - e.g., 8GB, 16GB, 32GB]
My specific data challenges: [INSERT ANY KNOWN ISSUES - e.g., encoding problems, missing values, mixed types]

MOST IMPORTANT!: Provide your output as a complete, executable Python script with detailed comments, proper error handling, and modular functions that can be easily customized for different data scenarios.
```
