# 🕵️ GraphSleuth AI

### Graph-Powered Cybersecurity Investigations with FalkorDB

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)](https://streamlit.io/)
[![Database](https://img.shields.io/badge/Graph%20Database-FalkorDB-purple)](https://www.falkordb.com/)
[![Docker](https://img.shields.io/badge/Containerization-Docker-2496ED)](https://www.docker.com/)

**GraphSleuth AI** is a graph-powered cybersecurity investigation prototype that traces relationships between accounts, devices, servers, and security alerts using FalkorDB.

Rather than asking an LLM to invent security evidence, the application retrieves connected evidence through graph queries and presents investigation results with persistent investigation history.

**Hackathon:** [Graph Hacks: Context for AI Agents](https://www.wemakedevs.org/hackathons/falkordb)  
**Track:** Agents That Act on Connected Data  
**Repository:** [GouravGC/GraphSleuth-AI](https://github.com/GouravGC/GraphSleuth-AI)

---

## 📸 Project Demo and Evidence

Explore the actual project evidence:

- 🎥 **[Demo Video](https://github.com/GouravGC/GraphSleuth-AI/tree/main/evidences/Demo%20Video)**
- 🖼️ **[Screenshots](https://github.com/GouravGC/GraphSleuth-AI/tree/main/evidences/Screenshots)**
- 💻 **[Source Code](https://github.com/GouravGC/GraphSleuth-AI)**

The evidence folders contain the recorded demonstration and screenshots of the working application and graph visualization.

---

## 🚨 Problem Statement

Cybersecurity investigations frequently involve connected entities: users, devices, servers, resources, and alerts.

Examining these entities separately can make it difficult to understand how a suspicious account is connected to sensitive systems. GraphSleuth AI uses graph traversal to surface those relationships and help investigators explore potential access paths.

## ✨ Key Features

- **Graph-powered investigations:** Trace account → device → server access paths.
- **Connected security evidence:** Retrieve linked alerts and sensitive destinations.
- **Persistent investigation memory:** Store investigation summaries for subsequent review.
- **Interactive graph exploration:** Inspect nodes and relationships using FalkorDB Browser.
- **Synthetic security data:** Demonstrate the investigation workflow without exposing real security records.
- **Streamlit interface:** Load demo data and run investigations through a user interface.
- **Containerized database setup:** Start FalkorDB with Docker Compose.

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Application logic |
| Streamlit | Interactive user interface |
| FalkorDB | Graph storage and traversal |
| Cypher | Graph queries and evidence retrieval |
| Docker Compose | Local database startup |
| Pytest | Automated testing |

## 🏗️ Architecture

1. Synthetic security entities and relationships are loaded into FalkorDB.
2. The investigation workflow queries connected entities.
3. Cypher queries retrieve account-to-device-to-server paths and related alerts.
4. The application summarizes the evidence returned by the graph.
5. Investigation records are persisted in FalkorDB for later review.

**Core principle:** The investigation evidence comes from graph queries against FalkorDB. The application does not rely on an LLM to fabricate evidence paths.

## 🕸️ Graph Data Model

The synthetic graph connects entities such as:

| Entity | Description |
|---|---|
| Account / Person | Subject of an investigation |
| Device | Workstation or laptop associated with an account |
| Server / Resource | Destination such as Payments API or Document Store |
| Alert | Security event associated