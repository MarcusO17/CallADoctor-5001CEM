from PyQt5.QtWidgets import QStackedWidget


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
            self.stack.append(pageWidget)
            pageWidget.show()
            self.stack[len(self.stack)-2].hide()

    def goBack(self):
        toBeRemovedPage = self.stack.pop()
        self.stack[len(self.stack)-1].show()
        toBeRemovedPage.close()

    def getPreviousPage(self):
        return self.stack[len(self.stack) - 2]

    def size(self):
        return len(self.stack)

class FrameLayoutManager():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FrameLayoutManager, cls).__new__(cls)
            cls._instance.indexStack = []
            cls._instance.frameLayout = QStackedWidget()
            cls._instance.basePages = 0
        return cls._instance

    def add(self, index):
        self.indexStack.append(index)

    def back(self):
        widget = self.frameLayout.widget(self.indexStack.pop())
        self.frameLayout.removeWidget(widget)
        widget.deleteLater()

    def backToBasePage(self, index):
        # deletes all except the starting pages
        if self.frameLayout.count() > self.basePages:
            numberOfPagesToBeRemoved = self.basePages - self.frameLayout.count()
            for i in range(numberOfPagesToBeRemoved):
                widget = self.frameLayout.widget(i+self.basePages)
                self.frameLayout.removeWidget(widget)
                widget.deleteLater()

        self.indexStack.clear()
        self.indexStack.append(index)

    def top(self):
        if self.indexStack:
            return self.indexStack[-1]
        else:
            return None

    def size(self):
        return len(self.indexStack)

    def setFrameLayout(self, frameLayout):
        self.frameLayout = frameLayout

    def getFrameLayout(self):
        return self.frameLayout

    def setBasePages(self, basePages):
        self.basePages = basePages

    def getBasePages(self):
        return self.basePages