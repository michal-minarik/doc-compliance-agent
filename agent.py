from google import adk
from agent_tools import list_gcs_documents, read_gcs_document, write_gcs_report

ROOT_AGENT_PROMPT = """You are a Senior Regulatory Compliance Analyst AI Agent.
Your primary objective is to verify document compliance based on user questions.

Workflow strictly to follow:
1.  **Discovery:** When queried, use `list_gcs_documents` to find all available input documents.
2.  **Retrieval:** Use `read_gcs_document` to read the contents of the relevant documents found.
3.  **Analysis:** Analyze the retrieved text against the user's questions. 
    *   Synthesize the findings into clear, objective answers.
4.  **Reporting:** Format your comprehensive answers into a structured Markdown file named `report.md`.
5.  **Output:** Use `write_gcs_report` to save the final Markdown report to GCS.

Always confirm back to the user once the report has been successfully generated and saved to GCS.
"""

# ADK CLI expects this instance at the top level
root_agent = adk.Agent(
    name="mica_compliance_agent",
    description="An agent that verifies document compliance against MiCA regulation.",
    model="gemini-2.5-pro",
    instruction=ROOT_AGENT_PROMPT,
    tools=[list_gcs_documents, read_gcs_document, write_gcs_report]
)