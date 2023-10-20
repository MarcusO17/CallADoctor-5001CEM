class PageManager():
    def __init__(self):
        self.stack = list()

    def add(self, pageWidget):
        self.stack.append(pageWidget)
        pageWidget.show()
        # still need to hide the current page

    def goBack(self):
        toBeRemovedPage = self.stack.pop()
        toBeRemovedPage.close()
        self.stack[len(self.stack)-1].show()

    def size(self):
        return len(self.stack)