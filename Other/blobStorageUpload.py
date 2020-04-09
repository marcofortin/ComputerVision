# Uploading local images (stored in asset folder) to ms azure blob

import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("Azure Blob storage v12 - Python quickstart sample")
    # Retrieve the connection string
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    print(connect_str)

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = "computervisiontest"

    # Create the container
    container_client = blob_service_client.create_container(container_name)

    # Get file path to upload and download
    local_path = "./asset"
    local_file_name = "image1.jpg"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

except Exception as ex:
    print('Exception:')
    print(ex)