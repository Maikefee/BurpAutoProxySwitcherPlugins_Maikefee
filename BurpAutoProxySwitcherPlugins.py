# -*- coding: utf-8 -*-

from burp import IBurpExtender, IHttpListener, ITab
from javax.swing import JPanel, JLabel, JTextField, JButton, JCheckBox, JTextArea, JScrollPane, JRadioButton, ButtonGroup
from java.awt import BorderLayout
import random
import io

class BurpExtender(IBurpExtender, IHttpListener, ITab):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName("Proxy Switcher")
        self._callbacks.registerHttpListener(self)
        
        # Create GUI components
        self.panel = JPanel()
        self.panel.setLayout(BorderLayout())
        
        self.top_panel = JPanel()
        self.toggle_plugin = JCheckBox("Enable Proxy Switcher", actionPerformed=self.toggleSwitch)
        self.path_label = JLabel("Path to proxy.txt:")
        self.path_field = JTextField(20)
        self.load_button = JButton('Load Proxies', actionPerformed=self.loadProxies)
        self.clear_button = JButton('Clear Output', actionPerformed=self.clearOutput)
        self.request_count_label = JLabel("Requests per Proxy:")
        self.request_count_field = JTextField("1", 5)
        
        # Proxy type selection
        self.radio_http = JRadioButton("HTTP", True)
        self.radio_socks5 = JRadioButton("SOCKS5")
        self.radio_group = ButtonGroup()
        self.radio_group.add(self.radio_http)
        self.radio_group.add(self.radio_socks5)
        
        self.top_panel.add(self.toggle_plugin)
        self.top_panel.add(self.path_label)
        self.top_panel.add(self.path_field)
        self.top_panel.add(self.load_button)
        self.top_panel.add(self.clear_button)
        self.top_panel.add(self.request_count_label)
        self.top_panel.add(self.request_count_field)
        self.top_panel.add(self.radio_http)
        self.top_panel.add(self.radio_socks5)
        
        self.response_area = JTextArea(10, 30)
        self.response_area.setEditable(False)
        self.scroll_pane = JScrollPane(self.response_area)
        
        self.panel.add(self.top_panel, BorderLayout.NORTH)
        self.panel.add(self.scroll_pane, BorderLayout.CENTER)
        
        self.enabled = False
        self.proxies = []
        self._callbacks.addSuiteTab(self)
        
        print("author:https://github.com/Maikefee/")
        print("Proxy Switcher loaded.")

    def getTabCaption(self):
        return "Proxy Switcher"

    def getUiComponent(self):
        return self.panel

    def toggleSwitch(self, event):
        self.enabled = self.toggle_plugin.isSelected()
        print("Proxy Switcher Enabled: {}".format(self.enabled))

    def loadProxies(self, event=None):
        if not self.enabled:
            return
        self.proxies = []
        path_to_proxies = self.path_field.getText() if self.path_field.getText() else "/path/to/your/proxies.txt"
        try:
            with io.open(path_to_proxies, "r", encoding="utf-8") as file:
                self.proxies = [line.strip() for line in file if line.strip()]
            self.response_area.append("Proxies loaded from {}\n".format(path_to_proxies))
        except Exception as e:
            self.response_area.append("Failed to load proxies: {}\n".format(str(e)))

    def clearOutput(self, event):
        self.response_area.setText("")

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if not self.enabled or not messageIsRequest:
            return
        try:
            if toolFlag in (self._callbacks.TOOL_INTRUDER, self._callbacks.TOOL_REPEATER) and self.proxies:
                proxy = random.choice(self.proxies)
                host, port = proxy.split(":")
                if self.radio_http.isSelected():
                    protocol = "http"
                elif self.radio_socks5.isSelected():
                    protocol = "socks5"
                service = self._helpers.buildHttpService(host, int(port), protocol)
                if service:
                    messageInfo.setHttpService(service)
                    self.response_area.append("Request from {} routed through: {}:{} using {} protocol.\n".format(
                        self._callbacks.getToolName(toolFlag), host, port, protocol.upper()))
                else:
                    self.response_area.append("Failed to set HttpService for {}:{} using {} protocol.\n".format(
                        host, port, protocol.upper()))
        except Exception as e:
            self.response_area.append("Error processing HTTP message: {}\n".format(str(e)))
