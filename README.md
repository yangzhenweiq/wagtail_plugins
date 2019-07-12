## tutor wagtail 插件。

参考文档： https://docs.tutor.overhang.io/plugins.html

安装插件

    pip install -e .

开启插件：

 tutor plugins enable wagtail
 
保存配置：

 tutor config save 

前提：需要通过插件的Dockerfile来build images： 

    hooks = {
        "build-image": {"myimage": "myimage:latest"}
    }
    
使用此钩子，用户将能够myimage:latest通过运行以下命令来构建docker镜像：
tutor images build wagtail

执行：

tutor local quickstart

此过程会默认创建 admin/admin 管理员账号，并且同步数据库。

访问 http://wagtail.localhost/admin/




