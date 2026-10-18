import os
from dotenv import load_dotenv

load_dotenv()

def get_config() -> dict:
    return {
        "host": os.getenv("FALKORDB_HOST", "localhost"),
        "port": int(os.getenv("FALKORDB_PORT", "6379")),
        "username": os.getenv("FALKORDB_USERNAME") or None,
        "password": os.getenv("FALKORDB_PASSWORD") or None,
        "ssl": os.getenv("FALKORDB_SSL", "false").strip().lower() in {"1", "true", "yes"},
        "graph_name": os.getenv("FALKORDB_GRAPH", "graphsleuth"),
    }
