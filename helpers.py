#Funktioner för att läsa och spara poängställning i fil.

def load_scores(path: str) -> tuple[int, int]:
    #Läser två heltal från fil: 'player_wins dealer_wins'.
    #Om filen saknas eller är trasig: returnera (0, 0).
    #Skapar inte filen här – den skapas vid save().
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
    except FileNotFoundError:
        return 0, 0
    except OSError as e:
        print(f"Kunde inte läsa filen: {e}")
        return 0, 0

    parts = content.split()
    try:
        return int(parts[0]), int(parts[1])
    except (IndexError, ValueError):
        # fel i  fil -> börja om från 0,0
        return 0, 0


def save_scores(path: str, player_wins: int, dealer_wins: int) -> None:
    #Sparar två heltal i formatet: 'player_wins dealer_wins'
    #Overwrite är avsiktligt (vi sparar aktuella totalsummor).

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"{player_wins} {dealer_wins}\n")
    except OSError as e:
        print(f"Kunde inte spara filen: {e}")