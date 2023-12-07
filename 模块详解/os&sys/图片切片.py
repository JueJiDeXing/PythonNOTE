import os
import re
from PIL import Image


def sliceImage(path: str) -> None:
    """
    输入一张png格式的图片,缩放至420*420大小
    然后将其16等分,每块大小105*105
    @:param path 文件路径

    """
    print("开始对图片切片")
    # 打开原图
    original_image = Image.open(path)
    # 居中裁剪
    width, height = original_image.size
    size = min(width, height)
    start_x = (width - size) // 2
    start_y = (height - size) // 2
    end_x = start_x + size
    end_y = start_y + size
    cut_image = original_image.crop((start_x, start_y, end_x, end_y))
    # 缩放
    target_size = (420, 420)
    cut_image.thumbnail(target_size)
    # 切割
    row = 4
    columns = 4
    count = 1
    out_width = target_size[0] // columns
    out_height = target_size[1] // row
    for j in range(row):
        for i in range(columns):
            start_x = i * out_width
            start_y = j * out_height
            end_x = start_x + out_width
            end_y = start_y + out_height
            out_image = cut_image.crop((start_x, start_y, end_x, end_y))
            # 保存
            out_image.save(path + f"\\{str(count)}.png")
            count += 1
    cut_image.save(path + "\\all.png")
    print("切片完成,当前目录文件有:\n", os.listdir(path))


path = r"E:\ideaProject\puzzleGame\image\Xue\xue_5\all.png"
sliceImage(path)


def change_suffix_name(path, new_suffix='jpg'):
    print("开始更改后缀名")
    for i in os.listdir(path):
        old_suffix = re.split(r"\.", i)[-1]
        os.replace(path + f"\\{i}",
                   path + f"\\{i.replace(old_suffix, new_suffix)}")
    print("已全部更改后缀名")


change_suffix_name(path)
os.remove(path + "\\16.jpg")
