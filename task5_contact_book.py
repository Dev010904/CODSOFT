# ============================================================
# TASK 5 - CONTACT BOOK
# CodSoft Python Programming Internship
# ============================================================

import json
import os

CONTACTS_FILE = "contacts.json"

# ── Data persistence ──────────────────────────────────────────

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# ── Display helpers ───────────────────────────────────────────

def print_header(title):
    print("\n" + "=" * 55)
    print(f"  📒  {title}")
    print("=" * 55)

def display_contact_list(contacts):
    if not contacts:
        print("\n  📭 No contacts found!")
        return
    print(f"\n  {'#':<4} {'Name':<22} {'Phone'}")
    print("  " + "-" * 40)
    for i, (name, info) in enumerate(sorted(contacts.items()), 1):
        print(f"  {i:<4} {name:<22} {info['phone']}")
    print()

def display_full_contact(name, info):
    print("\n  " + "-" * 40)
    print(f"  👤 Name   : {name}")
    print(f"  📞 Phone  : {info['phone']}")
    print(f"  📧 Email  : {info.get('email', 'N/A')}")
    print(f"  🏠 Address: {info.get('address', 'N/A')}")
    print("  " + "-" * 40)

# ── CRUD operations ───────────────────────────────────────────

def add_contact(contacts):
    print_header("ADD NEW CONTACT")
    name = input("  Full Name   : ").strip().title()
    if not name:
        print("  ⚠️  Name cannot be empty!")
        return
    if name in contacts:
        print(f"  ⚠️  Contact '{name}' already exists!")
        return

    phone = input("  Phone Number: ").strip()
    if not phone:
        print("  ⚠️  Phone number cannot be empty!")
        return

    email   = input("  Email (opt) : ").strip()
    address = input("  Address (opt): ").strip()

    contacts[name] = {
        "phone":   phone,
        "email":   email or "N/A",
        "address": address or "N/A",
    }
    save_contacts(contacts)
    print(f"\n  ✅ Contact '{name}' added successfully!")

def view_contacts(contacts):
    print_header("ALL CONTACTS")
    display_contact_list(contacts)

def search_contact(contacts):
    print_header("SEARCH CONTACT")
    query = input("  Enter name or phone to search: ").strip().lower()
    if not query:
        print("  ⚠️  Search query cannot be empty!")
        return

    results = {
        name: info for name, info in contacts.items()
        if query in name.lower() or query in info["phone"]
    }

    if results:
        print(f"\n  🔍 Found {len(results)} result(s):\n")
        for name, info in results.items():
            display_full_contact(name, info)
    else:
        print(f"\n  ❌ No contacts found matching '{query}'.")

def update_contact(contacts):
    print_header("UPDATE CONTACT")
    display_contact_list(contacts)
    if not contacts:
        return

    name = input("  Enter exact name to update: ").strip().title()
    if name not in contacts:
        print(f"  ⚠️  Contact '{name}' not found!")
        return

    print(f"\n  Updating '{name}' — press Enter to keep current value.")
    info = contacts[name]

    new_phone   = input(f"  New Phone   [{info['phone']}]  : ").strip()
    new_email   = input(f"  New Email   [{info['email']}]  : ").strip()
    new_address = input(f"  New Address [{info['address']}]: ").strip()

    if new_phone:
        info["phone"] = new_phone
    if new_email:
        info["email"] = new_email
    if new_address:
        info["address"] = new_address

    save_contacts(contacts)
    print(f"\n  ✅ Contact '{name}' updated successfully!")

def delete_contact(contacts):
    print_header("DELETE CONTACT")
    display_contact_list(contacts)
    if not contacts:
        return

    name = input("  Enter exact name to delete: ").strip().title()
    if name not in contacts:
        print(f"  ⚠️  Contact '{name}' not found!")
        return

    confirm = input(f"  Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
    if confirm in ("yes", "y"):
        del contacts[name]
        save_contacts(contacts)
        print(f"  🗑️  Contact '{name}' deleted successfully!")
    else:
        print("  ↩️  Deletion cancelled.")

# ── Main ──────────────────────────────────────────────────────

def main():
    print("\n" + "📒" * 18)
    print("       CONTACT BOOK APPLICATION")
    print("📒" * 18)

    contacts = load_contacts()

    menu = {
        "1": ("View All Contacts",  view_contacts),
        "2": ("Add New Contact",    add_contact),
        "3": ("Search Contact",     search_contact),
        "4": ("Update Contact",     update_contact),
        "5": ("Delete Contact",     delete_contact),
    }

    while True:
        print("\n  ---- MENU ----")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        print("  6. Exit")
        print()

        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "6":
            print("\n  👋 Goodbye! Your contacts are saved.\n")
            break
        elif choice in menu:
            menu[choice][1](contacts)
        else:
            print("  ⚠️  Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()
