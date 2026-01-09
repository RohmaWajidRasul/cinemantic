# Installation pre-requirements

To be able to run the system, you need to install the dependencies from our requirements.txt files. 

There are three in total: one for the model, one for the api-server and one for the frontend.

They can all be installed using the following command:

```
pip install -r requirements.txt
```

## Setting up the .env file
Another requirement to run the system is to have an .env file.

To do so, you can follow the example give in "env.example" file or use the following template:

```
POSTGRES_DB=cinemantic
POSTGRES_USER=postgres
POSTGRES_PASSWORD=cinemantic
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

AI_SERVICE_URL="http://localhost:xxxx"
API_SERVICE_URL="http://localhost:xxxx"

OMDB_API_KEY="OMDB_KEY"
OMDB_API_URL="https://www.omdbapi.com/"

MODEL_UPDATE_SECRET=secret
```

# Running the system

Command to run the API-server:
```
python manage.py runserver 8000
```

Command to run the frontend:
```
python manage.py runserver 8001
```

Command to run the AI-model:
```
uvicorn main:app --host localhost  --port 8002
```


# Individual contributions table

| Week 1/Task                  | Responsible | Delivered | Integrated |
|------------------------------|-------------|-----------|------------|
| Form the group               | All members | Yes       | Yes        |
| Brainstorm the project ideas | All members | Yes       | Yes        |
| Go to the lectures           | All members | Yes       | Yes        |


| Week 2/Task                            | Responsible | Delivered | Integrated |
|----------------------------------------|-------------|-----------|------------|
| Prepare the slides for the pitch ideas | All members | Yes       | Yes        |
| Go to the lectures                    | All members | Yes       | Yes        |
| Research on sentence transformers     | All members | Yes       | Yes        |


| Week 3/Task                                           | Responsible          | Delivered | Integrated |
|-------------------------------------------------------|----------------------|-----------|------------|
| Write the documentation (A1 - report)                 | All members          | Yes       | Yes        |
| Create toy model                                      | Bimnet and Rohma     | Yes       | Yes        |
| Research on data cleaning, labelling and validation   | Filipe and Júlia     | Yes       | Yes        |


| Week 4/Task                       | Responsible        | Delivered | Integrated |
|-----------------------------------|--------------------|-----------|------------|
| Implement API server              | Rohma              | Yes       | Yes        |
| Add poster_url to initial dataset | Rohma              | Yes       | Yes        |
| Create fine-tuned model           | Bimnet and Filipe  | Yes       | Yes        |
| Create UI prototype               | Júlia              | Yes       | Yes        |

| Week 5/Task                          | Responsible        | Delivered | Integrated |
|--------------------------------------|--------------------|-----------|------------|
| Implement validation                 | Filipe and Júlia   | Yes       | Yes        |
| Data labelling                       | Filipe             | Yes       | Yes        |
| Continue implementing API server     | Rohma              | Yes       | Yes        |
| Import into postgres database        | Rohma              | Yes       | Yes        |
| Implement frontend                   | Júlia              | Yes       | Yes        |
| Work on fine-tuned model             | Bimnet and Filipe  | Yes       | Yes        |

| Week 6/Task                           | Responsible        | Delivered | Integrated |
|---------------------------------------|--------------------|-----------|------------|
| Implement frontend                    | Júlia              | Yes       | Yes        |
| Implement views on frontend           | Júlia and Rohma    | Yes       | Yes        |
| Implement Cookies                     | Rohma              | Yes       | Yes        |
| Model Management Server               | Rohma              | Yes       | Yes        |
| Model Service                         | Bimnet and Filipe  | Yes       | Yes        |
| Refactor Model Service                | Rohma              | Yes       | Yes        |
| Terraform and Kubernetes              | Bimnet             | Yes       | Yes        |
| Set up presentation slides template   | Júlia              | Yes       | Yes        |
| Prepare presentation                  | All members        | Yes       | Yes        |


| Post Fair/Task                | Responsible  | Delivered | Integrated |
|-------------------------------|--------------|-----------|------------|
| Refactor frontend             | All members  | Yes       | Yes        |
| Refactor backend              | Rohma        | Yes       | Yes        |
| Refactor deployment and CI/CD | Bimnet       | Yes       | Yes        |
| Model evaluation              | Filipe       | Yes       | Yes        |
| Unit tests                    | Filipe       | Yes       | Yes        |
| Update the report             | All members  | Yes       | Yes        |

## Contributing

| Name                 | username (GitLab) |
| -------------------- | ----------------- |
| Bimnet Tesfamariam   | @bimnet           |
| Filipe Rosa          | @filipero         |
| Júlia Bonato         | @bonato           |
| Rohma Wajid          | @rohma            |