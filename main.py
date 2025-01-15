import uvicorn
from src.scoperag.server import server


def bootstrap():
    uvicorn.run(server, host="0.0.0.0", port=8000, log_level="info")


bootstrap()
