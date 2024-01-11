from PIL import Image, ImageFont, ImageDraw
import numpy as np


def fill_crop(img, size):
    w_max, h_max = size
    r_fixed = w_max / h_max  # ratio

    w, h = img.size
    r = w / h

    if r > r_fixed:  # 横長すぎる
        img = img.resize((int(h_max / h * w), h_max))

    elif r < r_fixed:  # 縦長すぎる
        img = img.resize((w_max, int(w_max / w * h)))

    w, h = img.size

    if w > w_max or h > h_max:
        left = int((w - w_max) / 2)
        upper = int((h - h_max) / 2)
        right = left + w_max
        lower = upper + h_max

        img = img.crop((left, upper, right, lower))

    return img


def overlay_logo(base_img, path, scale):
    try:
        logo = Image.open(path)
    except:
        print(f'指定されたロゴが存在しません: {path}')
        return base_img

    base_w, base_h = base_img.size
    logo_w, logo_h = logo.size
    logo_resized = logo.resize((int(logo_w * scale), int(logo_h * scale)))  # リサイズ
    logo_resized_w, logo_resized_h = logo_resized.size
    margin_right = 100
    margin_bottom = 80
    base_img.paste(logo_resized, (base_w - logo_resized_w - margin_right, base_h - logo_resized_h - margin_bottom),
                   logo_resized)
    return base_img


def overlay_icon(base_img, path, scale, icon_alpha, icon_y):
    try:
        icon = Image.open(path)
    except:
        print(f'指定されたアイコンが存在しません: {path}')
        return base_img

    if icon_alpha is not None:
        # icon_resized.putalpha(icon_alpha)
        # putalphaだと背景が黒くなってしまうのでnumpyつかう
        icon = np.array(icon)
        icon[icon[..., 3] != 0, 3] = icon_alpha
        icon = Image.fromarray(icon)

    if icon_y is None:
        icon_y = 0

    base_w, base_h = base_img.size
    icon_w, icon_h = icon.size

    icon_resized = icon.resize((int(icon_w * scale), int(icon_h * scale)))  # リサイズ
    icon_resized_w, icon_resized_h = icon_resized.size
    try:
        base_img.paste(icon_resized, (int((base_w - icon_resized_w) / 2), int((base_h - icon_resized_h) / 2) + icon_y),
                       icon_resized)
    except:
        base_img.paste(icon_resized, (int((base_w - icon_resized_w) / 2), int((base_h - icon_resized_h) / 2) + icon_y))

    return base_img


def overlay_text(base_img, text, font_path, font_size, font_color, stroke_color, stroke_width, text_y, double_stroke,
                 text_center, subtext, subtext_font_path):
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(base_img)

    if stroke_width is None:
        stroke_width = 0

    font_w, font_h = __get_font_width(text, font)
    base_img_w, base_img_h = base_img.size

    if text_y is None:
        text_y = 0

    if text_center:
        pos = ((base_img_w - font_w) / 2, (base_img_h - font_h) / 2 + text_y)
    else:
        pos = (150, 300 + text_y)

    if double_stroke:
        draw.text(
            pos,
            text,
            font=font,
            fill=stroke_color,
            stroke_width=stroke_width * 2,
            stroke_fill=font_color)

    draw.text(
        pos,
        text,
        font=font,
        fill=font_color,
        stroke_width=stroke_width,
        stroke_fill=stroke_color)

    if subtext:
        if subtext_font_path is None:
            subtext_font_path = font_path

        x, y = pos
        subpos = (int(x + 10), int(y - 135))
        subfont = ImageFont.truetype(subtext_font_path, 110)
        if stroke_width > 0:
            sub_stroke_width = int(stroke_width / 2)
        else:
            sub_stroke_width = 0

        draw.text(
            subpos, subtext,
            font=subfont,
            fill=font_color,
            stroke_width=sub_stroke_width,
            stroke_fill=stroke_color)

    return base_img


def fit_font_size(text, font_path, stroke_width, font_size=300, limit_width=1920, margin=100):
    """
    再起処理でフォントサイズ調整
    """
    font = ImageFont.truetype(font_path, font_size)
    (width, baseline), (_, _) = font.font.getsize(text)
    if width < (limit_width - margin):
        return font_size
    #    print('{}, {}, {}, {}'.format(text, font_path, stroke_width, font_size - 5))
    return fit_font_size(text, font_path, stroke_width, font_size - 5)


def __get_font_width(text, font):
    ans_w = 0
    ans_h = 0
    for line in text.splitlines():
        (width, baseline), (_, _) = font.font.getsize(line)
        if width > ans_w:
            ans_w = width
        ans_h += baseline
    return int(ans_w), int(ans_h)
