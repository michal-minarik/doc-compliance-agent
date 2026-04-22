# Regulatory Compliance Analysis Agent

This project contains an AI agent that acts as a Senior Regulatory Compliance Analyst. It uses the Gemini family of models via the Google AI Development Kit (`adk`) to analyze documents stored in Google Cloud Storage (GCS) and generate compliance reports based on user queries.

The agent is designed to be a multimodal, capable of analyzing various document formats (e.g., text files, PDFs, images) to provide comprehensive compliance verification.

## Key Features

- **Multimodal Analysis:** Leverages Gemini's multimodal capabilities to analyze a wide range of document types.
- **GCS Integration:** Seamlessly lists, reads, and writes documents and reports to Google Cloud Storage.
- **Extensible:** Built with the `google-adk` to be easily extensible with new tools and capabilities.

## Getting Started

### Prerequisites

- Python 3.x
- An active Google Cloud project
- The `gcloud` CLI installed and authenticated (`gcloud auth application-default login`)
- The following Google Cloud APIs enabled in your project:
    - Vertex AI API (`aiplatform.googleapis.com`)
    - Cloud Storage API (`storage.googleapis.com`)
    - Cloud Run API (`run.googleapis.com`)

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

The agent requires environment variables to be set for the Google Cloud Project and the GCS bucket.

You can set these directly in your terminal, or create a `.env` file in the root of the project. The `python-dotenv` package will automatically load them.

**Using a `.env` file (Recommended):**
Create a file named `.env` and add the following lines:
```env
GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
BUCKET_NAME="your-gcs-bucket-name"
```

**Using terminal exports:**
1.  **Set the `GOOGLE_CLOUD_PROJECT` environment variable:**
    ```bash
    export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
    ```

2.  **Set the `BUCKET_NAME` environment variable:**
    ```bash
    export BUCKET_NAME="your-gcs-bucket-name"
    ```

*Note: If `BUCKET_NAME` is not set, it defaults to `agent-work-dir`.*

3.  **Upload documents for analysis:**
    Upload the files you want the agent to analyze into your GCS bucket under a folder named `inputs/`.
    For example: `gs://your-gcs-bucket-name/inputs/document1.pdf`


### Running the Agent

The agent is designed to be run using the `adk` command-line interface.

- **Start the agent for interactive use:**
    ```bash
    adk run .
    ```
- After starting, you can ask the agent questions like "Which files do you see on the storage?" or "Analyze document1.pdf for compliance issues."

- **Deploy the agent as a Cloud Run service:**
    ```bash
    adk deploy .
    ```

## Project Structure

-   `agent.py`: Defines the core agent, its persona, and instructions.
-   `agent_tools.py`: Implements the tools the agent uses to interact with GCS.
-   `requirements.txt`: Lists the Python dependencies for the project.
-   `GEMINI.md`: Contains detailed internal documentation and instructions for the Gemini agent.

## Extending the Agent / Contributing

To improve or extend the capabilities of the agent, follow these steps:

1.  **Add a new tool function** in `agent_tools.py`. Ensure you include type hints and a detailed docstring, as the `adk` uses this information to describe the tool to the LLM.
2.  **Register the tool** in `agent.py`. Import your new function and add it to the `tools` list when initializing the `adk.Agent`.
3.  **Update the agent prompt** (if necessary) in `agent.py` to inform the agent about its new capabilities and when to use the new tool.
