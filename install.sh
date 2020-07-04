echo "[Pypo] Installing..."
pip install --editable .
echo "[Pypo] Setting up basic sounds"
mkdir -p ~/.pypo/sounds
echo "[Pypo] Setting up db folder"
mkdir -p ~/.pypo/db
cp sounds/stop.mp3 ~/.pypo/sounds
