class PageManager():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PageManager, cls).__new__(cls)
            cls._instance.stack = []
        return cls._instance

    def add(self, pageWidget):
        if len(self.stack) == 0:
            self.stack.append(pageWidget)
            pageWidget.show()
        else:
            self.stack[len(self.stack)-1].hide()
            self.stack.append(pageWidget)
            pageWidget.show()
        # still need to hide the current page

    def goBack(self):
        toBeRemovedPage = self.stack.pop()
        toBeRemovedPage.close()
        self.stack[len(self.stack)-1].show()

    def size(self):
        return len(self.stack)