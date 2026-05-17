#!/bin/bash

echo "🚀 Deploying updates to production server..."

ssh deploy@178.104.128.201 << 'EOF'
  echo "📦 Pulling latest changes for ournakshatra/app..."
  cd /srv/ournakshatra/app
  git fetch origin
  git reset --hard origin/main

  echo "🪔 Pulling latest changes for Bhajan..."
  cd /var/www/Bhajan
  git fetch origin
  git reset --hard origin/main
  git clean -fd

  echo "✅ Deployment successful!"
EOF
