# BJUT_Survival_Script
北工大生存脚本

## bjut_startup.py
开机启动脚本，自动登录网关，显示当前流量账户信息，启动微信等自定义软件。
### 使用
1. 安装依赖库

    pip install bjutNet

2. 修改脚本中用户配置 
3. 以win10为例，将脚本复制到`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup` 
4. 或者在启动目录建立start.bat批处理文件，内容为`python \path\bjut_startup.py` 