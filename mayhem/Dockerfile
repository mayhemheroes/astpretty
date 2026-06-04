# Build Stage
FROM python:3.11-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    clang \
    git \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

ENV CC=clang CXX=clang++
RUN pip install --no-cache-dir atheris

# Final Stage
FROM python:3.11-slim

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/python3.11 /usr/local/bin/python3.11
COPY --from=builder /usr/lib/llvm-* /usr/lib/llvm-*

ADD . /src
WORKDIR /src
RUN python3 -m pip install --no-cache-dir .

CMD ["/src/mayhem/fuzz_ast.py"]
