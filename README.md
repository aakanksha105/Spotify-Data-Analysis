# Spotify Data Analysis using Python, MongoDB & Tkinter

A desktop-based data analysis application built using Python, MongoDB, and Tkinter to analyze Spotify streaming data through NoSQL aggregation pipelines and an interactive graphical user interface.

---

## Overview

This project demonstrates how large-scale Spotify streaming data can be analyzed using MongoDB aggregation frameworks and presented through a Python-based desktop application. Users can execute predefined analytical queries via an interactive GUI and view results in structured tabular formats.

The application focuses on extracting insights related to artist and track popularity, streaming trends, ranking changes, audio features, and genre-based performance across regions and time periods.

---

## Key Highlights
- Implemented advanced MongoDB aggregation pipelines for analytical queries
- Built an interactive desktop GUI using Tkinter
- Analyzed large-scale Spotify chart data stored in a NoSQL database
- Enabled query execution and result visualization through a user-friendly interface
- Integrated database analytics with a Python application layer

---

## Tech Stack
- Programming Language: Python 3  
- Database: MongoDB (NoSQL)  
- GUI Framework: Tkinter  
- Database Driver: PyMongo  
- Data Handling: MongoDB Aggregation Framework  
- Date Handling: datetime, timezone  

---

## Dataset

The MongoDB collection contains structured Spotify chart data with attributes including:
- Track and artist metadata (track_name, artist_names, artist_genre)
- Streaming and ranking metrics (streams, rank, previous_rank, weeks_on_chart)
- Temporal and regional attributes (release_date, week, country)
- Audio features such as danceability, energy, loudness, valence, speechiness, and liveness
- Collaboration indicators

---

## Queries Implemented

### Top Tracks and Artists (2022, Non-Collaborative)
- Filters tracks released in 2022
- Excludes collaborative tracks
- Aggregates total streams per track and artist
- Displays the top 20 most-streamed tracks

### Rank Comparison (Previous vs Current Week – 2022)
- Analyzes weekly chart data for 2022
- Compares previous rank versus current rank
- Identifies ranking trends for top-performing tracks

### Audio Feature Analysis (Argentina)
- Filters tracks streamed in Argentina
- Analyzes audio features including danceability, energy, loudness, valence, speechiness, and liveness
- Displays the top 10 tracks based on maximum streams

### Genre-Based Chart Popularity (2021–2022)
- Groups tracks by artist genre
- Identifies tracks with maximum weeks on the chart
- Analyzes genre popularity trends over time

---

## User Interface

- Full-screen desktop application
- Interactive buttons to execute analytical queries
- Results displayed in tabular format using Treeview
- Simple navigation between views
- Clean layout optimized for data readability

---

## Installation & Setup

### Prerequisites
- Python 3.x
- MongoDB installed and running locally
- Spotify dataset imported into MongoDB

### Install Dependencies
pip install pymongo

### MongoDB Configuration
- Connection URI: mongodb://localhost:27017/
- Database Name: Nosql_Project
- Collection Name: Spotify

Ensure the dataset is loaded before running the application.

### Run the Application
python main.py

---

## Learning Outcomes
- Hands-on experience with MongoDB aggregation pipelines
- Designing desktop applications using Tkinter
- Integrating NoSQL databases with Python applications
- Performing analytical queries on real-world datasets
- Translating data insights into interactive visual outputs

---

## Author
Aakanksha Bhondve


