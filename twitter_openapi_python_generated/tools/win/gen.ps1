
# Move-Item "\\wsl.localhost\Ubuntu-22.04\home\yuki\openapi-generator\modules\openapi-generator-cli\target\openapi-generator-cli.jar" "tools/openapi-generator-cli.jar" -Force


./twitter-openapi/.venv/Scripts/Activate.ps1
Start-Process -FilePath "python" -ArgumentList "tools/build.py" -WorkingDirectory "twitter-openapi" -Wait -NoNewWindow

tools/win/clean.ps1
java -jar tools/openapi-generator-cli.jar generate -g python -c tools/openapi-generator-config.yaml --git-repo-id twitter_openapi_python --git-user-id fa0311

# Start-Process -FilePath "python" -ArgumentList "tools/win/replace.py" -Wait -NoNewWindow