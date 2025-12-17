# 🎵 Spotify Data Analysis

A desktop-based data analysis application built using **Python**, **MongoDB**, and **Tkinter** to analyze Spotify music trends through an interactive graphical user interface.

🔗 **GitHub Repository:**  
https://github.com/aakanksha105/Spotify-Data-Analysis

---

## 📌 Project Overview

This project is a **desktop-based data analytics application** that connects to a MongoDB database containing Spotify chart data.  
It allows users to execute predefined analytical queries using a **Tkinter-based GUI** and visualize results in structured tabular form.

The primary goal of this project is to demonstrate:
- NoSQL data modeling
- MongoDB aggregation pipelines
- Desktop UI-driven analytics
- Real-world data analysis using Spotify streaming data

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Database:** MongoDB (NoSQL)  
- **Database Driver:** PyMongo  
- **GUI Framework:** Tkinter, ttk  
- **Data Processing:** MongoDB Aggregation Framework  
- **Date Handling:** `datetime`, `timezone`

---

## 📂 Dataset Description

The MongoDB collection stores Spotify chart data with the following key fields:

- `track_name`
- `artist_names`
- `artist_genre`
- `streams`
- `rank`
- `previous_rank`
- `weeks_on_chart`
- `release_date`
- `week`
- `audio_features`
  - danceability
  - energy
  - loudness
  - valence
  - speechiness
  - liveness
- `country`
- `collab`

---

## 🖥️ Application Features

- Full-screen Tkinter desktop UI
- Button-driven execution of analytical queries
- Result visualization using `ttk.Treeview` tables
- Efficient data processing using MongoDB aggregation pipelines
- Clear separation of UI logic and query logic

---

## 📊 Implemented Queries

### **Query 1: Top Tracks & Artists (2022)**
- Analyzes artist names and track names based on **total streams**
- Filters **non-collaborative tracks**
- Displays **Top 20 most-streamed tracks released in 2022**

---

### **Query 2: Rank Comparison (2022)**
- Compares **current rank vs previous rank**
- Identifies ranking changes for tracks in 2022
- Displays **Top 20 results** sorted by previous rank

---

### **Query 3: Audio Feature Analysis (Argentina)**
- Analyzes tracks streamed in **Argentina**
- Computes maximum values for:
  - Streams
  - Danceability
  - Energy
  - Loudness
  - Valence
  - Speechiness
  - Liveness
- Displays **Top 10 tracks by streams**

---

### **Query 4: Popularity by Genre (2021–2022)**
- Analyzes track popularity across **artist genres**
- Uses **weeks on chart** as a popularity metric
- Displays top genres with representative tracks

---

## 🧩 Project Structure

