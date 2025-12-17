# 🎵 Spotify Data Analysis using Python, MongoDB & Tkinter

A desktop-based data analysis application built using **Python**, **MongoDB**, and **Tkinter** to analyze Spotify streaming data through advanced NoSQL aggregation queries and an interactive graphical user interface.

🔗 **GitHub Repository:**  
https://github.com/aakanksha105/Spotify-Data-Analysis

---

## 📌 Project Overview

This project demonstrates the use of **NoSQL (MongoDB)** aggregation pipelines combined with a **Python-based GUI** to analyze large-scale Spotify datasets.  
Users can execute predefined analytical queries through buttons and visualize results in structured tables.

The application focuses on:
- Artist and track popularity
- Streaming trends
- Ranking changes
- Audio feature analysis
- Genre-based chart performance

---

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Database:** MongoDB (NoSQL)
- **GUI Framework:** Tkinter
- **Database Driver:** PyMongo
- **Data Handling:** MongoDB Aggregation Framework
- **Date Handling:** `datetime`, `timezone`

---

## 📂 Dataset Description

The MongoDB collection (`Spotify`) contains structured Spotify chart data with fields such as:

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
- Audio features:
  - `danceability`
  - `energy`
  - `loudness`
  - `valence`
  - `speechiness`
  - `liveness`
- `collab`

---

## 📊 Features & Queries Implemented

### ✅ Query 1: Top Tracks & Artists (2022, Non-Collaborative)
- Filters tracks released in **2022**
- Excludes collaborations
- Aggregates total streams per track and artist
- Displays **Top 20 most streamed tracks**

---

### ✅ Query 2: Rank Comparison (Previous vs Current Week – 2022)
- Analyzes weekly chart data for **2022**
- Compares `previous_rank` vs `current_rank`
- Displays ranking trends for top tracks

---

### ✅ Query 3: Audio Feature Analysis (Argentina)
- Filters tracks streamed in **Argentina**
- Analyzes audio features:
  - Danceability
  - Energy
  - Loudness
  - Valence
  - Speechiness
  - Liveness
- Displays **Top 10 tracks** based on maximum streams

---

### ✅ Query 4: Genre-Based Chart Popularity (2021–2022)
- Groups tracks by `artist_genre`
- Finds tracks with **maximum weeks on chart**
- Analyzes genre popularity trends over time

---

## 🖥️ User Interface (GUI)

- Full-screen desktop application
- Interactive buttons for each query
- Results displayed in tabular format using `Treeview`
- Easy navigation with **Back to Main Page** option
- Clean, readable fonts and spacing for data visualization

---

## ⚙️ Installation & Setup

### 1️⃣ Prerequisites
Make sure you have:
- Python 3.x
- MongoDB installed and running locally
- Spotify dataset imported into MongoDB

---

### 2️⃣ Install Required Python Libraries

```bash
pip install pymongo
