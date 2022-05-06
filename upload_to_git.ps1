#!/usr/bin/env pwsh
Git add -A
$commit_message = $args[0]
Git commit -m $commit_message
Git push -u origin main
