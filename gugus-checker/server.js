const express = require("express");
const cors = require("cors");
const connectDB = require("./db");

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    message: "Gugus Checker API is running"
  });
});

app.get("/api/gugus-checker", async (req, res) => {
  const { nrp } = req.query;

  if (!nrp) {
    return res.status(400).json({
      success: false,
      message: "NRP wajib diisi"
    });
  }

  const db = await connectDB();

  const query = `
    SELECT 
      m.nrp,
      m.nama,
      g.gugus_name AS gugus,
      r.region_name AS region
    FROM mahasiswa_baru m
    JOIN gugus g ON m.gugus_id = g.gugus_id
    JOIN regions r ON g.region_id = r.region_id
    WHERE m.nrp = ?
  `;

  const data = await db.get(query, [nrp]);

  if (!data) {
    return res.status(404).json({
      success: false,
      message: "Data mahasiswa dengan NRP tersebut tidak ditemukan"
    });
  }

  return res.status(200).json({
    success: true,
    message: "Data gugus berhasil ditemukan",
    data: data
  });
});

app.listen(PORT, () => {
  console.log(`Server berjalan di http://localhost:${PORT}`);
});
