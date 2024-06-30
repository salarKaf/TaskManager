from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes='bcrypt', deprecated='auto')

class Hash:
    @staticmethod
    def bcrypt(password):
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed_password, Plain_password):
        return pwd_cxt.verify(Plain_password ,hashed_password)