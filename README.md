# 🕵️ GraphSleuth AI

**Graph-powered cybersecurity investigations using FalkorDB**

GraphSleuth AI is a cybersecurity investigation prototype that uses graph-based reasoning to trace relationships between accounts, devices, servers, and security alerts.

Instead of relying on an LLM to invent evidence, GraphSleuth retrieves investigation paths from FalkorDB using Cypher queries.

## 🚨 Problem

Security investigations often involve connected evidence scattered across users, devices, servers, and alerts. GraphSleuth helps investigators explore these relationships and understand potential access paths.

## ✨ Key Features

- **Graph-powered investigations:** Trace account → device → server relationships.
- **Connected evidence:** Identify related security alerts and sensitive destinations.
- **Persistent investigation memory:** Store investigation summaries in the graph database.
- **Synthetic security dataset:** Demonstrate investigations without exposing real security data.
- **Interactive investigation interface:** Explore investigation results through Streamlit and FalkorDB.

## 🧰 Tech Stack

- Python
- Streamlit
- FalkorDB
- Cypher graph queries
- Docker and Docker Compose
- Pytest

## 🏗️ Architecture

1. Synthetic security data populates FalkorDB.
2. The investigation workflow queries connected entities and relationships.
3. Cypher queries retrieve account-to-device-to-server paths and linked alerts.
4. The application summarizes the retrieved evidence.
5. Investigation records are persisted for subsequent review.

## 🔍 Example Investigation

**Subject:** Jordan Lee  
**Risk level:** High

Example results from the synthetic demo graph:

- 2 graph-traced access paths
- 1 device involved
- 2 destination servers
- 1 linked alert: `Unusual login burst`
- Critical-sensitivity destination: `Payments API`

These are demonstration results from fictional data, not findings about a real person or environment.

## 🕸️ Graph Model

The demo graph connects security entities such as accounts, devices, servers, and alerts through relationships representing access and investigation evidence.

Example graph query:

```cypher
MATCH (n)-[r]->(m)
RETURN n, r, m
LIMIT 50
```

This query retrieves connected nodes and relationships for graph inspection.

## ⚙️ Run Locally

### Prerequisites

- Python 3.11
- Docker Desktop
- Git

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd GraphSleuth-AI
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows CMD:

```cmd
.venv\Scripts\activate
```

### 3. Install dependencies

```cmd
pip install -r requirements.txt
```

### 4. Start FalkorDB

```cmd
docker compose up -d
```

### 5. Launch the application

Windows CMD:

```cmd
set PYTHONPATH=src
streamlit run app.py
```

Open the local Streamlit URL shown in your terminal, normally `http://localhost:8501`.

Use **Load synthetic demo graph** to populate the database before running an investigation.

## 🧪 Tests

Run:

```cmd
python -m pytest -q
```

## 🔐 Security and Limitations

- All included investigation data is fictional.
- Do not commit `.env` files, API keys, credentials, or real security logs.
- Findings depend on the available graph data and implemented query logic.
- This is a prototype and is not a substitute for a production security operations platform.

## 🏆 Hackathon

Built for **Graph Hacks: Context for AI Agents**, focusing on agents that act on connected data.

## 📸 Evidence and Demo

Screenshots and demo recording: see the `evidence/` directory and the project demonstration.

## 📄 License

Add a license before distributing the project for reuse.
