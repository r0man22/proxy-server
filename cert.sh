#!/bin/bash

openssl genrsa -out mitm.key 2048
openssl req -new -x509 -key mitm.key -out mitm.crt -days 365 -subj "/CN=Proxy"
