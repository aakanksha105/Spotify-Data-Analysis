import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient
from datetime import datetime, timezone

client = MongoClient('mongodb://localhost:27017/')
db = client['Nosql_Project']
collection = db['Spotify']

class MainPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("NoSQL Project")
        self.master.state('zoomed')  

        self.heading_label = tk.Label(master, text="Project 2", font=("Times New Roman", 24, "bold"), fg="dark blue")
        self.heading_label.pack(pady=15)

        self.subheading_label = tk.Label(master, text="Spotify Data Analysis", font=("Times New Roman", 24, "italic bold"),
                                         fg="dark green")
        self.subheading_label.pack(pady=15)

        button_names = [
            "Query 1: Analyze artist names and track names on the basis of streams and colabs in the year 2022",
            "Query 2: Analyze the previous and current week’s rank of track in the year 2022",
            "Query 3: Analyze the tracks based on audio features and streams for country Argentina",
            "Query 4: Analyze track names based on popularity on charts for each artist genre for year 2021 to 2022",
        ]

        self.buttons = []
        for i, button_text in enumerate(button_names, start=1):
            button = tk.Button(master, text=button_text, command=lambda i=i: self.button_action(i),
                               font=("Cambria", 16))
            button.pack(pady=10)
            self.buttons.append(button)

    def button_action(self, query_number):
        if query_number == 1:
            result = self.run_query1()
            self.show_result_window_query1(result, query_number)
        elif query_number == 2:
            result = self.run_query2()
            self.show_result_window_query2(result, query_number)
        elif query_number == 3:
            result = self.run_query3()
            self.show_result_window_query3(result, query_number)
        elif query_number == 4:
            result = self.run_query4()
            self.show_result_window_query4(result, query_number)
        
        elif query_number == 0:  
            self.master.destroy()  


    def run_query1(self):
       
        pipeline = [
            {
                '$match': {
                    'release_date': {
                        '$gte': datetime(2022, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                        '$lt': datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
                    },
                    'collab': 0
                }
            }, {
                '$group': {
                    '_id': {
                        'track_name': '$track_name',
                        'artist_names': '$artist_names'
                    },
                    'total_streams': {
                        '$sum': '$streams'
                    }
                }
            }, {
                '$sort': {
                    'total_streams': -1
                }
            }, {
                '$limit': 20
            }, {
                '$project': {
                    '_id': 0,
                    'track_name': '$_id.track_name',
                    'artist_names': '$_id.artist_names',
                    'total_streams': 1
                }
            }
        ]
        return list(collection.aggregate(pipeline))


    def run_query3(self):
        
        pipeline = [
            {
                '$match': {
                    'country': 'Argentina'
                }
            }, {
                '$sort': {
                    'streams': -1
                }
            }, {
                '$group': {
                    '_id': '$track_name',
                    'max_streams': {
                        '$max': '$streams'
                    },
                    'max_danceability': {
                        '$max': '$danceability'
                    },
                    'max_energy': {
                        '$max': '$energy'
                    },
                    'max_loudness': {
                        '$max': '$loudness'
                    },
                    'max_valence': {
                        '$max': '$valence'
                    },
                    'max_speechiness': {
                        '$max': '$speechiness'
                    },
                    'max_liveness': {
                        '$max': '$liveness'
                    }
                }
            }, {
                '$project': {
                    '_id': 0,
                    'track_name': '$_id',
                    'max_streams': 1,
                    'max_danceability': 1,
                    'max_energy': 1,
                    'max_loudness': 1,
                    'max_valence': 1,
                    'max_speechiness': 1,
                    'max_liveness': 1
                }
            }, {
                '$sort': {
                    'max_streams': -1
                }
            }, {
                '$limit': 10
            }
        ]
        return list(collection.aggregate(pipeline))

    def run_query2(self):
       
        pipeline = [
    {
        '$match': {
            'week': {
                '$gte': datetime(2022, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                '$lt': datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            }
        }
    }, {
        '$group': {
            '_id': {
                'track_name': '$track_name',
                'artist_names': '$artist_names'
            },
            'current_rank': {
                '$min': '$rank'
            },
            'previous_rank': {
                '$min': '$previous_rank'
            }
        }
    }, {
        '$match': {
            'previous_rank': {
                '$gt': 0
            }
        }
    }, {
        '$project': {
            '_id': 0,
            'track_name': '$_id.track_name',
            'artist_names': '$_id.artist_names',
            'previous_rank': 1,
            'current_rank': 1
        }
    }, {
        '$sort': {
            'previous_rank': 1
        }
    },{
                '$limit': 20
            }
]
        return list(collection.aggregate(pipeline))

    def run_query4(self):
        pipeline = [
    {
        '$match': {
            'week': {
                '$gte': datetime(2021, 4, 14, 0, 0, 0, tzinfo=timezone.utc), 
                '$lte': datetime(2022, 4, 14, 0, 0, 0, tzinfo=timezone.utc)
            }
        }
    }, {
        '$group': {
            '_id': '$artist_genre', 
            'maxWeekOnChart': {
                '$max': '$weeks_on_chart'
            }, 
            'trackName': {
                '$first': '$track_name'
            }, 
            'weekOnChart': {
                '$first': '$weeks_on_chart'
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'artistGenre': '$_id', 
            'trackName': 1, 
            'weekOnChart': 1
        }
    }, {
        '$limit': 20
    }
]



        return list(collection.aggregate(pipeline))

    def show_result_window_query1(self, result, query_number):
        result_window = tk.Toplevel(self.master)
        result_window.geometry("{0}x{1}+0+0".format(result_window.winfo_screenwidth(), result_window.winfo_screenheight()))
        result_window.title(f"Query {query_number} Result")

        back_button = tk.Button(result_window, text="Back to Main Page", command=result_window.destroy,
                                font=("Cambria", 12))
        back_button.pack(anchor=tk.NW, padx=10, pady=10)

        result_label = tk.Label(result_window, text=f"Query {query_number} Result:",
                                font=("Times New Roman", 22, "bold"), fg="dark blue")
        result_label.pack(pady=5)

        tree = ttk.Treeview(result_window, columns=('Sr. No.', 'Track Name', 'Artist Names', 'Total Streams'), show="headings")
        tree.heading('#1', text='Sr. No.')
        tree.heading('#2', text='Track Name')
        tree.heading('#3', text='Artist Name')
        tree.heading('#4', text='Number of Streams')

        tree.column('#1', width=80, anchor=tk.CENTER)
        tree.column('#2', width=250, anchor=tk.CENTER)
        tree.column('#3', width=250, anchor=tk.CENTER)
        tree.column('#4', width=250, anchor=tk.CENTER)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Times New Roman", 16, "bold"))
        style.configure("Treeview", font=("Cambria", 14))  
        style.configure("Treeview", rowheight=35)  

        for i, entry in enumerate(result, start=1):
            tree.insert('', 'end', values=(i, entry['track_name'], entry['artist_names'], entry['total_streams']))

        tree.pack(pady=(10, 20), padx=10)  

    def show_result_window_query2(self, result, query_number):
        result_window = tk.Toplevel(self.master)
        result_window.geometry("{0}x{1}+0+0".format(result_window.winfo_screenwidth(), result_window.winfo_screenheight()))
        result_window.title(f"Query {query_number} Result")

        back_button = tk.Button(result_window, text="Back to Main Page", command=result_window.destroy,
                                font=("Cambria", 12))
        back_button.pack(anchor=tk.NW, padx=5, pady=5)

        result_label = tk.Label(result_window, text=f"Query {query_number} Result:",
                                font=("Times New Roman", 22, "bold"), fg="dark blue")
        result_label.pack(pady=10)

        column_headers = ['Sr. No.', 'Track Name', 'Artist Name', 'Current Rank', 'Previous Rank']

        tree = ttk.Treeview(result_window, columns=column_headers, show="headings")
        for header in column_headers:
            tree.heading(header, text=header)

        tree.column('#1', width=80, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#2', width=250, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#3', width=250, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#4', width=150, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#5', width=150, anchor=tk.CENTER, stretch=tk.NO)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Times New Roman", 16, "bold"))
        style.configure("Treeview", font=("Cambria", 14))  
        style.configure("Treeview", rowheight=35)  

        for i, entry in enumerate(result, start=1):
            tree.insert('', 'end', values=(i, entry['track_name'], entry['artist_names'],
                                           entry['current_rank'], entry['previous_rank']))

        tree.pack(pady=(10, 20), padx=10)  


    def show_result_window_query3(self, result, query_number):
        result_window = tk.Toplevel(self.master)
        result_window.geometry("{0}x{1}+0+0".format(result_window.winfo_screenwidth(), result_window.winfo_screenheight()))
        result_window.title(f"Query {query_number} Result")

        back_button = tk.Button(result_window, text="Back to Main Page", command=result_window.destroy,
                                font=("Cambria", 12))
        back_button.pack(anchor=tk.NW, padx=5, pady=5)

        result_label = tk.Label(result_window, text=f"Query {query_number} Result:",
                                font=("Times New Roman", 22, "bold"), fg="dark blue")
        result_label.pack(pady=10)

        column_headers = ['Sr. No.', 'Track Name', 'Max Streams', 'Max Danceability', 'Max Energy',
                           'Max Loudness', 'Max Valence', 'Max Speechiness', 'Max Liveness']

        tree = ttk.Treeview(result_window, columns=column_headers, show="headings")
        for header in column_headers:
            tree.heading(header, text=header)

        tree.column('#1', width=80, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#2', width=180, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#3', width=150, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#4', width=150, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#5', width=150, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#6', width=150, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#7', width=150, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#8', width=150, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#9', width=150, anchor=tk.CENTER, stretch=tk.NO)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Times New Roman", 16, "bold"))
        style.configure("Treeview", font=("Cambria", 14))  
        style.configure("Treeview", rowheight=35)  

        for i, entry in enumerate(result, start=1):
            tree.insert('', 'end', values=(i, entry['track_name'], entry['max_streams'], entry['max_danceability'],
                                           entry['max_energy'], entry['max_loudness'], entry['max_valence'],
                                           entry['max_speechiness'], entry['max_liveness']))

        tree.pack(pady=(10, 20), padx=10)  

    def show_result_window_query4(self, result, query_number):
        result_window = tk.Toplevel(self.master)
        result_window.geometry("{0}x{1}+0+0".format(result_window.winfo_screenwidth(), result_window.winfo_screenheight()))
        result_window.title(f"Query {query_number} Result")

        back_button = tk.Button(result_window, text="Back to Main Page", command=result_window.destroy,
                            font=("Cambria", 12))
        back_button.pack(anchor=tk.NW, padx=5, pady=5)

        result_label = tk.Label(result_window, text=f"Query {query_number} Result:",
                            font=("Times New Roman", 22, "bold"), fg="dark blue")
        result_label.pack(pady=10)

        column_headers = ['Sr. No.', 'Track Name', 'Weeks on Chart', 'Artist Genre']

        tree = ttk.Treeview(result_window, columns=column_headers, show="headings")
        for header in column_headers:
            tree.heading(header, text=header)

        tree.column('#1', width=80, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#2', width=250, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#3', width=150, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('#4', width=250, anchor=tk.CENTER, stretch=tk.NO)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Times New Roman", 16, "bold"))
        style.configure("Treeview", font=("Cambria", 14)) 
        style.configure("Treeview", rowheight=35)  

        for i, entry in enumerate(result, start=1):
            tree.insert('', 'end', values=(i, entry['trackName'], entry['weekOnChart'], entry['artistGenre']))

        tree.pack(pady=(10, 20), padx=10)  



if __name__ == "__main__":
    root = tk.Tk()
    app = MainPage(master=root)
    app.mainloop()
