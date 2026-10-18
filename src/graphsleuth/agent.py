from datetime import datetime, timezone
from .db import get_graph

ACCOUNTS_QUERY = """
MATCH (a:Account)
RETURN a.id AS id, a.name AS name, a.risk AS risk
ORDER BY a.name
"""

INVESTIGATE_QUERY = """
MATCH (a:Account {id: $account_id})-[:AUTHENTICATED_FROM]->(d:Device)
      -[access:ACCESSED]->(s:Server)
RETURN a.id AS account_id, a.name AS account_name, a.risk AS risk,
       d.id AS device_id, d.name AS device_name, d.status AS device_status,
       s.id AS server_id, s.name AS server_name, s.sensitivity AS sensitivity,
       access.observed_at AS observed_at
ORDER BY s.sensitivity, s.name
"""

ALERTS_QUERY = """
MATCH (a:Account {id: $account_id})-[:TRIGGERED]->(al:Alert)
RETURN al.id AS alert_id, al.name AS alert_name, al.severity AS severity
ORDER BY al.severity
"""

SAVE_INVESTIGATION_QUERY = """
MATCH (a:Account {id: $account_id})
MERGE (i:Investigation {id: $investigation_id})
SET i.question = $question,
    i.summary = $summary,
    i.created_at = $created_at,
    i.session_key = $session_key
MERGE (i)-[:INVESTIGATED_ACCOUNT]->(a)
WITH i, a
MATCH (a)-[:AUTHENTICATED_FROM]->(:Device)-[:ACCESSED]->(s:Server)
MERGE (i)-[:FOUND_EVIDENCE_FOR]->(s)
RETURN i.id AS id
"""

MEMORY_QUERY = """
MATCH (i:Investigation)-[:INVESTIGATED_ACCOUNT]->(a:Account {id: $account_id})
RETURN i.question AS question, i.summary AS summary, i.created_at AS created_at
ORDER BY i.created_at DESC
LIMIT 8
"""

def list_accounts():
    return get_graph().query(ACCOUNTS_QUERY).result_set

def investigate(account_id: str, session_key: str = "default") -> dict:
    graph = get_graph()
    paths = graph.query(INVESTIGATE_QUERY, {"account_id": account_id}).result_set
    alerts = graph.query(ALERTS_QUERY, {"account_id": account_id}).result_set

    if not paths:
        summary = "No account-to-server access path was found in the current graph."
        account_name = account_id
    else:
        account_name = paths[0][1]
        servers = sorted({row[7] for row in paths})
        devices = sorted({row[5] for row in paths})
        critical = [row[7] for row in paths if str(row[8]).lower() == "critical"]
        summary = (
            f"{account_name} has {len(paths)} graph-traced account→device→server "
            f"access path(s), involving {len(devices)} device(s) and {len(servers)} "
            f"server(s)."
        )
        if critical:
            summary += " Critical-sensitivity destination(s): " + ", ".join(sorted(set(critical))) + "."
        if alerts:
            summary += f" Linked alert(s): {', '.join(str(row[1]) for row in alerts)}."

    now = datetime.now(timezone.utc).isoformat()
    investigation_id = f"inv-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f')}"
    graph.query(
        SAVE_INVESTIGATION_QUERY,
        {
            "account_id": account_id,
            "investigation_id": investigation_id,
            "question": f"Trace access paths for {account_name}",
            "summary": summary,
            "created_at": now,
            "session_key": session_key,
        },
    )
    return {
        "account_id": account_id,
        "account_name": account_name,
        "paths": paths,
        "alerts": alerts,
        "summary": summary,
        "investigation_id": investigation_id,
    }

def get_memory(account_id: str):
    return get_graph().query(MEMORY_QUERY, {"account_id": account_id}).result_set
