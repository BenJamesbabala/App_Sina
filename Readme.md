####纯python实现app自动化
现阶段：demo能启动app

config中可存放配置文件ini，app元素定位文件yaml(每个yaml为一个单独app或一个yaml包含多个app，都是三级定位)

####问题：
05-14：头条内容中在数字后输入中文，会显示为：2019&YhBlWXbuUk1ipYADU+qXAImB-100&UUMACg-100&UUNTBVQrgAOL1XnRdu52hGVZZ1CNRGWZTuVTyonGmJGL,k72AApOE3nR-:&YDtSBg-450&UgY-

05-17:
    page中的get_tost_element，是否该单独传入driver？？
    
 05-23:
    PO模式已完成，可通过excel调用测试数据，但是执行完用例后不能自动结束