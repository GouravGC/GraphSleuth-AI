from src.graphsleuth.config import get_config

def test_default_config_has_expected_local_values(monkeypatch):
    monkeypatch.delenv("FALKORDB_HOST", raising=False)
    monkeypatch.delenv("FALKORDB_PORT", raising=False)
    monkeypatch.delenv("FALKORDB_GRAPH", raising=False)
    cfg = get_config()
    assert cfg["host"] == "localhost"
    assert cfg["port"] == 6379
    assert cfg["graph_name"] == "graphsleuth"
