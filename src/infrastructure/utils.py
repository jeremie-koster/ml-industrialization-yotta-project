import os
import pickle
import src.config.base as base
import logging

from google.cloud import storage


def dump_model_locally(model, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    logging.info("Saving model...")
    with open(filepath, "wb") as file:
        pickle.dump(model, file)


def upload_model(source_file_name, destination_model_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_model_name = "storage-object-name"

    storage_client = storage.Client()
    bucket_id = os.getenv("BUCKET_NAME")

    bucket = storage_client.bucket(bucket_id)
    blob = bucket.blob(destination_model_name)

    blob.upload_from_filename(source_file_name)

    logging.info(
        "File {} uploaded to {}.".format(source_file_name, destination_model_name)
    )


def download_blob(source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(
        "chaos-2"
    )  # TODO: pass this through an environment variable

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print("Blob {} downloaded to {}.".format(source_blob_name, destination_file_name))
