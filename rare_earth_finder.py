# Rare Earth Element Finder
def show_menu():
    print("\n=== Rare Earth Element Finder ===")
    print("1. View all elements")
    print("2. Search for an element")
    print("3. Add a new element")
    print("4. Exit")
    print("=========================")

def view_elements(elements):
    if not elements:
        print("\nNo elements found.")
    else:
        print("\nRare Earth Elements:")
        for name, details in elements.items():
            print(f"- {name}: {details['symbol']} (Uses: {details['uses']})")

def search_element(elements):
    name = input("\nEnter the name of the element to search: ").capitalize()
    if name in elements:
        details = elements[name]
        print(f"\n{name} ({details['symbol']}):")
        print(f"Uses: {details['uses']}")
    else:
        print(f"Element '{name}' not found.")

def add_element(elements):
    name = input("\nEnter the name of the element: ").capitalize()
    symbol = input("Enter the symbol of the element: ").upper()
    uses = input("Enter the uses of the element: ")
    elements[name] = {"symbol": symbol, "uses": uses}
    print(f"Element '{name}' added!")

def main():
    elements = {
        "Scandium": {"symbol": "Sc", "uses": "Aerospace components, sports equipment"},
        "Yttrium": {"symbol": "Y", "uses": "LEDs, phosphors, superconductors"},
        "Lanthanum": {"symbol": "La", "uses": "Camera lenses, batteries"},
        "Cerium": {"symbol": "Ce", "uses": "Catalytic converters, glass polishing"},
        "Praseodymium": {"symbol": "Pr", "uses": "Magnets, aircraft engines"},
        "Neodymium": {"symbol": "Nd", "uses": "Magnets, lasers"},
        "Promethium": {"symbol": "Pm", "uses": "Nuclear batteries, luminous paints"},
        "Samarium": {"symbol": "Sm", "uses": "Magnets, neutron absorbers"},
        "Europium": {"symbol": "Eu", "uses": "Red and blue phosphors in TVs, LEDs"},
        "Gadolinium": {"symbol": "Gd", "uses": "MRI contrast agents, alloys"},
        "Terbium": {"symbol": "Tb", "uses": "Green phosphors, stabilizers for fuel cells"},
        "Dysprosium": {"symbol": "Dy", "uses": "Magnets, nuclear reactors"},
        "Holmium": {"symbol": "Ho", "uses": "Magnets, lasers"},
        "Erbium": {"symbol": "Er", "uses": "Fiber optics, lasers"},
        "Thulium": {"symbol": "Tm", "uses": "Portable X-ray devices"},
        "Ytterbium": {"symbol": "Yb", "uses": "Lasers, stress gauges"},
        "Lutetium": {"symbol": "Lu", "uses": "Petroleum refining, medical imaging"}
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            view_elements(elements)
        elif choice == "2":
            search_element(elements)
        elif choice == "3":
            add_element(elements)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()