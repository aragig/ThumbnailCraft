import yaml
import os

class Presets:
    def __init__(self, main_yaml_path, common_yaml_dir):
        self.main_yaml_path = main_yaml_path
        self.common_yaml_dir = common_yaml_dir

        self.base_path = None
        self.font_path = None
        self.out_path = None
        self.logo_path = None
        self.icon_path = None

        self.text = None
        self.subtext = None
        self.text_center = None
        self.common_yaml = None
        self.bg_color = None

        self.font_size = None
        self.font_color = None

        self.margin = None

        self.stroke_width = None
        self.stroke_color = None
        self.double_stroke = None

        self.logo_scale = None
        self.icon_scale = None
        self.icon_alpha = None

        self.text_y = None
        self.icon_y = None
        self.subtext_font_path = None

        self.load_yaml()

    def load_yaml(self):
        try:
            with open(self.main_yaml_path) as f:
                yaml_obj = yaml.safe_load(f)
                self.match(yaml_obj)
        except FileNotFoundError:
            print(f"Error: ファイル '{self.main_yaml_path}' が見つかりませんでした。")
            raise FileNotFoundError
        except Exception as e:
            print(f"Error: ファイルの読み込み中に予期せぬエラーが発生しました: {e}")
            raise e

        try:
            common_yaml = yaml_obj['common_yaml']
            common_yaml_path = os.path.join(self.common_yaml_dir, common_yaml)
            with open(common_yaml_path) as f:
                yaml_obj = yaml.safe_load(f)
                self.match(yaml_obj)
                # self.dump()
        except FileNotFoundError:
            print(f"Error: ファイル '{common_yaml_path}' が見つかりませんでした。")
            raise FileNotFoundError
        except Exception as e:
            print(f"Error: ファイルの読み込み中に予期せぬエラーが発生しました: {e}")
            raise e

    def match(self, yaml):
        if self.base_path is None:
            try:
                self.base_path = yaml['base_path']
            except:
                pass

        if self.logo_path is None:
            try:
                self.logo_path = yaml['logo_path']
            except:
                pass

        if self.icon_path is None:
            try:
                self.icon_path = yaml['icon_path']
            except:
                pass

        if self.out_path is None:
            try:
                self.out_path = yaml['out_path']
            except:
                pass

        if self.text is None:
            try:
                self.text = yaml['text']
            except:
                pass

        if self.subtext is None:
            try:
                self.subtext = yaml['subtext']
            except:
                pass

        if self.subtext_font_path is None:
            try:
                self.subtext_font_path = yaml['subtext_font_path']
            except:
                pass

        if self.font_size is None:
            try:
                self.font_size = yaml['font_size']
            except:
                pass

        if self.font_path is None:
            try:
                self.font_path = yaml['font_path']
            except:
                pass

        if self.bg_color is None:
            try:
                self.bg_color = tuple(yaml['bg_color'])
            except:
                pass

        if self.font_color is None:
            try:
                self.font_color = tuple(yaml['font_color'])
            except:
                pass

        if self.stroke_color is None:
            try:
                self.stroke_color = tuple(yaml['stroke_color'])
            except:
                pass

        if self.stroke_width is None:
            try:
                self.stroke_width = yaml['stroke_width']
            except:
                pass

        if self.double_stroke is None:
            try:
                self.double_stroke = yaml['double_stroke']
            except:
                pass

        if self.text_center is None:
            try:
                self.text_center = yaml['text_center']
            except:
                pass

        if self.logo_scale is None:
            try:
                self.logo_scale = yaml['logo_scale']
            except:
                pass

        if self.icon_scale is None:
            try:
                self.icon_scale = yaml['icon_scale']
            except:
                pass

        if self.icon_alpha is None:
            try:
                self.icon_alpha = yaml['icon_alpha']
            except:
                pass

        if self.text_y is None:
            try:
                self.text_y = yaml['text_y']
            except:
                pass

        if self.icon_y is None:
            try:
                self.icon_y = yaml['icon_y']
            except:
                pass

    def dump(self):
        print(vars(self))
