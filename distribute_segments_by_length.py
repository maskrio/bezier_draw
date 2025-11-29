import numpy as np


def distribute_segments_by_length(polylines, n_total_segments):
    m = len(polylines)
    lengths = np.array([len(p) for p in polylines], dtype=float)

    seg_counts = np.floor(n_total_segments * lengths / lengths.sum()).astype(int)
    seg_counts[seg_counts == 0] = 1

    current_total = seg_counts.sum()
    diff = n_total_segments - current_total

    if diff > 0:
        order = np.argsort(-seg_counts)
        for i in range(diff):
            seg_counts[order[i % m]] += 1
    elif diff < 0:
        order = np.argsort(-seg_counts)
        for i in range(-diff):
            if seg_counts[order[i % m]] > 1:
                seg_counts[order[i % m]] -= 1

    return seg_counts
