import numpy as np

def compute_pdf_transform(segments, page_w=500, page_h=500, margin=20):
    # segments: (N, 8) array [x1,y1,x2,y2,x3,y3,x4,y4]
    xs = segments[:, 0::2]  # all x columns
    ys = segments[:, 1::2]  # all y columns

    min_x, max_x = xs.min(), xs.max()
    min_y, max_y = ys.min(), ys.max()

    width = max_x - min_x
    height = max_y - min_y

    # keep aspect ratio
    s = min((page_w - 2 * margin) / width,
            (page_h - 2 * margin) / height)

    sx = sy = s
    tx = margin - sx * min_x
    ty = margin - sy * min_y

    return sx, sy, tx, ty


def to_pdf(x, y, sx, sy, tx, ty):
    X = sx * x + tx
    Y = sy * y + ty
    return X, Y


def segments_to_pdf_content(segments, page_w=500, page_h=500, margin=20):
    sx, sy, tx, ty = compute_pdf_transform(segments, page_w, page_h, margin)

    lines = []
    lines.append("0 0 0 RG")  # stroke color black
    lines.append("1 w")       # line width

    # move to first point
    x1, y1, x2, y2, x3, y3, x4, y4 = segments[0]
    X1, Y1 = to_pdf(x1, y1, sx, sy, tx, ty)
    lines.append(f"{X1:.2f} {Y1:.2f} m")

    # cubic bezier segments
    for (x1, y1, x2, y2, x3, y3, x4, y4) in segments:
        X2, Y2 = to_pdf(x2, y2, sx, sy, tx, ty)
        X3, Y3 = to_pdf(x3, y3, sx, sy, tx, ty)
        X4, Y4 = to_pdf(x4, y4, sx, sy, tx, ty)
        lines.append(f"{X2:.2f} {Y2:.2f} {X3:.2f} {Y3:.2f} {X4:.2f} {Y4:.2f} c")

    lines.append("S")  # stroke

    content = "\n".join(lines) + "\n"
    return content
