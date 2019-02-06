# 試し方

自分の試したいディレクトリ(`sample_app<num>`)に入りrequirements.txtでpythonのパッケージをインストールします

```
$ cd sample_app<num>
$ pip install -r requirements.txt
```

あとはDjangoの開発用サーバーを起動させればローカルホストで試すことができます。<br>
ローカルホストURL
http://127.0.0.1/

```
$ python manage.py runserver
```