# DESIGN

## なぜ monorepo か (= per-topic 別 repo にしない)

判断: **1 つの `infographics/` repo の中に topic 別 subdirectory を並べる**。

- (a) インフォグラフィック単体は小さい (= HTML 1 枚 + CSS 1 枚)。 repo 1 つにつき README/CLAUDE.md/SESSION.md/DESIGN.md/.gitignore の 5 ファイル + GitHub 側の security baseline (Dependabot/CodeQL/branch protection 等) が overhead で、 1 entry の本体ファイル数を上回る
- (b) 視覚 design system (= 色 / typography / grid) が将来共有される可能性が高い。 同 repo 内なら DESIGN.md 1 つで管理できる、 別 repo だと drift する
- (c) entry が単発で終わる可能性も高く、 「専用 repo を立てた割に 1 entry で凍結」 という負債を避けたい

却下案: **1 entry = 1 repo** (= 例: `cosmology-history` repo)。 上記 (a)(b)(c) でコストの方が大きい。

将来 reconsider トリガー:
- 単一 entry が肥大化 (= 50 ファイル / 5000 行超) → 切り出し検討
- 別 contributor が join + entry に独立 maintainership が必要 → split

## なぜ HTML + 埋め込み SVG か (= 単独 SVG / TikZ にしない)

判断: **HTML + CSS + inline SVG**。

| 候補 | Pros | Cons | 採否 |
|---|---|---|---|
| **HTML + inline SVG** | preview server で HMR、 modern CSS (gradient/shadow/var font)、 dark mode、 export 可 | print-to-PDF で font 埋め込みに注意 | ✓ |
| 単独 SVG | LaTeX `\includegraphics` に直接、 single file | CSS 表現が限定的、 iteration 遅い (= 座標電卓化) | × |
| TikZ (LaTeX) | 論文取り込みに最強 | 自由度低、 modern design (gradient/glassmorphism) が困難 | × |
| Mermaid | 軽量、 markdown 内 inline | layout 制御不能、 美麗化困難 | × |

HTML 起点なら → SVG / PNG / PDF いずれにも export 可能 (= chromium headless)。 逆方向 (= SVG → HTML reconstruction) は CSS 表現を失うため不可逆。

## design system

### 色 palette

**温度勾配 mapping**: timeline 8 段の色を **物理温度に対応** させる。 赤 (= 高温・初期宇宙) → 紫 → 青 (= 低温・現在) の diverging palette。 単に「段ごとに違う色」 にせず、 **色自体が物理量を encoding** する。

```
--temp-1: hsl(0,   85%, 55%)   /* インフレーション = 真っ赤 */
--temp-2: hsl(20,  85%, 55%)   /* QGP/ハドロン化 */
--temp-3: hsl(40,  80%, 55%)   /* BBN */
--temp-4: hsl(60,  75%, 50%)   /* 物質-放射等価 */
--temp-5: hsl(180, 70%, 50%)   /* 再結合/CMB */
--temp-6: hsl(220, 65%, 55%)   /* 最初の星/再電離 */
--temp-7: hsl(260, 60%, 60%)   /* 加速膨張/DE */
--temp-8: hsl(280, 50%, 55%)   /* 現在 */
```

### typography

- **本文**: `'IBM Plex Sans JP', system-ui, sans-serif` (= 漢字英数の重み・字幅整合)
- **数式・指数**: `'IBM Plex Mono', monospace` で digit alignment
- 元 infographic の数式 (= z = (λ_obs - λ_emit) / λ_emit) は **KaTeX** で組版 (CDN)
- 段ごとの数値 (z / t / T_γ) は 3 段固定 grid で縦揃え

### layout

- 8 段 timeline は **CSS Grid** (`grid-template-columns: repeat(8, 1fr)`)
- 各段は **glass card** (= `backdrop-filter: blur(10px)` + semi-transparent bg) で背景 gradient (= 温度勾配) を透かす
- ρ vs a プロット は inline SVG、 軸ラベル / 凡例 / 縦線も SVG 内

### dark mode

`@media (prefers-color-scheme: dark)` で背景反転。 温度勾配 palette は dark mode でも視認性を保つ (= saturation 高め、 lightness 5-10% 下げ)。

## 元 infographic からの修正方針

修正点と典拠は `cosmology-history/NOTES.md` に集約。 設計判断 (= 何を修正対象とし何を残すか) はここに書く。

### 修正の優先順位 (= 何を変えるか)

1. **物理的誤り** (= 教育的害が大きい): 必ず修正
   - BBN 核種ラベル ²He / ⁷He → ²H / ³He
   - 「光が再結合」 → 「光が周囲のガスを再電離」
   - 「水素・ヘリウム・少量のリチウム」 → 「重水素・ヘリウム・少量のリチウム」
2. **数値精度** (= 概数の幅): 大きく外れているもののみ修正
   - 100 MeV ↔ 10¹² K 換算 → 90 MeV (= 86 MeV のラウンド)
   - T_γ at z=0.3-0.7 → 3.5-4.6 K
   - t at z=6-20 → 2-10億年
3. **構成上の問題**: 削除 / 統合
   - 「角度の単位」 panel 削除 (= cosmology と無関係)
   - 加速膨張開始 (z=0.7) と DE 優勢 (z=0.33) を plot 上で **2 縦線** に分離

### 残すもの (= 元 infographic から保持)

- 8 段 timeline の構造そのもの (= 教育的に分かりやすい)
- 4 種類の軸 (赤方偏移・宇宙年齢・何年前・主な出来事)
- T_γ, ρ_rad/ρ_m/ρ_Λ ∝ a^n の式
- 換算表 (= MeV ↔ K)

## 典拠

- Planck 2018 cosmological parameters (z_eq ≈ 3402, z_rec ≈ 1089)
- PDG 2024 (粒子質量、 BBN 産物)
- BBN review: Cyburt+ Rev. Mod. Phys. 88, 015004 (2016)
