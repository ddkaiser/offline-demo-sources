# offline-demo-sources
Sample Sets : REST service demo handlers in various formats, for offline demos of web services

Tested with Python3
Need to install (pypi or pip) flask and jsonify

Tutorial on RESTful services with Flask API: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask


Commerce Demo::
/commerce/api/v1.0/orders : GET latest (random/sampled) order transaction, or none
/commerce/api/v1.0/customer/{id} : GET customer record by customerID
/commerce/api/v1.0/inventory/{id} : GET product inventory by productID


