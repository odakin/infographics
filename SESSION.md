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
- black → cream paper bg、 Libertinus Serif/Math/Sans、 card 70→48mm、 muted palette、 decoration 削減

第 6 段 (= 2026-05-19 20:00) data ブロックを真の align 環境に統合
- 旧 \datarow (3 個別 TikZ node を行ごとに配置) → 新 \databox で **1 個の `$\begin{array}{r@{\;}c@{\;}l}...\end{array}$`** に統合、 各 card は 1 ノード呼び出し
- 結果: 「ラベル右揃え / 関係記号中央 / 値左揃え」 の真の math 表組 (= LaTeX align/aligned 環境と同等)、 行間 baseline は math engine 管理で精密整列
- \text{過去} / \text{距離} の Japanese label は維持 (= 正しい用法、 math 内に Japanese を embed する LaTeX 標準)
- card 8 (DE twocol) も同じ array 環境を 2 つ並べる形に rewrite、 上に色付き section header (加速開始 / DE 優勢)
- info card 2 (BBN 質量) の label も `$\text{陽子}\ m_p$` 等で \text{} 内に統一

第 5 段 (= 2026-05-19 19:00) 全 data 行を math-wrapping、 日本語を \text{} 内に
- `\datarow` macro が args を $...$ で囲むよう変更、 全 9 card + 3 info card + footer を math syntax に書き換え
- 日本語 (過去 / 距離 / 億年前 / 億光年 / 万年 / 分 / 年前 / 光年 等) を `\text{...}` で math 内に取り込み、 baseline を math 軸で統一
- 単位 (K / s / MeV / GeV / eV) も `\text{...}` で upright Roman に (= math italic K 問題回避)
- en-dash も `\text{--}` で確実に en-dash になる (= math mode 内の "--" は double-minus にならない)
- 結果: 関係記号 (≈ / ≳ / ~ / =) の縦軸 alignment が math baseline で精密整列、 行間の drift 解消

第 4 段 (= 2026-05-19 18:00) EWPT 追加 (9 段化) + BBN icon overflow 修正 + 関係記号 alignment
- **9 段 timeline**: 既存 8 段に **電弱対称性の破れ (EWPT)** を 2 番目に挿入
  - 値: $z \sim 4{\times}10^{14}$, $t \sim 10^{-11}$ s, $T \sim 10^{15}$ K (= 100 GeV), $D_C \approx 462$ 億光年
  - icon: **Higgs potential Mexican hat** + 2 つの真空状態点 (= 自発的対称性破れの典型図)
  - card width 33 → 30mm に縮小、 palette c0-c8 (= 9 色 warm-to-cool)
- **BBN icon overflow 修正** (= bug): 旧版は ⁴He 中心 + 周囲に ²H/³He/⁷Li 配置 → ⁷Li label が separator (y=6) を越えて下にはみ出していた。 新版は **4 核種を horizontal row** で並列、 各 label を真下に配置 (= 干渉ゼロ)
- **関係記号 alignment**: `\datarow` を 4-arg 化 (label / relation / value)、 relation 記号を `anchor=base east` で同 x 位置に整列、 value を `anchor=base west` で直後に。 ≈ / ≳ / ~ / = の縦軸が全 card で揃う

第 3 段 (= 2026-05-19 17:00) 字サイズ底上げ + 距離 row + icon 強化
- **`Numbers = OldStyle` → `Lining`** (= 古い式数字をやめて modern lining numerals、 「数字がダサい」 解消)
- **font サイズ底上げ**: body 系を 7→8pt、 plot label 7.5→9pt 等、 A4 で読みやすい大きさに
- **共動距離 D_C 行追加** (= 5 列構成): 「光は X 億年前のもの、 でも今は Y 億光年先」 の expansion 教育的に有効、 飽和点 462 億光年 = 観測可能宇宙の縁が timeline で可視化
- **card 48→56mm** (= 距離追加分を吸収)
- **icon 強化**:
  - inflation: outer glow + quantum fluctuation dots
  - QGP: 背景 soup gradient + 波線 gluon
  - BBN: ⁴He を中心に配置 (= 25% mass の主産物として強調)、 D/³He/⁷Li を周辺
  - balance: 波線追加 + dots layered
  - recombination: H atom orbit + CMB photon escape 矢印
  - first stars: halo 二重円 + 電離領域 dashed
  - DE: 太い 3 矢印 + 副次矢印 + 膨張背景円
  - galaxy: spiral arms + 中心 bulge
- 結果 145 KB の PDF

## 要対応 (open)

- (なし)

## 次の方向性

- [ ] 第 2 entry の構想 (= 候補: 「素粒子の標準模型」 / 「銀河の階層」 / 「物理単位系」)
- [ ] 第 2 entry 追加時に common preamble (= 色定義 / font / card style) の `.sty` 化を再評価 (= 早すぎる抽象化を避けるため entry 3 件超でトリガー)
- [ ] HTML 版を保持するなら定期 sync を考えるか、 「LaTeX 正本、 HTML は古い snapshot」 の運用にするか
