# seed.py
import uuid
from datetime import datetime
from myapp.extensions import db
from myapp.models.user import User
from myapp.models.record import Record
from myapp.models.image import Image
from myapp.models.video import Video
from werkzeug.security import generate_password_hash

def seed():
    # Drop all tables and create them
    db.drop_all()
    db.create_all()

    # Create sample users
    user1 = User(
        username='johndoe',
        public_id=str(uuid.uuid4()),
        email='johndoe@example.com',
        password_hash=generate_password_hash('password123')
    )
    user2 = User(
        username='janedoe',
        public_id=str(uuid.uuid4()),
        email='janedoe@example.com',
        password_hash=generate_password_hash('password123')
    )
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()  # Commit users to get their IDs

    # Create sample records
    record1 = Record(
        title='Lost Dog',
        description='Lost my dog near the park.',
        location='Central Park',
        user_id=user1.id,
        status='open',
        created_at=datetime.now()
    )
    record2 = Record(
        title='Found Wallet',
        description='Found a wallet near the subway station.',
        location='5th Avenue',
        user_id=user2.id,
        status='resolved',
        created_at=datetime.now()
    )
    db.session.add(record1)
    db.session.add(record2)
    db.session.commit()  # Commit records to get their IDs

    # Create sample images
    image1 = Image(
        url='http://example.com/dog.jpg',
        record_id=record1.id
    )
    image2 = Image(
        url='http://example.com/wallet.jpg',
        record_id=record2.id
    )
    db.session.add(image1)
    db.session.add(image2)

    # Create sample videos
    video1 = Video(
        url='http://example.com/dog_video.mp4',
        record_id=record1.id
    )
    video2 = Video(
        url='http://example.com/wallet_video.mp4',
        record_id=record2.id
    )
    db.session.add(video1)
    db.session.add(video2)

    # Commit the changes
    db.session.commit()

if __name__ == '__main__':
    from myapp import create_app
    app = create_app()
    with app.app_context():
        seed()
