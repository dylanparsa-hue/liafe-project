#!/bin/bash
# Start LIAFE Django + Cloudflare Tunnel
# Usage: ./start.sh

cd "$(dirname "$0")"

echo "Starting LIAFE..."

# Kill anything already on port 8000
lsof -ti:8000 | xargs kill -9 2>/dev/null

# Start Django in background
python3 manage.py runserver 8000 &
DJANGO_PID=$!
echo "Django PID: $DJANGO_PID (port 8000)"
sleep 2

# Start Cloudflare Tunnel (prints your public URL)
echo ""
echo "Starting Cloudflare Tunnel — your public URL will appear below:"
echo ""
cloudflared tunnel --url http://127.0.0.1:8000 --no-autoupdate

# When Ctrl+C is pressed, also kill Django
kill $DJANGO_PID 2>/dev/null
