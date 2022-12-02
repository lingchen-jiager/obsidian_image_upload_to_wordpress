# obsidian_image_upload_to_wordpress
## English
### Upload_single_file.py
Use rest api to upload an img to your wordpress. 

This tool can upload jpg/gif/png ,of course **you can change the code to upload other filetype**.

For example,you can change "Content-Type"'s value to "video/mp4" to upload mp4.

### UploadObsidianLocalImg_and_ChangeLocalPathToUrl.py
This tool will read the test.md file and find all texts with features like ![[123.png]] (jpg/gif format can also be found),

Then upload "123.png" to wordpress,

And get the url on wordpress assuming it is "https://yourwordpress.com/123.jpg"

Replace ![[123.png]] with ![](https://yourwordpress.com/123.jpg)

Then rewrite it to the "replaced_test.md" file.

In addition, by default, all local pictures are located in the upper folder of this py file.

Files converted by this tool can be published with obsidian's third-party plugin "wordpress".

link: https://github.com/devbean/obsidian-wordpress

## 中文
### upload_single_file.py

使用wordpress的rest api来给你的wordpress上传图片

upload_single_file.py这个文件可以上传单个文件，支持jpg/gif/png，当然你也可以修改代码来上传别的类型文件。

比如把"Content-Type"的值改成"video/mp4"，就可以实现mp4的上传。


### UploadObsidianLocalImg_and_ChangeLocalPathToUrl.py
简单讲：将md文件中用到的本地图片传到你的wordpress并获取对应的图片url，将![[123.png]]这种本地连接替换为![]("https://xxx/123.png")这种形式。

然后你就可以使用第三方obsidian插件"wordpress"发布文章到wordpress。或者如果你想使用python发布到wordpress，可以参考：



此工具将读取test.md文件，发现所有特征像![[123.png]]的文本（jpg/gif格式也可以发现），

然后将"123.png"上传到wordpress，

并获取到wordpress上的url，假设是"https://yourwordpress.com/123.jpg"

之后将![[123.png]]替换成![](https://yourwordpress.com/123.jpg)

再重新写入到”replaced_test.md“文件中。

另外默认所有本地图片都位于这个py文件的上层文件夹。

这个工具转换后的文件可以用obsidian的第三方插件"wordpress"发布。

link：https://github.com/devbean/obsidian-wordpress
