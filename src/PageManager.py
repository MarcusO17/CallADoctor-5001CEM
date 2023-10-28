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
        return cls._instance

    def add(self, index):
        self.indexStack.append(index)

    def back(self):
        self.indexStack.pop()
        return self.indexStack[self.size()]

    def size(self):
        return len(self.indexStack)