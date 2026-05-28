# cosmology-history ポスター: visual hierarchy 強化

**作成日**: 2026-05-28
**対象**: `infographics/cosmology-history/cosmology-history.tex`
**Status**: draft / 別 session (cold-eyes) で着手予定
**Author**: 2026-05-28 author session (= 色 refactor 直後、 §11 confession で bias 明示)

---

## 1. 起源と文脈

### 1.1 ポスターそのものの来歴

`cosmology-history` は `infographics/` monorepo の**第 1 entry** で、 2026-05-19 に作成。 `infographics/` 自体は科学・物理・数学系の 1 枚もの図解を蓄積する**公開 (public) リポ**で、 同 entry は流通している宇宙年表で物理的に間違いやすい 3 点 (= 例: 「ビッグバン直後の photon が見える」 等の誤解) と数値精度 3 点 (= 例: 138 億年の有効数字、 z スケールの対数 vs 線形) を修正した版を意図している。

実装は **LuaLaTeX + TikZ + pgfplots** (HTML 版 `index.html` も併存するが、 印刷 fidelity 優先で LaTeX 版が primary)。 ポスター A4 横 (= 297mm × 210mm) で組まれており、 9 ステージカード (= inflation, EWPT, QGP, BBN, M-R equality, recombination, first stars, DE acceleration, today) を hero band の下に並べる構成。 ステージ番号と対応する色 (`c0`〜`c8`) は 9 段 gradient で揃えており、 hero band は別建ての endpoint 2 色による帯。

### 1.2 friend から受けた comment

外部レビュアー (= odakin の友人、 物理を専門としない一般読者層に近い視点を持つ) に v1 PDF を見せた結果、 以下を受領:

> 宇宙史の資料として綺麗にまとまっていてわかりやすかったです。 時系列を色のグラデーションで表していて視覚的にもいいなと思いました。 強いて言うならですが、 ポスターとしては文字のフォントや大きさの差があまりないので、 ぱっと見どこを見ればいいのかわかりづらいかなと思いました。

**この comment の重み**: friend は 9 ステージカードの中身を読めば理解できると言いつつ、「ぱっと見」 (= ポスター発見時の最初の 1-2 秒) で視線が滑る、 と指摘している。 これは**ポスターという媒体の本質的要求** (= 通行人が 1-2 秒で「これは何か」 を判定できないと素通りされる) に対する failure を示唆しており、 「綺麗 / わかりやすい」 という肯定的評価とは独立に対処価値が高い。

### 1.3 同 5/28 session での色 refactor との関係

本 plan 起草と同 session (= 2026-05-28) で **hero band の配色 refactor** を実施済:

- **変更前**: `left color=c0 (赤 #C73E3A) → right color=coolend (深い青 #1E3A8A)` = 「高温 → 低温」 (= CMB 慣習 + 「炎 = 熱」 一般直感)
- **変更後**: `left color=hotend (明るい水色 #B0DFF5) → right color=coldend (暗赤 #5C1818)` = 「明 → 暗」 (= 早期の放射 luminous → 現在の DE-dim という別軸メタファー)

これは friend comment への対応ではなく**別件の design exploration** で、 user (= odakin) が「上の左が赤で右が青のやつ、 左が青の明るい色、 右が赤の暗い色としてはどうか?」 と提案 → 試作 → 「いいね、 もうちょっと鮮やかに / もうちょっと暗く」 の iteration で landed。

**この変更が hierarchy 問題に与える副次影響** (= 本 plan の §3-D で扱う):
- 凡例の文言「高温 (初期) — 低温 (現在)」 は温度軸を述べているが、 hero band は今や明度軸 (= 物理的には放射エネルギー密度の時間発展) を表しており、 帯と凡例の**意味軸がずれている**
- friend comment 当時のポスターは「高温→低温」 の赤→青で、 帯の意味は凡例と整合していた。 5/28 改修で意味軸ズレが生じた

## 2. ポスターという媒体の設計前提 (= hierarchy 判断の baseline)

ポスター固有の制約:

1. **視聴距離が可変**: 遠距離 (= 1-3m、 walk-by) でタイトル + 全体構造を判別 → 近距離 (= 30-50cm、 stop-and-read) で 9 カードの中身を読む、 の 2 段階。 同じ font が両距離で機能することはない、 必ず階層が要る
2. **scan duration が短い**: 通行人の attention budget は 1-2 秒、 教科書 1 章を読む数十分とは桁が違う。 この秒数で「何の話か」 「次にどこを見るべきか」 が決まる必要がある
3. **視線誘導は明示的でなければならない**: 紙の本なら左上から右下への自然順に依存できるが、 ポスターは grid 構成のため**視線の入り口を design で指定する必要がある** (= タイトル → hero band → カード grid という階層)
4. **印刷サイズが最終的視認性を決める**: 同じ PDF を A4 で出すか A3 で出すかで font 絶対 pt の見え方は 1.4 倍違う、 が「視聴距離も対応して変わる」 ので相対比率 (= type scale) が支配的

**type scale の design 理論**: 1 つのデザインで使う font サイズ集合は、 等比数列に近い ratio を取ると階層が読みやすい。 代表的 ratio:
- 1.125 (= minor second) — subtle、 同質感
- 1.250 (= major third) — balanced、 web body text frequent
- 1.333 (= perfect fourth) — clear hierarchy
- 1.500 (= perfect fifth) — bold、 marketing/poster 向き
- 1.618 (= golden ratio) — classical

ポスターは scan duration が短いので **1.333〜1.618 のような大きめ ratio** が向いている (= 段差が小さいと「同じ重要度」 と読まれる)。

## 3. 現状の font hierarchy 抽出と問題の診断

`cosmology-history.tex` から実測した pt サイズ:

| # | 役割 | サイズ (pt) | 前段からの ratio | 場所 |
|---|---|---|---|---|
| 1 | メインタイトル「宇宙の歴史」 | 30 | — | header 左上 |
| 2 | サブタイトル「赤方偏移 z・宇宙年齢…で読む 138 億年」 | 10.5 | **2.86** ↓ | header |
| 3 | 凡例「高温(初期) — 時間 → 低温(現在)」 | 8 | 1.31 ↓ | header 右上 |
| 4 | カードタイトル (= 「インフレーション」 等) | 8.5 | ≈ 1.0 (近接) | 9 ステージカード上部 |
| 5 | 出典クレジット | 7.5 | 1.13 ↓ (italic) | header 右下 |
| 6 | カード description | 6.8 | 1.13 ↓ | 9 ステージカード下部 |
| 7 | カード data box (= z / t / D / T 等) | ~7 推定 | ≈ 1.0 | 9 ステージカード中央 |

**問題の診断** (= type scale 理論に照合):

### 問題 1: タイトルとサブタイトルの段差が極端 (= 2.86)
- 30 pt → 10.5 pt は ratio 2.86 で、 タイトルだけ突出し、 サブタイトル以降は「すべて small text」 という 2 階層構造になっている
- ポスターの 3 階層 (= 遠距離 = title only / 中距離 = title + subtitle + hero band / 近距離 = full text) を作るには、 中距離 layer (= ~16-20 pt 帯) が欠けている

### 問題 2: サブタイトル以降が全部 6.8〜10.5 pt の狭い帯に居る
- 10.5 / 8.5 / 8 / 7.5 / 6.8 の 5 種類が約 1.5 pt 刻みで詰まっており、 type scale ratio で言うと 1.04〜1.23 (= 全部 minor second 未満)
- friend comment 「フォントや大きさの差があまりない」 はこの帯を見て言っている可能性が極めて高い
- 近距離で読んでも「カードタイトル (= 8.5) と description (= 6.8) のどちらが上位か」 が一見で分からない (= 太字 / sans-serif で区別はしているが、 サイズだけ見ると ratio 1.25 で同等扱いに見える)

### 問題 3: hero band に文字情報が無い
- gradient だけで時間軸を示し、 数値 anchor (= 「$10^{-32}$ s」 「$\sim$3 億年」 「138 億年」 等) が hero band に乗っていない
- 結果: 帯の幅 (= 281 mm = 紙の 95%) と時間スケール 13.8 Gyr の対応が、 帯を見ただけでは分からない (= カード内のデータを読むまで scale 感が立ち上がらない)
- 「中距離 layer = ~16-20 pt」 の入る正しい場所が hero band 上で、 ここに anchor 文字を置くと層欠落と帯の意味付け不足を同時に解決できる

### 問題 4: 9 ステージカードが完全に等価
- 全カードが同じレイアウト + 同じフォントサイズ + 同じ色帯厚で並ぶ、 ステージ番号バッジの色だけが違う
- 物理的重要性 (= BBN, recombination, 加速膨張開始の 3 つは「教科書 1 章分」 級の event、 EWPT / QGP / first stars は「教科書 1 節」 級) が視覚的に等価化されている
- ポスターとして「物語の山場」 が立たない、 全部読まないと重要度が分からない設計

## 4. 改善案 (= 各案の design theory anchor + 想定効果 + tradeoff)

### 案 A: hero band に anchor 文字を 1 つだけ大きく置く

**具体**:
- 帯の左端付近 (= 一番初期) に「インフレーション」 + 「$\sim 10^{-32}$ s」 を ~20 pt sans-serif bold で配置
- 帯の右端 (= 現在) に「現在」 + 「138 億年」 を同サイズで配置
- 中間 (= BBN ≈ 3 min / recombination ≈ 38 万年 / 現在 ≈ 138 億年) に ~6-7 pt の tick label を 3-5 個並べる選択肢もあるが、 過剰だと帯のミニマリズムを壊すので**第一実装では端 2 つだけ**

**design theory anchor**:
- §2 の「3 階層構造」 で欠けている**中距離 layer (~16-20 pt)** をここに入れる
- type scale で言うと 30 → 20 → 10.5 → 8.5 の段差 (= 1.5 / 1.9 / 1.24) になり、 上段が perfect fifth 級でクリア、 下段は依然密だが中段が空ければ視線が下まで誘導される

**想定効果**:
- 視線誘導: title (30) → hero band 文字 (20) → カード grid (8.5 帯)、 の 3 段階階層が成立
- 帯の意味付け: anchor 文字が時間スケールを直接示すため、 帯の幅と時間範囲の対応が即理解される

**tradeoff**:
- 帯の高さ (= 現状 3.5 mm) に 20 pt 文字を内包できない、 帯を 6-8 mm に厚くする必要 (= レイアウト調整必要)
- 帯の上か下に文字を**外置き**する案もあるが、 帯と文字の所属関係が弱くなる
- 5/28 色 refactor の意味軸 (= 明 → 暗 = 放射優勢 → DE 優勢) と「時間 anchor 文字」 が衝突する可能性 (= 文字が温度や redshift を示すと、 帯の明度メタファーと別軸を併記することになる)

### 案 B: カードタイトルを強める

**B-1: 全カード一律 8.5 pt → 10.5 pt (= 等価強化)**
- ratio: subtitle (10.5) と同 pt にしてカード grid を「ポスター中部のメインコンテンツ」 と明示
- description (6.8) との段差 ratio が 1.54 になり perfect fifth 級、 「タイトル vs 説明」 の階層が明確化

**B-2: 主要 3 カードのみ強化 (= 重み付け強化)**
- 「主要」 = BBN (4) / recombination/CMB (6) / 加速膨張開始 (8) の 3 つを ~12 pt 太字に、 他は 8.5 pt キープ
- 物理的に「教科書 1 章分」 級の event を視覚化、 ポスターとして物語の起伏が立つ

**design theory anchor**:
- B-1 は **type scale 整合** (= タイトル群を一つの pt に揃える)
- B-2 は **information weighting** (= 視覚的強調 = 認知優先度) で、 設計理論的にはより高度だが「主要 3 つの選定」 という subjective 判断が入る

**想定効果**:
- B-1: 「ぱっと見」 でカード grid のタイトルが scan しやすくなる (= friend comment への直接対応)
- B-2: 「最初に読むべき 3 カード」 が誘導される、 物理史の「起伏」 が伝わる

**tradeoff**:
- B-1: カード幅 22 mm の text width に 10.5 pt が収まるか要確認 (= 「インフレーション」 = 7 文字 × 約 1 char width 5 pt → 35 pt = 12.3 mm、 OK そう。 「電弱対称性の破れ」 = 8 文字 → 14 mm、 ぎり)
- B-2: 「主要 3 つ」 の選定根拠を author (= odakin) が決める必要、 物理的に異論が出る可能性 (= 例: EWPT を入れない理由は何か)
- B-2: 強化と非強化の混在は「平等な 9 段」 という色 gradient design と矛盾する見方もある

### 案 C: カードタイトルとデータ間の visual gap を増やす

**具体**:
- タイトル直下の icon (= y = 22.5 タイトル / y = 13 アイコン中心、 現状 9.5 mm gap) を +1-2 mm 増やしてタイトルが「島」 として浮く感じを強める
- もしくはカード上端の色アクセント帯 (= 現状 0.5 mm) を 1 mm に厚くしてカードの「頭」 を強調

**design theory anchor**:
- **proximity principle** (Gestalt): 近いものは一群と認識される。 タイトルと icon が近すぎると「タイトル + icon = 1 つの島」 になり、 タイトル単独の優位性が弱まる

**想定効果**:
- 案 B でタイトル pt 上げをしない場合の代替手段
- タイトルが視覚的に「カード上の独立要素」 として浮く

**tradeoff**:
- カード高さ (= 56 mm) を増やすか、 他の領域を圧縮するか、 のレイアウト調整必要
- 効果は B より subtle、 friend comment への直接対応としては弱い

### 案 D: 凡例文言の整合 (= 5/28 色 refactor の follow-up)

**具体**:
- 凡例「高温 (初期) — 時間 → 低温 (現在)」 を改修
- option D-1: 帯の意味に合わせて「放射優勢 (初期) → 暗黒エネルギー優勢 (現在)」
- option D-2: 二軸併記「高温 (初期) / 放射優勢 — 低温 (現在) / 暗黒エネルギー優勢」
- option D-3: そのまま温存 (= 「高温 / 低温」 は redshift と温度の対応として正確で、 明度メタファーとは独立に成立すると判断する)

**design theory anchor**:
- **semantic consistency**: 視覚要素 (= 帯の明度) と凡例文言の意味が一致していないと、 読者は「どの軸を読まされているか」 で迷う

**想定効果**:
- D-1: 帯の明度メタファーを直接説明、 cleanest だが「温度」 という最も familiar な物理量を捨てる
- D-2: 二軸併記で読者に「両方の見方ができる」 と提示、 情報量は増えるが scan しにくくなる
- D-3: 帯と凡例の意味軸ズレを許容、 「明 → 暗」 はあくまで装飾、 物理は温度軸で読んでもらう

**tradeoff**:
- friend comment は色軸の文言を問題視していない、 が 5/28 改修の意味軸ズレは別問題として残る
- author の意図 (= 5/28 改修の動機) を明確化すべき、 「装飾として明度を取った」 のか「物理的意味として明度を取った」 のかで判断が変わる

## 5. 案の組み合わせ matrix

| 組み合わせ | 直接対応度 | 実装コスト | risk |
|---|---|---|---|
| **B-1 のみ** | ★★★ | 低 (= 1 行変更) | text width 超過のみ |
| **A + B-1** | ★★★★ | 中 (= hero band 高さ調整) | 帯の意味軸 (明度) と anchor 文字の衝突 |
| **A + B-2** | ★★★★ | 中〜高 (= 主要 3 つの選定根拠要) | 視覚的に「平等な 9 段」 と矛盾 |
| **A + B-1 + C** | ★★★★★ | 高 | layered 改修で意図が分散、 friend 再評価で「やりすぎ」 と返る可能性 |
| **A + B-1 + D-1** | ★★★★ | 中 | 5/28 改修と一緒に意味軸を refactor、 一貫性は最大 |

**推奨第一実装**: **B-1 単独 (= 全カードタイトル 10.5 pt 化)** から始める。 friend comment への最小対応 + 実装コスト低 + risk 限定。 これで再評価して足りなければ A を追加。

## 6. 実装手順 (= cold-eyes session 向け)

1. **現在の PDF を 1 部 print** (A4 / A3 両方) して紙で hierarchy を確認 (= 画面と紙で印象違うため、 cold-eyes session 開始時の grounding)
2. **B-1 を最小実装** (= `\fontsize{8.5}{10.5}` → `\fontsize{10.5}{13}` を 9 カード全部に置換、 `text width=22mm` を超えないか要確認)
3. **再 build + 紙 print + friend 再ヒアリング** (= 「最初にどこを見たか?」 「次にどこを見たか?」 「読みやすくなったか?」)
4. friend 再ヒアリング結果で:
   - **十分**: ここで stop、 plan close
   - **まだ平板**: 案 A 追加 (= hero band 文字、 帯高さ 3.5 → 6-8 mm)、 step 2-3 再実行
   - **「メリハリが強すぎて全体の調和が崩れた」**: 案 C で代替 (= 案 B を戻して visual gap で hierarchy 作る)
5. **5/28 色 refactor の意味軸ズレ** (= 案 D) は **(1)〜(4) と独立に判断**、 author に「5/28 改修は装飾意図か物理意図か」 を明示確認してから D-1/D-2/D-3 を選ぶ

## 7. open questions (= cold-eyes session 判断)

- **Q1**: 案 A 採用時、 帯の高さ (= 現状 3.5 mm) を何 mm まで増やすか? 帯が太くなりすぎると「カード grid との視覚バランス」 が崩れる、 上限の経験則は? (= 紙面の 5% = 約 10.5 mm が経験的 max か?)
- **Q2**: 案 B-2 を取る場合の「主要 3 カード」 選定: BBN (4) / recombination (6) / 加速膨張 (8) で異論ないか? author に物理的重要性 ranking を明示確認する
- **Q3**: 案 A の anchor 文字と案 B-1 のカードタイトル強化を**両方やると過剰**か? 案 B-1 単独で friend 再評価が positive なら案 A は不要、 という ordering 判断が正しいか
- **Q4**: ポスター想定の**印刷サイズ** (= A4 / A3 / A2 のどれか) を author に確認、 サイズによって絶対 pt の判断基準が変わる
- **Q5**: 5/28 色 refactor の意味は「装飾」 か「物理メタファー」 か、 author 明示確認 → D-1/D-2/D-3 選択 → 凡例文言確定
- **Q6**: ポスターの target audience (= 「物理を専門としない一般読者」 か「物理系の学生」 か「教育普及用」 か) を author 確認、 hierarchy 設計のターゲットが変わる

## 8. trigger / 着手判断

- **trigger 条件無し**: friend comment は「強いて言うなら」 で受け取り、 急務ではない。 別 session で着手するまで現状維持で可
- **再 surface タイミング**:
  - (a) ポスターを別の人に見せて同種コメントを再度受けた
  - (b) print して紙で見て自分でも hierarchy が気になった
  - (c) `infographics/` monorepo の他 entry を作る際に shared design system 化を検討、 そのタイミングで第 1 entry も一緒に改修
  - (d) ポスターをどこかに掲示 / 配布する具体予定が立った (= 学園祭、 オープンキャンパス、 学会 poster session 等、 「対外性が立つ瞬間」)
- **担当**: cold-eyes session (= author bias を避け、 friend comment を起点に独立判断、 §11 confession を参照)

## 9. 副次論点 (= 本 plan の scope 外だが関連で挙げておく)

- **9 段 gradient (c0..c8) と hero band gradient (hotend → coldend) の関係**: 現状 2 系統が別建てで動いており、 hero band が「明度」 軸、 9 段が「温度っぽい段階色」 軸として独立。 design として「2 軸ある」 のは情報量だが、 friend comment と直接関係ないので本 plan では触れない
- **plot 領域 (= 下段 energy density plot)** の typography: 軸ラベル / 凡例 / 注記の font size は本 plan で扱っていない、 別途要確認
- **アイコンの視認性**: 各カードのアイコンは 5-13 mm 程度の小さい SVG/TikZ で、 印刷サイズによっては潰れる可能性。 別 plan で扱う

## 10. 関連 file

- 対象 source: [`cosmology-history/cosmology-history.tex`](../cosmology-history/cosmology-history.tex)
- 生成物: [`cosmology-history/cosmology-history.pdf`](../cosmology-history/cosmology-history.pdf), [`cosmology-history/cosmology-history.png`](../cosmology-history/cosmology-history.png)
- メモ: [`cosmology-history/NOTES.md`](../cosmology-history/NOTES.md)
- 5/28 色 refactor 経緯: 2026-05-28 session log (= 当 session)

## 11. author confession (= 2026-05-28)

- **bias 1**: 本 plan の起草は author session = 5/28 ターンで、 色 refactor (= hot/cold blue→red の swap + bright/dark intensification) と同 session 内。 author は色変更直後で「hero band 全体への思い入れ」 が高まっている状態で書いており、 **hero band に文字を盛りすぎる方向 (= 案 A 推奨) に bias がかかっている可能性**
- **bias 2**: friend comment への対応として最も「実装が楽な」 案 (= B-1) を §5 で推奨第一実装にしているが、 これは author の「session 内で結論を出したい」 圧力からの bias とも読める。 cold-eyes session は **「逆方向 = hero band は文字を盛らず純粋な視覚 anchor のままにし、 hierarchy は card 側だけで作る」** という選択肢、 もしくは「friend comment は font size 問題ではなく font weight / contrast / color value 問題と diagnose 直す」 という別 diagnosis も独立評価してほしい
- **bias 3**: 「friend が「ぱっと見どこを見ればいいかわからない」 と言ったのは hero band の問題か card の問題か、 もしくは全く別 (= 色軸、 アイコン、 plot 領域) の問題か」 は author 単独では判別できていない。 cold-eyes が friend 再ヒアリング (= 「最初にどこを見たか?」 「次にどこを見たか?」) を可能なら author に提案 (= step 3 で formalize)
- **bias 4**: 本 plan は **§2 で type scale 理論を持ち出した**が、 これは author が design 理論を「知っている」 ことで「正しい improvement」 と権威付けしている可能性がある。 ポスター design の専門家が見れば「type scale だけで poster hierarchy は解けない、 layout・color・contrast の総合判断」 と言う可能性があり、 cold-eyes は理論への過信を warning とすべき
- **bias 5**: 9 ステージカードの「平等な並び」 を「物語の起伏が立たない」 と問題視 (= §3 問題 4) しているが、 これは author の物理史観 (= BBN / recombination / 加速膨張開始が「主要」 とする視点) を反映している。 一般読者にとっての「物語の山場」 は別の場所 (= 例: 「ビッグバン」 そのもの、 「最初の星」 の誕生、 「宇宙の現在」) かもしれない。 「主要 3 つ」 の選定は author 側で正当化が要る、 cold-eyes が決めるべきではない
