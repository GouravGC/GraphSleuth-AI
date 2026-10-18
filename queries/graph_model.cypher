// GraphSleuth AI synthetic graph model
// Nodes: Account, Device, Server, Alert, Investigation
// Relationships: AUTHENTICATED_FROM, ACCESSED, TRIGGERED,
// INVESTIGATED_ACCOUNT, FOUND_EVIDENCE_FOR

// 1) Trace an account through a device to servers (multi-hop reasoning)
MATCH (a:Account {id: $account_id})-[:AUTHENTICATED_FROM]->(d:Device)
      -[access:ACCESSED]->(s:Server)
RETURN a.name, d.name, s.name, s.sensitivity, access.observed_at;

// 2) Find alerts associated with an account
MATCH (a:Account {id: $account_id})-[:TRIGGERED]->(al:Alert)
RETURN a.name, al.name, al.severity;

// 3) Read persistent investigation memory
MATCH (i:Investigation)-[:INVESTIGATED_ACCOUNT]->(a:Account {id: $account_id})
RETURN i.question, i.summary, i.created_at
ORDER BY i.created_at DESC
LIMIT 8;

// 4) Inspect graph shape
MATCH (a)-[r]->(b)
RETURN labels(a) AS from_labels, type(r) AS relationship, labels(b) AS to_labels
LIMIT 50;
