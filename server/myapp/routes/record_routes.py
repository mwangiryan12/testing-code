from flask import Blueprint, request, jsonify
from ..models.record import Record, db
from ..models.image import Image
from ..models.video import Video
from ..services.cloudinary_service import upload_file


record_bp = Blueprint('record', __name__)

@record_bp.route('/records/<int:record_id>/images', methods=['POST'])
def upload_image(record_id):
    file = request.files['image']
    upload_result = upload_file(file)
    image = Image(url=upload_result['url'], record_id=record_id)
    db.session.add(image)
    db.session.commit()
    return jsonify({'message': 'Image uploaded successfully', 'url': upload_result['url']}), 201


@record_bp.route('/records/<int:record_id>/videos', methods=['POST'])
def upload_video(record_id):
    file = request.files['video']
    upload_result = upload_file(file)
    video = Video(url=upload_result['url'], record_id=record_id)
    db.session.add(video)
    db.session.commit()
    return jsonify({'message': 'Video uploaded successfully', 'url': upload_result['url']}), 201

