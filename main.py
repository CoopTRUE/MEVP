from cv2 import CAP_PROP_FPS, VideoCapture, imshow, waitKey, destroyAllWindows
from time import sleep

# cap = VideoCapture('trolol.mp4')
# assert cap.isOpened()

# wait = int(1/cap.get(CAP_PROP_FPS)*1000)


# read, frame = cap.read()
# while read:
#     imshow('Frame', frame)
#     read, frame = cap.read()
#     if waitKey(wait) & 0xFF == ord('q'):
#         break
# cap.release()
# destroyAllWindows()
SALT = b'hi'
def get_cipher(password: bytes, salt: bytes):
    '''Create and return a cipher using a password and salt'''
    kdf = PBKDF2HMAC(
        algorithm=SHA512(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    encrypted_password = urlsafe_b64encode(kdf.derive(password))
    cipher = Fernet(encrypted_password)
    return cipher
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA512
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet


if __name__ == '__main__':
    print(get_cipher(b'hi', SALT))