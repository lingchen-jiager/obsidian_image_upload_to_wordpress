'''
更新时间：2022/12/02
使用：
1.将你的wordpress用户名，密码，域名填写到data.json文件中
2.注意保证：所有引用的本地图片、md文件与这个py文件和data.json位于同一文件夹下。
3.在data.json中填写wordpress域名的时候，填写”https://www.youdomin.com/index.php“或者”https://www.youdomin.com“，两个都试一下，不同版本的接口不一样
原理：
此工具将读取选择的md文件，发现所有特征像![[123.png]]的文本（jpg/gif格式也可以发现），
然后将"123.png"上传到wordpress，
并获取到wordpress上的url，假设是"https://yourwordpress.com/123.jpg"
之后将![[123.png]]替换成![](https://yourwordpress.com/123.jpg)
再重新写入到”replaced_test.md“文件中。
这个工具转换后的文件可以用obsidian的第三方插件"wordpress"发布到你的wordpress网站。
link：https://github.com/devbean/obsidian-wordpress
***********************************************************
Usage：
1.Fill in your wordpress username, password, and domain name into the data.json file.
2.Note that all referenced local images, md files, this py file and data.json are located in the same folder.
3.When filling in the WordPress domain name in data.json, fill in "https://www.youdomin.com/index.php" or
"https://www.yourdomin.com", if one fails, try the other.

Principle：
This tool will read the .md file that you choose and find all texts with features like ![[123.png]] (jpg/gif format can also be found),
Then upload "123.png" to wordpress,
And get the url on wordpress assuming it is "https://yourwordpress.com/123.jpg"
Replace ![[123.png]] with ![](https://yourwordpress.com/123.jpg)
Then rewrite it to the "replaced_test.md" file.

The file converted by this tool can be published to your wordpress with obsidian's third-party plugin "wordpress".
link: https://github.com/devbean/obsidian-wordpress
'''
import json,easygui
import os,re
import requests
from datetime import datetime, timedelta

# get username,passwd,domin
with open("data.json",encoding="utf-8")as fe:
    data = fe.read()
data_format = json.loads(data)
yourusername = data_format["username"]      #wordpress username
yourpassword = data_format['password']          #wordpress password
yourdomin = data_format["domin"] #https://www.yourdomin.com/index.php  OR https://www.yourdomin.com

# choose .md file
file_list = os.listdir()
md_list =[]
for i in file_list:
    if i[-3:] == '.md':
        md_list.append(i)
if md_list == []:
    easygui.msgbox("This folder has no *.md file")
    os.exit()
else:
    filename  = easygui.choicebox(msg="please select the md file you want to convert",choices=md_list,title="公众号:零晨的小工具箱")  #获取当前选择的md文件




md_content = []   #test.md  content 存放test.md内容
md_jpg_list = []  #find all  ！[[xxx.png/png/jpg]] 找到所有！[[]]格式的匹配文本
md_jpg_list_striped = []  #strip "![[" and "]]" 去除多余符号
md_upload_img_url = []  # wordpress img url  上传到wordpress后获取的图片链接


with open(filename ,"r",encoding='utf-8')as fe:
    md_content = fe.read()
md_jpg_list = re.findall("!\[\[.*[png|jpg|gif]]]?",md_content)
md_jpg_list_striped = [i.strip("![[").strip(']]') for i in md_jpg_list] #去掉“![[”和"]]"




def upload_img(input_img_name): #传入的需要是当前文件夹下的jpg图片名称

    if input_img_name[-3:].lower()=="jpg": #这里设置引入图片的格式
        content_type = 'image/jpg'
    elif input_img_name[-3:].lower()=="png":
        content_type = 'image/png'
    elif input_img_name[-3:].lower()=="gif":
        content_type = 'image/gif'

    media_url = yourdomin + "/wp-json/wp/v2/media" #change to your site url .if the request failed you can delete "index.php" and retry.
    img_name = input_img_name
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
                                auth=(yourusername, yourpassword))
    user = json.loads(res.text)
    # 获取上传的链接 get img url in your wordpress
    upload_img_url = user["guid"]['rendered']
    md_upload_img_url.append(upload_img_url)

#upload imgs.Note that imgs,md,data.json and this py file should be located in the same folder.  这里是上传图片操作，默认图片、md文件,data.json,这个py文件位于同一文件夹
for i in md_jpg_list_striped:
    print(i)
    upload_img(i)

for i in range(len(md_jpg_list)):  #change ！[[123.png]] to ![](https://yourwordpress.com/123.png)
    print(md_jpg_list[i])
    print(md_upload_img_url[i])
    md_content = md_content.replace(md_jpg_list[i], f"![]({md_upload_img_url[i]})")

with open(f"replaced_{filename}.md",'w',encoding="utf-8")as fe:    #save to replaced_test.md 保存到新文件
    fe.write(md_content)

easygui.msgbox("转换完成!\nFinished!")
