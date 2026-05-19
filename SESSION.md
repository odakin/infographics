# SESSION

## 現状

- repo: 2026-05-19 作成、 public [odakin/infographics](https://github.com/odakin/infographics)
- entry 1 件: `cosmology-history/`
- security baseline 適用済 (Dependabot/CodeQL/PVR/branch protection)

## 直近の変更 (2026-05-19)

**LaTeX/TikZ への primary 移行** (= HTML 版で発覚した数式 clip / font OS 依存 / ベースライン整列の構造的弱点を解消):

- `cosmology-history.tex` (LuaLaTeX + ltjsarticle + TikZ + pgfplots) + `Makefile` 新規作成
- font: TeX Gyre Pagella (Latin) + Pagella Math (math) + Hiragino Mincho/Sans (Japanese, macOS native subset embed)
- TikZ で 8 stage card + アイコン (= 陽子/中性子配置で核種を描き分け) + 温度勾配 hero band + 3 info card
- pgfplots で era 背景 band + 温度勾配 palette と整合した line color + crossover marker + leader 付き annotation
- 解消した HTML 版の問題:
  - 赤方偏移式の clip → LaTeX 数式 native で絶対 clip しない
  - font の OS 依存・ダサさ → Hiragino を subset embed、 print fidelity 保証
  - 配置の揃え崩れ → TikZ 絶対座標で 1mm 単位
  - DE 優勢 annotation の見切れ → plot 内座標で確実に配置
- HTML 版 (`index.html` + `style.css`) は **web 配布用代替** として残す (= 削除しない、 用途分担)

## 要対応 (open)

- (なし)

## 次の方向性

- [ ] 第 2 entry の構想 (= 候補: 「素粒子の標準模型」 / 「銀河の階層」 / 「物理単位系」)
- [ ] 第 2 entry 追加時に common preamble (= 色定義 / font / card style) の `.sty` 化を再評価 (= 早すぎる抽象化を避けるため entry 3 件超でトリガー)
- [ ] HTML 版を保持するなら定期 sync を考えるか、 「LaTeX 正本、 HTML は古い snapshot」 の運用にするか
