# DataWarehouseCourse

# Tips
	请勿超时！目前单个实验时间是2h。
	由于平台不稳定，做出结果后请在本地备份以防提交失败。

# 关于实验二
	作业部分：
	问题一，需要仿照“六、测试验证”，把你输入的命令复制在此。
	问题二，不需要cat命令取出的统计结果（太长了！），把运行hadoop jar xxxx 后的控制台输出内容复制在此即可。

# 关于实验三
	在“四、Hadoop集群启动”处，需要先执行
	$ exit
	命令退出当前用户，到默认用户，然后执行
	$ sudo service ssh start
	然后再用
	$ su - hadoop
	切换回hadoop用户，执行
	$ start-dfs.sh
	后与实验指导一致。

# VIM常用命令简易指南
	分为编辑模式和命令模式
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

# 关于复制粘贴
	Web 端支持的不够好，复制需要选中后右键点击复制，粘贴需要右键选择粘贴
