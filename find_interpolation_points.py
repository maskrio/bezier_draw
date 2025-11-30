import numpy as np
from extract_interpolation_points import extract_interpolation_points
from polyline_to_bezier_segments import polyline_to_bezier_segments
from distribute_segments_by_length import distribute_segments_by_length
from write_to_pdf import write_to_pdf

N = 1000


def flip_y(points, img_height):
    pts = points.copy()
    pts[:, 1] = img_height - 1 - pts[:, 1]
    return pts


if __name__ == "__main__":
    image_path = "image.png"
    polylines, h = extract_interpolation_points(image_path=image_path)

    all_segments = []

    seg_counts = distribute_segments_by_length(polylines, N)

    for i, pts in enumerate(polylines):
        pts_flipped = flip_y(pts, h)
        segments = polyline_to_bezier_segments(pts_flipped, seg_counts[i])
        all_segments.append(segments)

    stacked = np.vstack(all_segments)
    np.savetxt("bezier_segments.txt", stacked)
    print("bezier_segments.txt created")

    write_to_pdf(stacked, "bezier_segments.pdf")
    print("bezier_segments.pdf created")
