import os
from typing import List
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

def read_gcs_document(gcs_uri: str) -> str:
    """Reads the content of a specific document from GCS.
    
    Args:
        gcs_uri: The specific GCS file URI (e.g., gs://agent-work-dir/inputs/doc1.txt).
    
    Returns:
        str: The raw text content of the document.
    """
    try:
        if not gcs_uri.startswith("gs://"):
            return "Error: Invalid GCS URI. Must start with gs://"
        
        path_parts = gcs_uri.replace("gs://", "").split("/", 1)
        bucket_name = path_parts[0]
        blob_name = path_parts[1]
        
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        
        content = blob.download_as_text()
        return content
    except Exception as e:
        return f"Error reading document: {str(e)}"

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
