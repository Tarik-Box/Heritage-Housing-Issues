#!/bin/bash
mkdir -p ~/.streamlit/
echo "[server]\nheadless = true\nenableCORS=false\nport=$PORT\n" > ~/.streamlit/config.toml
echo "[general]\nemail=\"\"\n" > ~/.streamlit/credentials.toml