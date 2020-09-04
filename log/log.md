## 2020-09-04
```
git clone https://github.com/macchanism/tweetpy.git
```

  * 以下のファイル、ディレクトリを作成
    - `.gitignore`
    - `log/`
      - `log.md`
    - `main/`
    - `else/`

  * Atom上で以下を実行
    - stage
    - commit
      - set up for developing
    - push

  * `README.md`を編集

```
git add .
git commit -m "modify README.md"
git push
```

```
git branch develop
git checkout develop
```

```
git add .
git commit -m "create develop branch"
```

  * `log/`を`.gitignore`入りに

```
git add .
git commit --amend
git push origin develop
```

  * `README.md`を修正

```
git add .
git commit -m "modify README.md"
git push origin develop
```

  * 以下のプログラムを作成
    - config.py
    - tweet.py
    - viewtl.py

  * README.mdを編集

```
git add .
git commit -m "modify README.md"
git push origin develop
```
