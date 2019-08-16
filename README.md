# Python CSV reader

Build your docker image by running `docker build --build-arg csvfile=users.csv -t pythonmachine .`.

> _users.csv_ is the csv file I used in this example. You can (and should) adapt it to use your own csv file. You will get something like `docker build --build-arg csvfile=MY_FILE.csv -t pythonmachine .`.

Run the image using the command `docker run pythonmachine`.