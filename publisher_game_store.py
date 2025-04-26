class PublisherGamesLists:
    """
    A class representing a publisher's list of games.
    You can initialize it with multiple game titles as arguments.
    """
    def __init__(self, *args):
        self.games_list = args
    
    def __str__(self):
        # Returns a string representation of the games list
        return f"Games: {', '.join(self.games_list)}"
    
    def __iter__(self):
        # Allows iteration over the games list
        yield from self.games_list

    def __eq__(self, other):
        # Compares two PublisherGamesLists objects for equality
        return self.games_list == other.games_list


class VideoGameStore:
    """
    A class representing a video game store's inventory.
    You can initialize it with multiple game titles as arguments.
    """
    def __init__(self, *args):
        self.games_list = args
    
    def __str__(self):
        # Returns a string representation of the store's games list
        return f"Games: {', '.join(self.games_list)}"
    
    def __iter__(self):
        # Allows iteration over the store's games list
        yield from self.games_list
    
    def __eq__(self, other):
        # Compares two VideoGameStore objects for equality
        return self.games_list == other.games_list


def main():
    # Create instances of PublisherGamesLists with games published by Bandai Namco
    bandai_namco = PublisherGamesLists("Dark Souls III", "Elden Ring")
    bandai_namco_2 = PublisherGamesLists("Elden Ring")
    
    # Create a video game store inventory using Bandai Namco's game list
    my_game_store_bandai = VideoGameStore(*bandai_namco)
    
    # Display the games in the store with their index
    for index, game in enumerate(my_game_store_bandai, 1):
        print(f"{index}: {game}")
    
    # Print the store's entire inventory
    print(f"Bandai Namco: {my_game_store_bandai}")
    
    # Compare two publisher game lists for equality
    if bandai_namco == bandai_namco_2:
        print("equal")
    else:
        print("not equal")


if __name__ == "__main__":
    main()
