# SESSION

## 現状

- repo: 2026-05-19 作成、 public [odakin/infographics](https://github.com/odakin/infographics)
- entry 1 件: `cosmology-history/`
- security baseline 適用済 (Dependabot/CodeQL/PVR/branch protection)

## 直近の変更 (2026-05-19)

**LaTeX/TikZ への primary 移行 + editorial light theme への refactor**:

第 1 段 (= 2026-05-19 14:00) LaTeX/TikZ への primary 移行
- `cosmology-history.tex` (LuaLaTeX + article + luatexja + TikZ + pgfplots) + `Makefile` 新規作成
- 解消した HTML 版の問題: 数式 clip / font OS 依存 / 配置揃え / annotation 見切れ
- HTML 版 (`index.html` + `style.css`) は **web 配布用代替** として残置

第 2 段 (= 2026-05-19 16:00) Editorial light theme への refactor
- **black → cream paper bg** (= 印刷インク代削減、 editorial 標準)
- **font**: TeX Gyre Pagella → **Libertinus Serif + Libertinus Math + Libertinus Sans** (= 最も refined な free math font ファミリー、 Pagella より優美)
- **card 高さ**: 70mm → 48mm (= data 行の下に 22mm の vacuum gap があった bug を解消)
- **palette muted** (= 高彩度 8 色から、 muted earth tone 系へ。 印刷 + cream bg で映える色相)
- **decoration 削減**: glass effect / drop shadow / gradient 重ね を排除、 hairline border + whitespace のみで modern editorial 化
- 結果 138 KB の PDF (= subset embed font 込み) 、 1 page A4 横置き

## 要対応 (open)

- (なし)

## 次の方向性

- [ ] 第 2 entry の構想 (= 候補: 「素粒子の標準模型」 / 「銀河の階層」 / 「物理単位系」)
- [ ] 第 2 entry 追加時に common preamble (= 色定義 / font / card style) の `.sty` 化を再評価 (= 早すぎる抽象化を避けるため entry 3 件超でトリガー)
- [ ] HTML 版を保持するなら定期 sync を考えるか、 「LaTeX 正本、 HTML は古い snapshot」 の運用にするか
