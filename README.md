# Spotify Data Analysis using Python, MongoDB, and Tkinter

A NoSQL data analysis project that analyzes Spotify chart and streaming data using MongoDB aggregation pipelines and a Python Tkinter desktop interface. The application allows users to run predefined analytical queries and view results in structured table format.

## Project Overview

This project analyzes Spotify tracks, artists, genres, rankings, streams, and audio features using a MongoDB collection. It was developed as a NoSQL database project to demonstrate how semi-structured music chart data can be queried and explored using MongoDB aggregation pipelines.

The application provides a Tkinter-based graphical user interface where users can select one of four analysis queries and view the results in tabular form.

## Key Features

- Connected Python application to MongoDB using PyMongo.
- Implemented MongoDB aggregation pipelines for analytical queries.
- Built a Tkinter desktop GUI to run queries interactively.
- Displayed query results using Tkinter Treeview tables.
- Analyzed Spotify data by streams, rankings, audio features, countries, genres, and chart performance.
- Included project proposal and report documentation explaining the analysis goals and outcomes.

## Tech Stack

- **Language:** Python
- **Database:** MongoDB
- **Database Driver:** PyMongo
- **GUI Framework:** Tkinter
- **Querying:** MongoDB Aggregation Framework
- **Data Handling:** datetime, timezone
- **Dataset Source:** Spotify dataset from Kaggle

## Project Structure

```text
Spotify-Data-Analysis/
├── README.md
├── spotify.py
├── spotify.ipynb
└── reports/
    ├── NoSQL-Report.pdf
    └── 2-Page-Proposal.pdf


## Dataset

The project uses Spotify chart data with fields such as:

- `track_name`
- `artist_names`
- `artist_genre`
- `streams`
- `rank`
- `previous_rank`
- `weeks_on_chart`
- `release_date`
- `week`
- `country`
- `danceability`
- `energy`
- `loudness`
- `valence`
- `speechiness`
- `liveness`
- `collab`

## Analyses Implemented

### 1. Top Tracks and Artists in 2022

This query analyzes tracks released in 2022, filters non-collaborative tracks, groups records by track and artist, calculates total streams, and returns the top streamed tracks.

### 2. Rank Comparison in 2022

This query compares previous and current weekly rankings for tracks in 2022 and displays ranking movement along with track and artist details.

### 3. Audio Feature Analysis for Argentina

This query filters Spotify chart data for Argentina and analyzes highly streamed tracks based on audio features such as danceability, energy, loudness, valence, speechiness, and liveness.

### 4. Genre-Based Chart Popularity from 2021 to 2022

This query analyzes artist genres and identifies tracks that remained on Spotify charts for the maximum number of weeks between 2021 and 2022.

## User Interface

The Tkinter application includes:

- A full-screen main page
- Four query buttons for different analyses
- Separate result windows for each query
- Tabular output using Treeview
- Back navigation from result windows to the main page

## MongoDB Configuration

The application connects to MongoDB using:

```text
Connection URI: mongodb://localhost:27017/
Database Name: Nosql_Project
Collection Name: Spotify
```

Make sure MongoDB is running and the Spotify dataset is imported into the `Spotify` collection before running the application.

## Installation

Install the required Python package:

```bash
pip install pymongo
```

Tkinter is included with most standard Python installations.

## Run the Application

```bash
python spotify.py
```

## Learning Outcomes

Through this project, I gained hands-on experience in:

- Designing NoSQL analytical queries using MongoDB aggregation pipelines.
- Connecting Python applications to MongoDB using PyMongo.
- Building a desktop-based GUI using Tkinter.
- Displaying database query results in structured table views.
- Analyzing Spotify streaming, ranking, audio feature, country, and genre data.
- Translating analytical questions into database queries and user-facing outputs.

## Future Improvements

- Add dataset import instructions or sample data.
- Add screenshots of the Tkinter interface and query outputs.
- Add error handling for missing MongoDB connection or empty query results.
- Add CSV export functionality for query results.

## Author

Aakanksha Bhondve

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
python spotify.py

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


