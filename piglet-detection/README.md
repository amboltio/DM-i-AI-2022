# Pig and Piglet Detection
In this use case, your task is to detect pigs and piglets and separate them from each other. 

You will be receiving XX images of animals, where you need to predict the bounding box locations of the pigs and piglets. The predictions should contain the top left and bottom right normalized coordinates of the predicted bounding box, as well as an object class and a confidence score. Pigs have object class 0 and piglets have object class 1. The confidence score is a value in the range [0-1] referring to the certainty of the detection. See the image below for an illustation of the concept.

<p align="center">
  <img src="../images/example2.png" width=400>
</p>

All the images have a fixed size of 640x640 px. A single image can contain up to 15 objects. **You have 10 seconds to return your predictions for each image.**
You will only be receiving images of what we deem a *visually clear piglet*. Thus, if it has been difficult to assess wheter an image contains a pig or a piglet, the image is removed. Such an example is given below.
<p align="center">
  <img src="../images/removed_sample2.jpg" width=350>
</p>

## Evaluation
During the week of the competition, you will be able to validate your solution against a validation set. The best score your model achieves on the validation set will be displayed on the scoreboard.

Your model will be evaluated using the mean Average Precission at a 0.5 IoU threshold (mAP@0.5). The score ranges from [0-1], with 1 being the highest score.
The validation request timeouts after 10 seconds, so you need to make sure that your solution can handle an images in under 10 seconds.

Notice that you can only submit once! We encourage you to validate your code and API before you submit your final model. You can find the documentation of your API where you can try out your model and verify the prediction. <br>
The documentation is by default found at `0.0.0.0:4242/docs`, and then find the prediction endpoint for the use case.


After evaluation, your final score will be provided. This score can be seen on the <a href="https://cases.dmiai.dk/">scoreboard</a> shortly after.


## Getting started using Emily
Once the repository is cloned, navigate to the folder using a terminal and type:
```
emily open piglet-detection
```
You will be prompted for selecting an application. For this use case, it might be beneficial to use a Computer Vision image, where you can select your prefered deep learning framework. Afterwards, you will be asked to mount a data folder for your project. This folder should include your data, for the first run it can empty and you can add data later. Then select an editor of your choice to open the Emily template for the use case. A Docker container with a Python environment will be opened. Some content needs to be downloaded the first time a project is opened, this might take a bit of time.

To take full advantage of Emily and the template, your code for prediction should go in api.py:
```python
@app.post('/api/predict', response_model=PigPredictResponseDto)
def predict(request: PigPredictRequestDto) -> PigPredictResponseDto:
    ############ Modify this ##########
    predictions = []
    for img in request.img:
        decoded_img = decode(img)
        predictions.append(predict(decoded_img))

    return PigPredictResponseDto(boxes=predictions)
```
You can add new packages to the Python environment by adding the names of the packages to requirements.txt and restarting the project, or by using pip install on a terminal within the container which will result in the package being installed temporarily i.e. it is not installed if the project is restarted. <a href="https://emily.ambolt.io/docs/latest">Click here</a> to visit the Emily documentation.

## Testing the connection to the API
See <a href="https://amboltio.github.io/emily-intro/deploy/test/">this guide</a> for details on how to test your setup before final submission.

## Submission
When you are ready for submission, <a href="https://emily.ambolt.io/docs/latest/cli/emily/deploy">click here</a> for instructions on how to deploy. Then, head over to the <a href="https://cases.dmiai.dk/">Submission Form</a> and submit your model by providing the host address for your API and your UUID obtained during sign up. Make sure that you have tested your connection to the API before you submit!<br>
