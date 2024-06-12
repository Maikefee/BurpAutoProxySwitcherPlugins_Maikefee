# BurpAutoProxySwitcherPlugins
# 红队必备

场景：在爆破批量封ip的情况下，爬取socks5代理在bp进行渗透测试。

说明：首先爬取大量的socks代理或者http代理，保存在某个txt，然后bp导入插件并启动，然后导入代理的txt，可设置一个请求换一次socks代理ip，这样就绕过了封ip的情况。
