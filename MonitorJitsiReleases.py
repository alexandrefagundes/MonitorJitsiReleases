name: Monitor Jitsi Releases

on:
  schedule:
    - cron: '0 0 * * *' # Executa diariamente

jobs:
  check-release:
    runs-on: ubuntu-latest
    steps:
      - name: Get latest release
        run: |
          curl -s https://api.github.com/repos/jitsi/jitsi-meet/releases | jq '.[0].tag_name'
