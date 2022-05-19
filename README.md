# flatten
This is just another scrip to flatten json dictionaries in python3

## Docker
1. Building the image.
```
docker build -t flatten_img .
```
2. Running the bash into the image.
```
docker run -it flatten_img bash
```

## Running tests
Inside the docker image:
1. Performace the pytest cases by:
```
# pytest test_flatten.py 
```
2. Performace the timeit by:
```
# python test_time_flatten.py -d
```
