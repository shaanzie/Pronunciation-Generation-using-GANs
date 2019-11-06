# Pronunciation-Generation-using-GANs

This is a system to detect mispronounced words in natural speech and generate the correct pronounciations in the user's voice.

To replicate the training procedure, first export all visible devices enabled by CUDA to -1.
Then change directory to the wavegan folder and run

```python3 train_wavegan.py train ./train --data_dir ./data/Apple```

For observing previews at defined checkpoints in the /train directory created, run

```python3 train_wavegan.py preview ./train --data_dir ./data/Apple```

This will take the latest checkpoint available and generate the audio for that.

This is the final report on the project. You may find this saved as Final_Paper___GANs.pdf on the same repository.

<object data="https://github.com/shaanzie/Pronunciation-Generation-using-GANs/blob/master/Final_Paper___GANs.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/shaanzie/Pronunciation-Generation-using-GANs/blob/master/Final_Paper___GANs.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/shaanzie/Pronunciation-Generation-using-GANs/blob/master/Final_Paper___GANs.pdf">View PDF</a>.</p>
    </embed>
</object>
