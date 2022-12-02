'''
此工具将读取test.md文件，发现所有特征像![[123.png]]的文本（jpg/gif格式也可以发现），
然后将"123.png"上传到wordpress，
并获取到wordpress上的url，假设是"https://yourwordpress.com/123.jpg"
之后将![[123.png]]替换成![](https://yourwordpress.com/123.jpg)
再重新写入到”replaced_test.md“文件中。

另外默认所有本地图片都位于这个py文件的上层文件夹。
这个工具转换后的文件可以用obsidian的第三方插件"wordpress"发布。
link：https://github.com/devbean/obsidian-wordpress
***********************************************************
This tool will read the test.md file and find all texts with features like ![[123.png]] (jpg/gif format can also be found),
Then upload "123.png" to wordpress,
And get the url on wordpress assuming it is "https://yourwordpress.com/123.jpg"
Replace ![[123.png]] with ![](https://yourwordpress.com/123.jpg)
Then rewrite it to the "replaced_test.md" file.

In addition, by default, all local pictures are located in the upper folder of this py file.
Files converted by this tool can be published with obsidian's third-party plugin "wordpress".
link: https://github.com/devbean/obsidian-wordpress
'''


import json
import os,re
import requests
from datetime import datetime, timedelta
filename = input("please input filename like test.md")   #input file path 输入md文件路径
md_content = []   #test.md  content 存放test.md内容
md_jpg_list = []  #find all  ！[[xxx.png/png/jpg]] 找到所有！[[]]格式的匹配文本
md_jpg_list_striped = []  #strip "![[" and "]]" 去除多余符号
md_upload_img_url = []  # wordpress img url  上传到wordpress后获取的图片链接
with open(filename ,"r",encoding='utf-8')as fe:
    md_content = fe.read()


md_jpg_list = re.findall("!\[\[.*[png|jpg|gif]]]?",md_content)
print(md_jpg_list)
md_jpg_list_striped = [i.strip("![[").strip(']]') for i in md_jpg_list] #去掉“![[”和"]]"
print(md_jpg_list)



def upload_img(input_img_name): #传入的需要是当前文件夹下的jpg图片名称

    if input_img_name[-3:].lower()=="jpg": #这里设置引入图片的格式
        content_type = 'image/jpg'
    elif input_img_name[-3:].lower()=="png":
        content_type = 'image/png'
    elif input_img_name[-3:].lower()=="gif":
        content_type = 'image/gif'

    media_url = "https://www.yourdomin.com/index.php/wp-json/wp/v2/media" #change to your site url .if the request failed you can delete "index.php" and retry.
    img_name = input_img_name
    date_now = datetime.now() - timedelta(days=1)
    # date_now =  datetime.now()
    today = date_now.strftime('%Y-%m-%dT%H:%M:%S')
    print("Today's date:", today)
    with open(img_name, 'rb')as fe:
        data = fe.read()
    fileName = os.path.basename(img_name)
    res = requests.post(media_url,
                                data=data,
                                headers={'Content-Type': content_type,
                                         'Content-Disposition': 'attachment; filename=%s' % fileName},
                                auth=('yourusername', 'yourpassword'))  #Attention！ input your wordpress username password.注意，这里填写你的账号密码
    user = json.loads(res.text)
    upload_img_url = user["guid"]['rendered'] #获取上传的链接 get img url in your wordpress
    md_upload_img_url.append(upload_img_url)





for i in md_jpg_list_striped:
    print(i)
    upload_img("../"+i) #upload imgs，My pictures are located in the upper folder of the py file  这里是上传图片操作，默认图片位于py文件的上层文件夹

for i in range(len(md_jpg_list)):  #change ！[[123.png]] to ![](https://yourwordpress.com/123.png)
    print(md_jpg_list[i])
    print(md_upload_img_url[i])
    md_content = md_content.replace(md_jpg_list[i], f"![]({md_upload_img_url[i]})")

with open(f"replaced_{filename}.md",'w',encoding="utf-8")as fe:    #save to replaced_test.md 保存到新文件
    fe.write(md_content)

