# SESSION

> 📌 SESSION.md = 案件ごとの現在地 + 正本への link (進んだら置き換える、 日付を見出しにした節・commit hash・messageId を置かない = 層1 claude-config/CONVENTIONS.md#session-no-durable-record)。 日付つきの節は SESSION-archive.md へ verbatim MOVE 済 (2026-09-28)。

## 現状

- repo: 2026-05-19 作成、 public [odakin/infographics](https://github.com/odakin/infographics)
- entry 1 件: `cosmology-history/`
- security baseline 適用済 (Dependabot/CodeQL/PVR/branch protection)

## 要対応 (open)

- [ ] **cosmology-history ポスターの visual hierarchy 強化** — レビューで「文字の書体や大きさの差が乏しく、 ぱっと見でどこを見ればよいかが分かりにくい」 という指摘を受けた (原文と出典は非公開の側の記録にある)。 type scale を付けて視線の入口 (タイトル → hero band → カード grid) を明確化する。詳細プラン: `plans/2026-05-28-cosmology-history-hierarchy.md`

## 次の方向性

- [ ] 第 2 entry の構想 (= 候補: 「素粒子の標準模型」 / 「銀河の階層」 / 「物理単位系」)
- [ ] 第 2 entry 追加時に common preamble (= 色定義 / font / card style) の `.sty` 化を再評価 (= 早すぎる抽象化を避けるため entry 3 件超でトリガー)
- [ ] HTML 版を保持するなら定期 sync を考えるか、 「LaTeX 正本、 HTML は古い snapshot」 の運用にするか
