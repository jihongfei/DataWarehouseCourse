# DataWarehouseCourse

# 置顶公告

## 平台
 1. 请勿超时！目前单个实验时间是2h。
 2. 由于平台不稳定，做出结果后请在本地备份以防提交失败。
 3. Web 端支持的不够好，复制需要选中后右键点击复制，粘贴需要右键选择粘贴。
 4. 如无法正确打开网页请换Chrome+4g网试试。

## 作业
 1. **第四周需完成BDP分析并提交pdf版报告**
 3. 每周四晚24点前提交上周作业，周五会统计。

# 课件
 1. 网盘链接(**第四周课件--数据仓库建模--已上传**)：http://pan.baidu.com/s/1o7S6DoI 密码：6u73

# 第四周实验内容
 1. 微信群和百度网盘（http://pan.baidu.com/s/1i5MlZr3 密码：7wvi）有pdf版

# 关于实验六/七
 1. 关于数据导入的博文：https://www.iteblog.com/archives/949.html
 2. 关于分区表的博文：http://blog.sina.com.cn/s/blog_6ff05a2c0100tah0.html
 3. 平台上实验指导流程有缺陷！请使用pdf版指导： http://pan.baidu.com/s/1i5MlZr3 密码：7wvi

# 关于实验四
 1. 3.2-(2)-设置环境变量，这里需要按以下步骤先启动ssh服务：
	1. 执行sudo vi /etc/profile 前先用exit退出到root用户
	2. 修改并保存/etc/profile
	3. Sudo service ssh start
	4. 切回到hadoop用户，su - hadoop
 2. 如果无法关闭hbase可参考 http://blog.csdn.net/u010027484/article/details/51879262
 3. 把 ${user.name}和 替换为 hadoop，把 ${HBase-Dir} 替换为你机器上HBase的安装目录


# 关于实验三
	
 1. 在“四、Hadoop集群启动”处，需要先执行

    `$ exit`
    
	命令退出当前用户，到默认用户，然后执行
	
    `$ sudo service ssh start`

	然后再用

    `$ su - hadoop`

	切换回hadoop用户，执行

    `$ start-dfs.sh`

	后与实验指导一致。
	

# 关于实验二
	
 1. 作业是对日志文件dpkg.log做词频统计，别做错了！!
 2. 作业第一问，需要仿照“六、测试验证”，把你输入的命令复制在此。
 3. 作业第二问，不需要cat命令取出的统计结果（太长了！），把运行hadoop jar xxxx 后的控制台输出内容复制在此即可。


    
# VIM简易指南
 1. 分为编辑模式和命令模式
 2. 命令：

 	光标上 k
 	
	光标下 j
	
	光标前 h
	
	光标后 l
	
	光标前键入 i
	
	光标后键入 a
	
	下一行键入 o
	
	删除行 dd
	
	撤销 u
	
	保存 :wq
	
	放弃保存 :q!
	
	删除光标处字符 x
	
	查找 / (下一个 n)


	
