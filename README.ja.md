# infographics

物理・数学などの 1 枚もの図解 (インフォグラフィック、 ポスター) を集めた repo。 本体は LuaLaTeX + TikZ + pgfplots で組む A4 の PDF。

[English version](README.md)

## 動機

教育的なインフォグラフィックには、 細かい (あるいは結構粗い) 物理的誤りが紛れていることが多い。 文句を言うだけでなく、 **修正版** を自己完結フォルダで蓄積し、 修正点と典拠を `NOTES.md` に明記する。

## エントリ

- **[cosmology-history/](cosmology-history/)** — 宇宙の歴史の年表 (= インフレーション〜現在の 9 段、 赤方偏移 / 宇宙年齢 / 温度 / 主な出来事 + 主要成分のエネルギー密度の log-log プロット)。 流通している日本語版に対し物理的誤り 3 点 + 数値精度 3 点を修正。 本体 = [cosmology-history.pdf](cosmology-history/cosmology-history.pdf)、 典拠は [NOTES.md](cosmology-history/NOTES.md)

## 構成

- `<topic>/<topic>.tex` — 本体 (LuaLaTeX)。 組んだ `<topic>.pdf` が配る版
- `<topic>/NOTES.md` — 出典・元図からの修正点・design 判断
- `<topic>/index.html` — web 版 (任意)。 cosmology-history の web 版は LaTeX に移る前の第 2 版で、 その後の LaTeX 版の変更 (9 段化・密度プロットの作り直しなど) は入っていない
- [CLAUDE.md](CLAUDE.md) — repo 規約 (組み方、 新規 entry の追加方法)
- [DESIGN.md](DESIGN.md) — 設計判断と design system (色 palette、 typography、 layout)

## 組み方

```bash
cd <topic>/
make        # lualatex で PDF
make png    # 300 DPI の PNG (web 共有用、 poppler の pdftoppm が要る)
```

web 版 (`index.html`) は Chromium ヘッドレスで PDF / PNG にもできる:

```bash
chromium --headless --disable-gpu --print-to-pdf=out.pdf \
  --no-pdf-header-footer "file://$(pwd)/<topic>/index.html"
```

## License

Content (TeX / HTML / SVG / text): CC BY-SA 4.0
