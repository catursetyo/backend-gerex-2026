from fastapi import APIRouter, HTTPException, Path
from app.database import get_db_connection

router = APIRouter(tags=["Gugus Checker"])


@router.get("/{nrp}")
def check_gugus(
    nrp: str = Path(..., pattern="^[0-9]+$", description="NRP mahasiswa baru")
):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            mahasiswa_baru.nrp,
            mahasiswa_baru.nama,
            gugus.gugus_name,
            regions.region_name
        FROM mahasiswa_baru
        JOIN gugus ON mahasiswa_baru.gugus_id = gugus.gugus_id
        JOIN regions ON gugus.region_id = regions.region_id
        WHERE mahasiswa_baru.nrp = ?
        """,
        (nrp,),
    )

    data = cursor.fetchone()
    conn.close()

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Data mahasiswa tidak ditemukan",
        )

    return {
        "nrp": data["nrp"],
        "nama": data["nama"],
        "gugus": data["gugus_name"],
        "region": data["region_name"],
    }
