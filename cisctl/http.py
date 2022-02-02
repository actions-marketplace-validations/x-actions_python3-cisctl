# Copyright 2020 xiexianbin.cn
# All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#        http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

"""python http utils."""

from urllib import parse
from urllib import request
from urllib import error as urllib_error


def get(url):
    try:
        return request.urlopen(url=url).read().decode('utf-8')
    except urllib_error.HTTPError:
        raise


def post(url, data, headers=None):
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    try:
        post_data = parse.urlencode(data).encode('utf8')
        req = request.Request(url, post_data)
        return request.urlopen(req, headers).read().decode('utf-8')
    except urllib_error.HTTPError:
        raise


def delete(url, headers=None):
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    try:
        req = request.Request(url=url, method="DELETE")
        return request.urlopen(req, headers).read().decode('utf-8')
    except urllib_error.HTTPError:
        raise