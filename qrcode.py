
import qrcode

url = "https://projeto-ssma.netlify.app"
img = qrcode.make(url)
img.save("qrcode_meusite.png")
