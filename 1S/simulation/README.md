シミュレーション学
=====

実行方法（ローカル）
-----
1. `cd src`
2. `python3 main.py` &nbsp; 実行結果の動画を作るのに1分ほどかかる（`MAX_TURN`によっては更にかかる）
3. パラメータは`src/setting.py`から変えることができる
4. 戦略は`src/strategy.py`の中の`strategy_list`から変更できる

実行方法（Docker）
-----
特別なライブラリは使ってないのでローカルで十分動くはずだが一応用意した
1. `docker-compose build`
2. `docker-compose run app /bin/bash`
3. 以下ローカルと同じ

コードの説明
-----
各ファイルの内容は名前の通りです
- `agent.py`
    - エージェントの挙動
- `bar.py`
    - バーの状態を保持
- `setting.py`
    - シミュレーションの設定
- `simulator.py`
    - シミュレーション全体の流れ
- `strategy.py`
    - エージェントが採用する戦略
- `visualize.py`
    - 可視化の実装

結果
-----
実行結果は`src/Result/`の中に保存される
- `src/Result/bar_record.png`はバーの混雑率の変化を表している
- `src/Result/strategy.gif`は各戦略の採用確率の変化を表している

環境
----
- 手元のPythonのバージョンは`3.9.5`。恐らくPythonのバージョンが`3.9`未満だとエラーが出る
- WSL2上で`Ubuntu-20.04`を使っている
