import os

from PIL import Image


def resize_image(path, max_size):

    if os.path.isfile(path):
        try:
            im = Image.open(path)
            if im.height > max_size or im.width > max_size:
                f, e = os.path.splitext(path)

                # if width > height:
                if im.width > im.height:
                    desired_width = max_size
                    desired_height = im.height / (im.width / max_size)

                # if height > width:
                elif im.height > im.width:
                    desired_height = max_size
                    desired_width = im.width / (im.height / max_size)

                else:
                    desired_height = max_size
                    desired_width = max_size

                # convert back to integer
                desired_height = int(desired_height)
                desired_width = int(desired_width)

                im_resized = im.resize((desired_width, desired_height))
                # im_resized.save(f + '_resized.jpg', 'JPEG', quality=90) # doesn't overwrite file
                if im.format == 'JPEG':
                    im_resized.save(f + e, 'JPEG', quality=80)  # does overwrite file
                elif im.format == 'PNG':
                    im_resized.save(f + e, 'PNG', quality=80)
                else:
                    print(im.format+' Unknown format')
                # im_resized.save('resized_' + f + '.jpg', 'JPEG', quality=100)
        except Exception as e:
            # TODO: add logger
            print(e)


# Template for local testing
def main():
    ...


if __name__ == '__main__':
    main()
