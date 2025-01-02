import pickle

class GameState:
    def __init__(self, player, current_level, obstacles):
        self.player = player
        self.current_level = current_level
        self.obstacles = obstacles

    def save_state(self, file_path="game_state.pkl"):
        """Save the current game state to a file."""
        with open(file_path, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load_state(file_path="game_state.pkl"):
        """Load a previously saved game state from a file."""
        try:
            with open(file_path, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
