# Players' Ball Possession Estimation During Football Matches

This project implements a computer vision system for the automated estimation of ball possession at both individual and team levels. The system analyzes broadcast soccer footage to extract objective and scalable performance metrics.

## Table of Contents
- [Project Objectives](#project-objectives)
- [System Architecture](#system-architecture)
- [Technologies and Models](#technologies-and-models)
- [Methodology and Refinement](#methodology-and-refinement)
- [Experimental Results](#experimental-results)
- [Authors](#authors)

## Project Objectives
Automated ball possession analysis aims to overcome the limitations of manual annotation, which is time-consuming, subjective, and difficult to scale. The main technical challenges addressed include:
* Tracking small objects (the ball) moving at high speeds.
* Managing motion blur and standard broadcast resolution (~640px).
* Handling frequent occlusions between players.
* Managing similar visual appearances among teammates.

## System Architecture
The system is structured as a sequential pipeline:

1.  **Object Detection**: Localization of the ball, players, goalkeepers, and referees.
2.  **Multi-Object Tracking (MOT)**: Temporal association of detections to maintain identity continuity.
3.  **Re-Identification (ReID)**: Extraction of visual descriptors to recover identities after long occlusions or players leaving the field of view.
4.  **Data Refinement**: Post-processing via data interpolation and identification conflict management.
5.  **Possession Logic**: Calculation of possession times based on the spatial intersection (overlap) between player and ball bounding boxes.

## Technologies and Models
* **Detection**: YOLO11 (Ultralytics), fine-tuned on the SoccerNet dataset.
* **Tracking**: BoT-SORT, integrating motion prediction and appearance analysis.
* **ReID**: OSNet (Omni-Scale Network) for robust embedding extraction.
* **Dataset**: SoccerNet-Tracking 2022, based on 12 matches from the Swiss Super League.

## Methodology and Refinement
To improve system robustness, several technical components were integrated:
* **Hungarian Algorithm**: Used to solve the optimal assignment problem between frames.
* **Swap Guard**: A safety mechanism based on embedding confidence thresholds to prevent accidental ID switches between nearby players.
* **Linear Interpolation**: Applied to estimate the ball's position during frames where the detector fails, ensuring statistical continuity.

## Experimental Results
The system was evaluated using standard metrics for multi-object tracking. Performance on human subjects (players and referees) shows a Recall between 97% and 98%.

| Metric | Result |
| :--- | :--- |
| Precision | 88.1% |
| Recall | 81.3% |
| MOTA | 63.0% |
| HOTA | 37.7% |

## Authors
Project developed for the Computer Vision course, A.Y. 2025/2026, Sapienza University of Rome.

* Davide Perniconi (1889270)
* Stefano Passanante (2158181)
* Robert Cristian Iacobus (1834884)