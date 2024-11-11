
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import requests

text_pairs = [
    ("Hello, how are you?", "Hello, how are you doing?"),
    ("Hello, how are you?", "Hello, who r u?"),
    ]
response = requests.post("http://127.0.0.1:8000/predict", json={"input": text_pairs})
print(f"Status: {response.status_code}\nResponse:\n {response.json()}")
