import unittest
import ThumbnailCraft as tc
import os


class TestMarkdownToHtml(unittest.TestCase):

    def test_craft(self):
        output_file_path = "output/output.png"
        common_dir = "./common"
        main_yaml_path = "eyecatch.yml"

        thumb_craft = tc.ThumbnailCraft(common_dir)
        thumb_craft.process(main_yaml_path).output(output_file_path)

        self.assertTrue(os.path.exists(output_file_path))


if __name__ == '__main__':
    unittest.main()
