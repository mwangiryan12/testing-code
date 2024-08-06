import cloudinary
import cloudinary.uploader


cloudinary.config(
    cloud_name='dycrqnjcs',
    api_key='314272631384883',
    api_secret='IeL3lkZx1jBVMW6VdYrdbNAM2uc'
)

def upload_file(file):
    result = cloudinary.uploader.upload(file)
    
    return result

