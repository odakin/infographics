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
    ├── <topic>.tex                      # LuaLaTeX 印刷版 (= primary)
    ├── <topic>.pdf                      # commit する deliverable
    ├── Makefile                         # make / make view / make png / make clean
    ├── index.html                       # HTML web 版 (= 任意、 web 配布用)
    ├── style.css
    └── NOTES.md                         # 典拠・修正点・出典のメモ
```

各 entry は **そのフォルダだけ複製しても動く** ことを invariant にする (= 共有 sty/CSS 持ち込まない、 重複許容)。
shared design system 化は entry が 3 件超えてから判断 (= 早すぎる抽象化を避ける)。

## 実行方法

**LuaLaTeX 版 (= 印刷 primary)**:

```bash
cd <topic>/
make           # lualatex で PDF compile
make view      # macOS Preview で開く
make png       # 300 DPI PNG 出力 (web sharing 用)
make clean     # aux ファイル削除
make distclean # PDF も含めて削除
```

**HTML 版 (= web 配布、 任意)**:

```bash
cd ~/Claude/infographics
preview_start <topic>  # preview MCP 経由
# または
python3 -m http.server -d <topic> 8000
```

## なぜ LaTeX を primary にしたか

HTML は数式 (KaTeX) の clip 問題・font の OS 依存・ベースライン整列の弱さで A4 印刷 fidelity が出ない。 LuaLaTeX + TikZ + pgfplots は (a) 数式 native (= 絶対 clip しない)、 (b) 日本語 font 完全制御 (= Hiragino subset embed)、 (c) 1mm 単位の配置、 (d) PDF 出力で印刷 fidelity 保証。

設計判断詳細は `DESIGN.md` 参照。 HTML 版は **web 配布用の代替手段** として残す (= 専用 device で render 不要、 link 共有可)。

## 新規 entry 追加手順

1. `<topic>/` を mkdir、 `index.html` + `style.css` + `NOTES.md` を作成
2. preview MCP で見栄え確認 (= `preview_screenshot` で記録)
3. README.md の index に entry を追加
4. SESSION.md の「直近の変更」 に記録、 commit + push

## 現在の entry

- **cosmology-history/** — 宇宙の歴史 (赤方偏移・年齢・温度・主な出来事を 8 段で並べる)。 2026-05-19 作成
