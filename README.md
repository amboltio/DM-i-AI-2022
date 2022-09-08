# DM i AI 2022
Welcome to the event <a href="https://dmiai.dk/">DM i AI</a> hosted by <a href="https://ambolt.io/">Ambolt ApS</a>.
In this GitHub repository, you will find all the necessary information needed for the event. Please read the entire information before proceeding to the use case, and please make sure to read the full description of all the use cases. You will be granted points for each use case based on how well you score in the respective use case.


<h2>Use cases</h2>
Below you can find the four different use cases for the  DM i AI event. <br>
Within each use case, you find a description together with a template that can be used to setup an API endpoint. <br> 
The API endpoint will be used for submission and is required. <a href="https://github.com/amboltio/emily-cli">Emily</a> can help with setting up the API, but you should feel free to set them up on your own. The requirements for the API endpoints are specified in the respective use cases. <br> <br>
<a href="https://github.com/amboltio/DM-i-AI-2022/tree/main/sentiment-analysis">- Sentiment Analysis</a> <br>
<a href="https://github.com/amboltio/DM-i-AI-2022/tree/main/piglet-detection">- Piglet Detection</a> <br>
<a href="https://github.com/amboltio/DM-i-AI-2022/tree/main/robot-robbers">- Robot Robbers</a> <br> <br>

Clone this GitHub repository to download Emily templates for all four use cases.
```
git clone https://github.com/amboltio/DM-i-AI-2022.git
```
Inside the DM-i-AI folder, you will find the four different use cases. To open a use case with Emily type `emily open <use-case>` e.g. `emily open wheres-waldo` to open the first use case.

<h2>Emily CLI</h2>
The <a href="https://ambolt.io/emily-ai/">Emily CLI</a> is built and maintained by <a href="https://ambolt.io/">Ambolt</a> to help developers and teams implement and run production ready machine learning powered micro services fast and easy. <br>
<a href="https://github.com/amboltio/emily-cli/wiki">Click here</a> for getting started with Emily. Emily can assist you with developing the required API endpoints for the use cases. Together with every use case a predefined and documented template is provided to ensure correct API endpoints for the specific use case. You can find the documentation of the entire framework <a href="https://amboltio.github.io/emily-cli-documentation-client/">here</a>. <br>
The use cases have been built on top of the <a href="https://fastapi.tiangolo.com/">FastAPI</a> framework, and should be used to specify endpoints in every use case.

<h2>Discord Channel</h2>
Come hang out and talk to other competitors of the event on our Discord channel. Discuss the use cases with each other or get in touch with any of the Ambolt staff, to solve eventual issues or questions that may arise during the competition. <a href="https://discord.gg/QhTt4Me2AQ">Join here!</a> <br>

<h2>Getting started without emily</h2>
You are not required to use Emily for competing in this event, however, we strongly recommend using Emily if you are not an expert in developing APIs and microservices. If you do not choose to use Emily, you should check the individual template and find the requirements for the different API endpoints. These have to be exactly the same for the evaluation service to work. Inside the `dtos` folder you can find information on the request and response models, describing the input and output requirements for your API. 

<h2>Submission</h2>
When you are ready for submission, <a href="https://amboltio.github.io/emily-intro/deploy/">click here</a> for instructions on how to deploy. Then, head over to the <a href="https://amboltio.github.io/DM-i-AI-client/#/submit">Submission Form</a> and submit your model by providing the host address for your API and your UUID obtained during sign up. Make sure that you have tested your connection to the API before you submit!<br><br>

**You can only submit once per use case.** We highly recommend that you test your solution before submitting. You can do this on the submission form by using the `Test submission` button. You can test as many times as you like, but you can only submit once per use case. When you test, your score from the test will show up on the leaderboard, so you can see how you compare to the other teams.

When you test your solution on the submission form, it will be evaluated on a test set. When you submit your solution and get the final score for that use case, your solution will be evaluated on a **validation test set which is different from the test set**. This means that the score you obtained when testing your solution may be different from the score you get when submitting. Therefore, we encourage you not to overfit to the test set!

<h3>Ranked score and total score </h3>
The scoreboard will display a "ranked score" for each usecase and a "total score".
The ranked score reflects the placement your best model has achieved relative to the other participants' models. The current best model gets the first place and 100 points. If two models perform equally well, they will share a ranked score.<br><br>

The total score is simply a summation of your ranked scores.<br>

This format also means that you can loose points / be overtaken by other teams during the week if they submit a model that is better than yours. 

<h3>Deadline for submission</h3>
The deadline for submission is Sunday November 7th EOD (23:59).

<h3>Final evaluation</h3>

Upon completion of the contest, the top 5 highest-ranking teams will be asked to submit their training code and the trained models for validation. The final ranking is announced on 30/11. 

<h2>How to get a server for deployment?</h2>
When you are doing the submission we are expecting you to host the server at which the REST API can be deployed. You can sign up to <a href="https://azure.microsoft.com/da-dk/free/students/">Azure for Students</a>, where you will get free credits that you can use to create a virtual machine. We expect you all to be able to do this, since the competition is only for students. Alternatively, you can also deploy your submission locally (This requires a public IP). <br> 
The following contain the necessary links for creating a virtual machine: <br> <br>

* <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal">Creating a linux virtual machine</a> <br>
* <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop">Install and configure xrdp to use Remote Desktop</a> <br>
* <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/windows/nsg-quickstart-portal#create-an-inbound-security-rule">Create an inbound security Rule</a> (This ensures that the API endpoints can be accessed when submitting)<br>


<h3>What if I have already used my Azure student credits?</h3>
If you have already used your credicts, reach out to us on either <a href="https://discord.gg/R9cvaZyzdu">discord</a> or on <a href="mailto:DMiAI@ambolt.io">DMiAI@ambolt.io</a> and we will help you out.<br>
