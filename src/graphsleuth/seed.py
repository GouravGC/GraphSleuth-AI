from .db import get_graph

# Synthetic demonstration data only. No real people, credentials, or incidents.
SEED_CYPHER = [
    """
    MERGE (a:Account {id: 'acct-104', name: 'Jordan Lee', risk: 'high'})
    MERGE (b:Account {id: 'acct-207', name: 'Taylor Morgan', risk: 'medium'})
    MERGE (d1:Device {id: 'dev-22', name: 'Windows Laptop 22', status: 'suspicious'})
    MERGE (d2:Device {id: 'dev-31', name: 'Workstation 31', status: 'monitored'})
    MERGE (s1:Server {id: 'srv-pay-01', name: 'Payments API', sensitivity: 'critical'})
    MERGE (s2:Server {id: 'srv-doc-02', name: 'Document Store', sensitivity: 'high'})
    MERGE (al:Alert {id: 'alert-9001', name: 'Unusual login burst', severity: 'high'})
    MERGE (a)-[:AUTHENTICATED_FROM]->(d1)
    MERGE (b)-[:AUTHENTICATED_FROM]->(d2)
    MERGE (d1)-[:ACCESSED {observed_at: '2026-10-18T20:14:00+05:30'}]->(s1)
    MERGE (d1)-[:ACCESSED {observed_at: '2026-10-18T20:16:00+05:30'}]->(s2)
    MERGE (d2)-[:ACCESSED {observed_at: '2026-10-17T11:02:00+05:30'}]->(s2)
    MERGE (a)-[:TRIGGERED]->(al)
    """
]

def seed_demo_data() -> None:
    graph = get_graph()
    for statement in SEED_CYPHER:
        graph.query(statement)
