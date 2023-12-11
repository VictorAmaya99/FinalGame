import json

class GameDataHandler:
    def __init__(self, filename="game_data.json"):
        self.filename = filename
        self.data = self.load_game_data()

    def load_game_data(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Creating a new data structure.")
            return {"level_1": [], "level_2": [], "level_3": []}
        except Exception as e:
            print(f"Error loading data: {e}")
            return {"level_1": [], "level_2": [], "level_3": []}

    def save_game_data(self, level, lives, score, elapsed_time):
        data = {
            "lives": lives,
            "score": score,
            "elapsed_time": elapsed_time
        }

        self.data[f"level_{level}"].append(data)

        try:
            with open(self.filename, "w") as file:
                json.dump(self.data, file, indent=4)
            print(f"Game data for level {level} saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def show_loaded_data(self):
        print("Loaded game data:")
        print(self.data)
