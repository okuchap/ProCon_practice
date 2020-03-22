# ProCon_practice
Solve the problems in the book, "Algorithms and Data Structures for Programming Contests".

* [プログラミングコンテスト攻略のためのアルゴリズムとデータ構造   渡部 有隆](https://www.amazon.co.jp/dp/4839952957/ref=cm_sw_r_tw_dp_U_x_c9lwEbZF3QEAX)
* [Aizu Online Judge](http://judge.u-aizu.ac.jp/onlinejudge/index.jsp)

## Problems

|問番号|テーマ|日付|メモ|
|--|--|--|--|
|1A|Insertion Sort|2020.03.03|添字の細かい部分で間違えないようにしたい|
|1B|Greatest Common Divisor|2020.03.03|再帰関数は最後にも`return`をつける|
|1C|Prime Number|2020.03.03|自明なケースは最初に省くと時間減らせる|
|2A|Bubble Sort|2020.03.04|`input().split()`としてないのでpresentation errorがでた|
|3A|Stack|2020.03.20|classとしてデータ構造を実装|
|3B|Queue|2020.03.21|`deque`というライブラリを使えば良い|
|4A|Linear Search|2020.03.22|番兵法|
|4B|Binary Search|2020.03.22|再帰は遅い．端点条件に注意．|


## Useful Links
### 概説
* [Python 競技プログラミング高速化tips (PythonでAtcoderをやる際に個人的に気を付けてること)](https://juppy.hatenablog.com/entry/2019/06/14/Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E9%AB%98%E9%80%9F%E5%8C%96tips_%28Python%E3%81%A7Atcoder%E3%82%92%E3%82%84%E3%82%8B%E9%9A%9B%E3%81%AB%E5%80%8B)
* [PythonでAtCoder青になるまで -Pythonで競プロやるときに気をつけること-](https://qiita.com/Kentaro_okumura/items/a6917572756a2e3c0da9)
* [Pythonで使う競技プログラミング用チートシート](https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0)
* [AtCoderをPythonで始めるときの環境構築といくつかのTIPS](https://qiita.com/recuraki/items/e60a90d8c21c3af0394d)

### 技術
#### 文法
* [Pythonで競プロやるときによく書くコードをまとめてみた](https://qiita.com/y-tsutsu/items/aa7e8e809d6ac167d6a1)

#### 高速化
* [計算量オーダーの求め方を総整理！ 〜 どこから log が出て来るか 〜](https://qiita.com/drken/items/872ebc3a2b5caaa4a0d0)
* [特集！知らないと損をする計算量の話](https://qiita.com/drken/items/18b3b3db5735241465ef)
* [Pythonistaなら知らないと恥ずかしい計算量のはなし](https://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb)
* [高速化のためのPython Tips](http://nonbiri-tereka.hatenablog.com/entry/2016/09/01/072402#PyPy)
* [Python を高速化したい](https://python.ms/optimization/#%E8%83%8C%E6%99%AF)



### 問題集
* [AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)
* [AtCoder 版！蟻本 (中級編)](https://qiita.com/drken/items/2f56925972c1d34e05d8)

### その他
* [自分がよく使用するMarkdownの書き方まとめ](https://qiita.com/toyokky/items/47a5a56c20ad99e1784c)

### 環境構築(失敗)
* [AtCoder用にPython3.4.3の環境を構築する](https://qiita.com/showyou/items/e9df09abe97071ef35f5)
* [Pythonで、Pipenvを使う](https://narito.ninja/blog/detail/58/)

**memo**

* なぜかはわからないが，pipenvでpypy3-2.4.0を導入しようとするとエラーが出て無理だった．(2020.3.3)
* python 3.4.3を入れようとしてもダメだ．なぜ．
    - よくわからないが，直下ではなく，一つ上の階層にあるPipfileに変更が加えられている．依存関係でむちゃくちゃなことが起きているらしい．
    - とりあえず，Pipfileを直下に用意し，pipenv installの際に[それを参照するように](https://qiita.com/tonluqclml/items/cd0d2a2cb0197cbaee42)する．-- これで依存関係が原因っぽいよくわからないエラーが起こらなくなった．
    - そのまま`pipenv --python 3.4.4`とやると「システム内に見つかりません」と出てダメ．
    - [ここ](https://pipenv-ja.readthedocs.io/ja/translate-ja/advanced.html#automatic-python-installation)にあるように，[pyenvをきちんと設定](https://tekunabe.hatenablog.jp/entry/2018/12/28/pyenv_pipenv)してやると，システムに入ってないバージョンをpipenvで入れようとしたとき，自動で入れてくれるようになるらしい．
    - [こんな感じのエラーが出る](https://github.com/pyenv/pyenv/issues/1188)
    - なんかよくわからんけど[ここ](https://github.com/pyenv/pyenv/issues/1066)に書いてあったこと試した．-- ダメ．
    - [env で "No versions found" というエラーが出た場合の対処法](https://qiita.com/georgenano/items/0b289e1a2859ceda9b70) -- あまり関係なさそう
* python 3.6系とかだと問題なく入る．諦め．