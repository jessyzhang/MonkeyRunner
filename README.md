# MonkeyRunner
MonkeyRunner测试/发送短信
前提: 确保环境变量配置完好
在用户变量中添加Path（如有， 则只需编辑），分别添加java, android sdk和Python的路径， 用分号隔开： C:\Program Files\Java\jdk1.8.0_73\bin;D:\Program Files\Java\android-sdk-windows;C:\Python27.
配置好后， 在cmd中试运行 java -version; python; monkeyrunner. 

代码关键的一个地方是获取点的坐标， 可以用monkeyrunner自带的 monkey_recorder.py 来获取坐标并录制脚本。 也可以用monkey_playback.py 来回放录制的事件
下载路径：
monkey_recorder.py: http://code.metager.de/source/history/android/4.0.3/sdk/monkeyrunner/scripts/monkey_recorder.py
monkey_playback.py : http://code.metager.de/source/history/android/4.0.3/sdk/monkeyrunner/scripts/monkey_playback.py

下载后可以将其放在 android sdk 子文件夹/tool中， 当然也可以按类别将其放在/tool/lib中， 到时运行的时候知名路径就可以了
接着运行monkeyrunner 命令来获取点的坐标
monkeyrunner monkey_recorder.py
运行成功后手机屏幕会通过 recorder镜像到桌面， 分辨点击 收件人， 文本框和发送这三个点， 获取这三个点的坐标， 将其代入到python程序的代码中作为当前连接的设备的三个点的坐标。

python脚本完成后可以同样放到tool中， 通过monkeyrunner命令来运行
monkeyrunner  SendMessage.py

代码没有问题的话， 运行会是成功的， 信息也会发送出去。
在脚本的最后对结果进行了截屏， 可以找到截屏保存的路径去查看结果