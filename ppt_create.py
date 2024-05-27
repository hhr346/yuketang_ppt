from pptx import Presentation
from pptx.util import Inches

# 创建一个PPT对象
prs = Presentation()

# 图片文件路径列表
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']

# 遍历图片路径列表，将每张图片插入到PPT中
for image_path in image_paths:
    slide_layout = prs.slide_layouts[6]  # 使用空白布局
    slide = prs.slides.add_slide(slide_layout)
    left = top = Inches(0)  # 将图片放置在页面的左上角
    width = prs.slide_width
    height = prs.slide_height
    slide.shapes.add_picture(image_path, left, top, width, height)

# 保存PPT文件
prs.save('images.pptx')