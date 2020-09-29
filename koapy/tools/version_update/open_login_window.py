import sys

from PyQt5.QtWidgets import QApplication

from koapy import KiwoomOpenApiQAxWidget, KiwoomOpenApiError

def open_login_window(exit_on_login=True):
    app = QApplication(sys.argv)
    control = KiwoomOpenApiQAxWidget()
    if control.GetConnectState() == 0:
        def OnEventConnect(errcode):
            control.OnEventConnect.disconnect(OnEventConnect)
            if exit_on_login:
                app.exit(errcode)
        control.OnEventConnect.connect(OnEventConnect)
        KiwoomOpenApiError.try_or_raise(control.CommConnect())
    return app.exec_()

if __name__ == '__main__':
    sys.exit(open_login_window())
