from flask import Flask,redirect
#ページインポート
from apps.systemMain import systemMain
app = Flask(__name__)

appSet = [
    systemMain
]

for appName in appSet:
    app.register_blueprint(appName)

#region エラー処理
@app.errorhandler(404) # 404エラーが発生した場合の処理
def error_404(error):
    # print("404エラー")
    return redirect("/")

@app.errorhandler(405) # 405エラーが発生した場合の処理
def error_405(error):
    print("405エラー")
    return redirect("/")

@app.errorhandler(500) # 500エラーが発生した場合の処理
def error_500(error):
    print("500エラー")
    return redirect("/")
#endregion

if __name__ == "__main__":
    app.run(debug=True)