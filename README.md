# Pronunciation-Generation-using-GANs

Please refer to the final paper for more details on the project.

To replicate the training procedure, first export all visible devices enabled by CUDA to -1.
Then change directory to the wavegan folder and run

```python3 train_wavegan.py train ./train --data_dir ./data/Apple```

For observing previews at defined checkpoints in the /train directory created, run

```python3 train_wavegan.py preview ./train --data_dir ./data/Apple```

This will take the latest checkpoint available and generate the audio for that.
