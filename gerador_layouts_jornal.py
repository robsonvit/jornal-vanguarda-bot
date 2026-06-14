import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# Configurações de tamanho (Instagram / Facebook 4:5 post)
W, H = 1080, 1350

def get_font(size):
    # Tentar pegar a fonte impact, senão fallback
    font_path = "fonts/impact.ttf" if os.path.exists("fonts/impact.ttf") else "C:\\Windows\\Fonts\\arialbd.ttf"
    try:
        return ImageFont.truetype(font_path, size)
    except:
        return ImageFont.load_default()

def create_base_image():
    # Cria uma imagem de teste simulando uma foto de jornal
    img = Image.new("RGB", (W, H), (100, 100, 100))
    draw = ImageDraw.Draw(img)
    # Padrão xadrez ou linhas para simular imagem
    for i in range(0, W, 100):
        draw.line([(i, 0), (i, H)], fill=(120, 120, 120), width=2)
    for i in range(0, H, 100):
        draw.line([(0, i), (W, i)], fill=(120, 120, 120), width=2)
    draw.text((W//2 - 150, H//2 - 50), "IMAGEM DA NOTÍCIA", fill=(200, 200, 200), font=get_font(40))
    return img

def layout_1_classico(img_base, text, tag):
    """Layout Clássico Vanguarda: Gradiente inferior escuro, título branco, tarja vermelha topo."""
    img = img_base.copy()
    
    # Gradiente
    overlay = Image.new("RGBA", (W, H), (0,0,0,0))
    draw_ov = ImageDraw.Draw(overlay)
    grad_h = int(H * 0.6)
    for y in range(H - grad_h, H):
        alpha = int(255 * ((y - (H - grad_h)) / grad_h))
        draw_ov.line([(0, y), (W, y)], fill=(0, 0, 0, min(255, alpha)))
    
    img = Image.alpha_composite(img.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(img)
    
    # Tarja
    draw.rectangle([50, 50, 350, 120], fill=(220, 20, 20))
    draw.text((200, 85), tag, fill="white", font=get_font(45), anchor="mm")
    
    # Texto
    draw.text((W//2, H - 200), text, fill="white", font=get_font(70), anchor="mm")
    draw.text((W//2, H - 100), "LEIA MAIS NO JORNAL VANGUARDA", fill=(200,200,200), font=get_font(30), anchor="mm")
    
    img.convert("RGB").save("layout_1_classico.jpg")

def layout_2_alerta(img_base, text, tag):
    """Layout Alerta (Estilo CNN): Barra inferior grossa vermelha com texto branco."""
    img = img_base.copy()
    
    # Crop para caber a barra em baixo
    img = img.resize((W, int(H * 0.75)))
    
    canvas = Image.new("RGB", (W, H), (20, 20, 20))
    canvas.paste(img, (0, 0))
    
    draw = ImageDraw.Draw(canvas)
    
    # Barra vermelha no fundo
    draw.rectangle([0, int(H * 0.75), W, H], fill=(200, 0, 0))
    
    # Tarja Amarela Breaking News
    draw.rectangle([50, int(H * 0.75) - 35, 450, int(H * 0.75) + 35], fill=(255, 200, 0))
    draw.text((250, int(H * 0.75)), tag, fill="black", font=get_font(50), anchor="mm")
    
    # Título principal na barra vermelha
    draw.text((W//2, int(H * 0.88)), text, fill="white", font=get_font(65), anchor="mm")
    
    canvas.save("layout_2_alerta.jpg")

def layout_3_revista(img_base, text, tag):
    """Estilo Revista: Fundo branco ou claro, foto emoldurada, texto escuro."""
    canvas = Image.new("RGB", (W, H), (245, 245, 245))
    
    img = img_base.resize((W - 100, int((W - 100) * 1.0)))
    canvas.paste(img, (50, 50))
    
    draw = ImageDraw.Draw(canvas)
    
    # Tag vermelha pequena
    draw.rectangle([50, 50 + img.height + 30, 250, 50 + img.height + 80], fill=(200, 20, 20))
    draw.text((150, 50 + img.height + 55), tag, fill="white", font=get_font(35), anchor="mm")
    
    # Texto grande escuro
    draw.text((50, 50 + img.height + 140), text.replace(" ", "\n", 2), fill=(20, 20, 20), font=get_font(80), anchor="ls")
    
    # Borda no canvas
    draw.rectangle([20, 20, W-20, H-20], outline=(20,20,20), width=5)
    
    canvas.save("layout_3_revista.jpg")

def layout_4_minimalista(img_base, text, tag):
    """Minimalista Moderno: Fundo escuro, foto ocupando o topo 60%, texto limpo embaixo."""
    canvas = Image.new("RGB", (W, H), (15, 15, 18))
    img = img_base.resize((W, int(H * 0.6)))
    canvas.paste(img, (0,0))
    
    draw = ImageDraw.Draw(canvas)
    
    draw.text((50, int(H*0.65)), tag, fill=(255, 100, 100), font=get_font(40))
    draw.text((50, int(H*0.75)), text, fill="white", font=get_font(75))
    
    draw.line([(50, int(H*0.9)), (200, int(H*0.9))], fill=(255,100,100), width=8)
    draw.text((50, int(H*0.92)), "JORNAL VANGUARDA", fill=(150,150,150), font=get_font(30))
    
    canvas.save("layout_4_minimalista.jpg")

def layout_5_impacto(img_base, text, tag):
    """Impacto: Imagem borrada no fundo, foto nítida no centro, barras vermelhas ao lado do texto."""
    canvas = img_base.copy().filter(ImageFilter.GaussianBlur(15))
    canvas = ImageEnhance.Brightness(canvas).enhance(0.4)
    
    img = img_base.resize((int(W*0.8), int(H*0.5)))
    canvas.paste(img, (int(W*0.1), 100))
    
    draw = ImageDraw.Draw(canvas)
    
    # Tag vermelha forte
    draw.rectangle([int(W*0.1), int(H*0.6) + 20, int(W*0.1) + 300, int(H*0.6) + 90], fill=(220, 0, 0))
    draw.text((int(W*0.1) + 150, int(H*0.6) + 55), tag, fill="white", font=get_font(45), anchor="mm")
    
    # Linha vertical vermelha ao lado do texto
    draw.line([(int(W*0.1) - 20, int(H*0.75)), (int(W*0.1) - 20, int(H*0.9))], fill=(220, 0, 0), width=10)
    
    # Texto principal
    draw.text((int(W*0.1), int(H*0.78)), text, fill="white", font=get_font(70))
    
    canvas.save("layout_5_impacto.jpg")

if __name__ == "__main__":
    img = create_base_image()
    title = "PREFEITO ANUNCIA\nNOVAS MEDIDAS"
    tag = "URGENTE"
    
    layout_1_classico(img, title, tag)
    layout_2_alerta(img, title, tag)
    layout_3_revista(img, title, tag)
    layout_4_minimalista(img, title, tag)
    layout_5_impacto(img, title, tag)
    print("5 Layouts gerados com sucesso!")
