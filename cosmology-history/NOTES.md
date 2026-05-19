# cosmology-history — NOTES

## 元 infographic からの修正点

このインフォグラフィックは、 流通している日本語版「宇宙の歴史: 赤方偏移・宇宙年齢・何年前・主な出来事」 (8 段 timeline + 4 サイドパネル + 下部 ρ vs a プロット) を題材に、 物理的誤り 3 点 + 数値精度 3 点 + 構成上の問題 1 点をゼロベース re-design で修正したもの。

### A. 物理的誤り (= 必ず修正)

**A-1. BBN パネルの核種ラベル**

| 元図 | 修正版 | 理由 |
|---|---|---|
| `²He` | **`²H` (D, 重水素)** | ²He = diproton は束縛状態を持たない (= 「核」 として存在しない)、 BBN 産物ではない |
| `⁷He` | **`³He`** | ⁷He は半減期 ~10⁻²¹ 秒、 BBN で有意量生成されない。 標準 BBN 産物は ²H/³He/⁴He/⁷Li |
| `⁴He` ✓ | `⁴He` | OK (主産物、 全質量の ~25%) |
| `⁷Li` ✓ | `⁷Li` | OK (微量、 BBN の "lithium problem" でも有名) |

アイコンも陽子 (赤) + 中性子 (青) の組合せで正しい構造を描画 (= ²H = 1p+1n, ³He = 2p+1n, ⁴He = 2p+2n, ⁷Li = 3p+4n)。

**A-2. ステージ 6「主な出来事」 の wording**

- 元図: 「最初の星・銀河が形成され、 **光が再結合して** 周囲のガスが再電離される」
- 修正版: 「最初の星・銀河が形成され、 **その紫外光が周囲の中性ガスを再電離する**」

「光が再結合」 は宇宙論に存在しない現象 (= 光子は再結合しない)。 再結合 (recombination) は ステージ 5 で電子+陽子 → 中性原子 の話、 ステージ 6 はその逆過程の **再電離 (reionization)** で、 ロジックが逆向きになっていた。

**A-3. ステージ 3 説明 「水素」 の混入**

- 元図: 「軽元素 (水素・ヘリウム・少量のリチウム) の原子核が合成される」
- 修正版: 「軽元素 (重水素・³He・⁴He・少量の ⁷Li) の原子核が合成される (= ¹H は既存)」

¹H (ただの陽子) は BBN で **新たに**合成される産物ではなく、 バリオン形成は BBN より遥か前 (= バリオジェネシス) で完了している。 BBN で合成されるのは D・³He・⁴He・⁷Li のみ (微量で ⁶Li, ⁷Be → ⁷Li 経由)。

### B. 数値精度 (= 元値が粗いものを修正)

**B-1. ステージ 2 の温度換算**

- 元図: `T_γ ≳ 10¹² K (≈ 100 MeV)`
- 修正版: `T_γ ≳ 10¹² K (≈ 90 MeV)`

換算 `100 MeV = 1.16 × 10¹² K` (= 右下の換算表) を使うと、 `10¹² K = 100/1.16 ≈ 86 MeV`、 「≈ 100 MeV」 はやや甘いラウンド。 「≈ 90 MeV」 が表との整合上正しい。

**B-2. ステージ 7 の T_γ 範囲**

- 元図: `T_γ ≈ 3 ~ 5 K`
- 修正版: 加速開始 (z=0.7) で `T_γ ≈ 4.6 K`、 DE 優勢 (z=0.33) で `T_γ ≈ 3.5 K`

`T = 2.725 × (1+z)` から、 z=0.3 で 3.54 K、 z=0.7 で 4.63 K。 元の「3〜5 K」 は下限がやや早く、 個別に書いた方が情報量が多い。

**B-3. ステージ 6 の t 範囲**

- 元図: `t ≈ 1 ~ 10 億年`
- 修正版: `t ≈ 約 2 ~ 10 億年`

z=20 で t ≈ 0.18 Gyr (= 1.8 億年)、 z=6 で t ≈ 0.94 Gyr (= 9.4 億年)。 「1 億年」 はやや早すぎ。

### C. 構成上の問題

**C-1. 「角度の単位」 panel 削除**

元図には `1° = 60′ = 3600″` (arcmin/arcsec) の解説パネルがあったが、 宇宙年表・赤方偏移と論理的に独立した内容で、 文脈から浮いていた。 CMB 角パワースペクトル (ℓ vs 角度) や視直径距離 d_A を別途図示するなら意味があるが、 本図では使われない。 削除。

**C-2. ρ vs a プロットの縦線分離**

元図は加速膨張開始 (z=0.7) と DE 優勢 (z=0.33) の区別が曖昧で、 1 本の縦線で代表させていた。 修正版は **2 本の縦線** で明確に区別 (= 教育的に重要な区別、 「加速」 と「DE 支配」 が別物だという誤解防止)。

## 典拠 (= 確認した値)

| 量 | 値 | 出典 |
|---|---|---|
| z_eq (matter-radiation equality) | ≈ 3402 | Planck 2018 cosmological parameters |
| z_rec (recombination) | ≈ 1089 | Planck 2018 |
| z_acc (acceleration onset) | ≈ 0.67 | Ω_m(1+z)³ = 2 Ω_Λ (Ω_m=0.3, Ω_Λ=0.7) |
| z_DE (DE dominance) | ≈ 0.33 | Ω_m(1+z)³ = Ω_Λ |
| t_0 (universe age today) | 13.8 Gyr | Planck 2018 |
| t at z=0.7 | 7.6 Gyr | ΛCDM integration |
| t at z=0.33 | 10.2 Gyr | ΛCDM integration |
| BBN nuclei | D, ³He, ⁴He, ⁷Li | Cyburt+ Rev. Mod. Phys. 88, 015004 (2016) |
| m_p | 938.272 MeV/c² | PDG 2024 |
| m_n | 939.565 MeV/c² | PDG 2024 |
| Δm = m_n - m_p | 1.293 MeV | PDG 2024 |
| T_γ today | 2.7255 K | COBE/FIRAS (Mather+) |
| 1 eV ↔ K | 11604 K/eV | k_B = 1.381e-23 J/K |

## 元 infographic で保持したもの (= 修正不要だった部分)

- 8 段 timeline 構造 (= 教育的に分かりやすい)
- 4 種類の data 軸 (赤方偏移 z / 宇宙年齢 t / 何年前 / 光子温度 T_γ)
- BBN の核物理メモ (= m_p, m_n, Δm)
- MeV ↔ K の換算表
- ρ vs a の対数-対数 plot
- 各段の主要事象記述 (= 1, 4, 5 はそのまま; 2 もほぼ OK)

## design 判断

- **色 palette**: 温度勾配 (= 赤 → 紫) を timeline 上の物理量 (T_γ) に mapping。 元図のような「段ごとに違うパステル色」 ではなく、 **色そのものが情報を encoding** する設計
- **typography**: IBM Plex Sans JP + IBM Plex Mono (= 数値・指数を mono で digit alignment)
- **layout**: CSS Grid で 8 段並列、 glass card (= backdrop-filter blur)
- **dark mode**: `prefers-color-scheme` 対応、 saturation を上げて視認性確保
- **数式**: KaTeX で `z = (λ_obs - λ_emit) / λ_emit` と `1+z = a₀/a` を組版
- **export**: chromium ヘッドレスで PDF / PNG 化可能 (= ../CLAUDE.md の Export 節参照)

## レイアウト・プロット design (= 2026-05-19 第 2 版)

**ページ size**: A4 横置き (297mm × 210mm) に完全 fit。 `@page` rule で印刷整合、 screen でも同サイズで center 表示。

**プロット再設計**:
- **era 背景 band** (= 放射優勢 / 物質優勢 / DE 優勢) を半透明 gradient で重ね、 3 つの epoch を視覚的に区分け (= 元版は単純な log-log で epoch 境界が読み取りにくかった)
- **line color** を温度勾配 palette と整合: 放射 = warm orange (= hot/early universe color) / 物質 = cool blue / DE = violet (= cool/late universe color)。 page 全体の温度色文法と統合され、 line そのものが時間軸の意味も帯びる
- **area fill** (= gradient で下方フェード) で line の下に depth 追加、 単純な細線より visually richer
- **直 line label** を plot 内に配置 + 白 stroke 背景で legibility 確保 → plot 下部の凡例を **完全廃止** (= 重複情報の削減)
- **crossover marker** (= filled circles with ring) を 3 か所 (M-R 等価 / 加速開始 / DE 優勢) に配置、 単純な交点ではなく明示的なイベント点として可視化
- **leader 付き annotation** で物理的近接の 2 点 (= 加速開始 a≈0.59 と DE 優勢 a≈0.75、 log a で 0.1 程度の差) を上下に分離 label、 元版の同居縦線重なり問題を解消
- 「現在 a=1」 縦点線 marker を右端に追加し、 plot 右端が「今」 であることを明示

## 将来の改善余地

- 各段の icon、 特にステージ 4 (天秤) と 5 (再結合) はさらに洗練可能
- PDF/PNG export を Makefile / shell script で 1 コマンド化
- KaTeX 依存を局所化 (= CDN ではなく self-host)、 offline 環境対応
- 動的要素 (= 各段の hover で詳細展開、 plot の line drawing animation) は静的 1 枚もの infographic の路線から外れるため別 entry での実験を検討
