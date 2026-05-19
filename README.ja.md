# infographics

物理・数学などの 1 枚もの図解 (インフォグラフィック) を集めた repo。 HTML + CSS + inline SVG、 ビルド不要。

[English version](README.md)

## 動機

教育的なインフォグラフィックには、 細かい (あるいは結構粗い) 物理的誤りが紛れていることが多い。 文句を言うだけでなく、 **修正版** を自己完結フォルダで蓄積し、 修正点と典拠を `NOTES.md` に明記する。

`<topic>/index.html` をブラウザで開けば動く。

## エントリ

- **[cosmology-history/](cosmology-history/)** — 宇宙の歴史 (= インフレーション〜現在の 8 段、 赤方偏移 / 宇宙年齢 / 温度 / 主な出来事)。 流通している日本語版に対し物理的誤り 3 点 + 数値精度 3 点を修正。 典拠は [NOTES.md](cosmology-history/NOTES.md)

## 構成

- `<topic>/index.html` — インフォグラフィック本体 (自己完結)
- `<topic>/NOTES.md` — 出典・元図からの修正点・design 判断
- [CLAUDE.md](CLAUDE.md) — repo 規約 (エクスポート手順、 新規 entry の追加方法)
- [DESIGN.md](DESIGN.md) — design system (色 palette、 typography、 grid)

## エクスポート

Chromium ヘッドレスで PDF / PNG 化:

```bash
chromium --headless --disable-gpu --print-to-pdf=out.pdf \
  --no-pdf-header-footer "file://$(pwd)/<topic>/index.html"
```

## License

Content (HTML / SVG / text): CC BY-SA 4.0
