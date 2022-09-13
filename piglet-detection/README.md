# Emily API

To start your API open a terminal inside the container and type:
```
python api.py
```
By default, your API will be accessible at http://localhost:4242.
To test out your API open `http://localhost:4242` in a browser.

From this window you can access health check by pressing <b>Run curl http://0.0.0.0:4242/api to test your API endpoint</b>.

# 📄 Automatic Documentation

You can access documentation about your endpoints at http://localhost:4242/docs or locate it in the browser tab.
Here you can try out your endpoints and observe information about inputs and outputs of your API.

Documentation will be generated automatically based on how you create your API endpoints.

# 🏃 Getting started with tutorials

You can easily download tutorials, you can try out to get you started with developing APIs in Emily,
the tutorials can be accessed from https://github.com/amboltio/emily-cli/wiki/Tutorials.

# 💾 Importing external data? 

Do you need to import data, that you would not like to deploy and include in the container, you can easily mount data
by running `emily mount <project name>` in your desired terminal. You'll be prompted to specify a directory you wish to mount.
For instance, training data often takes up lots of space and is not desired to keep in the container during deployment.
Note, that you must restart the container to apply these changes. `emily stop <project name>` followed by `emily open <project name>`.

💡 You can unmount the data again by calling `emily unmount <project name>`.

# 🚀 Deployment of your API

When you are done developing your API and you feel the API is ready for deployment.
Using Emily it is very simple to deploy your API to production, head back to your desired terminal,
and type `emily deploy server <project name>` to deploy to a server,
or `emily deploy kubernetes <project name>` to deploy your microservice to a Kubernetes cluster.

# ❓ Need more help?
You can find the version-controlled documentation of Emily at https://emily.ambolt.io, from this documentation
you can find detailed information about every command in Emily and examples of how to use it.