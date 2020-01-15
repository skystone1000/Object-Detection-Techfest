

from gcloud import storage

def explicit():
    from google.cloud import storage

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        'ObjectDetection-1ac191d1d257.json')

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)


#explicit()

import os
print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

#upload_blob('ai-ufdggn.appspot.com', 'N.jpg', 'Surr/N')
#upload_blob('ai-ufdggn.appspot.com', 'NW.jpg', 'Surr/NW')
#upload_blob('ai-ufdggn.appspot.com', 'W.jpg', 'Surr/W')
#upload_blob('ai-ufdggn.appspot.com', 'SW.jpg', 'Surr/SW')
#upload_blob('ai-ufdggn.appspot.com', 'S.jpg', 'Surr/S')
#upload_blob('ai-ufdggn.appspot.com', 'SE.jpg', 'Surr/SE')
#upload_blob('ai-ufdggn.appspot.com', 'E.jpg', 'Surr/E')
upload_blob('ai-ufdggn.appspot.com', 'NE.jpg', 'Surr/NE')
