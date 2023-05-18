def Redirect(sss, target):
    sss.parent().setCentralWidget(target().get_widget())