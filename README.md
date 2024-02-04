How to run the task:
- Build the task Docker image: `docker build -t task-image .`
- Run the task Docker container: `docker run task-image`

How to run tests:
- Build the test Docker image: `docker build -t test-image -f Dockerfile.test .`
- Run the test Docker container: `docker run test-image`

Ensure your CSV file 'orders.csv' is in the same directory as your script.

Ensure you have 'pytest' installed for running tests.
Install it using: `pip install pytest`
