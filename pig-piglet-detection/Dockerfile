FROM ambolt/emily:2.0.0-base

WORKDIR /workspace

# Static project file that allows us to COPY, RUN and cache setup scripts conditionally
ARG EMILY_IDREQ=.emily/.pid

# Build arguments
# Provided by Emily when opening projects in PyCharm
ARG CONFIGURE_PYCHARM_SSH_SCRIPT

# Run and cache the SSH configuration required for Pycharm if the script is present
COPY $EMILY_IDREQ $CONFIGURE_PYCHARM_SSH_SCRIPT ./
RUN if [ ! -z "$CONFIGURE_PYCHARM_SSH_SCRIPT" ]; then \
  SCRIPT=$(basename "$CONFIGURE_PYCHARM_SSH_SCRIPT"); \
  PID=$(basename "$EMILY_IDREQ"); \
  sudo /bin/bash "$SCRIPT"; \
  sudo rm $SCRIPT; \
  sudo rm $PID; \
  fi;

# Add your changes here e.g. apt package installations
# RUN apt-get --allow-releaseinfo-change -y update && apt-get install -y #     package1 #     package2 ... 

# Create and set the project user
RUN adduser --disabled-password --gecos "" --home /home/pig-piglet-dete --force-badname pig-piglet-dete
RUN adduser pig-piglet-dete sudo
RUN chown pig-piglet-dete /workspace
RUN chown pig-piglet-dete /home/pig-piglet-dete
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER pig-piglet-dete

ENV PATH="/home/pig-piglet-dete/.local/bin:$PATH"

RUN sudo apt-get --allow-releaseinfo-change -y update && sudo apt-get install -y ffmpeg libsm6 libxext6

# Install Pip requirements
COPY requirements.txt requirements.txt
RUN pip install --disable-pip-version-check -r requirements.txt





# Copy all directory contents (sans .dockerignore) into container
COPY . .

CMD ["/bin/bash", "run.sh"]
