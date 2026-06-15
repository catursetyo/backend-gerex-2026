from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database.db"


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        conn.executescript(
            """
            DROP TABLE IF EXISTS mahasiswa_baru;
            DROP TABLE IF EXISTS gugus;
            DROP TABLE IF EXISTS regions;

            CREATE TABLE regions (
                region_id INTEGER PRIMARY KEY AUTOINCREMENT,
                region_name TEXT NOT NULL
            );

            CREATE TABLE gugus (
                gugus_id INTEGER PRIMARY KEY AUTOINCREMENT,
                gugus_name TEXT NOT NULL,
                region_id INTEGER NOT NULL,
                FOREIGN KEY (region_id) REFERENCES regions(region_id)
            );

            CREATE TABLE mahasiswa_baru (
                maba_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nrp TEXT UNIQUE NOT NULL,
                nama TEXT NOT NULL,
                gugus_id INTEGER NOT NULL,
                FOREIGN KEY (gugus_id) REFERENCES gugus(gugus_id)
            );
            """
        )

        regions = [
            ("Region Surabaya",),
            ("Region Luar Surabaya",),
        ]

        gugus = [
            ("Gugus Arjuna", 1),
            ("Gugus Bima", 1),
            ("Gugus Nakula", 2),
        ]

        mahasiswa_baru = [
            ("5027251066", "Catur Setyo Ragil", 1),
            ("5027251001", "Evandra Raditya", 2),
            ("5027251051", "Hendra Manudinata", 3),
        ]

        conn.executemany("INSERT INTO regions (region_name) VALUES (?)", regions)
        conn.executemany(
            "INSERT INTO gugus (gugus_name, region_id) VALUES (?, ?)",
            gugus,
        )
        conn.executemany(
            "INSERT INTO mahasiswa_baru (nrp, nama, gugus_id) VALUES (?, ?, ?)",
            mahasiswa_baru,
        )

    print("Database berhasil dibuat dan data contoh berhasil dimasukkan.")
    print(f"Lokasi database: {DB_PATH}")


if __name__ == "__main__":
    init_db()
