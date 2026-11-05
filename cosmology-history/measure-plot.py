#!/usr/bin/env python3
"""measure-plot.py — 組んだポスターの PNG から密度プロットの余白・軸の枠・線ラベルの回転角を実測する。

pgfplots の配置は内部の geometry が直感と違うので、 推論でなく組んだ PNG を測って決める
(一般形 = claude-config の conventions/tikz-pgfplots.md の「中央寄せ = 平行移動」 の節)。
NOTES.md の §密度プロットの軸 の「線ラベルの回転」 と §プロットを card 内で中央寄せ の数値はこの script の出力。

出すもの:
  1. card の中の内容 (ink) の bounding box と、 card の 4 辺までの余白 (mm)。
     上下・左右の差がずれていたら、 tex の axis の scope の shift をその半分だけ動かす (size は変えない)。
  2. 軸の枠 (fgmute 色の長い縦線・横線) の位置と大きさ (mm)。
  3. log-log の傾き n の直線が画面で傾く角 = atan(n × (枠の高さ / y の桁数) / (枠の幅 / x の桁数))。
     線ラベルの `rotate=` はこの角の符号を負にした値。 axis の高さ・幅・範囲を変えたら測り直す。

使い方 (`make png` の後に):
  python3 measure-plot.py                       # 既定 = cosmology-history.png、 本 entry の card と軸の範囲
  python3 measure-plot.py --png other.png --card 90 289 14 118 --decades 10 40
  python3 measure-plot.py --selftest

前提: 紙 = A4 横 (297 × 210 mm)、 card の座標は tikz と同じ「左下が原点の mm」。
"""
import argparse
import math
import sys

import numpy as np
from PIL import Image

PAGE_W, PAGE_H = 297.0, 210.0
FGMUTE = (0x6E, 0x72, 0x80)  # 軸の枠の色 (tex の \definecolor{fgmute})


def card_box_px(shape, card, mm):
    """card = (x0, x1, y0, y1) in mm (y は下から)。 枠線を避けて 8px 内側の画素の範囲を返す。"""
    x0, x1, y0, y1 = card
    left, right = int(x0 * mm) + 8, int(x1 * mm) - 8
    top, bottom = int((PAGE_H - y1) * mm) + 8, int((PAGE_H - y0) * mm) - 8
    return left, right, top, bottom


def ink_margins(img, card, mm, threshold=60):
    """card の地の色 (内側の隅の 1 画素) から総差 threshold を超える画素を内容とみなし、 4 辺の余白 (mm) を返す。"""
    left, right, top, bottom = card_box_px(img.shape, card, mm)
    sub = img[top:bottom, left:right]
    ink = np.abs(sub - sub[5, 5]).sum(axis=2) > threshold
    rows = np.where(ink.any(axis=1))[0]
    cols = np.where(ink.any(axis=0))[0]
    if len(rows) == 0:
        return None
    return {
        "top": (rows[0] + 8) / mm,
        "bottom": (bottom - top - rows[-1] + 8) / mm,
        "left": (cols[0] + 8) / mm,
        "right": (right - left - cols[-1] + 8) / mm,
    }


def axis_frame(img, card, mm, color=FGMUTE, tol=60, frac=0.9):
    """card の中で color の画素が縦・横に frac 以上続く列と行から軸の枠を探し、 (左, 右, 上, 下) を mm (左上が原点) で返す。"""
    left, right, top, bottom = card_box_px(img.shape, card, mm)
    sub = img[top:bottom, left:right]
    m = np.abs(sub - np.array(color)).sum(axis=2) < tol
    # 縦の枠: 列の中で color が最も長く続く長さが、 card の高さの 40% 以上
    col_hits = [c for c in range(m.shape[1]) if _longest_run(m[:, c]) > 0.4 * m.shape[0]]
    if len(col_hits) < 2:
        return None
    c0, c1 = min(col_hits), max(col_hits)
    width = c1 - c0
    row_hits = [r for r in range(m.shape[0]) if m[r, c0:c1 + 1].sum() >= frac * width]
    if len(row_hits) < 2:
        return None
    r0, r1 = min(row_hits), max(row_hits)
    return ((left + c0) / mm, (left + c1) / mm, (top + r0) / mm, (top + r1) / mm)


def _longest_run(v):
    best = cur = 0
    for x in v:
        cur = cur + 1 if x else 0
        best = max(best, cur)
    return best


def slope_angle(n, frame_w, frame_h, x_decades, y_decades):
    """log-log で a^-n の直線が画面で下がる角 (度、 正の値)。"""
    return math.degrees(math.atan(n * (frame_h / y_decades) / (frame_w / x_decades)))


def measure(path, card, decades):
    img = np.asarray(Image.open(path).convert("RGB")).astype(int)
    mm = img.shape[1] / PAGE_W
    out = {"margins": ink_margins(img, card, mm), "frame": axis_frame(img, card, mm)}
    if out["frame"]:
        l, r, t, b = out["frame"]
        w, h = r - l, b - t
        out["frame_size"] = (w, h)
        out["angles"] = {n: slope_angle(n, w, h, *decades) for n in (4, 3)}
    return out


def report(out):
    m = out["margins"]
    if m:
        print("card の余白 (mm): 上 %.1f / 下 %.1f / 左 %.1f / 右 %.1f" % (m["top"], m["bottom"], m["left"], m["right"]))
        print("  上下の差 %.1f mm → scope の y を %+.2f mm 動かすと揃う / 左右の差 %.1f mm → x を %+.2f mm"
              % (m["top"] - m["bottom"], (m["top"] - m["bottom"]) / 2, m["left"] - m["right"], (m["right"] - m["left"]) / 2))
    else:
        print("card の中に内容が見つからない")
    if out["frame"]:
        l, r, t, b = out["frame"]
        w, h = out["frame_size"]
        print("軸の枠 (mm、 紙の左上から): 左 %.1f 右 %.1f 上 %.1f 下 %.1f = 幅 %.1f × 高さ %.1f" % (l, r, t, b, w, h))
        for n, a in out["angles"].items():
            print("  a^-%d の線の傾き = %.1f° → rotate=-%d 前後" % (n, a, round(a)))
    else:
        print("軸の枠が見つからない (色 fgmute の長い縦線 2 本と横線 2 本を探した)")


def selftest():
    """合成画像で、 余白と枠と角を既知の値と照合する。"""
    mm = 10.0  # 1 mm = 10 px の合成紙
    W, H = int(PAGE_W * mm), int(PAGE_H * mm)
    img = np.full((H, W, 3), 250, dtype=int)
    card = (90, 289, 14, 118)
    # card の地
    l, r, t, b = int(90 * mm), int(289 * mm), int((PAGE_H - 118) * mm), int((PAGE_H - 14) * mm)
    img[t:b, l:r] = 255
    # 内容 = 枠 (fgmute) 100..270 mm × 上 110..下 180 mm (左上原点)、 枠の外に文字の代わりの黒い点
    fx0, fx1, fy0, fy1 = 100, 270, 110, 180
    img[int(fy0 * mm), int(fx0 * mm):int(fx1 * mm) + 1] = FGMUTE
    img[int(fy1 * mm), int(fx0 * mm):int(fx1 * mm) + 1] = FGMUTE
    img[int(fy0 * mm):int(fy1 * mm) + 1, int(fx0 * mm)] = FGMUTE
    img[int(fy0 * mm):int(fy1 * mm) + 1, int(fx1 * mm)] = FGMUTE
    img[int(100 * mm), int(95 * mm)] = 0     # 最も上・最も左の内容
    img[int(190 * mm), int(280 * mm)] = 0    # 最も下・最も右の内容
    ok = True
    m = ink_margins(img, card, mm)
    exp = {"top": 100 - (PAGE_H - 118), "bottom": (PAGE_H - 14) - 190, "left": 95 - 90, "right": 289 - 280}
    for k, v in exp.items():
        good = abs(m[k] - v) < 0.3
        ok &= good
        print("%s 余白 %s: %.2f (期待 %.2f)" % ("✓" if good else "✗", k, m[k], v))
    fr = axis_frame(img, card, mm)
    good = fr is not None and all(abs(a - e) < 0.3 for a, e in zip(fr, (fx0, fx1, fy0, fy1)))
    ok &= good
    print("%s 枠 %s (期待 %s)" % ("✓" if good else "✗", fr, (fx0, fx1, fy0, fy1)))
    a = slope_angle(4, 171.2, 73.2, 10, 40)
    good = abs(a - 23.15) < 0.05
    ok &= good
    print("%s 角 n=4, 171.2×73.2, 10×40 桁 = %.2f° (期待 23.15)" % ("✓" if good else "✗", a))
    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--png", default="cosmology-history.png")
    ap.add_argument("--card", nargs=4, type=float, default=[90, 289, 14, 118],
                    metavar=("X0", "X1", "Y0", "Y1"), help="card の範囲 (mm、 左下が原点 = tikz と同じ)")
    ap.add_argument("--decades", nargs=2, type=float, default=[10, 40], metavar=("X", "Y"),
                    help="x と y の軸の桁数 (本 entry = a は 1e-9..10、 密度は 1e-5..1e35)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    report(measure(a.png, tuple(a.card), tuple(a.decades)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
