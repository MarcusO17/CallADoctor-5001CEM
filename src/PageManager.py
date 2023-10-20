from PyQt5.QtWidgets import QStackedWidget

class PageManager():
    def __init__(self):
        self.stack = QStackedWidget()

    def goToPage(self, pageWidget):
        self.stack.addWidget(pageWidget)
        pageWidget.show()

        # still need to hide the current page

    def goBack(self):
        toBeRemovedPage = self.stack.widget(self.stack.size())
        self.stack.removeWidget(toBeRemovedPage)
        toBeRemovedPage.close()

        # after removing widget from stack
        # get the top one and show

        self.stack.widget(self.stack.size()).show()


    def size(self):
        return self.stack.count()