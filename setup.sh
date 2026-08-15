#!/usr/bin/env bash
set -euo pipefail

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 not found. Please install Python 3."
  exit 1
fi

echo "Creating virtual environment (venv) if missing..."
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

if command -v pip3 >/dev/null 2>&1; then
  PIP=pip3
else
  PIP=pip
fi

echo "Installing dependencies from requirements.txt..."
mapfile -t pkgs < <(sed '/^\s*#/d;/^\s*$/d' requirements.txt)
total=${#pkgs[@]}
for i in "${!pkgs[@]}"; do
  n=$((i+1))
  pkg="${pkgs[i]}"
  percent=$((100 * n / total))
  printf "\nInstalling (%d/%d) %s — %d%%\n" "$n" "$total" "$pkg" "$percent"
  "${PIP}" install --upgrade "$pkg"
done

echo -e "\nAll dependencies installed. To use the venv:"
echo "  source venv/bin/activate"