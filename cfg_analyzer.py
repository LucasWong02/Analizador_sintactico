# Define las reglas de la gramática
cfg = {
    "S": ["floatdcl id", "intdcl id", "id assign Expr", "print id"],
    "Expr": ["id", "id Operator Expr", "inum", "fnum"],
    "Operator": ["plus", "minus", "multiply", "divide"]
}

# Detectar no terminales inaccesibles
def find_unreachable(cfg, start_symbol):
    reachable = set()
    worklist = [start_symbol]

    while worklist:
        current = worklist.pop()
        if current in reachable:
            continue
        reachable.add(current)
        for production in cfg.get(current, []):
            for symbol in production.split():
                if symbol in cfg:
                    worklist.append(symbol)

    return set(cfg.keys()) - reachable

# Detectar no terminales que no generan cadenas terminales
def find_non_generating(cfg):
    generating = set()
    worklist = []

    for nt, productions in cfg.items():
        if all(all(symbol not in cfg for symbol in production.split()) for production in productions):
            generating.add(nt)

    while True:
        updated = False
        for nt, productions in cfg.items():
            if nt not in generating and any(
                all(symbol in generating or symbol not in cfg for symbol in production.split())
                for production in productions
            ):
                generating.add(nt)
                updated = True

        if not updated:
            break

    return set(cfg.keys()) - generating

# Análisis
start_symbol = "S"
print("No terminales inaccesibles:", find_unreachable(cfg, start_symbol))
print("No terminales que no generan cadenas terminales:", find_non_generating(cfg))
