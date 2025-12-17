🎵 Spotify Data Analysis

📌 Project Overview
This project is a desktop-based data analysis application built using Python, MongoDB, and Tkinter to analyze Spotify music trends.
The application connects to a MongoDB database containing Spotify chart data and allows users to execute predefined analytical queries through an interactive graphical user interface.
The goal of this project is to demonstrate NoSQL data modeling, aggregation pipelines, and UI-driven analytics using real-world music streaming data.

🛠️ Tech Stack
Programming Language: Python
Database: MongoDB (NoSQL)
Database Driver: PyMongo
GUI Framework: Tkinter & ttk
Data Processing: MongoDB Aggregation Framework
Date Handling: datetime, timezone

📂 Dataset Description
The MongoDB collection stores Spotify chart data with fields such as:
track_name
artist_names
artist_genre
streams
rank
previous_rank
weeks_on_chart
release_date
week
audio_features (danceability, energy, loudness, valence, etc.)
country
collab

🖥️ Application Features
Full-screen Tkinter desktop UI
Button-driven execution of analytical queries
Result visualization using structured tables (Treeview)
MongoDB aggregation pipelines for efficient data processing
Clean separation of query logic and UI logic

📊 Implemented Queries
Query 1: Top Tracks & Artists (2022)
Analyzes artist names and track names based on total streams
Filters non-collaborative tracks
Displays Top 20 most-streamed tracks released in 2022

Query 2: Rank Comparison (2022)
Compares current rank vs previous rank
Identifies ranking changes for tracks in 2022
Displays Top 20 results sorted by previous rank

Query 3: Audio Feature Analysis (Argentina)
Analyzes tracks streamed in Argentina
Computes maximum values for:
Streams
Danceability
Energy
Loudness
Valence
Speechiness
Liveness
Displays Top 10 tracks by streams

Query 4: Popularity by Genre (2021–2022)
Analyzes track popularity across artist genres
Uses weeks on chart as a popularity metric
Displays top genres with representative tracks

🧩 Project Structure

Spotify-Data-Analysis/
│
├── main.py                 # Tkinter UI + MongoDB queries
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies

⚙️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/aakanksha105/Spotify-Data-Analysis.git
cd Spotify-Data-Analysis

2️⃣ Install Dependencies

pip install pymongo

3️⃣ Start MongoDB
Ensure MongoDB is running locally:

mongodb://localhost:27017/

4️⃣ Import Spotify Dataset
Load your Spotify dataset into MongoDB:

Database: Nosql_Project
Collection: Spotify

5️⃣ Run the Application

python main.py

🧠 Learning Outcomes
Hands-on experience with MongoDB aggregation pipelines
Building desktop analytics applications using Tkinter
Implementing real-world NoSQL queries
Designing interactive UI components for data visualization
Applying database-driven analytics concepts

🚀 Future Enhancements
Add dynamic filtering options (year, country, genre)
Export query results to CSV
Integrate charts using Matplotlib or Seaborn
Improve UI styling and responsiveness
Add pagination for large result sets

👩‍💻 Author
Aakanksha Bhondve
