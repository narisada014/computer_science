from secrets import token_bytes
from typing import Tuple
from PIL import Image
from io import BytesIO


# 画像を読み込んでByte文字列として返してやる
def get_bin_from_image() -> str:
    img = Image.open("./sake.jpg")
    with BytesIO() as output:
        # 画像をBytesIOオブジェクトoutputとして保存
        img.save(output, format="JPEG")
        contents: str = output.getvalue()  # バイナリからバイト文字列を取得
        return contents


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


# バイト文字列を入力としてdummyキーと暗号化したデータをintとしてreturn
def encrypt(original_bytes: bytes) -> Tuple[int, int]:
    # オリジナル文字列のバイトの長さのランダムな数値を生成する
    dummy: int = random_key(len(original_bytes))
    # オリジナル文字列のバイトから数値を生成する
    # この時点でdummyとoriginal_keyの数値のバイト長さは同じ
    original_key: int = int.from_bytes(original_bytes, "big")
    # 排他論理和で計算した結果は
    # 計算の元に使用された数値と排他論理和計算をすることで片方の数値を求めることができる特性がある！！(証明はしない)
    encrypted: int = original_key ^ dummy # XOR
    return dummy, encrypted


def decrypt(key_1: int, key_2: int) -> bytes:
    decrypted: int = key_1 ^ key_2
    # to_bytesの引数はバイト長なので
    # intをbitに直し、それをバイトに直す必要があるので8で割る必要がある(32 bit →4 byte)
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return temp


if __name__ == "__main__":
    image_bin = get_bin_from_image()
    key_1, key_2 = encrypt(image_bin)
    decrypt_image_bytes_str = decrypt(key_1, key_2)
    decrypt_image = Image.open(BytesIO(decrypt_image_bytes_str))
    decrypt_image.save("decrypt_sake.jpg")
