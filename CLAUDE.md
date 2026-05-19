# infographics

科学・物理・数学系の **インフォグラフィック (図解 1 枚もの)** を蓄積する monorepo。
1 トピック = 1 サブディレクトリ、 HTML + CSS + inline SVG で実装。

## ディレクトリ構造

```
infographics/
├── CLAUDE.md / SESSION.md / DESIGN.md   # 永続規約・現状・設計判断
├── README.md                            # 訪問者向け index (各 entry へ link)
├── .gitignore
└── <topic>/                             # 1 entry = 1 directory
    ├── index.html                       # 自己完結 HTML
    ├── style.css
    ├── icons/                           # SVG icon sprite (任意)
    └── NOTES.md                         # 典拠・修正点・出典のメモ
```

各 entry は **そのフォルダだけ複製しても動く** ことを invariant にする (= 共有 CSS / 共有 JS は持ち込まない、 重複は許容)。
shared design system 化は entry が 3 件超えてから判断 (= 早すぎる抽象化を避ける)。

## 実行方法

```bash
cd ~/Claude/infographics
preview_start <topic>/index.html  # preview MCP 経由
# または
python3 -m http.server -d <topic> 8000
```

ブラウザで開けば動く (= build step 不要)。 KaTeX 等の重い依存は CDN で。

## エクスポート

PDF / PNG 化は Chromium ヘッドレスで:

```bash
# PDF (印刷用、 A3 横で 1 枚にフィット想定)
chromium --headless --disable-gpu --print-to-pdf=<topic>.pdf \
  --no-pdf-header-footer "file://$(pwd)/<topic>/index.html"

# PNG (web 配布用、 高解像度)
chromium --headless --disable-gpu --screenshot=<topic>.png \
  --window-size=1920,1080 "file://$(pwd)/<topic>/index.html"
```

## 新規 entry 追加手順

1. `<topic>/` を mkdir、 `index.html` + `style.css` + `NOTES.md` を作成
2. preview MCP で見栄え確認 (= `preview_screenshot` で記録)
3. README.md の index に entry を追加
4. SESSION.md の「直近の変更」 に記録、 commit + push

## 現在の entry

- **cosmology-history/** — 宇宙の歴史 (赤方偏移・年齢・温度・主な出来事を 8 段で並べる)。 2026-05-19 作成
