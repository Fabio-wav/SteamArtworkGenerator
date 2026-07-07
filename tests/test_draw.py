from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Cria uma imagem preta
image = Image.new("RGBA", (500, 300), (0, 0, 0, 255))

# Cria um "lápis"
draw = ImageDraw.Draw(image)

# Carrega a fonte
font = ImageFont.truetype(
    "assets/fonts/consola.ttf",
    30
)

# Desenha o texto
draw.text(
    (200, 180),
    "CAPETINHA.EXE",
    font=font,
    fill=(255, 0, 0)
)

# Salva
output = Path("output")
output.mkdir(exist_ok=True)

image.save(output / "test.png")

print("Imagem criada!")