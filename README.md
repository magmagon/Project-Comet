# Comet - V1 Alpha 1.2
Phase 1 of Project Comet - Importing pictures, processing and exporting data to CSV

Requires the following modules
CSV (fairly self-explanatory, I used the default python included CSV package)
OS (for interaction with folders and file management)
numpy (for pixel calculations and array manipulations)
opencv (for image processing)

Timeline:
1. Put the image to be processed within the ingest folder and run ALPHA.py (or blobby.py)
2. The processed image will be put in the temporary folder (which will be overwritten), the numerical results will be written to the output folder
3. Analyze the image in sections to determine density of edges in a given portion and assign color coding
4. Overlay color coding to highlight busier sections of the image
5. Adapt the program to process video and export results as PDF
