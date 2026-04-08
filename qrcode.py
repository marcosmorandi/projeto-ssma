
import qrcode

url = "https://meusite.netlify.com"
img = qrcode.make(url)
img.save("qrcode_meusite.png")
