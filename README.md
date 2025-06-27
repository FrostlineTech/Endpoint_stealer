# Endpoint Stealer

> **DISCLAIMER**  
> This repository is intended *exclusively* for authorised security testing and
> educational research. Running this code against systems without the explicit,
> written consent of the owner is illegal and unethical. The authors and
> distributors of this software accept **no** responsibility for any misuse or
> damage caused.

## About

`Endpoint_Stealer.py` is a concise proof-of-concept that demonstrates how
attackers can exploit a misconfigured Cross-Origin Resource Sharing (CORS)
policy. It forges an `Origin` header in a single HTTP `POST` request and
prints:

* HTTP status code
* The value of the `Access-Control-Allow-Origin` response header
* A 500-character snippet of the response body

The script has been fully refactored and annotated, passing **flake8** with
zero linting errors.

## Requirements

This tool is designed with **Kali Linux** in mind and has been tested on the
latest rolling release. It should still run fine on any modern Linux distro (or
macOS/Windows) provided the following prerequisites are met:

* Python ≥ 3.8
* The packages listed in [`requirements.txt`](requirements.txt)

## Installation

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python Endpoint_Stealer.py \
    --url https://example.com/api/login/ \
    --origin https://evil-site.com \
    --username alice \
    --password secret
```

Arguments:

| Flag | Description | Required |
|------|-------------|----------|
| `--url` | Target endpoint URL. | Yes |
| `--origin` | `Origin` header value to send. | Yes |
| `--username` | *Optional* username for JSON body. | No |
| `--password` | *Optional* password for JSON body. | No |

## Contributing

Pull requests that improve documentation or extend functionality in a *legal*
and *ethical* manner are welcome. All contributions must adhere to the
[Code of Conduct](CODE_OF_CONDUCT.md) and abide by applicable laws and
regulations.

## License

Distributed under the MIT License. See `LICENSE` for more information.
