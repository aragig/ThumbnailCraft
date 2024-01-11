import os
from .utils import image_processor
from .utils import presets


class ThumbnailCraft:

    def __init__(self, common_dir):
        self.CONST_W = 1920  # TODO コンストラクタへ渡す
        self.CONST_H = 1200  # TODO コンストラクタへ渡す
        self.img = None
        self.directory_path = None
        self.presets = None
        self.common_dir = common_dir

    def process(self, main_yaml_path):
        self.directory_path = os.path.dirname(main_yaml_path)

        common_yaml_dir = os.path.join(self.common_dir, 'yml')
        self.presets = presets.Presets(main_yaml_path, common_yaml_dir)

        try:
            self.__overlay_base_img()
        except:
            # プレーン背景を生成
            self.img = image_processor.Image.new('RGB', (self.CONST_W, self.CONST_H), self.presets.bg_color)

        self.__overlay_icon()
        self.__overlay_text()
        self.__overlay_logo()
        return self

    def output(self, output_path=None):
        if output_path is None:
            output_path = os.path.join(self.directory_path, self.presets.out_path)

        self.img.save(output_path)
        return self

    def __overlay_base_img(self):
        base_path = os.path.join(self.directory_path, self.presets.base_path)
        self.img = image_processor.Image.open(base_path)
        self.img = self.img.convert('RGB')  # OSError: cannot write mode RGBA as JPEG 対策
        self.img = image_processor.fill_crop(self.img, (self.CONST_W, self.CONST_H))

    def __overlay_icon(self):
        if self.presets.icon_path is not None:
            p = os.path.join(self.common_dir + '/icons', self.presets.icon_path)
            self.img = image_processor.overlay_icon(self.img, p, self.presets.icon_scale, self.presets.icon_alpha,
                                                    self.presets.icon_y)

    def __overlay_text(self):
        if self.presets.text is not None:
            if self.presets.font_size is None:
                self.presets.font_size = image_processor.fit_font_size(self.presets.text, self.presets.font_path,
                                                                       self.presets.stroke_width)

            self.img = image_processor.overlay_text(self.img,
                                                    self.presets.text,
                                                    self.presets.font_path,
                                                    self.presets.font_size,
                                                    self.presets.font_color,
                                                    self.presets.stroke_color,
                                                    self.presets.stroke_width,
                                                    self.presets.text_y,
                                                    self.presets.double_stroke,
                                                    self.presets.text_center,
                                                    self.presets.subtext,
                                                    self.presets.subtext_font_path)

    def __overlay_logo(self):
        if self.presets.logo_path is not None:
            p = os.path.join(self.common_dir + '/logos', self.presets.logo_path)
            self.img = image_processor.overlay_logo(self.img, p, self.presets.logo_scale)
