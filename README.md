# mygit
牧原股份股评爬虫
第一步 :scrapy startproject 项目名
第二步：在spider文件夹 scrapy genspider py文件名
第三步：主py文件
第四步：pipline解析
tips:setting要放开注释
注意直接xpath，然后设置页码

![image](https://user-images.githubusercontent.com/92196058/161422036-d2770cf7-f5b1-4658-b100-44107340e5be.png)
pipline解析，注意根据获取内容不同，清洗不同
![image](https://user-images.githubusercontent.com/92196058/162144540-00b5ce14-8341-4d64-8218-5452887a5f16.png)
setting放开注释，加入warning
![image](https://user-images.githubusercontent.com/92196058/162144708-e6b025e3-2451-449a-80f8-c7d1e287c8ba.png)
![image](https://user-images.githubusercontent.com/92196058/162144827-6a780689-15d5-4029-96c3-7b980420c444.png)
items写入字典
![image](https://user-images.githubusercontent.com/92196058/162145062-543dfbbe-7482-4e81-b788-5e1f729ca74f.png)

