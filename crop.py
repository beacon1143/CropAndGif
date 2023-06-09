import os
from PIL import Image

images = []

cur_dir = os.getcwd()
new_dir = "cropped"
path = os.path.join(cur_dir, new_dir)
if not os.path.exists(path):
    os.mkdir(path)

for root, dirs, files in os.walk("."):  
    for filename in files:
        if filename[filename.find('.') + 1 :] == 'png':
            try:
                im = Image.open(filename)
            except FileNotFoundError:
                break
            just_name = filename[0 : filename.find('.')]
            print(just_name)
            im_crop = im.crop((200, 0, 1329, 484))
            #im_crop.show()
            full_name = 'cropped/' + just_name + '_.png'
            images.append(im_crop)
            im_crop.save(full_name)
images[0].save(
    'evolution.gif',
    save_all=True,
    append_images=images[1:],
    optimize=False,
    duration=400,
    loop=0
)
