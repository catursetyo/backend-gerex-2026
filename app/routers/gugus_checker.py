from typing import Annotated

from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from app.database import fetch_one
from app.schemas import ErrorResponse, GugusSuccessResponse

router = APIRouter(tags=["Gugus Checker"])


@router.get(
    "/api/gugus-checker",
    response_model=GugusSuccessResponse | ErrorResponse,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
def check_gugus(
    nrp: Annotated[str | None, Query(description="NRP mahasiswa baru")] = None,
):
    if not nrp or not nrp.strip():
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"success": False, "message": "NRP wajib diisi"},
        )

    query = """
        SELECT
            m.nrp,
            m.nama,
            g.gugus_name AS gugus,
            r.region_name AS region
        FROM mahasiswa_baru m
        JOIN gugus g ON m.gugus_id = g.gugus_id
        JOIN regions r ON g.region_id = r.region_id
        WHERE m.nrp = ?
    """

    data = fetch_one(query, [nrp.strip()])

    if not data:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "success": False,
                "message": "Data mahasiswa dengan NRP tersebut tidak ditemukan",
            },
        )

    return {
        "success": True,
        "message": "Data gugus berhasil ditemukan",
        "data": data,
    }
