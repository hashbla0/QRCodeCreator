import qrcode
import argparse
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

parser = argparse.ArgumentParser(description="QR-Code-Erstellung.")
parser.add_argument("url", type=str, help="Die URL, auf die der Code verweisen soll")
parser.add_argument("name", type=str, help="Der Name der Bilddatei, die im aktuellen Verzeichnis erstellt wird")
args = parser.parse_args()

# Ziel-URL
url = args.url
imgname = f"./{args.name}"

# QR-Code-Objekt erstellen
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# QR-Code-Bild mit abgerundeten Kästchen erstellen
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(back_color=(246, 242, 231), front_color=(0, 0, 0))
)

# Bild speichern
img.save(imgname)
print(f"QR-Code gespeichert als {imgname}")
