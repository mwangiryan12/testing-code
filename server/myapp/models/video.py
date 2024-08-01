from myapp.extensions import db


class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    record_id = db.Column(db.Integer, db.ForeignKey('records.id'), nullable=False)

def validate_url(url):
# Basic validation for video URL
 valid_extensions = ['mp4', 'avi', 'mov', 'mkv']
 if not any(url.lower().endswith(ext) for ext in valid_extensions):
  return False
# Further checks could be implemented based on specific needs
 return True
