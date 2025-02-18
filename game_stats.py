class GameStats:
    """Track stats for Alien Invasion game."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistiscs that can change during the game."""
        self.ships_left = self.settings.ship_limit