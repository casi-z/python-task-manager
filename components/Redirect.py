def Redirect(sss, target):
    sss.parent().setCentralWidget(target())
    # not lecvid