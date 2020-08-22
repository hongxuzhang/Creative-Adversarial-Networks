import boto3
import os

# s3 = boto3.resource('s3')
# s3.meta.client.upload_file('tmp/', BUCKET_NAME, 'tmp/')


def bucket_exists(bucket):
  client = storage.Client()
  bucket = client.get_bucket(bucket)
  blobs = list(bucket.list_blobs())
  return blobs
#  s3 = boto3.resource('s3')
#  return s3.Bucket(bucket) in s3.buckets.all()

def upload_path(source_file_name, bucket_name, destination_blob_name, certain_upload=False):
      """Uploads a file to the bucket."""
          # bucket_name = "your-bucket-name"
              # source_file_name = "local/path/to/file"
                  # destination_blob_name = "storage-object-name"

                      storage_client = storage.Client()
                          bucket = storage_client.bucket(bucket_name)
                              blob = bucket.blob(destination_blob_name)

                                  blob.upload_from_filename(source_file_name)

                                      print(
                                                "File {} uploaded to {}.".format(
                                                              source_file_name, destination_blob_name
                                                          )
                                            )
