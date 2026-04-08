
import qrcode

url = "https://meusite.vercel.app"
img = qrcode.make(url)
img.save("qrcode_meusite.png")
