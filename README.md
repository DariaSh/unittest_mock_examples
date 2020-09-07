# unittest_mock_examples
This repo contains few simple examples of code and correpondong test illustrating simple case of use of unittest.mock package.
Here you can find module bucket.py and my_module.py as well as tiny utils package with bucket_reader.py module inside.

Modules test_bucket.py and test_my_module.py contain tests for modules bucket and my_module correspondingly.

# requirements.txt
For illustration of code using Google Cloud Bucket there is a need to install corresponding library. 
Please run
$ pip3 install -r requirements.txt 

for install all libraries required.

# run test examples
Not all examples,mentioned in the blog article are available in the repo, but few the most essential ones.
To run tests you can simply type in commeand line 
$ python3 -m unittest test_*.py

