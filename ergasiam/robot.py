# robot_mid.py
from collections import deque
import sys # Θα χρειαστεί για την ανάγνωση παραμέτρων

ROWS, COLS = 10, 10 #αναγράφουμε ότι μέσα στο αρχείο txt υπάρχουν 10 γραμμές και 10 στήλες
EMPTY, OBST, ITEM = ".", "#", "*"

def load_world(path: str) -> list[list[str]]:
    """
    Φορτώνει τον Κόσμο από το αρχείο κειμένου.
    Ελέγχει τις διαστάσεις και τα σύμβολα.
    """
    world = [] 
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                # Διαβάζει τη γραμμή, αφαιρεί περιττά κενά και χωρίζει τα σύμβολα
                row = line.strip().split()
                if row:
                    world.append(row)
    except FileNotFoundError:
        print(f"Σφάλμα: Δεν βρέθηκε το αρχείο {path}")
        sys.exit(1)

    # Έλεγχος διαστάσεων (πρέπει να είναι 10x10)
    assert len(world) == ROWS and all(len(r) == COLS for r in world), "Λάθος διαστάσεις world.txt (Πρέπει να είναι 10x10)."

    # Έλεγχος έγκυρων συμβόλων
    valid = {EMPTY, OBST, ITEM}
    for r in world:
        for s in r:
            assert s in valid, f"Άκυρο σύμβολο βρέθηκε: {s}. Έγκυρα: {valid}"

    return world

def print_world(world: list[list[str]], r: int, c: int) -> None:
    """
    Εμφανίζει την τρέχουσα κατάσταση του Κόσμου, 
    συμπεριλαμβανομένης της θέσης του ρομπότ (R).
    r: τρέχουσα γραμμή ρομπότ, c: τρέχουσα στήλη ρομπότ
    """
    for i in range(ROWS):
        line = []
        for j in range(COLS):
            # Αν η θέση (i, j) είναι η θέση του ρομπότ (r, c), τυπώνουμε 'R', αλλιώς το περιεχόμενο του κελιού
            line.append("R" if (i, j) == (r, c) else world[i][j])
        print(" ".join(line))
    print()
def in_bounds(r: int, c: int) -> bool:
    """
    Ελέγχει αν η θέση (r, c) βρίσκεται μέσα στα όρια του πλέγματος.
    """
    return 0 <= r < ROWS and 0 <= c < COLS 
def neighbors(world, r: int, c: int):
    """
    Επιστρέφει τις συντεταγμένες των γειτονικών κελιών 
    στα οποία μπορεί να κινηθεί το ρομπότ (όχι εμπόδια).
    """
    # Πιθανές κινήσεις: Πάνω, Κάτω, Αριστερά, Δεξιά [cite: 139]
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc [cite: 140]
        # Ελέγχουμε αν είναι εντός ορίων ΚΑΙ δεν είναι εμπόδιο [cite: 141]
        if in_bounds(nr, nc) and world[nr][nc] != OBST:
            yield nr, nc [cite: 141]