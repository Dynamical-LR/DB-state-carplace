FROM python:3.10-bullseye
WORKDIR /project/dir/
LABEL author=Dynamical_LR

# Copying source files
COPY ./rest ./rest
COPY ./models ./models
COPY ./proj_requirements ./proj_requirements
COPY ./deployment ./deployment
COPY ./model_files ./model_files
COPY ./__init__.py ./

# Creating logging directory folder 
RUN mkdir logs

# Installing dependencies
RUN pip install --upgrade pip
RUN pip install -r proj_requirements/prod_requirements.txt

ENTRYPOINT ["sh", "deployment/entrypoint.sh"]