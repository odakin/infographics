# SESSION

## 現状

- repo: 2026-05-19 作成、 public [odakin/infographics](https://github.com/odakin/infographics)
- entry 1 件: `cosmology-history/`
- security baseline 適用済 (Dependabot/CodeQL/PVR/branch protection)

## 直近の変更 (2026-06-02)

**レビューフィードバックに基づくレイアウト修正 4 点** (`cosmology-history.tex`):

1. **EWPT アイコン (Card 2)**: Mexican-hat ポテンシャル曲線が x⁴ で縦に伸びてカードタイトルにかかっていた → `\iconEWPT` の `domain` を `-2.7:2.7` → `-2.3:2.3` に狭めて rim 高さを圧縮、タイトルとの干渉を解消 (横を狭めると縦も収まる)
2. **密度プロット 加速膨張開始 注釈**: z 値テキスト `(0.04, 5e-5)` が badge ⑦ `(0.09, 4e-5)` と同じ高さで被っていた → 注釈 (ラベル/z値/矢印始点) を `y=6e-3 / 9e-4` に持ち上げ、badge 行から ~1.3 decade 離して解消
3. **密度プロット 放射ラベル**: 「放射 ρ_rad ∝ a⁻⁴」が `(6e-6, 1e13)` で赤線から離れて浮いていた → `(8e-5, 5e12)` = 放射優勢域の赤線すぐ上に移動 (M-R 等価マーカーとも分離)
4. **再電離カード (Card 7)**: 「紫外光が中性ガスを再電離」だけ `\bfseries` で太字化していた (他カードは plain) → `\bfseries` 除去で統一

**レビューフィードバック 第 2 弾 6 点** (`cosmology-history.tex`):

1. **プロット全体を上へ**: 上部に ~12mm の白、下部の x ラベルが詰まり気味 → axis scope の `yshift` を `22` → `33` に上げて全体を上方シフト (タイトルがカード上端近くへ、下部に余裕)。axis cs 座標は scope shift に不変なので注釈位置は影響なし
2. **放射ラベルを物質線から離す**: `(8e-5, 5e12)` ではラベル右端が物質 (teal) 線と近接 → `(4e-5, 6e13)` に左上シフトで teal 線から離隔。併せて「放射優勢」era ラベルを `1e-5` → `5e-6` に左移動して放射ラベルと分離
3. **加速膨張開始の矢印始点**: 矢印が caption 左端 `(0.04, 6e-3)` から出て文字を貫いていた → caption 右上端 `(0.25, 1.3e-2)` 始点に変更して文字と分離・整列
4. **温度↔エネルギー換算表**: `1.16 × 10ⁿ K` の `1.16×` を除去 → `~ 10ⁿ K` (3 行とも、order-of-magnitude 表記に簡素化)
5. **略語定義を脚注に追加**: EWPT/QGP/BBN/CMB/DE が無定義だった → footer 下に略語凡例行を追加
6. **暗黒エネルギーの塗り (bug fix)**: DE 領域だけ塗られていなかった。原因 = `\addplot {1} \closedcycle` は**水平線に `\closedcycle` を使うと面積ゼロ**(始点↔終点が同高)。放射・物質は斜線なので塗れていた → `\fill[plotde] (axis cs:1e-7,1e-5) rectangle (axis cs:2,1)` の明示矩形に置換し、DE も線の下が塗られるよう統一

**データボックスのラベルを文字に統一** (`cosmology-history.tex`):

- 9 カードの databox で `z` / `t` / `T_γ`(記号) と `過去` / `距離`(文字) が混在していた不整合を、**全て文字に統一** (= レビュー判断: 記号 vs 文字 を熟慮し「文字統一」を選択、全 5 行維持):
  - `z` → `赤方偏移`、`t` → `年齢`、`T_{\gamma}` → `温度` (= `過去` / `距離` は据置)。9 カード × 3 ラベルを replace_all で一括置換
- **横溢れ対策**: `赤方偏移`(4 文字) がラベル列幅を広げ、括弧注記付きの「温度」行 (= Card 2 `(100 GeV)` / Card 3 `(90 MeV)` / Card 9 `(CMB)`) が右端に溢れた → `\databox` の font を `7.4` → `6.9pt`、node 位置を `(-13,5)` → `(-13.5,5)` に微調整して全 9 カード収容
- ヘッダーは「赤方偏移 z ・…」と word+記号 を併記する key なので据置 (= footer の数式 `T_γ=2.725(1+z)`, `D_C` でも記号を使用)。`過去`(遡及時間) はヘッダー 4 量に元々無いまま維持

**密度プロットの塗りを「床まで重ね塗り」に統一** (`cosmology-history.tex`):

- レビュー指摘「斜めの線の下は*すべて*同じ透過色で塗り、結果として下に行くほど色が重なる」を実装。
- 放射・物質の `\addplot {f} \closedcycle` は**端点同士を結ぶだけで床まで塗らない** (= 第2弾 point 6 の DE 水平線 `\closedcycle` 面積ゼロと同根) → `{f} -- (axis cs:2,1e-5) -- (axis cs:1e-7,1e-5) -- cycle` で **ymin(床)まで明示的に閉じる**形に変更。DE は矩形で既に床まで塗り済み。
- 3 つの透過塗り (放射 0.16 / 物質 0.14 / DE 0.16) が床まで重なり、層が重なる下ほど濃くなる。
- **era 背景帯は維持** (= レビューで「era 帯もいるやろ」、 一旦外したが復活)。era 帯 (縦カラム = 時代色) が線より上の領域を、 床まで塗りが線より下の重なりを担う相補構成。

**密度プロットの x 軸を BBN 域 (10⁻⁹) まで延長 + ステージバッジ再配置** (`cosmology-history.tex`):

- レビュー指摘「BBN の 10⁻⁸〜10⁻⁹ から図を始め、④ を図に入れ、①②③ は図の左外に出す」を実装。
- `xmin` を `1e-7` → `1e-9` に延長 (= BBN, z~10⁸⁻⁹, a~10⁻⁹⁻⁸ が図内に入る)。`xtick` に `1e-9, 1e-8` 追加。塗り (`domain`/床座標) + era 帯左端 + 線 domain を全て `1e-9` に更新 (replace_all 5+4 箇所)。
- **④ (BBN) をバッジ実位置 `a=3e-9` に配置** (= 従来 ①②③④ は左端に模式配置していた)。⑤〜⑨ は実 a 据置。
- **①②③ (a≪10⁻⁹) を軸の左外に配置** (= `\end{axis}` 後に `current axis.south west` 基準、クリップ外に描画)。「さらに過去」ラベル + バッジ横並び + ④ への矢印。
- **線ラベル回転を新アスペクト比に補正**: x が 7.3→9.3 decade に広がり傾きが急になるため、放射 `-34°`→`-41°`、物質 `-27°`→`-33°` (= axis cs 座標は不変なので位置はそのまま、回転のみ)。
- 模式配置ノート「(stages 1-4: a≪10⁻⁷)」は削除。

**追加微修正** (`cosmology-history.tex`):
- DE 線ラベル `暗黒エネルギー ρ_Λ=const` を右の注釈クラスタ (加速膨張開始/DE優勢/マーカー) から離すため `(5e-2,1)`→`(2e-3,1)` 左移動。
- **`ymax` を `1e16`→`1e20`→`1e30`→`1e35` に段階拡張** (= レビュー B→C→最終、密度の上昇を BBN まで見せる)。最終 `1e35` で放射線が左端 `a=1e-9` (密度 ~10³²) まで完全に可視。連動: era 帯天井・era ラベル (`5e34`)・`ytick` (`1e35` まで)・線ラベル回転を都度再補正。
- **`xmax` を `2`→`10` (10¹) に拡張** (= DE優勢 注釈の余白)。連動: `xtick` に `1e1` 追加、塗り/線 `domain` を `1e-9:10`、塗り右隅・DE 矩形・DE era 帯を `axis cs:10` に、線ラベル回転を再補正 (放射 `-26°`、物質 `-20°` = Dx 9.3→10)。
- **線ラベル + 優勢ラベルを各帯の幾何中心へ**: 放射 (帯 `[1e-9, 2.9e-4]` 中心 `5.4e-7`)、物質 (帯 `[2.9e-4, 0.75]` 中心 `1.5e-2`)、DE (帯 `[0.75, 10]` 中心 `2.74`)。`放射優勢`/`物質優勢`/`DE優勢` era ラベルと `放射 ρ_rad`/`物質 ρ_m` 線ラベルをそれぞれ帯中心 x に揃えた。
- **ステージバッジ ①②③ を ④〜⑨ と同じ行 (`y=4e-5` ≈ `+1.13mm`) に整列 + 連結矢印を削除** (= レビュー「①②③だけ縦位置が違う/矢印不要」)。軸外左 (`current axis.south west` 基準) で `さらに過去` ラベル付き。
- **圧縮で重なった注釈を整理**: ymax 拡張で後半 (DE 線・加速膨張開始・DE優勢) が下部 ~12% に圧縮 → `加速膨張開始`/`DE優勢` 注釈を DE 線上の空き領域 (右上、`a~1.3`) に 1.5 decade 間隔で縦積みし、各マーカーへ矢印。

## 直近の変更 (2026-05-19)

**LaTeX/TikZ への primary 移行 + editorial light theme への refactor**:

第 1 段 (= 2026-05-19 14:00) LaTeX/TikZ への primary 移行
- `cosmology-history.tex` (LuaLaTeX + article + luatexja + TikZ + pgfplots) + `Makefile` 新規作成
- 解消した HTML 版の問題: 数式 clip / font OS 依存 / 配置揃え / annotation 見切れ
- HTML 版 (`index.html` + `style.css`) は **web 配布用代替** として残置

第 2 段 (= 2026-05-19 16:00) Editorial light theme への refactor
- black → cream paper bg、 Libertinus Serif/Math/Sans、 card 70→48mm、 muted palette、 decoration 削減

第 7 段 (= 2026-05-19 21:00) plot 修正 6 点
- **hero band gradient**: 赤→紫 (= c0→c8) は同系色で対比弱、 赤→**deep cool blue** (`coolend` = HTML 1E3A8A) に変更、 hot↔cold の物理対比が直感的に
- **hero band tick 番号削除**: ❶❷❸... と card badge で番号が **2 度書かれていた重複** を解消、 hero band は pure gradient に
- **y 軸ラベルが card 外にはみ出し**: plot width 196→**188mm** に縮小、 card 内 (= 92〜287) に確実 fit
- **plot 上部の白い余白**: `ymax=1e20` (= 25 decade、 上部使用率低) → `1e16` (= 21 decade、 全 decade 有意義) に圧縮、 era label 位置を ymax 内部 (= `3e15`) へ
- **加速膨張開始 / DE 優勢 annotation 右はみ出し**: 全体的に左寄せ、 anchor を east→west に変えて両 annotation を plot 内に確実 fit
- **破線 leader → 実線 + Stealth arrow**: 視認性 UP、 矢印が label→marker 方向で「これを指している」 が明確化

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

- [ ] **cosmology-history ポスターの visual hierarchy 強化** — 宇宙の科学 第5回 (2026-05-21) の受講生コメント (出典 = git-crypt 暗号化された `lectures/2026/spring/uchu-no-kagaku/comments.yaml#uchu-2026-c356`、氏名は暗号化側のみに保持し当 public リポには置かない) で「綺麗にまとまって視覚的にも良い。強いて言えば文字のフォント・大きさの差が乏しく、ぱっと見どこを見ればいいか分かりづらい」と指摘。type scale を付けて視線の入口 (タイトル → hero band → カード grid) を明確化する。詳細プラン: `plans/2026-05-28-cosmology-history-hierarchy.md`
  - 補足: plan §1.2 は当初このコメントを「友人」と帰属していたが、実際は上記の受講生コメント (comments.yaml と一字一句一致) のため受講生コメントとして訂正済

## 次の方向性

- [ ] 第 2 entry の構想 (= 候補: 「素粒子の標準模型」 / 「銀河の階層」 / 「物理単位系」)
- [ ] 第 2 entry 追加時に common preamble (= 色定義 / font / card style) の `.sty` 化を再評価 (= 早すぎる抽象化を避けるため entry 3 件超でトリガー)
- [ ] HTML 版を保持するなら定期 sync を考えるか、 「LaTeX 正本、 HTML は古い snapshot」 の運用にするか
