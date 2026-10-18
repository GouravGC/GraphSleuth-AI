from falkordb import FalkorDB
from .config import get_config

def get_graph():
    cfg = get_config()
    client = FalkorDB(
        host=cfg["host"],
        port=cfg["port"],
        username=cfg["username"],
        password=cfg["password"],
        ssl=cfg["ssl"],
        socket_connect_timeout=4,
        socket_timeout=8,
    )
    return client.select_graph(cfg["graph_name"])

def ping_database() -> bool:
    graph = get_graph()
    # A harmless read verifies that the graph endpoint is reachable.
    graph.query("RETURN 1 AS ok")
    return True
