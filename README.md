# obsidian_image_upload_to_wordpress
## English
### Upload_single_file.py
Use rest api to upload an img to your wordpress. 

This tool can upload jpg/gif/png ,of course **you can change the code to upload other filetype**.

For example,you can change "Content-Type"'s value to "video/mp4" to upload mp4.

### UploadObsidianLocalImg_and_ChangeLocalPathToUrl.py

Upload the local image used in the md file to your wordpress and get the corresponding image url, replace the local link like ![[123.png]] with !\[]("https://xxx/123 .png").

Before using this python script you must first install the plugin "WordPress REST API Authentication" for your WordPress.

[Click here learn how to set the plugin?](https://github.com/lingchen-jiager/obsidian_image_upload_to_wordpress/blob/main/UploadObsidianLocalImg_and_ChangeLocalPathToUrl/set_plugin.md)

**comparison:**
<img width="960" alt="转换前后" src="https://user-images.githubusercontent.com/48639047/205258394-b3ac653c-8a13-438f-95a6-183535006ec6.png">


Then you can use the third-party obsidian plugin "wordpress" to publish articles to wordpress.

Third-party plug-in link: https://github.com/devbean/obsidian-wordpress

Or if you want to publish articles to wordpress using python,

You can refer to: https://github.com/winosli/Add-post-to-WordPress-with-rest-API, upload_single_file.py is also rewritten from this script, thanks to the author.

## 中文
### upload_single_file.py
使用wordpress的rest api给你的wordpress上传图片

upload_single_file.py这个文件可以上传单个文件，支持jpg/gif/png，当然你也可以修改代码来上传别的类型文件。

比如把"Content-Type"的值改成"video/mp4"，就可以实现mp4的上传。

### UploadObsidianLocalImg_and_ChangeLocalPathToUrl.py
简单讲：将md文件中用到的本地图片传到你的wordpress并获取对应的图片url，将![[123.png]]这种本地链接替换为!\[]("https://xxx/123.png")这种形式。
注意：使用这个python脚本之前你必须先给你的wordpress安装插件"WordPress REST API Authentication"，如何设置见：
[插件设置方法](https://github.com/lingchen-jiager/obsidian_image_upload_to_wordpress/blob/main/UploadObsidianLocalImg_and_ChangeLocalPathToUrl/set_plugin.md)

**前后对比:**

<img width="960" alt="转换前后" src="https://user-images.githubusercontent.com/48639047/205258394-b3ac653c-8a13-438f-95a6-183535006ec6.png">

然后你可以使用第三方obsidian插件"wordpress"发布文章到wordpress。

第三方插件链接：https://github.com/devbean/obsidian-wordpress

或者如果你想使用python发布文章到wordpress，

可以参考：https://github.com/winosli/Add-post-to-WordPress-with-rest-API, upload_single_file.py也是由此脚本改写，在此对作者表示感谢。



