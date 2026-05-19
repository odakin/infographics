# SESSION

## 現状

- repo 作成: 2026-05-19
- entry 1 件: `cosmology-history/` (= ユーザー指摘の元 infographic に対する修正版、 ゼロベース re-design)

## 直近の変更 (2026-05-19)

- `git init -b main`、 必須 4 点ファイル + README 作成
- `cosmology-history/index.html` 作成:
  - 元 infographic の物理的誤り 3 点修正 (BBN 核種 ²He/⁷He → ²H/³He、 ステージ 6「光が再結合」 → 「光が周囲のガスを再電離」、 ステージ 3「水素」 → 「重水素」)
  - 数値精度 3 点修正 (ステージ 2 100 MeV → 90 MeV、 ステージ 7 T_γ 3-5 K → 3.5-4.6 K、 ステージ 6 t 1-10億年 → 2-10億年)
  - 「角度の単位」 パネル削除 (= cosmology theme と無関係)
  - 温度勾配 palette (= 赤 → 青で T 物理意味に mapping)、 IBM Plex Sans JP、 CSS Grid、 dark mode、 ρ vs a plot に 2 縦線 (加速開始 / DE 優勢を区別)
  - 修正点と典拠は `NOTES.md`

## 要対応 (open)

- [ ] preview server で見え方確認 (= 次タスク)
- [ ] GitHub `odakin/infographics` public 作成、 push、 secure-new-repo.sh 適用
- [ ] `odakin-prefs/repos.md` と `odakin-prefs/CLAUDE.md` の現在の作業プロジェクトに登録
