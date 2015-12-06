from django.conf import settings
import requests
import json


def publishToFacebook(product):

    album = createAlbum(product)
    if album == '':
        print ('Cannot create Facebook Album for this product!')
        return

    albumId = json.loads(album)['id']
    access_token = settings.FB_ACCESS_KEY
    caption = product.name + '\\r\\n Giá: ' + str(int(product.price)) + ' vnd' + '\\r\\n\\r\\n' + product.description
    caption += '\\r\\n\\r\\n Đặt mua tại: ' + settings.ROOT_URL + '/products/' + str(product.id)

    batch = '['
    batch += extractImage(caption, product.avatar, albumId)
    batch += extractImage(caption, product.image1, albumId)
    batch += extractImage(caption, product.image2, albumId)
    batch += extractImage(caption, product.image3, albumId)
    batch += extractImage(caption, product.image4, albumId)
    batch += extractImage(caption, product.image5, albumId)
    batch += ']'
    response = requests.post(settings.FB_URL, params={'access_token':access_token, 'batch':batch})

    print (caption)
    print ('Batch: ', batch)
    print ('Facebook Request: ', response.url)
    print ('Facebook Response Code: ', response.status_code, response.reason)
    print ('Facebook Response Text: ', response.text)


def createAlbum(product):
    access_token = settings.FB_ACCESS_KEY
    name = product.name
    description = product.description

    response = requests.post(settings.FB_V5+'/me/albums', params={'access_token':access_token, 'name': name, 'description': description})
    print("Facebook Creating Album Response:")
    print(response.status_code, response.reason, response.text)

    if response.status_code != 200:
        return ''
    else:
        return response.text


def extractImage(caption, image, albumId):
    # url = 'http://www.keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image1.jpg'
    url = settings.ROOT_URL + 'media/' + str(image)
    if not image:
        return ''
    else:
        return '{"method":"POST", "relative_url":"' + albumId + '/photos", "body":"caption=' + caption + '&url='+url+'"},'
