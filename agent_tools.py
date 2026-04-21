import os
import mimetypes
from typing import List, Dict
from google.cloud import storage

BUCKET_NAME = os.getenv("BUCKET_NAME", "agent-work-dir")
INPUT_PREFIX = "inputs/"
OUTPUT_PREFIX = "outputs/report.md"

def list_gcs_documents() -> List[str]:
    """Lists all documents available in the input GCS path.
    
    Returns:
        List[str]: A list of file URIs available in the input directory.
    """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(BUCKET_NAME)
        blobs = bucket.list_blobs(prefix=INPUT_PREFIX)
        return [f"gs://{BUCKET_NAME}/{blob.name}" for blob in blobs if not blob.name.endswith('/')]
    except Exception as e:
        return [f"Error listing documents: {str(e)}"]

def read_gcs_document(gcs_uri: str) -> Dict[str, str]:
    """Reads the content of a specific document from GCS and returns its URI and mime type.
    
    Args:
        gcs_uri: The specific GCS file URI (e.g., gs://agent-work-dir/inputs/doc1.txt).
    
    Returns:
        Dict[str, str]: A dictionary containing the GCS URI and the inferred mime type.
    """
    try:
        if not gcs_uri.startswith("gs://"):
            raise ValueError("Invalid GCS URI. Must start with gs://")
        
        mime_type, _ = mimetypes.guess_type(gcs_uri)
        if not mime_type:
            # Default to plain text if mime type can't be inferred
            mime_type = "text/plain"
            
        return {"gcs_uri": gcs_uri, "mime_type": mime_type}
    except Exception as e:
        # It's better to return a descriptive error message
        # but for now, we'll raise the exception to be caught by the agent.
        raise e

def write_gcs_report(report_content: str) -> str:
    """Writes the final generated markdown report back to GCS.
    
    Args:
        report_content: The markdown formatted string containing the compliance report.
        
    Returns:
        str: Confirmation message with the output URI.
    """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(OUTPUT_PREFIX)
        
        blob.upload_from_string(report_content, content_type="text/markdown")
        return f"Successfully wrote report to gs://{BUCKET_NAME}/{OUTPUT_PREFIX}"
    except Exception as e:
        return f"Error writing report: {str(e)}"
