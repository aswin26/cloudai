FROM postgres:17.2-alpine3.21

# Install build dependencies and pgvector
RUN apk add --no-cache \
	git \
	build-base \
	clang \
	llvm \
	postgresql-dev && \
    cd /tmp && \
    git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git && \
    cd pgvector && \
    make && \
    make install && \
    cd / && \
    rm -rf /tmp/pgvector && \
    apk del git build-base clang llvm postgresql-dev
