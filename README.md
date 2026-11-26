# Ledger Explorer Indexing Completeness (dlt-fabric-project)

A project focused on verifying ledger index completeness, gap detection, and data verification within a Hyperledger Fabric environment.

## 📁 Project Architecture

Below is the directory breakdown of this repository:

*   **`prototype.html`**: The complete, standalone frontend application for the project.
*   **`.venv/`**: Python virtual environment containing required dependencies (ignored by version control).
*   **`api/`**: Backend API endpoints for handling data retrieval and communication.
*   **`dashboard/`**: Additional frontend assets, components, or UI files.
*   **`database/`**: Scripts, schemas, or storage mechanisms for maintaining local indexed data.
*   **`fabric-samples/`**: Local network configurations and sample binaries for Hyperledger Fabric test networks.
*   **`gap-detection/`**: Core logic or scripts responsible for locating missing blocks or discrepancies in the ledger indexing.
*   **`indexer/`**: Service tasked with continuously listening to the blockchain network and pulling blocks/transactions.
*   **`verification/`**: Validation scripts ensuring the integrity and authenticity of indexed ledger data against the blockchain state.
*   **`ledger-index-verifier.ps1`**: Executable automation script to kick off verification routines.
*   **`TEASL_construction_algorithm.py`**: Python file housing the construction logic for the project's algorithmic backbone.

---

## 💻 Frontend Application (`prototype.html`)

The **`prototype.html`** file located in the root directory is the **complete, standalone frontend** for this project. 

*   **Monolithic Design**: It contains the full HTML markup, integrated styling with **Tailwind CSS**, typography configuring **IBM Plex Sans / Mono**, and UI presentation logic entirely in a single file.
*   **Purpose**: It serves as the primary dashboard interface for the **Ledger Explorer Indexing Completeness** app, showing exactly how block metadata, gaps, and system statuses are visualized.
*   **How to view/run**: 
    Simply open the `prototype.html` file directly in any modern web browser (Chrome, Edge, Firefox, or Safari) to launch the frontend.

## 🚀 Live Prototype

Open the deployed prototype at **https://visala-p.github.io/QUINDEXER/**. The page starts the simulated chain and indexer automatically when it loads; no sign-in, local server, or Fabric network is required.

GitHub Actions deploys the standalone `prototype.html` as the site's home page whenever changes are pushed to `main`. For the first deployment, set the repository's Pages source to **GitHub Actions** in **Settings → Pages**. The demo runs entirely in the browser and does not connect to a real ledger, backend, or database.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.12+ (configured inside your `.venv`)
*   Hyperledger Fabric prerequisites (if deploying the network via `fabric-samples`)

### Quick Start
1. Clone the repository.
2. Open `prototype.html` in a web browser to view the entire user interface.
3. Configure the `api/` and `indexer/` engines to start feeding data to the application backend.
