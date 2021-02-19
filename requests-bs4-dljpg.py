import requests
import shutil


def download_img_from_article(img_url, img_name):
    r = requests.get(img_url, stream=True)
    file_name = img_name
    print('save img to  ./image/' + file_name + '.jpg')
    try:
        with open('./' + file_name + '.jpg', 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
    except:
        print('can not save img', img_url)


img_url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
img_name = 'google'
download_img_from_article(img_url, img_name)
# r = requests.get(img_url, stream=True)
# file_name = img_name
# with open('./' + file_name + '.jpg', 'wb+') as out_file:
#     shutil.copyfileobj(r.raw, out_file)
