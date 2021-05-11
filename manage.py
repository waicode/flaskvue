import os
from flaskvue import app


def __app_run():
    if os.environ['APP_ENV'] == 'production' or os.environ['APP_ENV'] == 'staging':
        app.run()
    elif os.environ['APP_ENV'] == 'development' or os.environ['APP_ENV'] == 'test':
        if os.environ['APPEXEC_ENV'] == 'container':
            app_port = 5000
        elif os.environ['APPEXEC_ENV'] == 'localhost':
            app_port = 5001
        else:
            raise Exception('想定外のAPPEXEC_ENVのため処理を終了')
        app.run(host='0.0.0.0', port=app_port, debug=True)
    else:
        raise Exception('想定外のAPP_ENVのため処理を終了')


if __name__ == '__main__':
    __app_run()
