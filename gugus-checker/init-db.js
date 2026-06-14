const connectDB = require("./db");

async function initDB() {
  const db = await connectDB();

  await db.exec(`
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
  `);

  await db.run(`INSERT INTO regions (region_name) VALUES (?)`, ["Region Surabaya"]);
  await db.run(`INSERT INTO regions (region_name) VALUES (?)`, ["Region Luar Surabaya"]);

  await db.run(
    `INSERT INTO gugus (gugus_name, region_id) VALUES (?, ?)`,
    ["Gugus Arjuna", 1]
  );

  await db.run(
    `INSERT INTO gugus (gugus_name, region_id) VALUES (?, ?)`,
    ["Gugus Bima", 1]
  );

  await db.run(
    `INSERT INTO gugus (gugus_name, region_id) VALUES (?, ?)`,
    ["Gugus Nakula", 2]
  );

  await db.run(
    `INSERT INTO mahasiswa_baru (nrp, nama, gugus_id) VALUES (?, ?, ?)`,
    ["5027251066", "Catur Setyo Ragil", 1]
  );

  await db.run(
    `INSERT INTO mahasiswa_baru (nrp, nama, gugus_id) VALUES (?, ?, ?)`,
    ["5027251001", "Evandra Raditya", 2]
  );

  await db.run(
    `INSERT INTO mahasiswa_baru (nrp, nama, gugus_id) VALUES (?, ?, ?)`,
    ["5027251051", "Hendra Manudinata", 3]
  );

  console.log("Database berhasil dibuat dan data contoh berhasil dimasukkan.");
}

initDB();
