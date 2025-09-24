# main.py
from helpers import load_scores, save_scores
from game_classes import Player, Game

#fil för highscore - finns den ej skapas den vid save
file_name = "highscore.txt"

def show_scoreboard(player: Player, dealer: Player):
    print(f"\n--- Highscore ---")
    print(f"Spelare vinster: {player.wins}")
    print(f"Dealer vinster : {dealer.wins}\n")

def display_menu():
    print("\n--- Blackjack Light ---")
    print("1. Spela runda")
    print("2. Visa ställning")
    print("3. Spara & Avsluta")

def main():
    # 1) Läs in highscore (skapar inte fil här; den skapas vid save om den saknas)
    player_wins, dealer_wins = load_scores(file_name)

    # 2) Initiera spelare & game, skickar in in wins från fil som ska uppdateras
    player = Player("Spelare", is_dealer=False, wins=player_wins)
    dealer = Player("Dealer", is_dealer=True, wins=dealer_wins)
    game = Game(player, dealer)

    print("Välkommen! Målet är att komma så nära 21 som möjligt utan att gå över.")
    show_scoreboard(player, dealer)

    while True:
        display_menu()
        choice = input("Välj ett alternativ (1-3): ").strip()
        if choice not in ("1", "2", "3"):
            print("Ogiltigt val. Välj 1, 2 eller 3.")
            continue

        if choice == "1":
            result = game.play_round()
            show_scoreboard(player, dealer)
        elif choice == "2":
            show_scoreboard(player, dealer)
        else:
            # Spara och avsluta
            save_scores(file_name, player.wins, dealer.wins)
            print(f"Highscore sparad i '{file_name}'. Hej då!")
            break

if __name__ == "__main__":
    main()
