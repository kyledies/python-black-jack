# models.py
import random

#Nedan definieras klasserna Player och Game
#Obs is_dealer används för att styra dealerns automatiska spel
#wins används för att hålla reda på antal vunna rundor
class Player:
    def __init__(self, name: str, is_dealer: bool = False, wins: int = 0):
        self.name = name
        self.is_dealer = is_dealer
        self.wins = wins #antal vunna rundor - ackumulerat mellan rundor
        self.total = 0   #totalen i pågående runda

    def reset(self):
        self.total = 0 #Nollställ totalen inför ny runda

    def hit(self) -> int:
        #Rulla en tärning (1–6) och addera till totalen. Returnerar slaget.
        roll = random.randint(1, 6)
        self.total += roll
        return roll

    #is_bust returnerar True om totalen är över 21
    def is_bust(self) -> bool:
        return self.total > 21

""" 
Game-klassen hanterar en runda av spelet mellan instanserna "spelare" och "dealer".
Logiken för dealerns automatiska val ligger i dealer_play-metoden medan spelarens val hanteras i play_round.
"""
class Game:
    def __init__(self, player: Player, dealer: Player):
        self.player = player
        self.dealer = dealer

    def dealer_play(self) -> list:
        #Dealern slår automatiskt tills minst 17.
        #Returnerar listan av dealer-slag (för utskrift).
        
        rolls = []
        while self.dealer.total < 17:
            r = self.dealer.hit()
            rolls.append(r)
            if self.dealer.is_bust():
                break
        return rolls

    def play_round(self) -> str:
        #Spelar EN runda. Returnerar 'player', 'dealer' eller 'push' - Kan användas för t.ex. tester
        #Sköter utskrift via print_func och inmatning via input_func.
        
        # Nollställ totals
        self.player.reset()
        self.dealer.reset()

        print("\n--- Ny runda ---")
        # Spelarens tur
        while True:
            print(f"Din total: {self.player.total}  | Dealer: {self.dealer.total}")
            choice = input("Vill du [r]ulla eller [s]tanna? ").strip().lower()
            if choice not in ("r", "s"):
                print("Ogiltigt val, skriv 'r' för rulla eller 's' för stanna.")
                continue

            if choice == "r":
                roll = self.player.hit()
                print(f"Du rullade: {roll}  -> Ny total: {self.player.total}")
                if self.player.is_bust():
                    print("Du gick över 21! Du förlorar denna runda.")
                    self.dealer.wins += 1
                    return "dealer"
            else:
                # Spelaren stannar -> dealer spelar
                print("\nDealern spelar...")
                dealer_rolls = self.dealer_play()
                if dealer_rolls: #false om tom lista
                    print(f"Dealer slog: {', '.join(map(str, dealer_rolls))}")
                print(f"Dealer total: {self.dealer.total}")

                
                # Avgör vinnare ("player", "dealer", "draw" används ej nedan - kan användas för tester)
                if self.dealer.is_bust():
                    print("Dealern gick över 21! Du vinner.")
                    self.player.wins += 1
                    return "player"

                # Inga busts -> jämför
                pt, dt = self.player.total, self.dealer.total
                if pt > dt:
                    print(f"Du är närmast 21 ({pt} vs {dt}). Du vinner!")
                    self.player.wins += 1
                    return "player"
                elif dt > pt:
                    print(f"Dealern är närmast 21 ({dt} vs {pt}). Du förlorar.")
                    self.dealer.wins += 1
                    return "dealer"
                else:
                    print(f"Lika! ({pt} vs {dt})")
                    return "draw"
