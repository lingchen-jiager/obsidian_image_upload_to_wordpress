from datetime import datetime, timedelta
import requests,os,json
def upload_img(img_name): #the img filename you want to upload 你要上传的文件名
    if img_name[-3:].lower()=="jpg": #judge the filetype    判断文件类型
        content_type = 'image/jpg'
    elif img_name[-3:].lower()=="png":
        content_type = 'image/png'
    elif img_name[-3:].lower()=="gif":
        content_type = 'image/gif'
    media_url = "https://www.yourdomin.com/index.php/wp-json/wp/v2/media"
    #or   media_url = "https://www.yourdomin.com/wp-json/wp/v2/media"
 #maybe the "index.php/" in this url can be deleted,but my wordpress need it,otherwise the request will be failed.
#改成你的wordpress网址，可能不需要加"index.php/"，但是我的版本需要加上才能正常返回数据
    date_now = datetime.now() - timedelta(days=1)
    # date_now =  datetime.now()
    today = date_now.strftime('%Y-%m-%dT%H:%M:%S')
    # print("Today's date:", today)
    with open(img_name, 'rb')as fe:
        data = fe.read()
    fileName = os.path.basename(img_name)
    res = requests.post(media_url,
                                data=data,
                                headers={'Content-Type': content_type,
                                         'Content-Disposition': 'attachment; filename=%s' % fileName},
                                auth=('username', 'password'))   #your wordpress username and password 填上wordpress的用户名和密码
    user = json.loads(res.text)
    upload_img_url = user["guid"]['rendered'] #get the img url 获取刚刚上传的图片网址
    print(upload_img_url)



upload_img("D:/img.gif")  #the img path.filetype can be jpg/gif/png 填上图片的路径 支持jpg/gif/png


