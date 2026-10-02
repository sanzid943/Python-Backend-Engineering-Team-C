IPHONES = {
    "11": {
        "year": 2019,
        "models": {
            "iPhone 11": {"price_bdt": 44000, "colors": ["Black", "Green", "Yellow", "Purple", "Red", "White"]},
            "iPhone 11 Pro": {"price_bdt": 58000, "colors": ["Space Gray", "Silver", "Gold", "Midnight Green"]},
            "iPhone 11 Pro Max": {"price_bdt": 68000, "colors": ["Space Gray", "Silver", "Gold", "Midnight Green"]}
        }
    },
    "12": {
        "year": 2020,
        "models": {
            "iPhone 12 mini": {"price_bdt": 48000, "colors": ["Black", "White", "Red", "Green", "Blue", "Purple"]},
            "iPhone 12": {"price_bdt": 56000, "colors": ["Black", "White", "Red", "Green", "Blue", "Purple"]},
            "iPhone 12 Pro": {"price_bdt": 72000, "colors": ["Graphite", "Silver", "Gold", "Pacific Blue"]},
            "iPhone 12 Pro Max": {"price_bdt": 82000, "colors": ["Graphite", "Silver", "Gold", "Pacific Blue"]}
        }
    },
    "13": {
        "year": 2021,
        "models": {
            "iPhone 13 mini": {"price_bdt": 58000, "colors": ["Starlight", "Midnight", "Blue", "Pink", "Green", "Red"]},
            "iPhone 13": {"price_bdt": 63000, "colors": ["Starlight", "Midnight", "Blue", "Pink", "Green", "Red"]},
            "iPhone 13 Pro": {"price_bdt": 88000, "colors": ["Graphite", "Gold", "Silver", "Sierra Blue", "Alpine Green"]},
            "iPhone 13 Pro Max": {"price_bdt": 99000, "colors": ["Graphite", "Gold", "Silver", "Sierra Blue", "Alpine Green"]}
        }
    },
    "14": {
        "year": 2022,
        "models": {
            "iPhone 14": {"price_bdt": 76000, "colors": ["Midnight", "Purple", "Starlight", "Red", "Blue", "Yellow"]},
            "iPhone 14 Plus": {"price_bdt": 86000, "colors": ["Midnight", "Purple", "Starlight", "Red", "Blue", "Yellow"]},
            "iPhone 14 Pro": {"price_bdt": 108000, "colors": ["Space Black", "Silver", "Gold", "Deep Purple"]},
            "iPhone 14 Pro Max": {"price_bdt": 120000, "colors": ["Space Black", "Silver", "Gold", "Deep Purple"]}
        }
    },
    "15": {
        "year": 2023,
        "models": {
            "iPhone 15": {"price_bdt": 86000, "colors": ["Black", "Blue", "Green", "Yellow", "Pink"]},
            "iPhone 15 Plus": {"price_bdt": 98000, "colors": ["Black", "Blue", "Green", "Yellow", "Pink"]},
            "iPhone 15 Pro": {"price_bdt": 122000, "colors": ["Black Titanium", "White Titanium", "Natural Titanium", "Blue Titanium"]},
            "iPhone 15 Pro Max": {"price_bdt": 140000, "colors": ["Black Titanium", "White Titanium", "Natural Titanium", "Blue Titanium"]}
        }
    },
    "16": {
        "year": 2024,
        "models": {
            "iPhone 16": {"price_bdt": 96000, "colors": ["Black", "White", "Pink", "Teal", "Ultramarine"]},
            "iPhone 16 Plus": {"price_bdt": 108000, "colors": ["Black", "White", "Pink", "Teal", "Ultramarine"]},
            "iPhone 16 Pro": {"price_bdt": 132000, "colors": ["Black Titanium", "White Titanium", "Natural Titanium", "Desert Titanium"]},
            "iPhone 16 Pro Max": {"price_bdt": 148000, "colors": ["Black Titanium", "White Titanium", "Natural Titanium", "Desert Titanium"]}
        }
    },
    "17": {
        "year": 2025,
        "models": {
            "iPhone 17": {"price_bdt": 115000, "colors": ["Midnight", "Silver", "Sage Green", "Soft Blue"]},
            "iPhone 17 Air": {"price_bdt": 128000, "colors": ["Space Gray", "Silver", "Sky Blue"]},
            "iPhone 17 Pro": {"price_bdt": 155000, "colors": ["Space Black", "Natural Titanium", "Dark Blue"]},
            "iPhone 17 Pro Max": {"price_bdt": 175000, "colors": ["Space Black", "Natural Titanium", "Dark Blue"]}
        }
    },
    "18": {
        "year": 2026,
        "models": {
            "iPhone 18": {"price_bdt": 108000, "colors": ["Midnight", "Starlight", "Mist Blue", "Sage", "Lavender"]},
            "iPhone 18 Pro": {"price_bdt": 200000, "colors": ["Black", "Silver", "Glacier", "Burgundy"]},
            "iPhone 18 Pro Max": {"price_bdt": 230000, "colors": ["Black", "Silver", "Glacier", "Burgundy"]},
            "iPhone Duo": {"price_bdt": 350000, "colors": ["Night Sky", "Star White"]}
        }
    }
}

def display_model(name, data, year):
    colors = ", ".join(data["colors"])
    formatted_price = f"{data['price_bdt']:,}"
    print(f"\n{name} ({year})\n  • BD Market Price: ৳{formatted_price}\n  • Available Colors: {colors}")

def search_phone(query):
    query = query.strip().lower()
    found = False
    for series, info in IPHONES.items():
        year = info["year"]
        for name, data in info["models"].items():
            if query in name.lower() or query == series:
                display_model(name, data, year)
                found = True
    if not found:
        print(f"No results found matching '{query}'.")

def main():
    while True:
        entry = input("\nEnter iPhone model/series (e.g. '18', 'iPhone 18', 'Duo') or 'q' to quit: ").strip()
        if entry.lower() in ("q", "exit"):
            break
        search_phone(entry)

if __name__ == "__main__":
    main()
