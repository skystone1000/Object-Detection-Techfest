from google.cloud import storage

#bucket_name = 'ai-ufdggn.appspot.com'
#destination_file_name = 'E.jpg'

## Initialise a client
#storage_client = storage.Client("ObjectDetection")
## Create a bucket object for our bucket
#bucket = storage_client.get_bucket(bucket_name)
## Create a blob object from the filepath
#blob = bucket.blob("Surr/Edownload.jpg")
## Download the file to a destination
#blob.download_to_filename(destination_file_name)


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))

download_blob('ai-ufdggn.appspot.com','Surr','/home/skystone/Desktop/upload/a.jpg')
