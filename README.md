# ThumbnailCraft

ブログなどのサムネ、アイキャッチ画像を作成するPythonパッケージです。

![ThumbnailCraft](./logo.png)



## インストール

```zsh
pip3 install git+https://github.com/aragig/ThumbnailCraft.git
```

## 使い方
```python
import ThumbnailCraft as tc


output_file_path = "output/output.png"
common_dir = "./common"
main_yaml_path = "eyecatch.yml"

thumb_craft = tc.ThumbnailCraft(common_dir)
thumb_craft.process(main_yaml_path).output(output_file_path)
```

![生成されたサムネ](./tests/output/output.png)

## yaml記述例

個別設定例:
```yaml:eyecatch.yml
common_yaml: default.yml
subtext: サブテキストサブテキスト
text: 記事のタイトル
icon_path: scrabble.png
logo_path: logo.png
stroke_width: 10
base_path: base.jpg
```

共通設定例:
```yaml:default.yml
out_path: eyecatch.jpg

font_path: /Users/mopipico/Library/Fonts/yawarakadragon.otf

bg_color:
  - 33 # R
  - 33 # G
  - 33 # B

font_color:
  - 255 # R
  - 255 # G
  - 255 # B

stroke_color:
  - 33 # R
  - 33 # G
  - 33 # B

stroke_width: 0

logo_scale: 0.8
icon_scale: 2.0

text_center: True

```


## ファイル構成

```zsh
$ tree 
.
├── base.jpg
├── common
│   ├── icons
│   │   └── scrabble.png
│   ├── logos
│   │   └── logo.png
│   └── yml
│       └── default.yml
├── eyecatch.yml
├── output
│   └── output.png
└── test_craft.py

```