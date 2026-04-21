# Project Overview

This project implements a AI agent that acts as a Senior Regulatory Compliance Analyst. The agent is built using the `google-adk` library and is designed to analyze documents stored in a Google Cloud Storage (GCS) bucket to verify compliance based on user queries.

## Key Technologies

- Python
- Google ADK (`google-adk`)
- Google Cloud AI Platform (`google-cloud-aiplatform`)
- Google Cloud Storage (`google-cloud-storage`)

## Architecture

The project consists of two main Python files:

- `agent.py`: This file defines the core agent, including its persona, instructions, and the tools it can use. The agent is named `mica_compliance_agent` and uses the `gemini-2.5-pro` model.
- `agent_tools.py`: This file provides the implementation for the tools used by the agent. These tools handle the interaction with Google Cloud Storage, allowing the agent to list documents, read them for multimodal analysis, and write reports. The `read_gcs_document` function is designed to handle various file types by returning a dictionary containing the file's GCS URI and MIME type.

## Building and Running

### Prerequisites

- Python 3.x
- An active Google Cloud project
- The `gcloud` CLI installed and authenticated

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

The agent requires access to a Google Cloud Storage bucket. The name of the bucket can be configured using the `BUCKET_NAME` environment variable. If not set, it defaults to `agent-work-dir`.

-  **Set the `BUCKET_NAME` environment variable:**
    ```bash
    export BUCKET_NAME="your-gcs-bucket-name"
    ```
-  **Set the `GOOGLE_CLOUD_PROJECT` environment variable:**
    ```bash
    export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
    ```

### Running the Agent

The agent is designed to be run using the `adk` command-line interface.

- **Start the agent:**
    ```bash
    adk run .
    ```
- **Deploy the agent:**
    ```bash
    adk deploy .
    ```

## Development Conventions

- The agent's logic is defined in `agent.py`.
- The tools used by the agent are implemented in `agent_tools.py`.
- The agent's dependencies are listed in `requirements.txt`.
- The agent's prompt and instructions are defined in the `ROOT_AGENT_PROMPT` constant in `agent.py`.
