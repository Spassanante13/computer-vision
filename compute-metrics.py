import motmetrics as mm
from pathlib import Path
import pandas as pd


dataset_path = Path("test")
pred_path = Path("predictions")

accs = []
names = []

for seq_dir in sorted(dataset_path.iterdir()):
    if not seq_dir.is_dir():
        continue

    seq_name = seq_dir.name
    gt_file = seq_dir / "gt" / "gt.txt"
    pred_file = pred_path / f"{seq_name}.txt"

    if not pred_file.exists() or pred_file.stat().st_size == 0:
        print(f"Empty file")
        continue
    
    current_acc = mm.MOTAccumulator(auto_id=True)
    
    gt = pd.read_csv(gt_file, header=None)
    pred = pd.read_csv(pred_file, header=None)

    for frame_id in sorted(gt[0].unique()):
        gt_frame = gt[gt[0] == frame_id]
        pred_frame = pred[pred[0] == frame_id]

        gt_ids = gt_frame[1].values
        pred_ids = pred_frame[1].values

        dist_matrix = mm.distances.iou_matrix(
            gt_frame[[2, 3, 4, 5]].values, 
            pred_frame[[2, 3, 4, 5]].values, 
            max_iou=0.5
        )

        current_acc.update(gt_ids, pred_ids, dist_matrix)
    
    accs.append(current_acc)
    names.append(seq_name)



custom_metrics = [
    'recall', 'precision', 'num_false_positives', 'num_misses', # Detection pura
    'mota', 'motp', 'idf1', 'num_switches',                     # Tracking
     'hota_alpha'
]
mh = mm.metrics.create()

summary = mh.compute_many(
    accs, 
    names=names, 
    metrics=custom_metrics, 
    generate_overall=True
)

print("\n" + "="*80)
print(mm.io.render_summary(summary, formatters=mh.formatters, namemap=mm.io.motchallenge_metric_names))
