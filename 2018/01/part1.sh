#!/bin/bash
cat input.txt | tr -d '\n' | sed 's/^+//' | bc
