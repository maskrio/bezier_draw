import cv2

def extract_interpolation_points(image_path):
    # source : https://www.geeksforgeeks.org/python/find-and-draw-contours-using-opencv-python/
    #          https://opencv.org/blog/edge-detection-using-opencv/

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {image_path}")

    h, w = img.shape

    # Apply Gaussian Blur to reduce noise
    blur = cv2.GaussianBlur(img, (5, 5), 1.4)

    # Apply Canny Edge Detector
    edges = cv2.Canny(blur, threshold1=100, threshold2=200)

    # mencari contour, boundaries dari gambar
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # reshape to points
    polylines = []
    for c in contours:
        pts = c.reshape(-1, 2).astype(float)
        if pts.shape[0] < 4:
            continue
        polylines.append(pts)

    return polylines, h
