# BurpAutoProxySwitcherPlugins
# 红队必备

中文：


环境：1.本地安装 PySocks 库：pip install PySocks 2.安装jpython环境

功能：自动切换代理，绕过封ip的情景。

场景：在爆破批量封ip的情况下，爬取socks5代理在bp进行渗透测试。

说明：首先爬取大量的socks代理或者http代理，保存在某个txt，然后bp导入插件并启动，然后导入代理的txt，可设置一个请求换一次socks代理ip，这样就绕过了封ip的情况。比如设置1次切换，则每一个repeater和intruder请求都会触发插件切换功能

插件环境自行下载:jython-standalone-2.7.1.jar

注：仅用于分享学习交流，切勿用于非法用途，与本人无关。



English：

Environment: 1. Local installation of PySocks library: pip install PySocks 2. Install jPython environment
Function: Automatically switch proxies to bypass IP blocking scenarios.
Scenario: Crawling socks5 agents for penetration testing in BP while blasting batch IP blocking.
Explanation: First, crawl a large number of Socks or HTTP proxies and save them in a certain txt. Then, import the BP plugin and start it, and then import the proxy's txt. You can set a request to change the Socks proxy IP once, which bypasses the situation of IP blocking. For example, setting one switch will trigger the plugin switch function for each repeater and integrator request
Download the plugin environment yourself: jython standalone 2.7.1. jar
Note: For sharing, learning, and communication purposes only, do not use for illegal purposes, and have nothing to do with oneself.

![image](https://github.com/Maikefee/BurpAutoProxySwitcherPlugins/blob/main/WX20240613-093041%402x.png)
