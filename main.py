from cv2 import CAP_PROP_FPS, VideoCapture, imshow, waitKey, destroyAllWindows
from time import sleep
from os import remove
from uuid import uuid4
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
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA512
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet

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

def encrypt_video(remove_old: bool = True):
    '''Encrypt a video and write a new video password encrypted'''
    name = input('Video name: ')
    with open(name, 'rb') as file:
        data = file.read()

    if remove_old: remove(name)

    password = input('Video password: ')

    cipher = get_cipher(password.encode(), SALT)
    new_data = cipher.encrypt(data)

    new_name = str(uuid4())[:8] + '.MEVP'
    with open(new_name, 'wb') as new_file:
        new_file.write(new_data)

def play_encrypted_video():
    name = input('Encrypted video name: ')



def main():
    r = input('[E]encrypt video or [P]play encrypted video: ').lower()
    if r == 'e':
        encrypt_video(False)
    elif r == 'p':
        play_encrypted_video()



if __name__ == '__main__':
    main()