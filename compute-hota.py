import os
import numpy as np
import motmetrics as mm


def compute_motchallenge(dir_name):
    # `gt.txt` and `test.txt` should be prepared in MOT15 format
    df_gt = mm.io.loadtxt(os.path.join(dir_name, "gt.txt"))
    df_test = mm.io.loadtxt(os.path.join(dir_name, "test.txt"))
    # Require different thresholds for matching
    th_list = np.arange(0.05, 0.99, 0.05)
    res_list = mm.utils.compare_to_groundtruth_reweighting(df_gt, df_test, "iou", distth=th_list)
    return res_list

# `data_dir` is the directory containing the gt.txt and test.txt files
acc = compute_motchallenge("data_dir")
mh = mm.metrics.create()

summary = mh.compute_many(
    acc,
    metrics=[
        "deta_alpha",
        "assa_alpha",
        "hota_alpha",
    ],
    generate_overall=True,  # `Overall` is the average we need only
)
strsummary = mm.io.render_summary(
    summary.iloc[[-1], :],  # Use list to preserve `DataFrame` type
    formatters=mh.formatters,
    namemap={"hota_alpha": "HOTA", "assa_alpha": "ASSA", "deta_alpha": "DETA"},
)
print(strsummary)
"""
# data_dir=motmetrics/data/TUD-Campus
         DETA  ASSA  HOTA
OVERALL 41.8% 36.9% 39.1%
# data_dir=motmetrics/data/TUD-Stadtmitte
         DETA  ASSA  HOTA
OVERALL 39.2% 40.9% 39.8%
"""