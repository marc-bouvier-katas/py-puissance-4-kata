#!/bin/bash
watch --color "pytest -vv| tail -n $(($LINES - 25))"
