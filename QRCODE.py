import os
import qrcode
from PIL import Image
from pyzbar import pyzbar

thisDir = os.path.dirname(os.path.abspath(__file__))


def make_qr_code_easy(content, save_path="%s/make_qr_code_easy.jpg" % thisDir):
    img = qrcode.make(data=content)
    if save_path:
        img.save(save_path)
    else:
        img.show()


def make_qr_code(content, save_path="%s/make_qr_code_easy.jpg" % thisDir):
    # 更多参数
    qr_code_maker = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=8,
        border=1,
    )
    qr_code_maker.add_data(data=content)
    qr_code_maker.make(fit=True)
    img = qr_code_maker.make_image(fill_color="black", back_color="white")
    img.save(save_path)


def make_qr_code_with_icon(content, icon_path="%s/icon.jpg" % thisDir, save_path="%s/make_qr_code_easy.jpg" % thisDir):
    if not os.path.exists(icon_path):
        raise FileExistsError(icon_path)

    # 创建基本的QRCODE
    qr_code_maker = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=1,
    )
    qr_code_maker.add_data(data=content)
    qr_code_maker.make(fit=True)
    qr_code_img = qr_code_maker.make_image(fill_color="black",
                                           back_color="white").convert('RGBA')

    # 加载LOGO
    icon_img = Image.open(icon_path)
    code_width, code_height = qr_code_img.size
    icon_img = icon_img.resize((code_width // 4, code_height // 4),
                               Image.ANTIALIAS)

    # LOGO放置到QRCODE
    qr_code_img.paste(icon_img, (code_width * 3 // 8, code_width * 3 // 8))

    qr_code_img.save(save_path)


def decode_qr_code(code_img_path):
    """
    输入文件路径，进行解码
    中文编码问题无法解决
    """
    if not os.path.exists(code_img_path):
        raise FileExistsError(code_img_path)

    result = pyzbar.decode(Image.open(code_img_path),
                           symbols=[pyzbar.ZBarSymbol.QRCODE])
    return result[0].data


if __name__ == "__main__":
    make_qr_code_easy("text", "%s/qrcode.jpg" % thisDir)
    print(decode_qr_code("%s/qrcode.jpg" % thisDir))
