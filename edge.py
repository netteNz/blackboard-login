from msedge.selenium_tools import Edge, EdgeOptions


# Launch Microsoft Edge (Chromium)
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)

driver.get("https://github.com/netteNz")
