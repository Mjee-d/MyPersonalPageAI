# Coffee Image Classifier

This project uses a Google Teachable Machine model trained to recognize two distinct classes. The model is deployed and verified using a Python script inside a Google Colab notebook environment.

## Repository Structure
* `model/`: Contains the pre-trained Keras model (`.h5`) and class labels text file.
* `test_images/`: Sample image used to verify the model accuracy.
* `teachable_machine_test.ipynb`: Jupyter notebook containing the inference pipeline code.

## How to Run
1. Open Google Colab and upload the `teachable_machine_test.ipynb` notebook.
2. Upload the files from the `model/` directory into your Colab runtime.
3. Upload a test image to the runtime environment.
4. Execute the cells to see the classification output and confidence scores.
