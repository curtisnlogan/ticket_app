class PublisherGamesLists:
    """
    A class relating to publishers that can you can feed args lists of games to.
    """
    def __init__(self, *args):
        self.games_list = args
    
    def __str__(self):
        return f"Games: {', '.join(self.games_list)}"
    
    def __iter__(self):
        yield from self.games_list

    def __eq__(self, other):
        return self.games_list == other.games_list

class VideoGameStore:
    """A class relating to video game stores, which you can feed args lists of games to.
    """
    def __init__(self, *args):
        self.games_list = args
    
    def __str__(self):
        return f"Games: {', '.join(self.games_list)}"
    
    def __iter__(self):
        yield from self.games_list
    
    def __eq__(self, other):
        return self.games_list == other.games_list

def main():
    bandai_namco = PublisherGamesLists("Dark Souls III", "Elden Ring")
    bandai_namco_2 = PublisherGamesLists("Elden Ring")
    my_game_store_bandai = VideoGameStore(*bandai_namco)
    for index, game in enumerate(my_game_store_bandai, 1):
        print(f"{index}: {game}")
    print(f"Bandai Namco: {my_game_store_bandai}")
    if bandai_namco == bandai_namco_2:
        print("equal")
    else:
        print("not equal")
if __name__ == "__main__":
    main()