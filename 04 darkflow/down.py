from google.cloud import storage

def download_blob(bucket_name,prefix,dl_dir):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name=bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
    for blob in blobs:
        filename = blob.name.replace('/', '_') 
        blob.download_to_filename(dl_dir + filename)  # Download

#Download image from which is uploaded from mobile
download_blob('ai-ufdggn.appspot.com','uploads/','/home/skystone/iitb/darkflow/')
print("All files in directory /uploads downloaded")
