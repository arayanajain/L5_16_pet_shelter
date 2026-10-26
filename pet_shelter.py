
"""Manage a simple animal shelter adoption register."""

import secrets
import sqlite3


class Shelter:
    """Manage pet registrations and adoptions."""

    def __init__(self):
        """Initialize the in-memory pet database."""
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute(
            """
            CREATE TABLE pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                age INTEGER,
                adopted INTEGER
            )
            """
        )
        self.adoption_count = 0

    def register_pet(self, name, species, age, tags=None):
        """Register a pet and return its updated tags."""
        if tags is None:
            tags = []

        self.conn.execute(
            """
            INSERT INTO pets (name, species, age, adopted)
            VALUES (?, ?, ?, 0)
            """,
            (name, species, age),
        )
        tags.append(species)
        return tags

    def adopt(self, pet_id):
        """Adopt an available pet and count successful adoptions."""
        cursor = self.conn.execute(
            "UPDATE pets SET adopted = 1 WHERE id = ? AND adopted = 0",
            (pet_id,),
        )
        if cursor.rowcount > 0:
            self.adoption_count += 1
            return True
        return False

    @staticmethod
    def adoption_code():
        """Generate an unpredictable adoption code."""
        return f"PET-{secrets.randbelow(9000) + 1000}"

    def oldest_available(self):
        """Return the oldest available pet's name, or None."""
        row = self.conn.execute(
            """
            SELECT name, age
            FROM pets
            WHERE adopted = 0
            ORDER BY age DESC
            LIMIT 1
            """
        ).fetchone()
        return row[0] if row is not None else None

    def clear_unadopted(self):
        """Delete all pets that have not been adopted."""
        self.conn.execute("DELETE FROM pets WHERE adopted = 0")

    def shelter_status(self):
        """Return the current shelter activity status."""
        if self.adoption_count > 0:
            return "active"
        return "quiet"


def main():
    """Run the shelter demonstration."""
    shelter = Shelter()
    shelter.register_pet("Bruno", "dog", 7)
    shelter.register_pet("Mitzi", "cat", 3)
    shelter.register_pet("Kiwi", "parrot", 12)
    shelter.adopt(1)
    print(
        shelter.oldest_available(),
        shelter.adoption_code(),
        shelter.shelter_status(),
    )
    shelter.clear_unadopted()
    shelter.conn.close()


if __name__ == "__main__":
    main()
