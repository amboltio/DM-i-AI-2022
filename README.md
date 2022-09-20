# DM i AI 2022
<h3>Welcome to the annual <a href="https://dmiai.dk/">DM i AI</a> event hosted by <a href="https://ambolt.io/">Ambolt ApS.</a></h3> <br>
In this repository, you will find all the information needed to participate in the event. Please read the entire information before proceeding to the use cases, and please make sure to read the full description of every use case. You will be granted points for every use case that you provide a submission for and a total score will be calculated based on the individual submissions. <br> <br>


<h2>Use cases</h2>
Below you can find the three use cases for the DM i AI 2022 event. <br>
Within each use case, you find a description together with a template that can be used to setup an API endpoint. <br> 
The API endpoint will be used for submission and is required. <a href="https://ambolt.io/download/">Emily</a> can help with setting up the API, but you should feel free to set them up on your own. The requirements for the API endpoints are specified in the respective use cases. <br> <br>
<a href="https://github.com/amboltio/DM-i-AI-2022/tree/main/sentiment-analysis">- Sentiment Analysis</a> <br>
<a href="https://github.com/amboltio/DM-i-AI-2022/tree/main/piglet-detection">- Piglet Detection</a> <br>
<a href="https://github.com/amboltio/DM-i-AI-2022/tree/main/robot-robbers">- Robot Robbers</a> <br> <br>

Clone this GitHub repository to download Emily templates for all three use cases.
```
git clone https://github.com/amboltio/DM-i-AI-2022.git
```
Inside the DM-i-AI-2022 folder, you will find the three use cases. To open a use case with Emily type `emily open <use-case>` e.g. `emily open robot-robbers` to open the last use case.

<h2>Emily CLI</h2>
The <a href="https://ambolt.io/emily-ai/">Emily CLI</a> is built and maintained by <a href="https://ambolt.io/">Ambolt</a> to help developers and teams implement and run production ready machine learning powered micro services fast and easy. <a href="https://emily.ambolt.io/docs/latest">Click here</a> for getting started with Emily. If you <a href="https://emily.ambolt.io/register">sign up</a> to Emily using your student email, you can get free access to the full Emily-CLI with Emily Academy. <br> <br>
Emily can assist you with developing the required API endpoints for the use cases. Together with every use case a predefined and documented template is provided to ensure correct API endpoints and DTOS for the specific use case. You can find the documentation of the entire framework <a href="https://emily.ambolt.io/docs/latest">here</a>. <br>
The use cases have been built on top of the <a href="https://fastapi.tiangolo.com/">FastAPI</a> framework, and can be used to specify endpoints in every use case.

<h2>Discord Channel</h2>
Come hang out and talk to other competitors of the event on our Discord channel. Discuss the use cases with each other or get in touch with any of the Ambolt staff, to solve issues or questions that may arise during the competition. <a href="https://discord.gg/QhTt4Me2AQ">Join here!</a> <br>

<h2>Getting started without emily</h2>
You are not required to use Emily for competing in this event, however, we strongly recommend using Emily if you are not an expert in developing APIs and microservices. If you do not choose to use Emily, you should check the individual template and find the requirements for the different API endpoints. These have to be exactly the same for the evaluation service to work. Inside the `dtos` folder you can find information on the request and response models, describing the input and output requirements for your API. 

<h2>Submission</h2>
When you are ready for submission, <a href="https://emily.ambolt.io/docs/latest/cli/emily/deploy">click here</a> for instructions on how to deploy. Then, head over to the <a href="https://cases.dmiai.dk/">Submission Form</a> and submit your model by providing the host address for your API and your UUID obtained during sign up. Make sure that you have tested and validated your connection to the API before you submit!<br><br>

**You can only submit once per use case.** We highly recommend that you validate your solution before submitting. You can do this on the submission form by using the `QUEUE VALIDATION ATTEMPT` button. You can validate as many times as you like, but you can only evaluate once per use case. When you queue validation, your score from the run will show up on the scoreboard, so you can see how you compare to the other teams.

When you validate your solution on the submission form, it will be evaluated on a validation set. When you submit your solution and get the final score for that use case, your solution will be evaluated on a **test set which is different from the validation set**. This means that the score you obtained when validating your solution may be different from the score you get when evaluating. Therefore, we encourage you not to overfit to the validation set!

<h3>Ranked score and total score </h3>
The scoreboard will display a score for each usecase and a "total score".
The individual score reflects the placement your best model has achieved relative to the other participants' models.

The total score is simply an average of your individual scores.<br>

This format also means that you can loose points / be overtaken by other teams during the week if they submit a model that is better than yours. 

<h3>Deadline for submission</h3>
The deadline for submission is Monday the 10th of October at 14:00.

<h3>Final evaluation</h3>

Upon completion of the contest, the top 3 highest-ranking teams will be asked to submit their training code and the trained models for validation no later than Tuesday the 11th of October at 14:00 (24 hours after the deadline). The final ranking is announced Friday the 14th of October.

<h2>How to get a server for deployment?</h2>
When you are doing the submission we are expecting you to host the server at which the REST API can be deployed. You can sign up to <a href="https://azure.microsoft.com/da-dk/free/students/">Azure for Students</a>, where you will get free credits that you can use to create a virtual machine. We expect you all to be able to do this, since the competition is only for students. Alternatively, you can also deploy your submission locally (This requires a public IP). <br> 
The following contains the necessary links for creating a virtual machine: <br> <br>

* <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal">Creating a linux virtual machine</a> <br>
* <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop">Install and configure xrdp to use Remote Desktop</a> <br>
* <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/windows/nsg-quickstart-portal#create-an-inbound-security-rule">Create an inbound security Rule</a> (This ensures that the API endpoints can be accessed when submitting)<br>


<h3>What if I have already used my Azure student credits?</h3>
If you have already used your credicts, reach out to us on either <a href="https://discord.gg/QhTt4Me2AQ">discord</a> or on <a href="mailto:DMiAI@ambolt.io">DMiAI@ambolt.io</a> and we will help you out. However, we cannot provide you with GPU servers, so remember to design you solutions such that they run within the time constraints specified for the independent use cases.<br>

**We do not provide servers for training,** hence you are expected to train your models and solutions using your own hardware, Google Colab etc. 
<br>

